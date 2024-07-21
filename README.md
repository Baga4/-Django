# Django CRUD Project

This is a Django project that implements basic CRUD (Create, Read, Update, Delete) operations, along with user registration, user login, and a feed page where posts can be managed by their respective creators (current logged-in users).

This project is intended to be the base for creating any feed related project where users can post their content . This project is just a base to create a bigger / scaleable application

## Features

- User Registration
- User Login/Logout
- Create, Read, Update, Delete (CRUD) operations for posts
- Feed page displaying posts
- Posts can only be edited or deleted by the user who created them

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sagardonut/Django.git
   ```
1. Navigate to the project:
   ```bash
   cd Django
   ```
2. Create a virtual environment:
```bash
pythom -m venv venv
```
3. Activate the virtual environment:
   * on windows
     ```bash
     venv\Scripts\activate
     ```
   * on macOS / Linux
     ```bash
     source venv/bin/activate
     ```
4. Install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```
5. Apply migrations
   * Make migrate
  ```bash
   python manage.py migrate
   ```
   * Apply migrations
   ```bash
   python manage.py makemigrations
   ```
6. Create superuser
   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server
   ```bash
   python manage.py runserver
   ```
* navigate to the registration page `https://127.0.0.1:8000/`
* You will be redirected to login page where you can create a new user and view the feed page
  
## Usage
  * User Registration
  ### User login
## CRUD operations
  * Create a new post
  * Update / edit self created post 
  * Delete a post

## Project Structure 
  ```
Django/
│
├── baseapp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── feed.html
│
├── static/
│   ├── css/
|       └── base-style.css
│   │   └── styles.css
│   └── js/
│       └── scripts.js
│
├── manage.py
└── requirements.txt
```
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. This directory is just 
a base and has a lots of improvement opportunities .

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
