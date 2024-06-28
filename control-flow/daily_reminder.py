def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bouned = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high":
            if time_bouned == "yes":
                print(
                    f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
                )
            else:
                print(
                    f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time."
                )
        case _:
            print(
                f"'{task}' is a {priority} priority task. Consider completing it at your convenience."
            )


if __name__ == "__main__":
    daily_reminder()
