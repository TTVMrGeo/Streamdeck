import tkinter as tk
from tkinter import messagebox
import os, requests
from secret_stuff import OWNER, REPO, GITHUB_TOKEN

def update_check():
    VERSION = open("version.txt", "r").read()

    def update_now():
        try:
            os.system('git pull master master')
            messagebox.showinfo("Update complete", "Update has been completed!")
            open("version.txt", "w").write(check_latest_github_version(VERSION))
        except Exception as e:
            messagebox.showinfo("Update complete", f"Update has failed!\n{e}")
        root.destroy()

    def not_now():
        root.destroy()  # Simply close the window

    # Create the main window
    root = tk.Tk()
    root.title("Update Available!")
    root.geometry("300x150")  # Set window size

    # Add a label
    label = tk.Label(root, text=f"A new update is available!\nWould you like to install it now?")
    label.pack(pady=20)

    # Add the Update button
    update_btn = tk.Button(root, text="Update Now", command=update_now, width=15)
    update_btn.pack(pady=5)

    # Add the Not Now button
    notnow_btn = tk.Button(root, text="Not Now", command=not_now, width=15)
    notnow_btn.pack(pady=5)

    def check_latest_github_version(current_version):
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"

        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json"
        }

        try:
            response = requests.get(url)
            response.raise_for_status()
            latest_release = response.json()
            latest_version = latest_release['tag_name']
            
            if latest_version != current_version:
                root.mainloop()
                return f"Update available: {latest_version}"
        except Exception as e:
            return f"Error checking version: {e}"

    return(check_latest_github_version(VERSION))