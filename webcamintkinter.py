# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2
import time

# Create an instance of TKinter Window or frame
window = Tk()

# Set the size of the window
window.geometry("700x350")

# Create a Label to capture the Video frames
label =Label(window)
label.grid(row=0, column=0)
cap= cv2.VideoCapture(0)

def startTimer():
    if(running):
        global second
        global minute
        global hour
        second += 1
        time.sleep(1)
        secondText.configure(text="%02d" % second)
        minuteText.configure(text="%02d" % minute)
        hourText.configure(text="%02d" % hour)
        if second == 59:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
    window.after(10, startTimer)

def start():
    global running
    running = True

def stop():
    global running
    running = False

def reset():
    global running
    global second
    if not running:
        second = 0
        secondText.configure(text=str(second))

running = False
window.geometry("640x480+600+250")

second, minute, hour = 58, 59, 0

colonText1 = Label(window, text=":", font=("Helvetica", 80))
colonText2 = Label(window, text=":", font=("Helvetica", 80))

colonText1.grid(row=1, column=1)
colonText2.grid(row=1, column=3)

secondText = Label(window, text="%02d" % second, font=("Helvetica", 60), width=3)
secondText.grid(row=1, column=4)

minuteText = Label(window, text="%02d" % minute, font=("Helvetica", 60), width=3)
minuteText.grid(row=1, column=2)

hourText = Label(window, text="%02d" % hour, font=("Helvetica", 60), width=3)
hourText.grid(row=1, column=0)

def stop1(event):
    global running
    running = False
secondText.bind("<Button-1>", stop1)

def start1(event):
    global running
    running = True
secondText.bind("<Button-1>", start1)

def reset1(event):
    global second
    if not running:
        second = 0
        secondText.configure(text=str(second))
secondText.bind("Button-1", reset1)

startButton = Button(window, text='시작', bg="yellow", command=start)
startButton.grid(row=2, column=0)

stopButton = Button(window, text='중지', bg="yellow", command=stop)
stopButton.grid(row=2, column=1)

resetButton = Button(window, text='초기화', bg="yellow", command=reset)
resetButton.grid(row=2, column=2)

face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')

# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #인식된 얼굴 갯수를 출력
    print(len(faces))

    # 인식된 얼굴에 사각형을 출력한다
    for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label.after(20, show_frames)
    # cv2.imshow('frame',frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     cap.release()
    #     cv2.destroyAllWindows()

show_frames()
startTimer()
window.mainloop()