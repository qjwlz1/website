from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Sneaker, SneakerFavorite
from django.shortcuts import render
from django.http import JsonResponse
from .models import Sneaker, SneakerFavorite, SneakerCart

@login_required
def clear_cart(request):
    SneakerCart.objects.filter(user=request.user).delete()
    return redirect('cart')  

@login_required
def cart(request):
    cart_items = SneakerCart.objects.filter(user=request.user)
    total_price = sum(item.sneaker.price * item.quantity for item in cart_items)
    return render(request, 'home/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def toggle_cart(request, sneaker_color):
    sneaker = get_object_or_404(Sneaker, color=sneaker_color)
    cart_item = SneakerCart.objects.filter(user=request.user, sneaker=sneaker).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        is_in_cart = True
    else:
        SneakerCart.objects.create(user=request.user, sneaker=sneaker, quantity=1)
        is_in_cart = True
    return JsonResponse({'is_in_cart': is_in_cart, 'quantity': cart_item.quantity if cart_item else 1})


@login_required
def toggle_favorite(request, sneaker_color):
    sneaker = get_object_or_404(Sneaker, color=sneaker_color)
    favorite = SneakerFavorite.objects.filter(user=request.user, sneaker=sneaker).first()
    if favorite:
        favorite.delete()
        is_favorite = False
    else:
        SneakerFavorite.objects.create(user=request.user, sneaker=sneaker)
        is_favorite = True
    return JsonResponse({'is_favorite': is_favorite})

@login_required
def add_to_sneakersmarks(request, color):
    sneaker = get_object_or_404(Sneaker, color=color)
    favorite_exists = SneakerFavorite.objects.filter(user=request.user, sneaker=sneaker).exists()
    
    if not favorite_exists:
        SneakerFavorite.objects.create(user=request.user, sneaker=sneaker)
    
    return redirect('profile')

@login_required
def profile(request):
    sneaker_favorites = SneakerFavorite.objects.filter(user=request.user)
    return render(request, 'home/profile.html', {'SneakerFavorite': sneaker_favorites})

def order(request):
    return render(request, 'home/order.html')

def sneaker_red(request):
    return render(request, 'sneakers/red.html')

def sneaker_green(request):
    return render(request, 'sneakers/green.html')

def sneaker_orange(request):
    return render(request, 'sneakers/orange.html')

def sneaker_yellow(request):
    return render(request, 'sneakers/yellow.html')

def sneaker_black(request):
    return render(request, 'sneakers/black.html')

def sneaker_blue(request):
    return render(request, 'sneakers/blue.html')

def index(request):
    return render(request, 'home/index.html')

def login_page(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username_or_email, password=password)

        if user is None:
            try:
                user = User.objects.get(email=username_or_email)
                if user.check_password(password):
                    login(request, user)
                else:
                    user = None  
            except User.DoesNotExist:
                user = None  
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'enter/login.html')

def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                form.add_error('email', "This email is already in use.")
            else:
                user = form.save()
                login(request, user)
                messages.success(request, "You have successfully registered!")
                return redirect('index')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
    else:
        form = UserRegisterForm()

    return render(request, 'enter/register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('index')