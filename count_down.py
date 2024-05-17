# Importing the modules
import time
from tkinter import *
from tkinter import messagebox
from playsound import playsound

# initialing the root and setting geometry
root = Tk()
root.geometry('300x250')

# setting title for the window
root.title('Count Down Timer')

# Declaring Varaibles to connect to the entry widget
hr = StringVar()
min = StringVar()
sec = StringVar()

# Setting the variables to default value of '00'
hr.set('00')
min.set('00')
sec.set('00')

# Creating a frame widget
frame = Frame(root, height=250, width=300)
frame.place(x=0, y=0)

# Hour entry widget
hr_entry = Entry(frame, width=2, font=('Arial', 40, 'bold'), textvariable=hr, fg='#FCBB00', bd=5)
hr_entry.place(x=60, y=20)

# Minite Entry widget
min_entry = Entry(frame, width=2, font=('Arial', 40, 'bold'), textvariable=min, fg='#FCBB00', bd=5)
min_entry.place(x=135, y=20)

# Seconds entry widget
sec_entry = Entry(frame, width=2, font=('Arial', 40, 'bold'), textvariable=sec, fg='#FCBB00', bd=5)
sec_entry.place(x=210, y=20)


# Function to start the countdown timer when the button is clicked
def start_count_down():

    
    try: 
        # converting the hours, minutes to seconds and adding it up to that
        temp = int(hr.get())*3600 + int(min.get())*60 + int(sec.get())
    except:
        print('Enter correct values')


    while temp > -1:
        # divmod divmod(temp, 60) -> value_1 = temp//60, value_2 =  temp%60
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)
        
        # Formationg the text
        hr.set("{0:2d}".format(hours))
        min.set("{0:2d}".format(mins))
        sec.set("{0:2d}".format(secs))

        # updating the root window
        root.update()
        # waiting for 1 secs
        time.sleep(1)

        # checking if the temp is equal to 
        if temp == 0:
            #  Playing sound
            playsound('Done.mp3')
            
            # Displaying a window messagebox saying time up
            messagebox.showinfo("Time Countdown", "Time Up")
        temp-=1


# The button that activate the start count down funtion
btn = Button(frame, text='Start Count Down', bd=5, command=start_count_down, bg='#A08516', fg='#16A085', font=('Arial', 12, 'bold'))
btn.place(x=70, y=120)

# Running the root in a loop
root.mainloop()
