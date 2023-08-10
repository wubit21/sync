import datetime
from tkinter import *
import time
from threading import *
from playsound import playsound

root = Tk()
root.title('Alarm Clock')
root.geometry("300x200")

def Threading():
	t1=Thread(target=alarm)
	t1.start()
def alarm():
    while True:
     set_alarm_time = f"{hour.get()}:{minute.get()}"
     current_time = datetime.datetime.now().strftime("%H:%M")
     time.sleep(1)
     print(current_time,set_alarm_time)
     if current_time == set_alarm_time :
      print("TIME TO GET UP!!!")
      playsound("Wake Me Up.mp3")

Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23'
		)
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)


root.mainloop()