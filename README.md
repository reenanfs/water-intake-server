# Water Intake App Server

Welcome to the Water Intake App server! This server is responsible for handling the backend functionality for a Water Intake App which will help users track and manage their daily water consumption. The server is implemented in Python and utilizes various libraries and frameworks to provide a robust and efficient experience for the users.

## Features

The Water Intake App server offers the following features:

1. User Registration and Authentication: Users can register an account and log in securely to access their personalized water intake data.

2. Daily Water Intake Tracking: Users can record their daily water consumption, including the amount and time of intake, to keep track of their progress.

3. Goal Setting: Users can set a daily water intake goal based on their needs and preferences.

4. Analytics and Insights: Users can retrieve their water intake data within specified date ranges. The server provides intake records filtered by start date and end date, allowing users to view their consumption over time and analyze trends.

## Technologies Used

The Water Intake App server is built using the following technologies:

- **Python**: The server is primarily written in Python, which is a powerful and versatile programming language.

- **Flask**: Flask is a lightweight web framework for Python that provides a simple and efficient way to handle HTTP requests, routing, and other web-related tasks.

- **Flask-Migrate**: Flask-Migrate is an extension for Flask that integrates SQLAlchemy database migrations into the Flask application. It simplifies the process of managing and applying database schema changes.

- **PostgreSQL**: PostgreSQL is a powerful, open-source, object-relational database management system. It is used for storing user data in the Water Intake App.

- **JSON Web Tokens (JWT)**: JWT is used for user authentication and authorization. It enables secure transmission of user credentials and generates access tokens that are used to authenticate subsequent requests.

## Getting Started

To set up the Water Intake App server locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-repo.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure the server settings by creating a `.env` file in the project root directory. Set the following variables:

        # FLASK ENVS
        DEBUG=True
        DEVELOPMENT=True
        SECRET_KEY="your-secret-key"
        PORT=5000

        # POSTGRE ENVS
        POSTGRES_URI="postgresql://username:password@host:port/database"

        # APP ENVS
        BASE_INTAKE=35 # Base intake used in target water intake amount calculation
        
4. Set up the database by using Flask-Migrate running the command `flask db upgrade`.
5. Start the server: `python app.py`
6. The server should now be running on `http://localhost:5000`. You can access the endpoints using an API client.

## API Documentation

The server exposes the following API endpoints:

### Register

- **Endpoint**: `POST /auth/register`
- **Authentication required**: No

### Login

- **Endpoint**: `POST /auth/login`
- **Authentication required**: No

### Logout

- **Endpoint**: `POST /auth/logout`
- **Authentication required**: Yes (JWT)

### Get User Profile

- **Endpoint**: `GET /auth/profile`
- **Authentication required**: Yes (JWT)

### Refresh Access Token

- **Endpoint**: `POST /auth/refresh`
- **Authentication required**: Yes (JWT with refresh token)

### Update User Profile

- **Endpoint**: `PUT /users`
- **Authentication required**: Yes (JWT)

### Get User Water Intake

- **Endpoint**: `GET /water-intakes`
- **Authentication required**: Yes (JWT)

### Record User Water Intake

- **Endpoint**: `POST /water-intakes`
- **Authentication required**: Yes (JWT)

### Calculate Water Intake Target

- **Endpoint**: `POST /water-intakes/calculate-target`
- **Authentication required**: Yes (JWT)

Please refer to the API documentation for more detailed information on each endpoint, including request and response formats.

## Contributing

Contributions to the Water Intake App server are welcome! If you find any bugs, have suggestions for improvements, or want to add new features, please submit an issue or a pull request on the GitHub repository.

## License

The Water Intake App server is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute the code as per the license terms.

