# agent.py
from crew import Agent

def add_task(agent, task_name, duration_minutes, priority, task_manager):
    """Add a new task to the task manager."""
    task_manager.add_task(task_name, duration_minutes, priority)
    agent.say(f"Task '{task_name}' added with priority {priority} and is due in {duration_minutes} minutes.")

def list_tasks(agent, task_manager):
    """List all tasks in the task manager."""
    task_list = task_manager.list_tasks()
    agent.say(task_list)

def check_task_status(agent, task_manager):
    """Check if any tasks are due."""
    task_status = task_manager.check_task_status()
    agent.say(task_status)

def break_reminder(agent, interval_minutes):
    """Remind the user to take a break."""
    agent.say(f"Reminder: It's been {interval_minutes} minutes. Time to take a short break!")

def optimize_time(agent, task_manager):
    """Optimize the task schedule."""
    optimized_tasks = task_manager.optimize_tasks()
    agent.say("Tasks have been optimized based on priority and deadlines.")
    agent.say(optimized_tasks)

def send_task_notification(agent, task_manager):
    """Send task notifications for tasks nearing the deadline."""
    notifications = task_manager.get_task_notifications()
    if notifications:
        agent.say(f"Upcoming deadlines: {notifications}")
    else:
        agent.say("No tasks are close to their deadlines.")

# Define agents here
scheduler_agent = Agent(name="Task Scheduler", task=add_task)
reminder_agent = Agent(name="Task Reminder", task=check_task_status)
break_agent = Agent(name="Break Reminder", task=break_reminder)
optimizer_agent = Agent(name="Time Optimizer", task=optimize_time)
notification_agent = Agent(name="Task Notification", task=send_task_notification)
