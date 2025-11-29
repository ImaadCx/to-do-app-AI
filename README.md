<<<<<<< HEAD
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
=======
## TO DO APP in Python using the Django Framework 
Time taken 5 minutes 
Done as an Home work for AI Devs zoomcamp 
Link :https://github.com/DataTalksClub/ai-dev-tools-zoomcamp

Screeshots of the App:
<img width="1767" height="791" alt="image" src="https://github.com/user-attachments/assets/9e651ecf-ec16-4c17-9b00-a56ee141af67" />
<img width="956" height="836" alt="image" src="https://github.com/user-attachments/assets/ae59c57e-dad5-4add-8ae0-6e114e8b2bc7" />
>>>>>>> b64bdb91572c00c298603025204c0aa8e85159fd
