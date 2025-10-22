import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2
import os
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'support@smartpresence.com' ")

def check_haarcascadefile():
    # First try to find the file in current directory
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        return "haarcascade_frontalface_default.xml"
    else:
        # Try to use OpenCV's built-in haar cascade
        try:
            cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            if os.path.isfile(cascade_path):
                return cascade_path
            else:
                mess._show(title='File Missing', message='Haar Cascade file not found. Please ensure OpenCV is properly installed.')
                window.destroy()
                return None
        except:
            mess._show(title='Error', message='Please contact us for help or reinstall OpenCV')
            window.destroy()
            return None

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel/psd.txt")
    if exists1:
        tf = open("TrainingImageLabel/psd.txt", "r")
        key = tf.read()
        tf.close()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel/psd.txt", "w")
            tf.write(new_pas)
            tf.close()
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = (old.get())
    newp = (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel/psd.txt", "w")
            txf.write(newp)
            txf.close()
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("450x250")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="#1e1e2e")
    
    title = tk.Label(master, text='Change Password', bg='#1e1e2e', fg='#00d9ff', 
                     font=('Segoe UI', 18, 'bold'))
    title.pack(pady=20)
    
    input_frame = tk.Frame(master, bg='#1e1e2e')
    input_frame.pack(pady=10)
    
    lbl4 = tk.Label(input_frame, text='Old Password:', bg='#1e1e2e', fg='white', 
                    font=('Segoe UI', 11))
    lbl4.grid(row=0, column=0, pady=10, padx=10, sticky='w')
    global old
    old = tk.Entry(input_frame, width=25, fg="white", bg='#2e2e3e', relief='flat', 
                   font=('Segoe UI', 11), show='*', insertbackground='white')
    old.grid(row=0, column=1, pady=10, padx=10)
    
    lbl5 = tk.Label(input_frame, text='New Password:', bg='#1e1e2e', fg='white', 
                    font=('Segoe UI', 11))
    lbl5.grid(row=1, column=0, pady=10, padx=10, sticky='w')
    global new
    new = tk.Entry(input_frame, width=25, fg="white", bg='#2e2e3e', relief='flat', 
                   font=('Segoe UI', 11), show='*', insertbackground='white')
    new.grid(row=1, column=1, pady=10, padx=10)
    
    lbl6 = tk.Label(input_frame, text='Confirm Password:', bg='#1e1e2e', fg='white', 
                    font=('Segoe UI', 11))
    lbl6.grid(row=2, column=0, pady=10, padx=10, sticky='w')
    global nnew
    nnew = tk.Entry(input_frame, width=25, fg="white", bg='#2e2e3e', relief='flat', 
                    font=('Segoe UI', 11), show='*', insertbackground='white')
    nnew.grid(row=2, column=1, pady=10, padx=10)
    
    btn_frame = tk.Frame(master, bg='#1e1e2e')
    btn_frame.pack(pady=20)
    
    save1 = tk.Button(btn_frame, text="Save Changes", command=save_pass, fg="white", 
                      bg="#00d9ff", height=1, width=15, relief='flat',
                      activebackground="#00b8d4", font=('Segoe UI', 11, 'bold'),
                      cursor='hand2')
    save1.grid(row=0, column=0, padx=10)
    
    cancel = tk.Button(btn_frame, text="Cancel", command=master.destroy, fg="white", 
                       bg="#ff4757", height=1, width=15, relief='flat',
                       activebackground="#ee2f3a", font=('Segoe UI', 11, 'bold'),
                       cursor='hand2')
    cancel.grid(row=0, column=1, padx=10)
    
    master.mainloop()

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel/psd.txt")
    if exists1:
        tf = open("TrainingImageLabel/psd.txt", "r")
        key = tf.read()
        tf.close()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel/psd.txt", "w")
            tf.write(new_pas)
            tf.close()
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')

def clear():
    txt.delete(0, 'end')
    res = "Ready to capture images"
    message1.configure(text=res)

def clear2():
    txt2.delete(0, 'end')
    res = "Ready to capture images"
    message1.configure(text=res)

def TakeImages():
    cascade_path = check_haarcascadefile()
    if cascade_path is None:
        return
    
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("StudentDetails/StudentDetails.csv")
    if exists:
        with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails/StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    
    Id = (txt.get())
    name = (txt2.get())
    
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cam.set(cv2.CAP_PROP_FPS, 30)
        cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        
        detector = cv2.CascadeClassifier(cascade_path)
        sampleNum = 0
        frame_count = 0
        
        cv2.namedWindow('Capturing Images', cv2.WINDOW_NORMAL)
        
        while sampleNum < 150:
            ret, img = cam.read()
            if not ret:
                continue
            
            frame_count += 1
            
            if frame_count % 3 == 0:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30))
                
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 217, 255), 2)
                    
                    if frame_count % 6 == 0:
                        sampleNum += 1
                        cv2.imwrite("TrainingImage/" + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                                    gray[y:y + h, x:x + w])
                        cv2.putText(img, f"Captured: {sampleNum}/150", (10, 30), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            cv2.putText(img, "Press 'q' to stop", (10, img.shape[0] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.imshow('Capturing Images', img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cam.release()
        cv2.destroyAllWindows()
        res = "✓ Images captured for ID: " + Id
        row = [serial, '', Id, '', name]
        with open('StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "⚠ Enter correct name"
            message1.configure(text=res)

def TrainImages():
    cascade_path = check_haarcascadefile()
    if cascade_path is None:
        return
    
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cascade_path)
    faces, ID = getImagesAndLabels("TrainingImage")
    
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations', message='Please Register someone first!!!')
        return
    
    recognizer.save("TrainingImageLabel/Trainner.yml")
    res = "✓ Profile saved successfully"
    message1.configure(text=res)
    message.configure(text='Total Registrations: ' + str(ID[0]))

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

def TrackImages():
    cascade_path = check_haarcascadefile()
    if cascade_path is None:
        return
    
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    
    for k in tv.get_children():
        tv.delete(k)
    
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    exists3 = os.path.isfile("TrainingImageLabel/Trainner.yml")
    
    if exists3:
        recognizer.read("TrainingImageLabel/Trainner.yml")
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return
    
    faceCascade = cv2.CascadeClassifier(cascade_path)

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("StudentDetails/StudentDetails.csv")
    
    if exists1:
        df = pd.read_csv("StudentDetails/StudentDetails.csv")
    else:
        mess._show(title='Details Missing', message='Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        return
    
    # Dictionary to track recognized people
    recognized_dict = {}
    
    while True:
        ret, im = cam.read()
        if not ret:
            continue
            
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        # Apply histogram equalization for better recognition
        gray = cv2.equalizeHist(gray)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5, minSize=(100, 100))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 217, 255), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            
            # Relaxed confidence threshold - lower is better (more confident)
            if (conf < 70):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                
                if len(aa) > 0 and len(ID) > 0:
                    ID = str(ID)
                    ID = ID[1:-1]
                    bb = str(aa)
                    bb = bb[2:-2]
                    attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
                    
                    # Show confidence score
                    conf_text = f"{bb} ({int(conf)})"
                    cv2.putText(im, conf_text, (x, y - 10), font, 0.7, (0, 255, 0), 2)
                else:
                    bb = 'Unknown'
                    cv2.putText(im, f"Unknown ({int(conf)})", (x, y - 10), font, 0.7, (0, 0, 255), 2)
            else:
                Id = 'Unknown'
                bb = str(Id)
                # Show why it's unknown (high confidence value means low confidence)
                cv2.putText(im, f"Unknown ({int(conf)})", (x, y - 10), font, 0.7, (0, 0, 255), 2)
            
            cv2.putText(im, str(bb), (x, y + h + 30), font, 1, (0, 217, 255), 2)
        
        # Add instructions on screen
        cv2.putText(im, "Press 'q' to stop and save attendance", (10, 30), 
                    font, 0.6, (255, 255, 255), 2)
        cv2.putText(im, f"Faces detected: {len(faces)}", (10, 60), 
                    font, 0.6, (255, 255, 255), 2)
        
        cv2.imshow('Taking Attendance', im)
        
        if (cv2.waitKey(1) == ord('q')):
            break
    
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Attendance/Attendance_" + date + ".csv")
    
    if exists:
        with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
        csvFile1.close()
    else:
        with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)
        csvFile1.close()
    
    with open("Attendance/Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()
    cam.release()
    cv2.destroyAllWindows()

# Global variables
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")

mont = {'01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
        }

# Main Window
window = tk.Tk()
window.geometry("1400x800")
window.resizable(True, True)
window.title("SmartPresence - Attendance System")
window.configure(background='#1e1e2e')

# Header Frame
header_frame = tk.Frame(window, bg="#00d9ff", height=100)
header_frame.pack(fill='x', side='top')

title_label = tk.Label(header_frame, text="SmartPresence", fg="white", bg="#00d9ff", 
                       font=('Segoe UI', 32, 'bold'))
title_label.pack(side='left', padx=30, pady=20)

subtitle_label = tk.Label(header_frame, text="AI-Powered Attendance System", fg="#1e1e2e", 
                          bg="#00d9ff", font=('Segoe UI', 14))
subtitle_label.pack(side='left', padx=10)

datetime_frame = tk.Frame(header_frame, bg="#00d9ff")
datetime_frame.pack(side='right', padx=30)

datef = tk.Label(datetime_frame, text=day + " " + mont[month] + " " + year, 
                 fg="white", bg="#00d9ff", font=('Segoe UI', 16, 'bold'))
datef.pack()

clock = tk.Label(datetime_frame, fg="white", bg="#00d9ff", font=('Segoe UI', 20, 'bold'))
clock.pack()
tick()

# Content Frame
content_frame = tk.Frame(window, bg="#0f0fe6")
content_frame.pack(fill='both', expand=True, padx=20, pady=20)

# Left Panel
left_panel = tk.Frame(content_frame, bg="#2e2e3e", relief='flat', bd=0)
left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))

left_header = tk.Label(left_panel, text="📊 Attendance Records", fg="white", bg="#2e2e3e", 
                       font=('Segoe UI', 18, 'bold'))
left_header.pack(pady=20)

trackImg = tk.Button(left_panel, text="▶ Start Attendance", command=TrackImages, fg="white", 
                     bg="#00d9ff", width=30, height=2, relief='flat',
                     activebackground="#00b8d4", font=('Segoe UI', 13, 'bold'),
                     cursor='hand2')
trackImg.pack(pady=10)

# Treeview Style
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview",
                background="#2e2e3e",
                foreground="white",
                rowheight=30,
                fieldbackground="#2e2e3e",
                borderwidth=0,
                font=('Segoe UI', 10))
style.map('Treeview', background=[('selected', '#00d9ff')])
style.configure("Treeview.Heading",
                background="#00d9ff",
                foreground="white",
                relief="flat",
                font=('Segoe UI', 11, 'bold'))

tree_frame = tk.Frame(left_panel, bg="#2e2e3e")
tree_frame.pack(fill='both', expand=True, padx=20, pady=10)

tv = ttk.Treeview(tree_frame, height=15, columns=('name', 'date', 'time'))
tv.column('#0', width=100)
tv.column('name', width=150)
tv.column('date', width=120)
tv.column('time', width=120)
tv.pack(side='left', fill='both', expand=True)
tv.heading('#0', text='ID')
tv.heading('name', text='NAME')
tv.heading('date', text='DATE')
tv.heading('time', text='TIME')

scroll = ttk.Scrollbar(tree_frame, orient='vertical', command=tv.yview)
scroll.pack(side='right', fill='y')
tv.configure(yscrollcommand=scroll.set)

quitWindow = tk.Button(left_panel, text="✕ Exit System", command=window.destroy, fg="white", 
                       bg="#ff4757", width=30, height=2, relief='flat',
                       activebackground="#ee2f3a", font=('Segoe UI', 13, 'bold'),
                       cursor='hand2')
quitWindow.pack(pady=20)

# Right Panel
right_panel = tk.Frame(content_frame, bg="#2e2e3e", relief='flat', bd=0)
right_panel.pack(side='right', fill='both', expand=True, padx=(10, 0))

right_header = tk.Label(right_panel, text="👤 Student Registration", fg="white", bg="#2e2e3e", 
                        font=('Segoe UI', 18, 'bold'))
right_header.pack(pady=20)

input_frame = tk.Frame(right_panel, bg="#2e2e3e")
input_frame.pack(pady=20, padx=40)

id_label = tk.Label(input_frame, text="Student ID", fg="#00d9ff", bg="#2e2e3e", 
                    font=('Segoe UI', 12, 'bold'))
id_label.grid(row=0, column=0, sticky='w', pady=(10, 5))

txt = tk.Entry(input_frame, width=35, fg="white", bg="#1e1e2e", relief='flat', 
               font=('Segoe UI', 12), insertbackground='white', bd=2)
txt.grid(row=1, column=0, pady=(0, 20), ipady=8)

clearButton = tk.Button(input_frame, text="✕", command=clear, fg="white", bg="#ff4757", 
                        width=3, height=1, relief='flat', font=('Segoe UI', 10, 'bold'),
                        cursor='hand2')
clearButton.grid(row=1, column=1, padx=(5, 0), pady=(0, 20))

name_label = tk.Label(input_frame, text="Student Name", fg="#00d9ff", bg="#2e2e3e", 
                      font=('Segoe UI', 12, 'bold'))
name_label.grid(row=2, column=0, sticky='w', pady=(10, 5))

txt2 = tk.Entry(input_frame, width=35, fg="white", bg="#1e1e2e", relief='flat', 
                font=('Segoe UI', 12), insertbackground='white', bd=2)
txt2.grid(row=3, column=0, pady=(0, 20), ipady=8)

clearButton2 = tk.Button(input_frame, text="✕", command=clear2, fg="white", bg="#ff4757", 
                         width=3, height=1, relief='flat', font=('Segoe UI', 10, 'bold'),
                         cursor='hand2')
clearButton2.grid(row=3, column=1, padx=(5, 0), pady=(0, 20))

button_frame = tk.Frame(right_panel, bg="#2e2e3e")
button_frame.pack(pady=20)

takeImg = tk.Button(button_frame, text="📷 Capture Images", command=TakeImages, fg="white", 
                    bg="#5f27cd", width=25, height=2, relief='flat',
                    activebackground="#4d1fa6", font=('Segoe UI', 12, 'bold'),
                    cursor='hand2')
takeImg.pack(pady=10)

trainImg = tk.Button(button_frame, text="💾 Save Profile", command=psw, fg="white", 
                     bg="#00d9ff", width=25, height=2, relief='flat',
                     activebackground="#00b8d4", font=('Segoe UI', 12, 'bold'),
                     cursor='hand2')
trainImg.pack(pady=10)

message1 = tk.Label(right_panel, text="Ready to capture images", bg="#2e2e3e", fg="#00d9ff", 
                    font=('Segoe UI', 11, 'italic'), wraplength=400)
message1.pack(pady=10)

message = tk.Label(right_panel, text="", bg="#2e2e3e", fg="white", 
                   font=('Segoe UI', 11, 'bold'))
message.pack(pady=5)

# Count existing registrations
res = 0
exists = os.path.isfile("StudentDetails/StudentDetails.csv")
if exists:
    with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations: ' + str(res))

# Menu Bar
menubar = tk.Menu(window, relief='flat', bg='#2e2e3e', fg='white', 
                  activebackground='#00d9ff', font=('Segoe UI', 10))
filemenu = tk.Menu(menubar, tearoff=0, bg='#2e2e3e', fg='white', 
                   activebackground='#00d9ff', font=('Segoe UI', 10))
filemenu.add_command(label='🔒 Change Password', command=change_pass)
filemenu.add_command(label='📧 Contact Us', command=contact)
filemenu.add_separator()
filemenu.add_command(label='🚪 Exit', command=window.destroy)
menubar.add_cascade(label='Settings', menu=filemenu)

window.configure(menu=menubar)
window.mainloop()