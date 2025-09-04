from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)

    # In-memory store for workouts
    workouts = []

    @app.route("/")
    def home():
        return "Welcome to ACEest Fitness and Gym!", 200

    # Members endpoint
    @app.route("/members")
    def get_members():
        members = [
            {"id": 1, "name": "Alice Johnson", "age": 28, "membership": "Gold"},
            {"id": 2, "name": "Bob Smith", "age": 35, "membership": "Silver"},
            {"id": 3, "name": "Charlie Brown", "age": 22, "membership": "Platinum"},
        ]
        return jsonify({"members": members})


    # Trainers endpoint
    @app.route("/trainers")
    def get_trainers():
        trainers = [
            {"id": 1, "name": "David Miller", "specialty": "Strength Training"},
            {"id": 2, "name": "Emma Wilson", "specialty": "Yoga"},
        ]
        return jsonify({"trainers": trainers})


    # Health stats endpoint
    @app.route("/health")
    def health_check():
        return jsonify({"status": "ok", "app": "ACEEST Fitness API"})

    @app.route("/workouts", methods=["GET"])
    def get_workouts():
        workouts = [
            {"id": 1, "title": "Full Body Workout", "duration": 60},
            {"id": 2, "title": "Cardio Blast", "duration": 30},
            {"id": 3, "title": "Yoga Flow", "duration": 45},
        ]
        return jsonify({"workouts": workouts}), 200

    @app.route("/workouts", methods=["POST"])
    def add_workout():
        data = request.get_json(silent=True) or {}
        workout = (data.get("workout") or "").strip()
        duration = data.get("duration")

        if not workout or duration is None:
            return jsonify({"error": "Please provide both workout and duration"}), 400

        try:
            duration = int(duration)
        except ValueError:
            return jsonify({"error": "Duration must be a number"}), 400

        workouts.append({"workout": workout, "duration": duration})
        return jsonify({"message": f"'{workout}' added successfully!", "workouts": workouts}), 201

    @app.route("/workouts/<int:index>", methods=["DELETE"])
    def delete_workout(index):
        if 0 <= index < len(workouts):
            removed = workouts.pop(index)
            return jsonify({"message": f"Removed {removed['workout']}", "workouts": workouts}), 200
        return jsonify({"error": "Invalid workout index"}), 404

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
