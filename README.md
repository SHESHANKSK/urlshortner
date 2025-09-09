# URL Shortener

A simple Flask-based web application to shorten URLs, built with Python, Flask, and SQLite. The app provides a web interface and API for generating short URLs and managing them.

## Features
- Shorten long URLs to easy-to-share short links
- Delete short URLs using a unique delete key
- Web interface and API documentation
- SQLite database for persistent storage
- Asset minification for faster load times

## Project Structure
```
app.py                  # Main Flask application
requirements.txt        # Python dependencies
Procfile                # Heroku deployment configuration
static/                 # Static assets (CSS, images)
templates/              # HTML templates
urlshortnerdb.sqlite3   # SQLite database file
.env                    # Environment variables (optional)
.venv/                  # Python virtual environment
.git/                   # Git version control
.idea/                  # IDE configuration
__pycache__/            # Python cache files
```

## Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/SHESHANKSK/urlshortner.git
cd urlshortner
```

### 2. Create and activate a virtual environment (recommended)
```
python -m venv .venv
.venv\Scripts\activate   # On Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Initialize the database
If running for the first time, create the database tables:
```python
# In Python shell
from app import db
with db.app.app_context():
    db.create_all()
```

### 5. Run the application locally
```
python app.py
```
The app will be available at http://127.0.0.1:5000/

### 6. Deploying to Heroku
- Ensure you have a Heroku account and the Heroku CLI installed.
- Login to Heroku and create a new app.
- Push your code to Heroku. The Procfile will instruct Heroku to use gunicorn to run the app.

## Usage
- Visit the home page to shorten URLs.
- Use the API page for documentation and programmatic access.
- Short URLs and delete links are generated and shown after submission.

## License
This project is for educational purposes.

