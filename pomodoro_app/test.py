import tkinter as tk
from pomodoro_timer import PomodoroTimer
from task_manager import TaskManager
from character import Character
from feedback import Feedback

# 创建全局对象
pomodoro = PomodoroTimer()
task_manager = TaskManager()
character = Character()
feedback = Feedback()

# GUI 初始化
root = tk.Tk()
root.title("Pomodoro App with Task, Character, and Feedback")

# 更新计时器显示
def update_timer_display():
    minutes, seconds = divmod(pomodoro.time_left, 60)
    timer_label.config(text=f"{minutes:02}:{seconds:02}")
    if pomodoro.is_running and pomodoro.time_left > 0:
        pomodoro.time_left -= 1
        root.after(1000, update_timer_display)  # 每隔1秒更新一次显示
    elif pomodoro.time_left == 0:
        on_task_complete()

# 当一个任务完成时触发
def on_task_complete():
    feedback.complete_task()  # 反馈系统记录完成的任务
    character.complete_task()  # 小人升级
    task_status_label.config(text=character.get_status())  # 更新小人状态
    reminder_label.config(text=f"Tasks completed today: {feedback.get_daily_feedback()}")
    pomodoro.reset_timer()  # 重置计时器

# 开始任务时触发
def start_task():
    task_name = task_entry.get()
    task_description = task_desc_entry.get()
    task_manager.set_task(task_name, task_description)
    pomodoro.is_running = True
    pomodoro.time_left = pomodoro.work_time  # 重置计时器
    update_timer_display()  # 启动计时器

# GUI 元素
timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
timer_label.pack()

# 任务输入框
task_label = tk.Label(root, text="Task Name:")
task_label.pack()
task_entry = tk.Entry(root)
task_entry.pack()

task_desc_label = tk.Label(root, text="Task Description:")
task_desc_label.pack()
task_desc_entry = tk.Entry(root)
task_desc_entry.pack()

# 显示任务状态的小人
task_status_label = tk.Label(root, text=character.get_status())
task_status_label.pack()

# 提示框
reminder_label = tk.Label(root, text="")
reminder_label.pack()

# 控制按钮
start_button = tk.Button(root, text="Start Task", command=start_task)
start_button.pack()

reset_button = tk.Button(root, text="Reset", command=pomodoro.reset_timer)
reset_button.pack()

# 启动主循环
root.mainloop()
