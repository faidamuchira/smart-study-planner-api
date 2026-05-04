from flask import Flask, request, jsonify
#from db_utils import get_all_sessions, add_sessions, get_recommendation

# Create Flask app instance
app = Flask(__name__)

@app.route("/")
def home():
    # A simple route to check if the API is running.
    return {"message": "Smart Study Planner API is running"}

if __name__ == "__main__":
    app.run(debug=True)