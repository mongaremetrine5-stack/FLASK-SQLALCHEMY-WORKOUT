#!/usr/bin/env python3
#!/usr/bin/env python3

from app import app
from models import db, Workout, Exercise, WorkoutExercise
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # Exercises
    e1 = Exercise(name="Push Ups", category="Strength", equipment_needed=False)
    e2 = Exercise(name="Running", category="Cardio", equipment_needed=False)

    # Workout
    w1 = Workout(date=date.today(), duration_minutes=45, notes="Morning workout")

    # Join
    we1 = WorkoutExercise(workout=w1, exercise=e1, sets=3, reps=15)
    we2 = WorkoutExercise(workout=w1, exercise=e2, duration_seconds=600)

    db.session.add_all([e1, e2, w1, we1, we2])
    db.session.commit()

    print("Database seeded")