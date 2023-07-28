import datetime

def add_log_entry():
    log_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = input("Enter the logging activity: ")
    with open("jungle_logs.txt", "a") as file:
        file.write(f"{log_date}: {log_entry}\n")
    print("Log entry added successfully!")

def view_all_logs():
    with open("jungle_logs.txt", "r") as file:
        logs = file.read()
        print("All Log Entries:")
        print(logs)

def search_logs_by_keyword(keyword):
    with open("jungle_logs.txt", "r") as file:
        logs = file.readlines()
        matching_logs = [log.strip() for log in logs if keyword.lower() in log.lower()]
        if matching_logs:
            print("Matching Log Entries:")
            for log in matching_logs:
                print(log)
        else:
            print("No logs found matching the given keyword.")

def main():
    print("Welcome to Jungle Logging Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add a log entry")
        print("2. View all log entries")
        print("3. Search logs by keyword")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_log_entry()
        elif choice == "2":
            view_all_logs()
        elif choice == "3":
            keyword = input("Enter the keyword to search for: ")
            search_logs_by_keyword(keyword)
        elif choice == "4":
            print("Exiting Jungle Logging Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
