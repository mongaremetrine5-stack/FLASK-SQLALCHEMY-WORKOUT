from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Workout, Exercise, WorkoutExercise
from schemas import workout_schema, workouts_schema, exercise_schema, exercises_schema

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# ---------------- WORKOUT ROUTES ----------------

@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return workouts_schema.dump(workouts), 200


@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return workout_schema.dump(workout), 200


@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()

    new_workout = Workout(
        date=data.get('date'),
        duration_minutes=data.get('duration_minutes'),
        notes=data.get('notes')
    )

    db.session.add(new_workout)
    db.session.commit()

    return workout_schema.dump(new_workout), 201


@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return {"message": "Workout deleted"}, 200


# ---------------- EXERCISE ROUTES ----------------

@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return exercises_schema.dump(exercises), 200


@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    return exercise_schema.dump(exercise), 200


@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()

    new_exercise = Exercise(
        name=data.get('name'),
        category=data.get('category'),
        equipment_needed=data.get('equipment_needed', False)
    )

    db.session.add(new_exercise)
    db.session.commit()

    return exercise_schema.dump(new_exercise), 201


@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return {"message": "Exercise deleted"}, 200


# ---------------- ADD EXERCISE TO WORKOUT ----------------

@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    data = request.get_json()

    new_entry = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=exercise_id,
        sets=data.get('sets'),
        reps=data.get('reps'),
        duration_seconds=data.get('duration_seconds')
    )

    db.session.add(new_entry)
    db.session.commit()

    return {"message": "Exercise added to workout"}, 201


if __name__ == "__main__":
    app.run(port=5555, debug=True)