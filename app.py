from flask import Flask, request, jsonify
from db_utils import get_all_sessions, add_session, get_recommendation

# Create Flask app instance
app = Flask(__name__)

@app.route("/")
def home():
    # A simple route to check if the API is running.
    return {"message": "Smart Study Planner API is running"}

@app.route("/sessions", methods=["GET"])
def get_sessions():
    # Retrieve all study sessions from the database
    try:
        sessions = get_all_sessions()
        
        # Return data as JSON with HTTP 200(OK)
        return jsonify(sessions), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/sessions", methods=["POST"])
def create_session():
    # Add a new study session with validation
    
    try:
        data = request.get_json()
        
        # Check if request body exists
        if not data:
            return jsonify({"error": "No data provided"}),400
        
        # Required fields
        required_fields = ["subject", "duration", "difficulty", "date"]
        
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        # Type validation
        if not isinstance(data["subject"], str):
            return jsonify({"error": "Subject must be a string"}), 400

        if not isinstance(data["duration"], int):
            return jsonify({"error": "Duration must be an integer"}), 400

        if not isinstance(data["difficulty"], int):
            return jsonify({"error": "Difficulty must be an integer"}), 400

        # Logical validation
        if data["duration"] <= 0:
            return jsonify({"error": "Duration must be greater than 0"}), 400

        if not (1 <= data["difficulty"] <= 5):
            return jsonify({"error": "Difficulty must be between 1 and 5"}), 400

        # Call DB function
        result = add_session(
            data["subject"],
            data["duration"],
            data["difficulty"],
            data["date"]
        )

        return jsonify({"message": result}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True)