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
        
    