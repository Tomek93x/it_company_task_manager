# IT Company Task Manager

A Django application for managing tasks, roles, and employees in IT projects.  
**Version:** 1.0

## Features
- Task list with filtering and sorting functionality
- Task detail page with comment support
- Management for roles, task types, and workers
- Strong password validation during user creation
- Backend and user interface built on Bootstrap 5

## How to Run

1. **Clone this repository**
    ```
    git clone https://github.com/yourusername/it-company-task-manager.git
    cd it-company-task-manager
    ```

2. **Create and activate a virtual environment**
    ```
    python -m venv venv
    source venv/bin/activate      # On macOS/Linux
    venv\Scripts\activate         # On Windows
    ```

3. **Install required packages**
    ```
    pip install -r requirements.txt
    ```

4. **Run database migrations**
    ```
    python manage.py makemigrations
    python manage.py
