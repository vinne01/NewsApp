# Chailheadq NewsApp

This is a Django-based News Application named `chailheadq` with an app called `tweet`. Follow the instructions below to set up the project and configure the necessary folders.

## Setup Instructions

### 1. Create the Django Project

Run the following command to create a new Django project named `chailheadq`:

```bash
django-admin startproject chailheadq
cd chailheadq
python manage.py startapp tweet
# chailheadq/settings.py

INSTALLED_APPS = [
    ...
    'tweet',
    ...
]
mkdir static
mkdir templates
# chailheadq/settings.py

import os

# Directory for static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Directory for templates
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
