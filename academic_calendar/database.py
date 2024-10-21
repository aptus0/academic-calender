import sqlite3

# Veritabanı bağlantısı
def connect_db():
    conn = sqlite3.connect('academic_calendar.db')
    return conn

# Etkinlik ekleme fonksiyonu
def add_event_to_db(date, event):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events (date, event) VALUES (?, ?)", (date, event))
    conn.commit()
    conn.close()

# Tüm etkinlikleri alma fonksiyonu
def get_all_events():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT date, event FROM events")
    events = cursor.fetchall()
    conn.close()
    return events

# Etkinlik silme fonksiyonu
def delete_event_from_db(event_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
    conn.commit()
    conn.close()

# Etkinlik güncelleme fonksiyonu
def update_event_in_db(event_id, new_date, new_event):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE events SET date = ?, event = ? WHERE id = ?", (new_date, new_event, event_id))
    conn.commit()
    conn.close()
