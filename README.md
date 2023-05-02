# URL Shortener
The URL Shortener is a web application that allows users to create shortened URLs for longer, harder-to-remember URLs.  The application uses FastAPI as the web framework for the backend APIs.

## Installation
To install the necessary dependencies for the URL Shortener, run:

```
pip install -r requirements.txt
```

## Application Configuration
The URL Shortener uses environment-specific settings to configure the application. By default, the application runs in development mode, but you can switch to production mode by setting the `APP_ENV` environment variable to `production`.

The settings files are located in the `app/settings` directory, and include:

* `base.py`: The base settings class that defines the required settings.
* `development.py`: The development environment settings.
* `production.py`: The production environment settings.

You can set the `DEV_DATABASE_URL` and `PROD_DATABASE_URL` environment variables to configure the database connection URL for development and production modes, respectively.

The application also uses a `.env` file to load environment variables. An example `.env` file is provided, but you should create your own for your specific configuration.



## Application Usage
To start the URL Shortener web application, run:

```
uvicorn app.main:app --reload
```
This will start the application in development mode and automatically reload the server when changes are made.

The API endpoints are:

* `POST /v1/shorten`: Shorten a long URL and store it in the database.
* `GET /v1/{short_url}`: Redirect to the original URL corresponding to a given shortened URL.

The API requires a valid JSON payload in the request body for the `POST /v1/shorten` endpoint, containing a `url` field with a valid HTTP or HTTPS URL.

## Diagrams-as-Code Configuration
* Install Graphviz: If you have not installed Graphviz yet, download and install it from the official website (https://graphviz.org/download/). Make sure to add the installation directory to your system's PATH.
* Add Graphviz to your PATH: If you have already installed Graphviz but it is not added to your system's PATH, you can add it manually. To do this, open a command prompt and type set PATH=%PATH%;C:\path\to\graphviz\bin, replacing C:\path\to\graphviz\bin with the actual path to the Graphviz bin directory.

## Diagrams-as-Code Usage
To generate the diagrams:

* Go to the `diagrams` directory.
* Run `python {diagram_name}.py`, replacing `{diagram_name}` with the name of the diagram you want to generate. For example:
```
python high_level_architecture.py
```
* The diagram will be generated in the `diagrams\generated_diagrams` directory.

## Files
* `app`: The main application directory containing the FastAPI application, models, utilities, and other modules.
* `diagrams`: The directory containing Diagram-as-Code diagrams for the URL Shortener project.
* `.env`: The environment variable file containing the configuration settings.
* `config.py`: The configuration file that loads the appropriate settings based on the current environment.
* `database.py`: The database configuration file that creates the database engine and session factory.
* `main.py`: The main application entry point.
* `requirements.txt`: The list of required Python dependencies.
* `README.md`: The README file for the URL Shortener project.
* `.gitignore`: The list of files and directories to ignore in Git.

## Future Feature Roadmap
* Custom short URLs: Allow users to provide a custom short URL alias when they create a new shortened URL. This could make it easier for users to remember the short URL or to create branded short URLs.
* Expiration: Add an expiration date to the short URLs, after which the short URL will no longer be valid. Example use case: temporary URLs or promotional content that should only be available for a limited time. Also to reduce database size.
* Analytics: Track the number of clicks, unique visitors, and other metrics for each short URL. This could provide valuable insights for users to gauge the effectiveness of their links and understand their audience better.
* SSO (Single Sign-On): Allow users to sign in to the application using their Google, Facebook, or other social media accounts.
* Rate limiting: Add rate limiting to API endpoints to protect from abuse and to ensure fair usage among users.
* API Documentation: Create thorough API documentation using tools like Swagger.
* Custom domain support: Allow users to use their own custom domains for the short URLs.
* Bulk URL shortening: Add an endpoint that allows users to shorten multiple URLs in a single request. 
* QR code generation: Generate QR codes for the short URLs, making it easier for users to share the URLs, especially on printed materials or in situations where typing is not convenient.
