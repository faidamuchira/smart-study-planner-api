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
        
        # Convert response to JSON and print
        print(response.json())
        
    except Exception as err:
        print("Error sending POST request:", err)
        
def get_sessions_client():
    # Send a GET request to retrieve all study sessions.
    try:
        # Send GET request to /sessions endpoint
        response = requests.get(f"{BASE_URL}/sessions")
        
        print("\n All Study Sessions: ")
        # Print JSON response
        print(response.json())
        
    except Exception as err:
        print("Error fetching sessions:", err)
        
def get_recommendation_client():
    # Send a GET request to get a study recommendation.
    
    try:
        # Send GET request to /recommend endpoint
        response = requests.get(f"{BASE_URL}/recommend")
        
        print("\n Study Recommendation:")
        
        # print json response
        print(response.json())

    except Exception as e:
        print("Error getting recommendation:", e)
        
        

        


        
if __name__ == "__main__":
    get_sessions_client()
    get_recommendation_client()
    
