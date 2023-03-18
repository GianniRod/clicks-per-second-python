import tkinter as tk

root = tk.Tk()
root.title("Clicks")
root.geometry("800x650")

count = 0
time_left = 10
timer_running = False

def clicked():
    global count
    count += 1
    label.config(text="Clicks: " + str(count))

def reset():
    global time_left, count, timer_running
    time_left = 10
    count = 0
    label.config(text="Clicks: " + str(count))
    timer_running = False
    start_pause_button.config(text="Start")
    button.config(state=tk.NORMAL)
    average_label.config(text="")

def update_timer():
    global time_left, timer_running
    if time_left > 0 and timer_running:
        time_left -= 1
        label_timer.config(text="Time left: " + str(time_left))
        root.after(1000, update_timer)
    elif time_left == 0:
        button.config(state=tk.DISABLED)
        timer_running = False
        start_pause_button.config(text="Start")
        show_average()

def show_average():
    global count
    average = count / 10
    average_label.config(text="Average clicks per second: " + str(average))

def start_pause():
    global timer_running
    if timer_running:
        timer_running = False
        start_pause_button.config(text="Start")
    else:
        timer_running = True
        start_pause_button.config(text="Pause")
        update_timer()

button = tk.Button(root, text="Click Me", command=clicked, font=("Arial", 100))
button.pack()

reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 30))
reset_button.pack()

label = tk.Label(root, text="Clicks: " + str(count), font=("Arial", 60))
label.pack()

label_timer = tk.Label(root, text="Time left: " + str(time_left), font=("Arial", 30))
label_timer.pack()

start_pause_button = tk.Button(root, text="Start", command=start_pause, font=("Arial", 30))
start_pause_button.pack()

average_label = tk.Label(root, text="", font=("Arial", 30))
average_label.pack()

root.mainloop()
