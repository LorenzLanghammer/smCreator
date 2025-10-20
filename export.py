from database.dbInterface import *


def export_tt_accounts():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error connecting to database")
    
    cursor = conn.cursor()
    cursor.execute(f"SELECT username, TiktokProfiles.password, GmxProfiles.email, GmxProfiles.password FROM GmxProfiles INNER JOIN TiktokProfiles ON TiktokProfiles.email = GmxProfiles.id")
    rows = cursor.fetchall()

    with open("accounts/tiktok_accounts.txt", "w") as file:
        for row in rows:
            file.write(f"{row[0]}:{row[1]}:{row[2]}:{row[3]}\n")
            

    conn.close()
    return rows

export_tt_accounts()