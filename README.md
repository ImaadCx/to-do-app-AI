# Django To-Do App

A feature-rich To-Do application built with Django, featuring priority management, theme customization, and comprehensive test coverage.

## Features

- ✅ **CRUD Operations**: Create, Read, Update, and Delete tasks
- 📅 **Due Dates**: Assign and track due dates for tasks
- 🎯 **Priority System**: Assign High/Medium/Low priority with visual color coding
- ✔️ **Completion Tracking**: Mark tasks as done/undone
- 🌓 **Light/Dark Mode**: Toggle between themes
- 🎨 **Advanced Customization**: Customize colors via Settings modal
- 🧪 **Test Coverage**: Comprehensive pytest test suite (26 tests)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ImaadCx/to-do-app-AI.git
   cd to-do-app-AI
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows
   source venv/bin/activate      # Linux/Mac
   ```

3. Install dependencies:
   ```bash
   pip install django pytest pytest-django
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Running Tests

Run the test suite with pytest:
```bash
pytest -v
```

All 26 tests should pass, covering:
- Model creation and validation
- CRUD operations
- Priority system
- URL routing
- View functionality

## Project Structure

```
HW1/
├── manage.py
├── pytest.ini
├── todo_project/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tasks/                 # Main app
    ├── models.py          # TodoItem model
    ├── views.py           # CRUD views
    ├── urls.py            # URL routing
    ├── test_models.py     # Model tests
    ├── test_views.py      # View tests
    ├── test_urls.py       # URL tests
    ├── templates/         # HTML templates
    │   └── tasks/
    │       ├── base.html
    │       ├── todo_list.html
    │       ├── todo_form.html
    │       └── todo_confirm_delete.html
    └── static/            # CSS and JS
        └── tasks/
            └── style.css
```

## Technologies Used

- **Backend**: Django 5.2.8
- **Database**: SQLite
- **Testing**: pytest, pytest-django
- **Frontend**: HTML, CSS, JavaScript (Vanilla)

## License

MIT License
