import sqlite3
import pandas as pd

# Step 1: Connect to the SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('/Users/aryanjain/Documents/python_ex_DS593/health_events_data.db')
cursor = conn.cursor()

# Step 2: Load the CSV file using Pandas
df = pd.read_csv('/Users/aryanjain/Documents/python_ex_DS593/funny_epidemiological_events.csv')

# Step 3: Create a table in SQLite
cursor.execute('''
    CREATE TABLE IF NOT EXISTS epidemiological_events (
        event_id REAL,
        condition TEXT,
        agent TEXT,
        reporting_agency TEXT,
        affected_population REAL,
        city TEXT,
        event_start_date TEXT,
        event_end_date TEXT,
        outcome TEXT,
        cost_of_damages REAL
    )
''')

# Step 4: Insert the data into the SQLite table
df.to_sql('epidemiological_events', conn, if_exists='replace', index=False)

# Step 5: Commit the changes and close the connection
conn.commit()
conn.close()

print("Data imported successfully into health_events_data.db!")
