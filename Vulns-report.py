import pandas as pd
from tkinter import filedialog
import tkinter as tk

# Hide the main window
root = tk.Tk()
root.withdraw()

# Ask user to pick files
print("Pick your Vulns file...")
vulns_file = filedialog.askopenfilename(title="Select Vulns CSV")

print("Pick your Agents file...")
agents_file = filedialog.askopenfilename(title="Select Agents CSV")

# Load the files
vulns = pd.read_csv(vulns_file)
agents = pd.read_csv(agents_file)

# Merge them
merged = vulns.merge(agents[['Name', 'IP address', 'Last keep alive']], left_on='agent.name', right_on='Name', how='left')

# Drop the extra 'Name' column (since agent.name already exists)
merged.drop(columns=['Name'], inplace=True)

# Save result
merged.to_csv("final_report.csv", index=False)

print("✅ Done! Saved as final_report.csv")
