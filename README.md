# IT Company Task Manager

# IT Company Task Manager

A Django application for managing tasks, roles, and employees in IT projects.  
**Version:** 1.0

## Features

- List, filter, and sort project tasks  
- Detailed task view with comment support  
- Management for roles, task types, and workers  
- Strong password validation during user creation  
- Bootstrap 5-based front-end

## Getting Started

### 1. Clone the repository


### 2. Create and activate a virtual environment


### 3. Install required packages


### 4. Set up environment variables

Create a `.env` file in your project root (next to `manage.py`) with your secret key:

**Never commit `.env` to your repository.**

### 5. Migrate the database


### 6. Create a superuser


### 7. Run the development server


Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and log in!

## Code structure

- `catalog/` - main app with models, views, forms
- `templates/` - HTML templates
- `manage.py` - entrypoint script
- `requirements.txt` - dependencies

## Security & Best Practices

- Do **not** store sensitive data (e.g., `SECRET_KEY`) in code or repository.
- Always keep the `.env` file out of version control.
- Review `.gitignore` for unnecessary files/folders (venv, db.sqlite3, .env etc).

## License

MIT License

---

If you have any issues or suggestions, feel free to open an issue or pull request!
