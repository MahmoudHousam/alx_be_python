def daily_reminder():
    task = input("Enter your task: ")
    priority = input("riority (high/medium/low): ")
    time_bouned = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high":
            if time_bouned == "yes":
                print(
                    f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
                )
            elif time_bouned == "no":
                print(
                    f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time."
                )
        case "medium":
            if time_bouned == "yes":
                print(
                    f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
                )
            elif time_bouned == "no":
                print(
                    f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time."
                )
        case "low":
            if time_bouned == "yes":
                print(
                    f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
                )
            elif time_bouned == "no":
                print(
                    f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
                )


if __name__ == "__main__":
    daily_reminder()
