task=input("Enter your task: ")
Priority=input("Priority (high/medium/low): ").lower()
Time_bound=input("Is it time-bound? (yes/no): ").lower()
match Priority:
    case "high":
        if Time_bound=="yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a high priority task. Consider completing it when you have free time")
    case "medium":
        if Time_bound=="yes":
            print(f"Reminder: {task} is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a medium priority task. Consider completing it when you have free time")
    case "low":
        if Time_bound=="yes":
            print(f"Reminder: {task} is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time")
        