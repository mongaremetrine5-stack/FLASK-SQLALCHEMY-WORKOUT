from marshmallow import Schema, fields, validates, ValidationError

# ---------------- EXERCISE ----------------
class ExerciseSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool()

    @validates('name')
    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError("Name too short")


# ---------------- WORKOUT EXERCISE ----------------
class WorkoutExerciseSchema(Schema):
    id = fields.Int()
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()
    exercise = fields.Nested(ExerciseSchema)


# ---------------- WORKOUT ----------------
class WorkoutSchema(Schema):
    id = fields.Int()
    date = fields.Date()
    duration_minutes = fields.Int()
    notes = fields.Str()
    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True)


# instances
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)