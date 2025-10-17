import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "db.db")  # adjust if needed

def addProfile(username, password, country):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    cursor = conn.cursor()
    print("inserting name: ")
    print(username)
    cursor.execute("INSERT INTO Profiles (username, password, country) VALUES (?, ?, ?)", (username, password, country))
    conn.commit()
    print("Profile added successfully.")

    cursor.close()
    conn.close()




def get_email_ig_without_ap():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    
    cursor = conn.cursor()
    cursor.execute("SELECT * from GmailProfiles where ig_used = 0 AND app_password is NULL Limit 1")

    conn.commit()
    
    row = cursor.fetchone()
    conn.close()
    if row:
        return (row[0], row[1],  row[2], row[3], row[4])

def get_gmail_ig():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    
    cursor = conn.cursor()
    cursor.execute("SELECT * from GmailProfiles where ig_used = 0 Limit 1")
    row = cursor.fetchone()
    
    #cursor.execute("UPDATE GmailProfiles SET ig_used = ? WHERE id = ?", (1, row[0]))
    conn.commit()
    
    conn.close()
    if row:
        return (row[0], row[1],  row[2], row[3], row[4])
    
def get_gmx_ig():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    
    cursor = conn.cursor()
    cursor.execute("SELECT * from GmxProfiles where ig_used = 0 Limit 1")
    row = cursor.fetchone()
    
    #cursor.execute("UPDATE GmxProfiles SET ig_used = ? WHERE id = ?", (1, row[0]))
    conn.commit()
    
    conn.close()
    if row:
        print(row[0])
        return (row[0], row[1],  row[2], row[3])
    

def get_gmx_tt():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    
    cursor = conn.cursor()
    cursor.execute("SELECT * from GmxProfiles where tt_used = 0 Limit 1")
    row = cursor.fetchone()
    
    #cursor.execute("UPDATE GmxProfiles SET ig_used = ? WHERE id = ?", (1, row[0]))
    conn.commit()
    
    conn.close()
    if row:
        print(row[0])
        return (row[0], row[1],  row[2], row[3])
    


def set_ig_used_gmx(profile_id):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    cursor = conn.cursor()
    cursor.execute("UPDATE GmxProfiles SET ig_used = ? WHERE id = ?", (1, profile_id))
    conn.commit()
    conn.close()
    

def set_tt_used_gmx(profile_id):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    cursor = conn.cursor()
    cursor.execute("UPDATE GmxProfiles SET tt_used = ? WHERE id = ?", (1, profile_id))
    conn.commit()
    conn.close()


def get_email_fb():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    
    cursor = conn.cursor()
    cursor.execute("SELECT * from Profiles where fb_used = 0 AND app_password is NULL Limit 1")
    row = cursor.fetchone()

    if row:
        id = row[0]
        return (row[0], row[1], row[2])
    else:
        print("No matching row found.")

    conn.close()



def copy_to_database_gmail_ig(filename):
    accounts_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "accounts/ig_accounts.txt")
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    cursor = conn.cursor()
    with open(accounts_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or ':' not in line:
                continue
            try:
                parts = line.split(':', 3)
                gmail_email = parts[0].strip()
                gmail_password = parts[1].strip()
                two_fa = parts[3].strip()
                cursor.execute('INSERT INTO GmailProfiles (email, password, "2fa", ig_used) VALUES (?, ?, ?, ?)', 
                               (gmail_email, gmail_password ,two_fa, 0))
            except ValueError as e:
                print(f"Skipping invalid line: {line}")
    conn.commit()
    conn.close()


def copy_to_database_gmx_ig(filename):
    accounts_path = os.path.join((os.path.dirname(os.path.dirname(__file__))), "accounts/gmx_accounts.txt")
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    cursor = conn.cursor()
    with open(accounts_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or ':' not in line:
                continue
            try:
                parts = line.split(':', 2)
                gmx_email = parts[0].strip()
                gmx_password = parts[1].strip()
      
                cursor.execute('INSERT INTO GmxProfiles (email, password, ig_used, tt_used) VALUES (?, ?, ?, ?)', 
                               (gmx_email, gmx_password, 0, 0))
                
            except ValueError as e:
                print(f"Skipping invalid line: {line}")
    conn.commit()
    conn.close()




def add_app_password(id, app_password):
    """Create a database connection to the SQLite database specified by db_file."""
    print("adding app password")
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    cursor = conn.cursor()
    cursor.execute("UPDATE GmailProfiles SET app_password = ? WHERE id = ?", (app_password, id))
    conn.commit()
    print("App password added successfully.")

    cursor.close()
    conn.close()


def add_instagram_account(username, password, email, two_fa):
    """Create a database connection to the SQLite database specified by db_file."""
    print("adding instagram account")
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO InstagramAccounts (username, password, email, two_fa) VALUES (?, ?, ?, ?)", 
                   (username, password, email, two_fa))
    conn.commit()
    print("Instagram account added successfully.")
    cursor.close()
    conn.close()


def add_tiktok_account(username, password, email):
    print("adding tiktok account")
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    cursor = conn.cursor()
    cursor.execute("INSERT INTO TiktokProfiles (username, password, email) VALUES (?, ?, ?)", 
                   (username, password, email))
    conn.commit()
    print("Tiktok account added successfully.")

    cursor.close()
    conn.close()


def get_all_gmx():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    cursor = conn.cursor()
    cursor.execute("SELECT * from GmxProfiles WHERE tt_used = 0")
    #conn.commit()
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_gmx_by_id(id):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database")
    
    cursor = conn.cursor()
    cursor.execute(f"SELECT * from GmxProfiles WHERE id = {id}")
    row = cursor.fetchone()
    conn.close()
    return row

#get_all_gmx()
#get_gmx_ig()
#copy_to_database_gmx_ig("gmx_accounts.txt")
