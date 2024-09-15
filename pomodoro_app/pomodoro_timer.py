import time
import tkinter as tk
from tkinter import messagebox

class PomodoroTimer:
    def __init__(self, work_time=1*20, break_time=1*10):
        self.work_time = work_time
        self.break_time = break_time
        self.is_running = False
        self.time_left = self.work_time

    def start_timer(self, update_callback):
        self.is_running = True
        while self.is_running and self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            update_callback(self.time_left)
        if self.time_left == 0:
            self.is_running = False
            messagebox.showinfo("Pomodoro", "Time's up! Take a break.")

    def reset_timer(self):
        self.is_running = False
        self.time_left = self.work_time

# 用于更新显示的简单 GUI
def update_timer_display(time_left):
    minutes, seconds = divmod(time_left, 60)
    timer_label.config(text=f"{minutes:02}:{seconds:02}")

root = tk.Tk()
root.title("Pomodoro Timer")

timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
timer_label.pack()

pomodoro = PomodoroTimer()

start_button = tk.Button(root, text="Start", command=lambda: pomodoro.start_timer(update_timer_display))
start_button.pack()

reset_button = tk.Button(root, text="Reset", command=pomodoro.reset_timer)
reset_button.pack()

root.mainloop()
