## Setup and Installation

### Prerequisites

Python 3.10+
PostgreSQL

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
