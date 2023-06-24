# django-base
Basic monolithic Django project with custom user model and Flowbite/Tailwind CSS styling

## Installation

Django-base can be installed via Pip.

* Clone the repo to your local computer and change into that directory

```
$ git clone https://github.com/jbarrfitz/django-base.git
$ cd django-base
```

### Pip

```python
$ python -m venv .venv

$ source .venv/bin/activate

(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

