class Character:
    def __init__(self):
        self.level = 1
        self.experience = 0

    def complete_task(self):
        self.experience += 1
        if self.experience >= 5:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0

    def get_status(self):
        return f"Level: {self.level}, XP: {self.experience}/5"
