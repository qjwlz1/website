[Русский](#russian-version) | [English](#english-version)
<a name="russian-version"></a>
# Проект магазина кроссовок "Vibe"

## 🚀 Описание проекта
Это веб-приложение — основа для интернет-магазина, разработанная на мощном фреймворке **Django**. Проект демонстрирует ключевые функции e-commerce: надежную систему регистрации и входа пользователей с работой с базой данных, а также отображение товаров из БД. Реализован полноценный функционал корзины, куда можно добавлять и удалять товары. На данном этапе данные о товарах управляются напрямую в коде, что закладывает прочный фундамент для будущей реализации административной панели и полного цикла оформления заказов.

## ✨ Основной функционал
* **Система аутентификации:** Пользователи могут регистрироваться и входить в систему, используя логин и пароль.
* **Личный кабинет:** Авторизованные пользователи получают доступ к своему профилю и разделу **"Избранное"** для сохранения любимых товаров.
* **Корзина покупок:**
    * Добавление товаров в корзину с указанием количества.
    * Просмотр, изменение количества и удаление товаров из корзины.
    * Отображение специального сообщения при пустой корзине.
* **Разграничение прав доступа:** Реализованы три роли пользователей (Администратор, Пользователь, Гость) с разными уровнями доступа к функциям сайта.
* **Защита данных:** Приложение защищено от распространенных атак, включая CSRF.

## 🎨 Дизайн и пользовательский интерфейс
Дизайн проекта выполнен в современном, динамичном и графичном стиле, который привлекает внимание и отражает "уличную" эстетику:
* **Цветовая палитра:** Используется контрастное сочетание ярких акцентов с черным и белым. Для каждой страницы товара может быть своя цветовая схема.
* **Стиль и графика:** Дизайн сочетает минималистичные карточки с товарами и смелые, абстрактные фоновые паттерны и графические элементы.
* **Типографика:** Использование крупных, выразительных шрифтов придает интерфейсу индивидуальность.
* **UI-элементы:** Акцентные кнопки, иконки (например, для "Избранного") и карточки с закругленными углами создают современный и удобный интерфейс.
* **Адаптивность:** **Важно отметить, что текущая версия проекта оптимизирована для отображения на настольных компьютерах с соотношением сторон 16:9. Адаптация под мобильные устройства и другие разрешения пока не реализована и является одним из направлений для дальнейшего развития.**

## 📸 Галерея / Скриншоты

Здесь вы можете увидеть, как выглядит пользовательский интерфейс проекта:

### Часть главной страницы
![Главная страница](https://i.imgur.com/DIVIEY8.png)

### Профиль пользователя
![Профиль пользователя](https://i.imgur.com/3D0aKqW.png)

### Корзина покупок
![Корзина покупок](https://i.imgur.com/EWz0HSN.png)

### Футер
![Футер](https://i.imgur.com/CpjKGJE.png)

## 🛠️ Стек технологий
* **Язык программирования:** Python 3.12
* **Фреймворк:** Django
* **База данных:** SQLite (встроенная)
* **Фронтенд:** HTML5, CSS3 (собственные статические файлы), JavaScript
* **Система контроля версий:** Git, GitHub
* **Развертывание:** PythonAnywhere

## 🖥️ Ссылка на работающее приложение
Вы можете посмотреть и протестировать живую версию проекта по следующей ссылке:
[https://qjwlz.pythonanywhere.com/](https://qjwlz.pythonanywhere.com/)

---

### 🌐 Альтернативное развертывание: локальный хостинг

В качестве альтернативы облачному хостингу, проект был успешно развернут на локальном ПК с использованием собственного домена. 

**Основные шаги развертывания включали:**
* Настройку веб-сервера Nginx для обслуживания статических файлов и проксирования запросов к приложению.
* Использование Gunicorn в качестве WSGI-сервера для обработки HTTP-запросов.
* Конфигурацию доменного имени и DNS-записей.
* Настройку правил брандмауэра (firewall) для открытия нужных портов.
* Обеспечение доступа к сайту по собственному домену qjwlz.ru (сейчас не работает).
* Поддержание непрерывной работы сервера (uptime) для постоянной доступности приложения.
* Использование supervisor для управления процессами приложения.

Это развертывание демонстрирует понимание полного цикла работы веб-приложения, от кода до его доступности в сети.

---

## 🔧 Установка и запуск проекта локально
Следуйте этим инструкциям, чтобы запустить проект на вашем компьютере:
1.  **Клонирование репозитория:**
    ```bash
    git clone [https://github.com/qjwlz1/website.git](https://github.com/qjwlz1/website.git)
    ```
2.  **Переход в директорию проекта:**
    ```bash
    cd website
    ```
3.  **Создание и активация виртуального окружения:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  **Установка всех необходимых зависимостей:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Применение миграций базы данных:**
    ```bash
    python manage.py migrate
    ```
6.  **Запуск локального сервера Django:**
    ```bash
    python manage.py runserver
    ```
    Теперь приложение будет доступно по адресу `http://127.0.0.1:8000/` в вашем браузере.

## 👥 Автор
* **Разработчик:** qjwlz1

## 📄 Лицензия
Этот проект распространяется под лицензией [MIT License](https://opensource.org/licenses/MIT).
---
<a name="english-version"></a>

# "Vibe" Sneaker Store Project

## 🚀 Project Description
This is a web application—the foundation for an online store, built with the powerful **Django** framework. The project demonstrates key e-commerce functionalities, including a robust user registration and login system with database integration, as well as displaying products from the database. A fully functional shopping cart has been implemented, allowing users to add and remove items. At this stage, product data is managed directly within the code, which lays a solid foundation for future implementation of a full-fledged admin panel and a complete checkout cycle.

**Note:** The live application and its user interface are in Russian.

## ✨ Key Features
* **Authentication System:** Users can register and log in using a username and password.
* **User Profile:** Authenticated users get access to their profile and a **"Favorites"** section to save their preferred items.
* **Shopping Cart:**
    * Add products to the cart with a specified quantity.
    * View, update quantities, and remove items from the cart.
    * A special message is displayed when the cart is empty.
* **Access Control:** Three user roles are implemented (Administrator, User, Guest) with different levels of access to site functions.
* **Data Security:** The application is protected against common attacks, including CSRF.

## 🎨 Design and User Interface
The project's design is executed in a modern, dynamic, and graphical style that captures attention and reflects a "streetwear" aesthetic:
* **Color Palette:** It uses a high-contrast combination of vibrant accents with black and white. Each product page can have its own color scheme.
* **Style & Graphics:** The design combines minimalist product cards with bold, abstract background patterns and graphic elements.
* **Typography:** The use of large, expressive fonts gives the interface a unique identity.
* **UI Elements:** Accentuated buttons, icons (e.g., for "Favorites"), and cards with rounded corners create a modern and user-friendly interface.
* **Responsiveness:** **It is important to note that the current version of the project is optimized for desktop displays with a 16:9 aspect ratio. Responsiveness for mobile devices and other resolutions is not yet implemented and is a planned feature for future development.**

## 📸 Gallery / Screenshots
Here you can see what the user interface of the project looks like:

### Part of the Main Page
![Main Page](https://i.imgur.com/DIVIEY8.png)

### User Profile
![User Profile](https://i.imgur.com/3D0aKqW.png)

### Shopping Cart
![Shopping Cart](https://i.imgur.com/EWz0HSN.png)

### Footer
![Footer](https://i.imgur.com/CpjKGJE.png)

## 🛠️ Tech Stack
* **Programming Language:** Python 3.12
* **Framework:** Django
* **Database:** SQLite (built-in)
* **Frontend:** HTML5, CSS3 (custom static files), JavaScript
* **Version Control:** Git, GitHub
* **Deployment:** PythonAnywhere

## 🖥️ Live Application Link
You can view and test a live version of the project at the following link:
[https://qjwlz.pythonanywhere.com/](https://qjwlz.pythonanywhere.com/)

---

### 🌐 Alternative Deployment: Local Hosting
As an alternative to cloud hosting, the project was successfully deployed on a local PC using a custom domain. 

**The main deployment steps included:**
* **Configuring the Nginx web server** for serving static files and proxying requests to the application.
* **Using Gunicorn** as a WSGI server to handle HTTP requests.
* **Configuring the domain name** and DNS records.
* **Setting up firewall rules** to open the necessary ports.
* **Ensuring site access via the custom domain qjwlz.ru.**
* **Maintaining server uptime** for continuous application availability.
* **Using Supervisor** for managing the application processes.

This deployment demonstrates an understanding of the full web application lifecycle, from code to network accessibility.

---

## 🔧 Installation and Local Setup
Follow these instructions to run the project on your computer:
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/qjwlz1/website.git](https://github.com/qjwlz1/website.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd website
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  **Install all necessary dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Run the local Django server:**
    ```bash
    python manage.py runserver
    ```
    The application will now be available at `http://127.0.0.1:8000/` in your browser.

## 👥 Author
* **Developer:** qjwlz1

## 📄 License
This project is distributed under the [MIT License](https://opensource.org/licenses/MIT).
