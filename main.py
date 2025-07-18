import tkinter as tk
from tkinter import messagebox
import re
import tldextract
import time

# Function to check if the URL is suspicious
def is_phishing(url):
    phishing_keywords = ['login', 'verify', 'update', 'bank', 'secure', 'account', 'paypal']
    ip_pattern = r'https?:\/\/\d{1,3}(\.\d{1,3}){3}'

    # Keyword check
    for keyword in phishing_keywords:
        if keyword in url.lower():
            return True

    # IP-based URL check
    if re.match(ip_pattern, url):
        return True

    # Very short domain check
    domain_info = tldextract.extract(url)
    if len(domain_info.domain) <= 3:
        return True

    return False

# Typing animation function
def animated_result(text, color):
    result_label.config(text="", fg=color)
    for i in range(len(text) + 1):
        result_label.config(text=text[:i])
        window.update()
        time.sleep(0.03)

# Function to handle button click
def check_url():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    if is_phishing(url):
        animated_result("⚠️ Phishing Link Detected!", "red")
    else:
        animated_result("✅ Safe Link", "green")

# GUI setup using Tkinter
window = tk.Tk()
window.title("Phishing Link Scanner")
window.geometry("500x250")
window.config(bg="#f0f0f0")

# GUI Widgets
title_label = tk.Label(window, text="Phishing Link Scanner", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

url_entry = tk.Entry(window, width=60, font=("Helvetica", 12))
url_entry.pack(pady=10)

check_button = tk.Button(window, text="Check Link", font=("Helvetica", 12), command=check_url, bg="#4CAF50", fg="white")
check_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#f0f0f0")
result_label.pack(pady=10)

# Start the GUI loop
window.mainloop()
