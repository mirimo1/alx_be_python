# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Task priority '{priority}' is not recognized."

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    if priority == "low":
        message += ". Consider completing it when you have free time."
    else:
        message += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium"]:
    message += ". You can schedule it for later."

print(message)
