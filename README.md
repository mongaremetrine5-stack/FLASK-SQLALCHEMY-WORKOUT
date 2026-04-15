Project Title
Workout-Application-Backend-Flask-SQLAlchemy

Project Description
This project is a backend API built using Flask, SQLAlchemy, and Marshmallow for a workout tracking application used by personal trainers. The API allows trainers to create workouts, assign multiple exercises to each workout, and track details such as sets, reps, and duration.

The system is designed with reusable exercises, ensuring that the same exercise can be used across multiple workouts. It follows RESTful API principles and enforces data integrity through validations and constraints.

Installation Instructions
1. Clone the repository
git clone <your-repo-url>
cd Workout-Application-Backend-Flask-SQLAlchemy
2. Install dependencies using Pipenv
pipenv install
pipenv shell
3. Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development
4. Initialize and migrate the database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
5. Seed the database
python seed.py
Run Instructions
Start the Flask server:

flask run
The API will run at:

http://127.0.0.1:5000/

API Endpoints
Workouts
GET /workouts → Retrieve all workouts GET /workouts/<id> → Retrieve a single workout POST /workouts → Create a new workout PATCH /workouts/<id> → Update a workout DELETE /workouts/<id> → Delete a workout

Exercises
GET /exercises → Retrieve all exercises GET /exercises/<id> → Retrieve a single exercise POST /exercises → Create a new exercise PATCH /exercises/<id> → Update an exercise DELETE /exercises/<id> → Delete an exercise

Workout-Exercises (Association)
POST /workout_exercises → Add exercise to workout PATCH /workout_exercises/<id> → Update sets/reps/duration DELETE /workout_exercises/<id> → Remove exercise from workout

Tech Stack
Python 3.8+ Flask Flask-SQLAlchemy Flask-Migrate Marshmallow SQLite

Features
RESTful API design Many-to-many relationship between workouts and exercises Data validation using Marshmallow Database migrations using Flask-Migrate Seed data for testing Clean project structure

Project Structure
. ├── LICENSE ├── README.md ├── requirements.txt ├── server │ ├── app.py │ ├── instance │ │ └── app.db │ ├── migrations │ │ ├── alembic.ini │ │ ├── env.py │ │ ├── README │ │ ├── script.py.mako │ │ └── versions │ ├── models.py │ ├── pycache │ │ ├── app.cpython-312.pyc │ │ └── models.cpython-312.pyc │ └── seed.py └── venv ├── bin │ ├── activate │ ├── activate.csh │ ├── activate.fish │ ├── Activate.ps1 │ ├── alembic │ ├── flask │ ├── mako-render │ ├── pip │ ├── pip3 │ ├── pip3.12 │ ├── python -> python3 │ ├── python3 -> /usr/bin/python3 │ └── python3.12 -> python3 ├── include │ ├── python3.12 │ └── site ├── lib │ └── python3.12 ├── lib64 -> lib └── pyvenv.cfg

Testing
Run tests using: python3 seed.py

Author
METRINE MONGARE

License
This project is licensed under the apache license.