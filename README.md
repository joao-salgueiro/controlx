# 🎮 CONTROLX

**CONTROLX** is a blog-style web project built with **Django**, focused on showcasing the history and evolution of gaming controllers.  
This project is also a personal challenge aimed at improving my skills in Django, Python, and basic database management.

---

## 🚀 Features

- 📝 Blog-like posts for each controller
- 📷 Image support for each post
- 📱 Fully responsive design (desktop, tablet, mobile)
- 🔐 Google authentication (via `django-allauth`)
- 🧾 Profile picture auto-fetch on social login
- 🗃️ Admin interface for content management

---

## 🛠️ Technologies Used

- Python 3
- Django
- SQLite (default, can be replaced)
- HTML5 / CSS3 (with media queries for responsiveness)
- Django Allauth (for social login)

---

## 💡 Learning Goals

This project helped me:

- Practice Django models, views, templates, and static files
- Understand user authentication (including social auth via Google)
- Manage user profiles and handle images
- Improve frontend responsiveness using media queries
- Deploy a Django project and make it available online


## ⚙️ How to Run Locally

```bash
git clone https://github.com/your-username/controlx.git
cd controlx
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
