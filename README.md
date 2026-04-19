# StudyFlow Backend (Django)

---

## Overview

A backend system for a multi-user task management application, built with Django and PostgreSQL, focusing on data modelling, request handling, and user-specific data isolation.

This repository showcases my individual backend contributions, including API logic, validation, and database design.

---

## Example API Flow

Create Category:
```http
POST /categories/
Content-Type: application/json

{

  "name": "Work"

}
```
Response:
```JSON
{

  "id": 1,

  "name": "Work"

}
```

---

## Design Decisions

- Enforced user-specific uniqueness to prevent data conflicts in multi-user environments  

- Structured validation logic to ensure consistent backend behaviour  

- Used modular architecture (models / views / urls) to improve maintainability and scalability

- Applied separation of concerns to isolate data models, request handling, and routing logic 

---

## What this repository demonstrates

- Designing backend data models using Django ORM
- Implementing request handling and business logic for category management
- Building user-specific data access control
- Structuring backend components in a modular and maintainable way

---

## Key backend features

- **Relational data modelling** with Django ORM  
  - Designed models with user ownership and constraints  
  - Enforced uniqueness of category names per user  

- **Request handling and CRUD operations**  
  - Implemented create, read, update, delete flows for categories  
  - Built reusable validation logic for consistent data handling  

- **Validation and error handling**  
  - Prevented empty inputs and duplicate category names  
  - Ensured clean and predictable backend behaviour  

- **Authentication-aware data access**  
  - Scoped all queries to the authenticated user  
  - Ensured data isolation in a multi-user environment  

- **Sorting and query optimisation**  
  - Implemented case-insensitive sorting using Django query functions  

---

## Backend structure

- `core/models.py`  
  Defines database schema using Django ORM, including constraints and relationships  

- `core/views.py`  
  Handles HTTP requests, validation logic, and business operations  

- `core/urls.py`  
  Defines URL routing for category-related operations  

- `requirements.txt`  
  Specifies backend dependencies and environment setup  

---

## Technical highlights

- Django ORM model design and query handling  
- REST-style backend architecture  
- Request validation and error handling  
- User-based data isolation  
- Clean and modular backend structure  

---

## Tech stack

- Python  
- Django  
- PostgreSQL  
- REST APIs  
- Git / GitHub  

---

## Project context

StudyFlow was developed as a team project.  
I was primarily responsible for backend logic, including models, request handling, and validation.

This repository is a curated selection of the components I implemented, extracted and reorganised for demonstration purposes.

Full team project repository:  
👉 https://github.com/itech-groupBR/tech-group-project
