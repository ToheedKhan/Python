Try Atlas: https://www.mongodb.com/cloud/atlas/r...
FastAPI with MongoDB: https://www.mongodb.com/developer/tec...
MongoDB Learning Resources: https://learn.mongodb.com/?utm_campai...

## To make User interface quickly - 
Bootstrape

Jinja2 templates

http://127.0.0.1:800://127.0.0.1:8000/docs

Run server
uvicorn main:app --reload


 What is Jinja2?
Jinja2 is a templating engine for Python — it's used to generate dynamic HTML (or other text files) by mixing Python-like code with static content.

✅ Common Use Case:
Jinja2 is most commonly used in web frameworks like:

Flask

Django (Django uses its own template engine but is very similar)

FastAPI (when rendering HTML)


# Step 1: Activate your environment
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate.bat  # Windows

# Step 2: Run your project / use installed packages
python main.py

# Step 3: Done? Deactivate it
deactivate


To create an __init__.py file in a folder (so Python treats it as a package), follow one of these simple methods:
Why Is This Needed?
It tells Python the directory is a package.

Without it, you may get import errors like ModuleNotFoundError.
