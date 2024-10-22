# main.py
from agent import scheduler_agent, reminder_agent, break_agent, optimizer_agent, notification_agent
from tasks import TaskManager
from crew import Crew

# Initialize the task manager
task_manager = TaskManager()

# Create the crew and add the agents
task_manager_crew = Crew(agents=[scheduler_agent, reminder_agent, break_agent, optimizer_agent, notification_agent])

# Task Manager Loop
def run_task_manager():
    print("Starting Personal Daily Routine Task Manager with Crew AI 🐝")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Check task status")
        print("4. Set a break reminder")
        print("5. Optimize task schedule")
        print("6. Send task notifications")
        print("Type 'exit' to quit.")
        
        user_input = input("Your choice: ").lower()
        
        if user_input == "1":
            task_name = input("Enter task name: ")
            duration = int(input("How many minutes until this task is due? "))
            priority = int(input("Enter task priority (1 = High, 3 = Low): "))
            scheduler_agent.run(task_name, duration, priority, task_manager)

        elif user_input == "2":
            listing_agent.run(task_manager)

        elif user_input == "3":
            reminder_agent.run(task_manager)

        elif user_input == "4":
            interval = int(input("Set break reminder interval (minutes): "))
            break_agent.run(interval)

        elif user_input == "5":
            optimizer_agent.run(task_manager)

        elif user_input == "6":
            notification_agent.run(task_manager)

        elif user_input == "exit":
            print("Exiting the Task Manager. Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")

# Run the task manager
run_task_manager()
