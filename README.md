# StudyFlow Backend Components

This repository showcases the backend components I implemented in the StudyFlow project, a multi-user task management web application.

## 🚀 What I Built
- Designed and implemented RESTful APIs using Django
- Developed database models using Django ORM (PostgreSQL)
- Implemented core business logic for task and category management
- Enabled asynchronous updates using AJAX

## 🧠 What I Learned
- Backend system design in a team-based project
- API design and request/response lifecycle
- Relational database modelling and data integrity
- Writing clean, modular, and maintainable code

## 🛠 Tech Stack
- Python
- Django
- PostgreSQL
- REST APIs

## 🔍 Key Backend Logic (views.py)

This file demonstrates:

- User-specific data isolation using `request.user`
- Input validation and duplicate prevention
- CRUD operations for category management
- Sorting using database functions (`Lower`)
- Access control using Django decorators (`@login_required`)
