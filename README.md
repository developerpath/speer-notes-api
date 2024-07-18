## Notes API

This project is a secure and scalable RESTful API built with Django and Django REST Framework (DRF). It allows users to create, read, update, and delete notes, share notes with other users, and search for notes based on keywords. The application implements authentication, rate limiting, and request throttling to handle high traffic.

### Prerequisites

Python 3.10+
PostgreSQL

#### Technology Stack

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **PostgreSQL**: A powerful, open-source object-relational database system.

#### Third-Party Tools

- **Django REST Framework (DRF)**: Used for building the RESTful API. DRF provides a powerful framework for creating Web APIs with features like authentication, serialization, and view sets, making it a natural choice for building robust and maintainable APIs.
- **Simple JWT**: Used for JSON Web Token authentication. It provides a simple and secure way to handle authentication using tokens.

#### Why Django
Choosing Django for building web applications, including RESTful APIs, offers numerous advantages. Here are some compelling reasons to opt for Django:

1. Rapid Development
2. Comprehensive Documentation and Community Support
3. Scalability
4. Security
5. Admin Interface
8. ORM and Database Abstraction
9. Mature and Stable

#### Why PostgeSQL

1. Advanced SQL Support
2. Extensibility and Custom Extensions
3. Performance and Optimization
4. Security
5. Scalability (Vertical and even Horizontal using tools like Citus)
6. Mature and Stable

### Installation

Clone the repository:
```
git clone git@github.com:developerpath/speer-notes-api.git
```

Change directory to repository folder
```
cd speer-notes-api
```

1. **Run script**

```
chmod +x setup.sh
   ./setup.sh
```

2. **Run commands manually**
   Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

   Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

   Create sqlite db file:
   ```
   touch db.sqlite3
   ```

   Apply the migrations:
   ```
   python manage.py migrate
   ```

   Run the development server:
   ```
   python manage.py runserver
   ```

**Running Tests**
To run the tests, use the following command:
```
python manage.py test
```

### API Endpoints

#### Authentication Endpoints

`POST /api/auth/signup`: Create a new user account.
`POST /api/auth/login`: Authenticate a user and return a JWT token.

#### Note Endpoints
`GET /api/notes`: Get a list of all notes for the authenticated user.
`GET /api/notes/<id>`: Get a note by ID for the authenticated user.
`POST /api/notes`: Create a new note for the authenticated user.
`PUT /api/notes/<id>`: Update an existing note by ID for the authenticated user.
`DELETE /api/notes/<id>`: Delete a note by ID for the authenticated user.
`POST /api/notes/<id>/share`: Share a note with another user for the authenticated user.
`GET /api/search?q=<query>`: Search for notes based on keywords. This endpoint is publicly accessible.
