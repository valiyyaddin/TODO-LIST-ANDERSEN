🚀 What is this app about?
This is a todo-app built in Django, where you can add, filter, delete, view, and update your tasks.

📥 How to run the app
Clone the repo:

1)https://github.com/valiyyaddin/TODO-LIST-ANDERSEN

2)Run this command to create a superuser:
python manage.py createsuperuser

3)Create your user and password.

4)Run the server:

python manage.py runserver

5) Open your browser and you will first see the login page (built using Simple JWT, tested with Postman and Django tests).
Enter the password you used when creating the superuser.

6) After login, you can view and manage your tasks with full CRUD operations.

🛠 Tools used
Authentication: Simple REST Framework JWT

Testing: Postman and Django tests.py for API endpoint tests

API Documentation: Swagger

Database: PostgreSQL configured via Railway

📚 API Documentation
After running the app, visit these URLs to see API docs:

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/

