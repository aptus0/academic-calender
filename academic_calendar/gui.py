import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from academic_calendar.database import add_event_to_db, get_all_events, delete_event_from_db, update_event_in_db
from PIL import Image, ImageTk

def run_app():
    root = tk.Tk()
    root.title("Akademik Takvim")
    root.geometry("700x600")
    root.configure(bg='#F0F0F0')

    # Apple tarzı simge ekleme
    try:
        icon_image = Image.open("apple_icon.png")
        icon_image = icon_image.resize((50, 50), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon_image)
        icon_label = tk.Label(root, image=icon, bg='#F0F0F0')
        icon_label.image = icon
        icon_label.pack(pady=10)
    except Exception as e:
        print(f"İkon yüklenemedi: {e}")

    title_label = tk.Label(root, text="Akademik Takvim", bg='#F0F0F0', font=('Helvetica', 20, 'bold'))
    title_label.pack(pady=10)

    # Takvim bileşeni
    calendar = Calendar(root, selectmode='day', year=2024, month=10, day=21)
    calendar.pack(pady=10)

    # Etkinlik girişi
    event_label = tk.Label(root, text="Etkinlik:", bg='#F0F0F0', font=('Helvetica', 12))
    event_label.pack(pady=5)
    event_entry = tk.Entry(root, font=('Helvetica', 12))
    event_entry.pack(pady=5)

    selected_event = None  # Seçili etkinlik saklanacak

    def select_event(event):
        global selected_event
        selected_item = event_list.selection()
        if selected_item:
            selected_event = event_list.item(selected_item)['values']
            calendar.selection_set(selected_event[0])  # Takvimde tarihi ayarla
            event_entry.delete(0, tk.END)
            event_entry.insert(0, selected_event[1])

    def add_event():
        date = calendar.get_date()
        event = event_entry.get()
        if event:
            add_event_to_db(date, event)
            refresh_event_list()
            event_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir etkinlik girin.")

    def update_event():
        if selected_event:
            new_event = event_entry.get()
            if new_event:
                update_event_in_db(selected_event[0], calendar.get_date(), new_event)
                refresh_event_list()
            else:
                messagebox.showwarning("Uyarı", "Lütfen güncellenecek etkinliği girin.")
        else:
            messagebox.showwarning("Uyarı", "Lütfen güncellemek için bir etkinlik seçin.")

    def delete_event():
        if selected_event:
            delete_event_from_db(selected_event[0])
            refresh_event_list()
        else:
            messagebox.showwarning("Uyarı", "Lütfen silmek için bir etkinlik seçin.")

    # Düğmeler
    add_button = tk.Button(root, text="Etkinlik Ekle", command=add_event, bg='#28a745', fg='white', font=('Helvetica', 12))
    add_button.pack(pady=10)

    update_button = tk.Button(root, text="Etkinliği Güncelle", command=update_event, bg='#007bff', fg='white', font=('Helvetica', 12))
    update_button.pack(pady=5)

    delete_button = tk.Button(root, text="Etkinliği Sil", command=delete_event, bg='#dc3545', fg='white', font=('Helvetica', 12))
    delete_button.pack(pady=5)

    # Etkinlik listesi
    event_list = ttk.Treeview(root, columns=("Tarih", "Etkinlik"), show="headings", height=15)
    event_list.heading("Tarih", text="Tarih")
    event_list.heading("Etkinlik", text="Etkinlik")
    event_list.pack(pady=20, fill=tk.BOTH, expand=True)

    event_list.bind('<ButtonRelease-1>', select_event)

    def refresh_event_list():
        for row in event_list.get_children():
            event_list.delete(row)
        for row in get_all_events():
            event_list.insert('', 'end', values=row)

    refresh_event_list()
    root.mainloop()

if __name__ == "__main__":
    run_app()
