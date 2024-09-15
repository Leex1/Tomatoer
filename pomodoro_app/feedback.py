import datetime

class Feedback:
    def __init__(self):
        self.tasks_completed = {}

    def complete_task(self):
        today = str(datetime.date.today())
        if today not in self.tasks_completed:
            self.tasks_completed[today] = 0
        self.tasks_completed[today] += 1

    def get_daily_feedback(self):
        today = str(datetime.date.today())
        return self.tasks_completed.get(today, 0)

    def remind_review(self):
        # 实现提醒逻辑
        pass
