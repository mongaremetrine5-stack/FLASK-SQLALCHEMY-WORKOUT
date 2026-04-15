from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import date

db = SQLAlchemy()

    #Exercise model
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise', cascade='all, delete')

    @validates('name')
    def validate_name(self, key, value):
        if len(value) < 3:
            raise ValueError("Exercise name too short")
        return value
    
    # Workout model 
class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship('WorkoutExercise', back_populates='workout', cascade='all, delete')

    @validates('duration_minutes')
    def validate_duration(self, key, value):
        if value <= 0:
            raise ValueError("Duration must be positive")
        return value

    
    # Workout  Exercise model
class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)

    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

    __table_args__ = (
        db.UniqueConstraint('workout_id', 'exercise_id', name='unique_workout_exercise'),
    )

    @validates('reps', 'sets', 'duration_seconds')
    def validate_numbers(self, key, value):
        if value is not None and value <= 0:
            raise ValueError("Must be positive")
        return value