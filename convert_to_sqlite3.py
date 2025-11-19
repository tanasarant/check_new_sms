"""
This script demonstrates how to store a Python variable (that contains JSON-like data)
into a SQLite database file. SQLite is a lightweight, file-based database engine that
lets you query data later using SQL commands.

We assume you already have a Python variable named `data` which contains the same
structure as the 'data.json' file shown earlier. We'll drop the "total" key (just like
we did when exporting to CSV) and insert each message (M1, M2, etc.) into a table.

Steps:
1. Import the `sqlite3` module (built-in in Python).
2. Define your variable `data` with the JSON-like structure.
3. Connect to a SQLite database file (e.g., "messages.db").
   - If the file does not exist, SQLite will create it.
4. Create a table named `messages` with appropriate columns.
5. Iterate through the dictionary items, skipping the "total" key.
6. Insert each message into the table.
7. Commit the changes and close the connection.
"""

import sqlite3  # Provides functions to work with SQLite databases
from check_new_sms import data

def convert_to_sqlite3(data, db_filename):
    
    # Step 3: Connect to SQLite database file (creates "messages.db" if not exists)
    conn = sqlite3.connect(db_filename)
    
    # Step 4: Create a cursor object to execute SQL commands
    cur = conn.cursor()
    
    # Step 4: Create the table (if not already exists)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
    id TEXT PRIMARY KEY,
    phone TEXT,
    date TEXT,
    tag TEXT,
    msg TEXT,
    read INTEGER,
    class INTEGER,
    storeInSim INTEGER)""")
    
    # Step 5: Iterate through the dictionary items
    for key, value in data.items():
        if key == "total": continue  # Skip the "total" key
        
        # Step 6: Insert each message into the table
        cur.execute("""
        INSERT OR REPLACE INTO messages (id, phone, date, tag, msg, read, class, storeInSim)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (
        key,  # id column (M1, M2, etc.)
        value.get("phone"),
        value.get("date"),
        value.get("tag"),
        value.get("msg"),
        value.get("read"),
        value.get("class"),
        value.get("storeInSim")))
        
    # Step 7: Commit changes to save data into the file
    conn.commit()
        
    # Step 7: Close the connection
    conn.close()

"""
After running this script:
- A file named 'messages.db' will appear in your working directory.
- It contains a table 'messages' with rows for each message (M1, M2, ...).
- You can query it later using SQL commands, for example:
  SELECT * FROM messages WHERE phone='GOMO-AIS';
"""
db_filename = 'messages.db'
convert_to_sqlite3(data,db_filename)
print(db_filename, " created.")

