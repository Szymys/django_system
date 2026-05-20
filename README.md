# 🎯 Django System

## 🌐 Live Demo
🔗 [www.szymys.eu](https://www.szymys.eu)

**Django-based admin system** for e-commerce management. No-code interface for administrators to customize appearance, manage products, categories, and orders. Customers can register, authenticate via email, and access their personal dashboard.

![Screenshot - Homepage](https://raw.githubusercontent.com/Szymys/django_system/main/diagrams/makiety/glowna.png)

## 🔧 Stack

- **Backend**: Django 5, Python 3.12
- **Frontend**: Bootstrap 5 
- **Database**: PostgreSQL
- **Web server**: Nginx (with HTTPS)
- **Deployment**: Docker & Docker Compose
- **Hosting**: Ubuntu VPS

---

## 🚀 Features

### 👨‍💼 Admin Panel (No-Code Interface)
- 🛍️ Manage products without coding
- 📁 Create and organize categories
- 🎨 Customize store appearance & description
- 📋 View and manage customer orders
- 👥 Manage user accounts
- ⚙️ Configure system settings

### 👤 User Panel
- 🔒 User authentication with email activation
- 📱 Personal account dashboard
- 🧾 Order history & status tracking
- 🏠 Delivery address management
- ✏️ Update email & personal information
- 📬 Email notifications

### 🛒 Customer Features
- 📦 Product listings & categories
- 🛒 Shopping cart
- 💳 Checkout process
- 🔐 Secure authentication
- ✅ Form validation with custom error messages

---

## ⚙️ Quick Start (Local Dev)

### Prerequisites
- Docker & Docker Compose
- Git

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/Szymys/django_system
cd django_system

# 2. Create a .env file (in project root, same level as docker-compose.local.yml)
# Example configuration:

SECRET_KEY=your_secret_key_here
DEBUG=True
POSTGRES_DB=django_system_db
POSTGRES_USER=django_user
POSTGRES_PASSWORD=secure_password_here
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your.email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

# 3. Build Docker images
docker-compose -f docker-compose.local.yml build

# 4. Start containers in the background
docker-compose -f docker-compose.local.yml up -d

# 5. Enter the Django container
docker-compose -f docker-compose.local.yml exec web bash

# 6. Create database tables
python manage.py makemigrations
python manage.py migrate

# 7. Create superuser (admin account)
python manage.py createsuperuser

# 8. Load initial data (if applicable)
python manage.py loaddata initial_data

# 9. Access the application
# Admin Panel: http://localhost:8000/admin
# Frontend: http://localhost:8000
