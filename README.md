# URL Shortener
The URL Shortener is a web application that allows users to create shortened URLs for longer, harder-to-remember URLs.  The application uses FastAPI as the web framework for the backend APIs.

## Installation
To install the necessary dependencies for the URL Shortener, run:

```
pip install -r requirements.txt
```

## Configuration
The URL Shortener uses environment-specific settings to configure the application. By default, the application runs in development mode, but you can switch to production mode by setting the `APP_ENV` environment variable to `production`.

The settings files are located in the `app/settings` directory, and include:

* `base.py`: The base settings class that defines the required settings.
* `development.py`: The development environment settings.
* `production.py`: The production environment settings.

You can set the `DEV_DATABASE_URL` and `PROD_DATABASE_URL` environment variables to configure the database connection URL for development and production modes, respectively.

The application also uses a `.env` file to load environment variables. An example `.env` file is provided, but you should create your own for your specific configuration.

## Usage
To start the URL Shortener web application, run:

```
uvicorn app.main:app --reload
```
This will start the application in development mode and automatically reload the server when changes are made.

The API endpoints are:

* `POST /v1/shorten`: Shorten a long URL and store it in the database.
* `GET /v1/{short_url}`: Redirect to the original URL corresponding to a given shortened URL.

The API requires a valid JSON payload in the request body for the `POST /v1/shorten` endpoint, containing a `url` field with a valid HTTP or HTTPS URL.

## Files
* `app`: The main application directory containing the FastAPI application, models, utilities, and other modules.
* `.env`: The environment variable file containing the configuration settings.
* `config.py`: The configuration file that loads the appropriate settings based on the current environment.
* `database.py`: The database configuration file that creates the database engine and session factory.
* `main.py`: The main application entry point.
* `requirements.txt`: The list of required Python dependencies.
* `README.md`: The README file for the URL Shortener project.
* `.gitignore`: The list of files and directories to ignore in Git.
