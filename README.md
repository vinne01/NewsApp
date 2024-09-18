# NewsApp

Welcome to NewsApp, a Django-based application where users can read the latest news, search for news by topic, description, and date, and contact us if they encounter issues or incorrect news. This app also includes administrative features for managing news content with a team of members.
# My Project

Here is a great video about my project:

[Watch the video here](https://streamable.com/ti4c6x)




## Features

1. **Read Latest News**
   - Users can browse and read the latest news articles available on the app.

2. **Search Functionality**
   - Users can search for news based on:
     - **Topic**: Find news articles related to specific topics.
     - **Description**: Search within the description of news articles.
     - **Date**: Filter news articles by date.

3. **Contact Us**
   - If users encounter any errors or incorrect news, they can contact us through a contact form for assistance.

4. **Administrative Features**
   - **Team Management**: Admins can create a team of 10-15 members.
   - **User Accounts**: Admins share usernames and passwords with team members.
   - **Team Login**: Team members can log in using their provided credentials.
   - **News Management**: Team members can add news articles to the website.
   - **News Tracking**: Admins can see which team members added specific news articles and when.

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/newsapp.git
cd newsapp


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
