from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User

def index(request):
    return render(request, 'home/index.html')  # Возвращаем шаблон главной страницы

def login_page(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        # Попробуем аутентифицировать пользователя по имени пользователя
        user = authenticate(request, username=username_or_email, password=password)

        # Если не удалось, попробуем найти пользователя по email
        if user is None:
            try:
                user = User.objects.get(email=username_or_email)
                if user.check_password(password):
                    login(request, user)
                else:
                    user = None  # Неправильный пароль
            except User.DoesNotExist:
                user = None  # Пользователь не найден

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")  # Сообщение об успешном входе
            return redirect('index')  # Перенаправление на главную страницу
        else:
            messages.error(request, "Invalid username or password.")  # Сообщение об ошибке
    return render(request, 'enter/login.html')  # Возвращаем шаблон входа


def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        # Проверка на валидность формы
        if form.is_valid():
            # Проверка на наличие уже существующего пользователя с таким же email
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                form.add_error('email', "This email is already in use.")  # Добавляем ошибку к полю email
            else:
                # Сохраняем пользователя, если email не занят
                user = form.save()
                login(request, user)
                messages.success(request, "You have successfully registered!")  # Сообщение об успешной регистрации
                return redirect('index')  # Перенаправление на главную страницу
        else:
            # Обработка ошибок для каждого поля, если форма не валидна
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
    else:
        form = UserRegisterForm()
    
    return render(request, 'enter/register.html', {'form': form})  # Возвращаем шаблон регистрации с формой

def logout_user(request):
    logout(request)  # Выход пользователя
    messages.success(request, "You have successfully logged out!")  # Сообщение об успешном выходе
    return redirect('index')  # Перенаправление на главную страницу
