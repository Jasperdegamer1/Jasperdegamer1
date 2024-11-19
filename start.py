import os
import subprocess
import threading
import webbrowser
import tkinter as tk
from tkinter import messagebox

# De map waarin je project zich bevindt
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_FILE = os.path.join(PROJECT_DIR, 'server.js')
# Specifiek IP-adres gebruiken in plaats van localhost
BROWSER_URL = "http://172.21.0.78:3000"

# Functie om de server te starten
def start_server():
    try:
        # Start de server in een nieuw proces
        subprocess.run(["node", SERVER_FILE], check=True)
    except Exception as e:
        messagebox.showerror("Fout", f"Er is een fout opgetreden bij het starten van de server: {e}")

# Functie om de browser te openen
def open_browser():
    try:
        # Open de browser met de URL van de chatapp
        webbrowser.open(BROWSER_URL)
    except Exception as e:
        messagebox.showerror("Fout", f"Er is een fout opgetreden bij het openen van de browser: {e}")

# Functie om de server en browser te starten
def start_app():
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # Open de browser na een korte vertraging
    root.after(2000, open_browser)

# Functie om de GUI te sluiten
def quit_app():
    if messagebox.askokcancel("Afsluiten", "Weet je zeker dat je de applicatie wilt afsluiten?"):
        root.quit()

# GUI instellen met tkinter
root = tk.Tk()
root.title("Chat App Starter")
root.geometry("300x200")

label = tk.Label(root, text="Start de Chat App Server en Client", font=("Arial", 12))
label.pack(pady=20)

start_button = tk.Button(root, text="Start Chat App", command=start_app, bg="#4CAF50", fg="white", padx=10, pady=5)
start_button.pack(pady=10)

quit_button = tk.Button(root, text="Afsluiten", command=quit_app, bg="#f44336", fg="white", padx=10, pady=5)
quit_button.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", quit_app)
root.mainloop()
