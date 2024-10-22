# tasks.py
from datetime import datetime, timedelta

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, duration_minutes, priority):
        """Add a new task."""
        task_time = datetime.now() + timedelta(minutes=duration_minutes)
        self.tasks.append({"task": task_name, "time": task_time, "priority": priority})

    def list_tasks(self):
        """List all tasks."""
        if not self.tasks:
            return "You have no tasks for today!"
        
        task_list = "Here are your tasks for today:\n"
        for task in self.tasks:
            task_list += f"- {task['task']} (Priority: {task['priority']}, Complete by {task['time'].strftime('%H:%M')})\n"
        return task_list

    def check_task_status(self):
        """Check if any tasks are due."""
        now = datetime.now()
        due_tasks = [task['task'] for task in self.tasks if task['time'] <= now]
        if due_tasks:
            return f"These tasks are due now: {', '.join(due_tasks)}. Please complete them."
        return "No tasks are due at the moment!"

    def optimize_tasks(self):
        """Optimize the task schedule based on priority and deadline."""
        sorted_tasks = sorted(self.tasks, key=lambda x: (x['priority'], x['time']))
        optimized_task_list = "Optimized task order:\n"
        for task in sorted_tasks:
            optimized_task_list += f"- {task['task']} (Priority: {task['priority']}, Complete by {task['time'].strftime('%H:%M')})\n"
        return optimized_task_list

    def get_task_notifications(self):
        """Send notifications for tasks close to their deadline."""
        now = datetime.now()
        notifications = [f"{task['task']} (due at {task['time'].strftime('%H:%M')})"
                         for task in self.tasks if now + timedelta(minutes=10) >= task['time'] > now]
        return ", ".join(notifications) if notifications else None
