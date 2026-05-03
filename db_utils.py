import mysql.connector
from config import db_config # Import database configuration

def get_db_connection():
    # Create and return a database connection.
    return mysql.connector.connect(**db_config)
def get_all_sessions():
    '''
    Retrieve all study sessions from the database
    '''
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True) # Return results as dictionaries
        
        query = "SELECT * FROM study_sessions"
        cursor.execute(query)
        
        results = cursor.fetchall()
        
        conn.close()
        return results
    except Exception as e:
        print("Error fetching sessions:", e)
        return []

def add_session(subject, duration, difficulty, date):
    """ Insert a new study session into the database.
    
    Parameters:
    - subject (str): Name of the subject studied
    - duration (int): Duration in minutes
    - difficulty (int): Difficulty rating (e.g. 1–5)
    - date (str): Date of the session (YYYY-MM-DD)
    """
    
    try:
        # Establish connection to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # SQL query to insert a new record into the study_sessions table
        # Using placeholders (%s) to safely pass values (prevents SQL injection)
        query = """
        INSERT INTO study_sessions (subject, duration, difficulty, date)
        VALUES (%s, %s, %s, %s)
        """
        
        # Execute the query with the provided values
        cursor.execute(query, (subject, duration, difficulty, date))
        
        conn.commit() #save changes in the database
        
        conn.close() # close to free resources
        
        return "Session added successfully"
    
    except Exception as e:
        # Print error for debugging purposes
        print("Error adding session:", e)
        
        return "Error"
        
        