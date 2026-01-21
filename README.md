# Space Pioneers API

A comprehensive web application for exploring and managing data about space pioneers, missions, agencies, astronauts, and extravehicular activities (EVAs) from the early era of human spaceflight.

## Project Description

Space Pioneers API is a Django-based web application that provides a rich interface for browsing and managing historical space mission data, covering the period from the first solo mission into space (April 1961) to the last crewed lunar landing (December 1972). The application offers detailed information about:

- **Astronauts**: Biographies, missions, and career statistics
- **Space Agencies**: NASA, Soviet/Russian space program, and other national agencies
- **Missions**: Complete mission details, crew assignments, and mission patches
- **EVAs (Spacewalks)**: Comprehensive records of extravehicular activities
- **Crew Members**: Role assignments and astronaut ages at launch

## Author and Contact

**Contact Email**: info@spacepioneersapi.com
**Website**: spacepioneersapi.com
**Location**: London, UK

## Technology Stack

### Backend
- **Framework**: Django 5.1.6
- **Language**: Python 3.12
- **API Framework**: Django REST Framework 3.13.1
- **Database**: PostgreSQL 14 (with SQLite3 support for local development)

### Frontend
- **CSS Framework**: Bootstrap 4 with Material Design (MDBootstrap)
- **Icons**: Font Awesome
- **Templates**: Django template engine

### Authentication
- **django-allauth**: Social authentication with GitHub and Bitbucket OAuth support

### Development Tools
- **Django Debug Toolbar**: Performance profiling and debugging
- **Django Extensions**: Enhanced management commands
- **import-export**: Admin panel data import/export capability

### Deployment
- **Containerization**: Docker & Docker Compose
- **WSGI Server**: Gunicorn (via Docker)
- **Web Server**: Nginx (recommended for production)

## Architecture Overview

### Project Structure

```
space-pioneers-api/
├── config/                      # Django configuration
│   ├── settings/
│   │   └── settings.py         # Main Django settings
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI application entry point
│   └── asgi.py                 # ASGI application entry point
│
├── apps/                        # Django applications
│   ├── pages/                  # Landing page and static pages
│   ├── common/                 # Common utilities and base models
│   ├── accounts/               # User authentication and profiles
│   ├── agencies/               # Space agencies management
│   ├── astronauts/             # Astronaut database
│   ├── evas/                   # Extravehicular activities
│   └── missions/               # Space missions and crew assignments
│
├── templates/                   # HTML templates (project-level)
│   ├── base.html               # Base template with navigation
│   ├── pages/                  # Page templates
│   ├── account/                # Authentication templates
│   ├── agencies/               # Agency templates
│   ├── astronauts/             # Astronaut templates
│   ├── evas/                   # EVA templates
│   └── missions/               # Mission templates
│
├── static/                      # Static assets
│   └── base/
│       ├── css/                # Stylesheets
│       ├── js/                 # JavaScript files
│       └── images/             # Images and logos
│
├── media/                       # User-uploaded files
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Docker image definition
├── requirements.txt            # Python dependencies
├── manage.py                   # Django management script
└── README.md                   # This file
```

### Application Architecture

The project follows Django's MVT (Model-View-Template) architecture:

- **Models**: Define database schema for astronauts, missions, agencies, EVAs, and crew assignments
- **Views**: Handle HTTP requests and business logic
- **Templates**: Render HTML responses using Django template language
- **URLs**: Map URL patterns to views

### Database Schema

Key models include:

- `Astronaut`: Personal information, nationality, career statistics
- `Agency`: Space agency details and country of origin
- `Mission`: Mission name, type, launch date/time, duration, crew size
- `Crew`: Join table linking astronauts to missions with roles
- `EVA`: Spacewalk details including duration, type, and astronaut

## Development Environment Setup

### Prerequisites

- Python 3.12+
- Docker and Docker Compose (recommended)
- PostgreSQL 14+ (if running without Docker)
- Git

### Option 1: Docker Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd human-spaceflight-api-code
   ```

2. **Build and start containers**
   ```bash
   docker-compose up --build
   ```

3. **Run migrations**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create a superuser**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Access the application**
   - Web app: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

### Option 2: Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd human-spaceflight-api-code
   ```

2. **Create and activate virtual environment**
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=postgresql://user:password@localhost:5432/spacepioneers
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Web app: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

### Loading Initial Data

If you have fixture files or data dumps:

```bash
python manage.py loaddata <fixture-name>
```

## Common Problems and Solutions

### 1. Database Connection Issues

**Problem**: Cannot connect to PostgreSQL database

**Solutions**:
- Verify PostgreSQL is running: `docker-compose ps` (Docker) or `systemctl status postgresql` (local)
- Check database credentials in settings or `.env` file
- Ensure database exists: `createdb spacepioneers`
- For Docker: Ensure containers are on the same network

### 2. Static Files Not Loading

**Problem**: CSS/JS files not loading in development

**Solutions**:
```bash
python manage.py collectstatic
```
- Verify `STATIC_URL` and `STATIC_ROOT` settings
- Check that `django.contrib.staticfiles` is in `INSTALLED_APPS`

### 3. Migration Conflicts

**Problem**: Migration conflicts or inconsistent database state

**Solutions**:
```bash
# Reset migrations (WARNING: Development only!)
python manage.py migrate <app_name> zero
python manage.py migrate

# Or create a fresh database
dropdb spacepioneers && createdb spacepioneers
python manage.py migrate
```

### 4. Port Already in Use

**Problem**: Port 8000 already in use

**Solutions**:
```bash
# Use a different port
python manage.py runserver 8080

# Or kill the process using port 8000
lsof -ti:8000 | xargs kill -9  # Unix/Mac
```

### 5. OAuth Authentication Issues

**Problem**: GitHub/Bitbucket login not working

**Solutions**:
- Verify OAuth app credentials in Django admin: `/admin/socialaccount/socialapp/`
- Ensure callback URLs are correctly configured in GitHub/Bitbucket
- Check that `django-allauth` is properly configured in `INSTALLED_APPS`

### 6. Docker Build Failures

**Problem**: Docker image fails to build

**Solutions**:
```bash
# Clean build without cache
docker-compose build --no-cache

# Remove old images and volumes
docker system prune -a
docker volume prune
```

## Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test apps.astronauts

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## Management Commands

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Open Django shell
python manage.py shell

# Run development server
python manage.py runserver
```

## Contributing

When contributing to this project:

1. Create a feature branch from `main`
2. Follow PEP 8 style guidelines
3. Write tests for new features
4. Update documentation as needed
5. Submit a pull request with a clear description

## License

All rights reserved. Copyright © 2026 Space Pioneers API.

## Acknowledgments

Data sourced from historical space mission records and publicly available space agency databases.
