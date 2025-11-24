from datetime import date, datetime
FILE = "health.txt"
DATE_FMT = "%Y-%m-%d"
def ensure_file():
    """Create file if missing."""
    try:
        open(FILE, "r").close()
    except FileNotFoundError:
        open(FILE, "w").close()
def date_input(s):
    s = s.strip()
    if s == "":
        return date.today().strftime(DATE_FMT)
    try:
        datetime.strptime(s, DATE_FMT)
        return s
    except ValueError:
        return None
def add_entry():
    print("\nEnter Data:")
    today = date.today().strftime(DATE_FMT)
    while True:
        d = input(f"Date [{today}]: ").strip() or today
        if date_input(d):
            break
        print("Invalid")
    weight = input("Weight (kg): ").strip()
    steps = input("Steps : ").strip()
    sleep = input("Sleep hours : ").strip()
    notes = input("Notes (if any) : ").strip()
    enter_data = f"{d} | weight={weight} | steps={steps} | sleep={sleep} | notes={notes}\n"
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(enter_data)
def view():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Try Again...\n")
        return
    if not lines:
        print("Try Again...\n")
        return
    print("\nYour Entries...")
    for idx, line in enumerate(lines, start=1):
        print(f"{idx}. {line.strip()}")
    print()
def delete_entry():
    view()
    try:
        num = int(input("Enter entry number to delete = "))
    except:
        print("Try Again....")
        return
    if num == 0:
        print("Removed...")
        return
    with open(FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    del lines[num - 1]
    with open(FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("Removed...\n")
def stats():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No Data, Try Again...\n")
        return
    weights = []
    sleeps = []
    for line in lines:
        parts = line.split("|")
        for p in parts:
            p = p.strip()
            if p.startswith("weight="):
                val = p.replace("weight=", "").strip()
                if val:
                    try:
                        weights.append(float(val))
                    except:
                        pass
            if p.startswith("sleep="):
                val = p.replace("sleep=", "").strip()
                if val:
                    try:
                        sleeps.append(float(val))
                    except:
                        pass
    print("\nSimple Stats...")
    if weights:
        print(f"Avg Weight: {sum(weights) / len(weights):.2f} kg")
    else:
        print("No Data Found, Try Again...")
    if sleeps:
        print(f"Avg Sleep: {sum(sleeps) / len(sleeps):.2f} hours")
    else:
        print("No Data Found, Try Again...")
    print()
def main():
    ensure_file()
    while True:
        print("Health Tracker.")
        print("1) Add Entry.")
        print("2) View Entries.")
        print("3) Delete Entry.")
        print("4) Show Stats.")
        print("0) Quit.")
        T=input("Enter Option...=")
        if T == "1":
            add_entry()
        elif T == "2":
            view()
        elif T == "3":
            delete_entry()
        elif T == "4":
            stats()
        else:
            print("Thank You...")
            break
main()