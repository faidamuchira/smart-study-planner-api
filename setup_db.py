import mysql.connector
from config import db_config  # Import full config (includes database)

try:
    # Create a copy of the config dictionary
    # This prevents modifying the original config used elsewhere
    db_config_no_db = db_config.copy()

    # Remove the 'database' key because the database may not exist yet
    # The connection will fail when creating the DB if we keep it
    db_config_no_db.pop("database")

    # Connect to MySQL server (without selecting a database)
    conn = mysql.connector.connect(**db_config_no_db)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create the database if it does not already exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS study_planner")

    # Select the new database
    cursor.execute("USE study_planner")

    # Create the table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_sessions (
            id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique ID for each session
            subject VARCHAR(100),                -- Subject studied
            duration INT,                        -- Duration in minutes
            difficulty INT,                      -- Difficulty rating (1–5)
            date DATE                            -- Date of study session
        )
    """)

    # Print confirmation message
    print("Database and table created successfully!")

    # Close the connection to free resources
    conn.close()

except Exception as e:
    # Catch and print any errors that occur
    print("Error:", e)