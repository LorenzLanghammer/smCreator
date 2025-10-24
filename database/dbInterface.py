import sqlite3
import os
from structures import *

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "db.db")

    

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


def copy_to_database_gmail(filename):
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


def copy_to_database_gmx(filename):
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


def add_tiktok_account(username, password, email, cookies, country):
    print("adding tiktok account")
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    cursor = conn.cursor()
    cursor.execute("INSERT INTO TiktokProfiles (username, password, email, cookies, country) VALUES (?, ?, ?, ?, ?)", 
                   (username, password, email, cookies, country))
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


def get_random_tt():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database")
    
    cursor = conn.cursor()
    cursor.execute(f"SELECT * from TiktokProfiles WHERE Country IS NOT NULL ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return Account(row[1], row[2], row[3], row[4], row[5])



#get_all_gmx()
#get_gmx_ig()
#copy_to_database_gmx("gmx_accounts.txt")
