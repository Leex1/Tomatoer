class TaskManager:
    def __init__(self):
        self.current_task = None

    def set_task(self, task_name, task_description):
        self.current_task = {
            'name': task_name,
            'description': task_description
        }

    def get_task(self):
        return self.current_task
