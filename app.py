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

if __name__ == "__main__":
    app.run(debug=True)