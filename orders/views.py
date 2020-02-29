from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


#   from .models import Pizza, Topping, Sub, Extra, Primo, Platter
from .models import MenuItem, Category, Product, Cart, AddedItem, Order, ExtraSelection
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, "orders/index.html", {"message": None})

def menu(request):
    if request.method == "POST":
        canOrder = request.user.is_authenticated

        # First, get the user's cart
        cart = Cart.objects.filter(user=request.user, ordered=False).last()
        # If cart doesn't exist for some reason, create a cart
        if not cart:
            cart = Cart(user=request.user)
            cart.save()

        insufficient = False
        # Create the PRIMARY item that is added
        item = MenuItem.objects.get(id=request.POST["additem"])
        # If ths item is a PIZZA or a SUB, get the selection for TOPPINGS / EXTRAS 
        if str(item.product.category) == "Regular Pizza" or str(item.product.category) == "Sicilian Pizza" or str(item.product.category) == "Sub":
            extras = request.POST.getlist("extras")

            # If the number of TOPPINGS are less than the LIMIT, it's insufficient, do not proceed 
            if not len(extras) == item.product.addon_limit and item.product.addon_limit > 0:
                insufficient = True

                ### Need to render the page with the new context
                context = {
                    "user": request.user,
                    "canOrder": canOrder,
                    "products": Product.objects.all(),
                    "categories": Category.objects.all(),
                    "topping": Category.objects.get(name="Topping"),
                    "extra": Category.objects.get(name="Extra"),
                    "cart": cart,
                    "insufficient": insufficient
                }
                return render(request, "orders/home.html", context)

            else:
                insufficient = False

        # Add the item to the cart
        addeditem = AddedItem.objects.filter(cart=cart, item=item)
        # If the item (MenuItem ID) already exists, increase the quantity
        if addeditem.count() > 0:
            addeditem = addeditem.first()
            addeditem.quantity += 1
            addeditem.save()
        else:
        # Else: create a new AddedItem
            addeditem = AddedItem(item=item, cart=cart)
            addeditem.save()
        
        if str(item.product.category) == "Regular Pizza" or str(item.product.category) == "Sicilian Pizza" or str(item.product.category) == "Sub":
            extraselected = ExtraSelection(main=addeditem)
            extraselected.save()
            for extra in extras:
                extraitem = MenuItem.objects.get(id=extra)
                extraselected.item.add(extraitem)
            extraselected.save()

        debug = request.POST["additem"]
        # img = "/static/orders/images/pizza/0.jpg"
        context = {
            "user": request.user,
            "canOrder": canOrder,
            "products": Product.objects.all(),
            "categories": Category.objects.all(),
            "topping": Category.objects.get(name="Topping"),
            "extra": Category.objects.get(name="Extra"),
            "cart": cart,
            "debug": debug,
            "insufficient": insufficient
        }
        return render(request, "orders/home.html", context)
    elif request.method == "GET":
        canOrder = request.user.is_authenticated    
        context = {
            "user": request.user,
            "canOrder": canOrder,
            "products": Product.objects.all(),
            "categories": Category.objects.all(),
            "topping": Category.objects.get(name="Topping"),
            "extra": Category.objects.get(name="Extra")
        }
        return render(request, "orders/home.html", context)

""" Cart, adding items and ordering """

@login_required(login_url='/login')
def cart(request):
    cart = Cart.objects.filter(user=request.user, ordered=False).last()
    if not cart:
        cart = Cart(user=request.user)
        cart.save()

    addeditems = AddedItem.objects.filter(cart=cart).all

    context = {
        "cart": cart,
        "addeditems": addeditems
    }

    if request.method == "POST":
        context["debug"] = request.POST
        if "additem" in request.POST:        
            itemid = request.POST["additem"]
            item = AddedItem.objects.get(id=itemid)
            item.quantity += 1
            item.save()
        elif "minusitem" in request.POST:
            itemid = request.POST["minusitem"]
            item = AddedItem.objects.get(id=itemid)
            if item.quantity == 1:
                item.delete()
            else:
                item.quantity -= 1
                item.save()
        elif "deleteitem" in request.POST:
            itemid = request.POST["deleteitem"]
            item = AddedItem.objects.filter(id=itemid)
            item.delete()

    return render(request, "orders/cart.html", context)

""" User login/register/logout """

def login_view(request):
    if request.method == "GET":
        return render(request, "orders/login.html", {"message": None})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("menu"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid Credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, "orders/register_success.html", {"message": None})
    else:
        form = RegistrationForm()
    return render(request, "orders/register.html", {"form": form})