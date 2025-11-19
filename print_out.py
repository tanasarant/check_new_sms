"""
This script shows how to run the SQL query
  SELECT phone, date, msg FROM sms WHERE read=0 ORDER BY date DESC;
using Python's sqlite3 module instead of the sqlite shell prompt.

Steps:
1. Import sqlite3.
2. Connect to your SQLite database file (e.g., messages.db).
3. Create a cursor to execute SQL commands.
4. Run the query exactly as written.
5. Fetch all results.
6. Print them row by row.
"""

import sqlite3
from convert_to_sqlite3 import db_filename 

def print_out(db_filename):
    
    # Step 2: Connect to the SQLite database file
    conn = sqlite3.connect(db_filename)
    
    # Step 3: Create a cursor object
    cur = conn.cursor()
    
    # Step 4: Execute the query
    cur.execute("SELECT phone, date, msg FROM messages WHERE read=0 ORDER BY date DESC;")
    
    # Step 5: Fetch all matching rows
    rows = cur.fetchall()
    
    # Close connection
    conn.close()
    
    # Step 6: Print results
    return rows 

print("you have unread SMS: ",print_out(db_filename))