import requests

# Base URL of your Flask API
BASE_URL = "http://127.0.0.1:5000"

def add_session_client(subject, duration, difficulty, date):
    """
    Send a POST request to add a new study session.

    Parameters:
    - subject (str): Name of the subject
    - duration (int): Duration in minutes
    - difficulty (int): Difficulty level (1–5)
    - date (str): Date in format YYYY-MM-DD
    """
    
    # Create JSON payload to send to API 
    data = {
        "subject": subject,
        "duration": duration,
        "difficulty": difficulty,
        "date": date
    }
    
    try:
        # Send POST request to /sessions endpoint
        response = requests.post(f"{BASE_URL}/sessions", json=data)
        
        print("\n Add Session Response: ")
        
        # Convert response to JSON and message from the API
        print(response.json()["message"])
        
    except Exception as err:
        # Catch connection issue errors
        print("Error sending POST request:", err)
        
def get_sessions_client():
    # Send a GET request to retrieve all study sessions.
    try:
        # Send GET request to /sessions endpoint
        response = requests.get(f"{BASE_URL}/sessions")
        # Convert JSON response into Python list
        sessions = response.json()
        
        print("\n All Study Sessions: ")
        # Handle case where no data exist
        if not sessions:
            print("No study sessions found.\n")
            return

        # Loop through each session and print details clearly
        for session in sessions:
            print(f"ID: {session['id']}")
            print(f"Subject: {session['subject']}")
            print(f"Duration: {session['duration']} mins")
            print(f"Difficulty: {session['difficulty']}")
            print(f"Date: {session['date']}")
            print("-" * 30)
        
    except Exception as err:
        # Catch error during request
        print("Error fetching sessions:", err)
        
def get_recommendation_client():
    # Send a GET request to get a study recommendation.
    
    try:
        # Send GET request to /recommend endpoint
        response = requests.get(f"{BASE_URL}/recommend")
        
        # Convert response to JSON
        data = response.json()
        
        print("\n 💡Study Recommendation:\n")
        
        # Display recommendation message
        print(data["recommendation"])

    except Exception as e:
        print("Error getting recommendation:", e)
        
def run():
    """
    Simulate a realistic user interaction with the API.

    This function:
    1. Checks if the API is running
    2. Adds multiple study sessions
    3. Retrieves all sessions
    4. Gets a recommendation
    """
    
    print("\n" + "=" * 40)
    print("📚 Welcome to Smart Study Planner API\n")
    print("=" * 40)

    # Check if API is running
    try:
        response = requests.get(BASE_URL)

        if response.status_code != 200:
            print("⚠️ API is not responding correctly.")
            return

        print("✅ API is running successfully!\n")

    except Exception:
        print("❌ Could not connect to API. Make sure app.py is running.")
        return

    # Add multiple study sessions (different subjects for better testing)
    print("➡️ Adding study sessions...\n")

    add_session_client("Math", 60, 3, "2026-05-04")
    add_session_client("Python", 45, 2, "2026-05-04")
    add_session_client("History", 30, 4, "2026-05-04")

    # Retrieve all sessions
    print("\n➡️ Fetching all study sessions...\n")
    get_sessions_client()

    # Get recommendation
    print("\n➡️ Getting study recommendation...\n")
    get_recommendation_client()

    print("\nSimulation complete!")
        
        
if __name__ == "__main__":
    run()
    
