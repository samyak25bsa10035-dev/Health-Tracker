# Health-Tracker
---

📘 Health Tracker (Python Console Application)

A simple and lightweight Python-based Health Tracker that allows users to record and manage daily health data using a plain text file (health.txt).
This beginner-friendly project demonstrates file handling, functions, top-down design, and basic data analysis in Python.


---

🧾 Features

✔ Add daily health entries (date, weight, steps, sleep hours, notes)
✔ View all saved entries with numbering
✔ Delete an entry by its index
✔ Calculate basic statistics
 — Average weight
 — Average sleep hours
✔ Fully offline (no database required)
✔ Uses only core Python — no external libraries


---

📂 File Structure

health-tracker/
│── health_tracker.py
│── health.txt                # auto-created if missing
│── README.md
│── project_report.pdf        # optional


---

▶ How to Run the Program

1. Install Python

Ensure Python 3.8 or above is installed:

python --version

2. Run the script

In your terminal or command prompt:

python health_tracker.py

The program will automatically create health.txt if it does not already exist.


---

🧮 How Data Is Stored

Each entry in health.txt follows this format:

YYYY-MM-DD | weight=70 | steps=10000 | sleep=7 | notes=Felt good

This makes the data readable and easy to edit manually.


---

🏗 Program Structure (Top-Down Design)

main()
│
├── ensure_file()   → Create file if missing
├── add_entry()     → Add a new entry
├── view()          → Display all entries
├── delete_entry()  → Delete selected entry
└── stats()         → Show average weight & sleep


---

📌 Example Usage

Menu displayed to the user:

Health Tracker
1) Add Entry
2) View Entries
3) Delete Entry
4) Show Stats
0) Quit
Enter option:


---

🧠 Concepts Demonstrated

File handling (open, readlines, writelines)

Functions and modular design

Date validation with datetime

Basic statistics computation

Error handling and input validation

String parsing and formatting



---

🧪 Future Enhancements

🔹 Convert text storage to CSV or JSON
🔹 Add edit entry feature
🔹 Add charts/graphs using matplotlib
🔹 Create a GUI using Tkinter
🔹 Build a Flask web interface
🔹 Export data as Excel or PDF


---

📝 License

This project is open-source and free to use