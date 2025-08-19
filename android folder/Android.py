import tkinter as tk
import time
import math

# Create full-screen window
root = tk.Tk()
root.title("Android OS Simulation")
root.attributes('-fullscreen', True)
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

GOOGLE_COLORS = ["#EA4335", "#34A853", "#FBBC05", "#4285F4"]  # red, green, yellow, blue

# --- Startup Animation ---
def draw_rotating_g(angle):
    canvas.delete("all")
    x, y = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2 - 100
    radius = 80
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline=GOOGLE_COLORS[3], width=10)
    tail_x = x + radius * math.cos(angle)
    tail_y = y + radius * math.sin(angle)
    canvas.create_line(x, y, tail_x, tail_y, fill=GOOGLE_COLORS[0], width=10)
    canvas.create_text(x, y, text="G", font=("Arial", 60, "bold"), fill=GOOGLE_COLORS[3])
    root.update()

def animate_g():
    for i in range(60):
        angle = i * (math.pi / 30)
        draw_rotating_g(angle)
        time.sleep(0.05)

def animate_google_text():
    canvas.delete("all")
    text = "Google"
    x_start = root.winfo_screenwidth() // 2 - 210
    y = root.winfo_screenheight() // 2 - 100
    for i, letter in enumerate(text):
        canvas.create_text(x_start + i * 70, y, text=letter, font=("Arial", 80, "bold"), fill=GOOGLE_COLORS[i % len(GOOGLE_COLORS)])
        root.update()
        time.sleep(0.3)

def draw_loading_bar():
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    canvas.create_text(w // 2, h // 2, text="Loading...", font=("Arial", 30), fill="gray")
    bar_x, bar_y = w // 2 - 200, h // 2 + 50
    bar_width = 400
    bar_height = 30
    canvas.create_rectangle(bar_x, bar_y, bar_x + bar_width, bar_y + bar_height, outline="gray", width=2)
    for i in range(0, bar_width + 1, 4):
        canvas.create_rectangle(bar_x, bar_y, bar_x + i, bar_y + bar_height, fill="gray", outline="")
        root.update()
        time.sleep(0.02)

# --- Shutdown ---
def show_shutdown_screen():
    shutdown = tk.Toplevel(root)
    shutdown.geometry("400x200+200+200")
    shutdown.title("Shutdown")
    shutdown.configure(bg="white")
    tk.Label(shutdown, text="Shutdown %", font=("Arial", 20), fg="red", bg="white").pack(pady=20)
    tk.Label(shutdown, text="Android is shutdown", font=("Arial", 14), bg="white").pack()
    shutdown.after(2000, root.destroy)

# --- Control Panel ---
def show_control_panel():
    panel = tk.Toplevel(root)
    panel.geometry("800x100+0+0")
    panel.overrideredirect(True)
    panel.configure(bg="#DDDDDD")
    tk.Label(panel, text="Control Panel", font=("Arial", 14), bg="#DDDDDD").pack(side="left", padx=20)
    tk.Button(panel, text="Shutdown", command=show_shutdown_screen).pack(side="right", padx=20)
    panel.after(3000, panel.destroy)

# --- Apps ---
def show_app_window(title, content_lines, color):
    app = tk.Toplevel(root)
    app.attributes('-fullscreen', True)
    app.title(title)
    app.configure(bg="white")
    tk.Label(app, text=title, font=("Arial", 30, "bold"), fg=color, bg="white").pack(pady=20)
    for line in content_lines:
        tk.Label(app, text=line, font=("Arial", 16), bg="white").pack()
    tk.Label(app, text=f"Closing {title} App %", font=("Arial", 12), fg="gray", bg="white").pack(side="bottom", pady=20)
    app.after(3000, app.destroy)

def show_settings_screen():
    settings = [
        "Connections %", "Sound %", "Vibration %", "Notifications %",
        "Display %", "Wallpaper %", "Lock screen %", "Security %",
        "Privacy %", "Location %", "Google %", "Accounts and Backup %",
        "Battery %", "Software Update %", "Accessibility %", "About Android %"
    ]
    show_app_window("Settings", settings, "#4285F4")

def show_messages_screen():
    show_app_window("Messages", ["Messages opening %"], "#EA4335")

def show_calls_screen():
    show_app_window("Calls", ["Calls opening %"], "#34A853")

# --- Launcher ---
def show_android_launcher():
    canvas.delete("all")
    canvas.create_text(root.winfo_screenwidth() // 2, 50, text="Android Launcher", font=("Arial", 30, "bold"), fill="#4285F4")
    icons = ["📞", "💬", "⚙️"]
    labels = ["Calls", "Messages", "Settings"]

    def launch_app(name):
        if name == "Settings":
            show_settings_screen()
        elif name == "Messages":
            show_messages_screen()
        elif name == "Calls":
            show_calls_screen()

    for i in range(3):
        x = root.winfo_screenwidth() // 2 - 150 + i * 150
        y = root.winfo_screenheight() // 2
        btn = tk.Button(root, text=f"{icons[i]}\n{labels[i]}", font=("Arial", 14), command=lambda n=labels[i]: launch_app(n))
        btn.place(x=x - 40, y=y - 40, width=80, height=80)

    canvas.bind("<Button-1>", lambda e: show_control_panel())

# --- Sequence ---
def run_full_sequence():
    animate_g()
    animate_google_text()
    draw_loading_bar()
    show_android_launcher()

root.after(500, run_full_sequence)
root.mainloop()