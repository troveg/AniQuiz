#####IMPORTS
import random
from os import environ
import pygame
import glob, os
from tkinter import *
from threading import Timer
from PIL import Image, ImageTk
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

#####VARIABLES
score1 = 0
score2 = 0
score = 0
mode = 0
aninumber = 1
aninumber1 = 0
aninumber2 = 0
location2used = 0
filenumber = 0
total_len = 0
count = 0
anime_title0 = 0
anime_title000 = 0
turn = 0
filetitle = {}
imported = []
sbgs = []
colors = []

#####LOCATION
directory = os.path.dirname(os.path.realpath("app.pyw"))
directory1 = "B:\\Media\\Python Projects\\Anime OP Quiz\\AU\\"
directory2 = "B:\\Media\\Python Projects\\Anime OP Quiz\\BG\\"
slash = r'"\"'
slash1 = slash.replace('"', "")
location = directory1

#####TK WIDGETS
root = Tk()
root.state('zoomed')
frame = Frame(root, bg = "#9fcef5", highlightbackground="black", highlightthickness=1)
frame.place(width=377, height=57, x=800, y=800)
frame1 = Frame(root, bg="#9fcef5")
frame1.place(width=150, height=150, x=1750, y=800)
frame2 = Frame(root, bg="#9fcef5", highlightbackground="black", highlightthickness=1)
frame2.place(width=377, height=77, x=800, y=857)
frame3 = Frame(root, bg="#9fcef5")
frame3.place(width=500, height=150, x=50, y=800)
frame4 = Frame(root, bg="#9fcef5")
frame4.place(width=550, height=150, x=50, y=20)
frame5 = Frame(root, bg="#9fcef5")
frame5.place(width=200, height=150, x=1700, y=20)
canvas = Canvas(root)
canvas.place(x=0,y=0, width=1920, height=1080)
pilImage = Image.open("bg.png")
image = ImageTk.PhotoImage(pilImage)
imagePic = image
pilImageEnd = Image.open("bgEnd.png")
imageEnd = ImageTk.PhotoImage(pilImageEnd)
background_label = Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#####CHECK FOR IMPORTS
def importd():
    global filenumber
    global location2used
    global mode
    for file in glob.glob("*.mp3"):
        filenumber += 1
        filetitle["file{0}".format(filenumber)] = location + file
        filetitleA = (filetitle["file{0}".format(filenumber)])
        filetitle3 = filetitleA.replace(".mp3", "")
        filetitleB = filetitle3.replace(location, mode)
        imported.append(filetitleB)
        location2used = 1
def easy():
    global mode
    global total_len
    easy_button.configure(state=DISABLED)
    os.chdir(location + "/easy/")
    mode = "/easy/"
    importd()
    otaku_button.configure(state=DISABLED)
    hard_button.configure(state=DISABLED)
    medium_button.configure(state=DISABLED)
    total_len = str(len(imported))
def medium():
    global mode
    global total_len
    medium_button.configure(state=DISABLED)
    os.chdir(location + "/medium/")
    mode = "/medium/"
    importd()
    easy_button.configure(state=DISABLED)
    os.chdir(location + "/easy/")
    mode = "/easy/"
    importd()
    otaku_button.configure(state=DISABLED)
    hard_button.configure(state=DISABLED)
    total_len = str(len(imported))
def hard():
    global mode
    global total_len
    hard_button.configure(state=DISABLED)
    os.chdir(location + "/hard/")
    mode = "/hard/"
    importd()
    medium_button.configure(state=DISABLED)
    os.chdir(location + "/medium/")
    mode = "/medium/"
    importd()
    easy_button.configure(state=DISABLED)
    otaku_button.configure(state=DISABLED)
    total_len = str(len(imported))
def otaku():
    global mode
    global total_len
    otaku_button.configure(state=DISABLED)
    os.chdir(location + "/otaku/")
    mode = "/otaku/"
    importd()
    hard_button.configure(state=DISABLED)
    os.chdir(location + "/hard/")
    mode = "/hard/"
    importd()
    easy_button.configure(state=DISABLED)
    medium_button.configure(state=DISABLED)
    total_len = str(len(imported))
def diff_all():
    otaku()
    medium()
    global total_len
    total_len = str(len(imported))
    all_button.configure(state=DISABLED)

#####FUNCTIONS
def renew_bgs():
    global sbgs
    global filenumber
    global colors
    colors = ["#b25379", "#3f48cc", "#4d4d4d", "#5599ff", "#2d4c32",
              "#d53333", "#65557e", "#5c526b", "#919aa8", "#493a5e",
              "#0b1728", "#542323", "#82a1ce", "#8b8297", "#d391ba",
              "#ff943d", "#b3a0d8", "#aa2d3c", "#0f8377", "#7f4e01"]
    os.chdir(directory2)
    for file in glob.glob("*.png"):
        filenumber += 1
        filetitle["file{0}".format(filenumber)] = directory2 + file
        filetitleA = (filetitle["file{0}".format(filenumber)])
        filetitle3 = filetitleA.replace(".mp3", "")
        filetitleB = filetitle3.replace(directory2, "")
        sbgs.append(filetitleB)
def raise_frame():
    frame.tkraise()
    frame1.tkraise()
    frame2.tkraise()
    frame3.tkraise()
    frame4.tkraise()
    frame5.tkraise()
    frame_title.lower()
    loop()
def bgselect():
    global imagePic
    global directory2
    if len(sbgs) <= 0:
        renew_bgs()
    sbgmax = len(sbgs) - 1
    selectbg = random.randint(0,sbgmax)
    sbg = sbgs[selectbg]
    color = colors[selectbg]
    pilImagePic = Image.open(directory2 + sbg)
    imagePic = ImageTk.PhotoImage(pilImagePic)
    status2.configure(bg=color)
    statusp.configure(bg=color)
    status_mode.configure(bg=color)
    status_type.configure(bg=color)
    sbgs.remove(sbg)
    colors.remove(color)
def loop():
    global score
    global aninumber
    if (turn % 2) == 0:
        score = score1
        statusp.config(text="Player 1")
    else:
        score = score2
        statusp.config(text="Player 2")
    bgselect()
    background_label.config(image=imagePic)
    status4.configure(text="Anime Number: " + str(aninumber) + "/" + str(total_len))
    status1.configure(text="Correct Answer: ")
    status3.configure(text="Player 1's Score: " + str(score1))
    status5.configure(text="Player 2's Score: " + str(score2))
    if len(imported) > 0:
        main()
    else:
        end()
def end():
    global count
    global aninumber2
    global aninumber1
    status2.configure(bg="#9fcef5")
    statusp.configure(bg="#9fcef5")
    frame4.lower()
    frame5.lower()
    aninumber2 -= 1
    count = 0
    pygame.mixer.music.stop()
    total1 = score1
    total2 = score2
    total = total1 + total2
    aninumber3 = aninumber - 2
    end_button.configure(command=exit)
    status4.configure(text="Press <()> To Exit")
    checkbutton.configure(state=DISABLED)
    contbutton.configure(state=DISABLED)
    score_add.configure(state=DISABLED)
    score_sub.configure(state=DISABLED)
    replay_button.configure(state=DISABLED)
    if aninumber3 > 0:
        background_label.configure(image=imageEnd)
        percent1_0 = (total1 / aninumber1) * 100
        percent1_1 = str(percent1_0) + "%"
        percent2_0 = (total2 / aninumber2) * 100
        percent2_1 = str(percent2_0) + "%"
        percent_0 = (total / aninumber3) * 100
        percent = str(percent_0) + "%"
        status3.configure(text="Player 1's Final Score: " + percent1_1 + ", " + str(total1) + "/" + str(aninumber1))
        status5.configure(text="Player 2's Final Score: " + percent2_1 + ", " + str(total2) + "/" + str(aninumber2))
        status1.configure(text="Players' Total Score: " + percent + ", " + str(total) + "/" + str(aninumber3))
        #BUTTON.grid() -- On Button Press: exit()
    else:
        background_label.configure(image=imageEnd)
        status1.configure(text="Final Score: 0%, 0/0")
        # BUTTON.grid() -- On Button Press: exit()
def main():
    global location2used
    if location2used > 0:
        quiz()
    else:
        end()
def quiz():
    global score1
    global turn
    global anime_title0
    global anime_title000
    global count
    global aninumber1
    global aninumber2
    global aninumber
    if len(imported) > 0:
        if (turn % 2) == 0:
            aninumber2 += 1
            aninumber += 1
        else:
            aninumber1 += 1
            aninumber += 1
        animax = len(imported) - 1
        select = random.randint(0,animax)
        anime_title0 = imported[select]
        play_anime = location + anime_title0 + ".mp3"
        anime_title00 = imported[select].replace("/easy/", "")
        anime_title0000 = anime_title00.replace("/hard/", "")
        anime_title00000 = anime_title0000.replace("/otaku/", "")
        anime_title000 = anime_title00000.replace("/medium/", "")
        anime_mode0 = anime_title0.replace(anime_title000, "")
        anime_mode = anime_mode0.replace("/", "")
        status_mode.configure(text=anime_mode.upper())
        if "OP" in anime_title000:
            status_type.configure(text="OP")
        else:
            status_type.configure(text="ED")
        pygame.mixer.init()
        pygame.mixer.music.load(play_anime)
        pygame.mixer.music.play(1)
        imported.remove(anime_title0)
        checkbutton.configure(state = DISABLED)
        contbutton.configure(state = DISABLED)
        score_add.configure(state = DISABLED)
        score_sub.configure(state = DISABLED)
        replay_button.configure(state = DISABLED)
        count = 15
        def timer0():
            global count
            status2.configure(text=str(count))
            if count > 0:
                timer = Timer(1, timer0)
                count -= 1
                timer.start()
            else:
                status2.configure(text="0")
                quiz1()
        timer0()
    else:
        loop()
def quiz1():
    pygame.mixer.music.fadeout(1250)
    checkbutton.configure(state=NORMAL)
    replay_button.configure(state=NORMAL)
def quiz2():
    global score1
    global anime_title000
    global turn
    score_add.configure(state = NORMAL)
    score_sub.configure(state = NORMAL)
    status1.configure(text = "Correct Answer: " + anime_title000)
    turn += 1
def quizr():
    global score1
    global turn
    global anime_title0
    global count
    global aninumber1
    global aninumber2
    global aninumber
    play_anime = location + anime_title0 + ".mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(play_anime)
    pygame.mixer.music.play(1)
    checkbutton.configure(state = DISABLED)
    contbutton.configure(state = DISABLED)
    score_add.configure(state = DISABLED)
    score_sub.configure(state = DISABLED)
    replay_button.configure(state = DISABLED)
    count = 15
    def timer1():
        global count
        status2.configure(text=str(count))
        if count > 0:
            timer = Timer(1, timer1)
            count -= 1
            timer.start()
        else:
            status2.configure(text="0")
            quiz1()
    timer1()
def add_score():
    global score1
    global score2
    global turn
    if (turn % 2) == 0:
        score2 += 1
    else:
        score1 += 1
    contbutton.configure(state=NORMAL)
    replay_button.configure(state=DISABLED)
    score_add.configure(state=DISABLED)
    score_sub.configure(state=DISABLED)
def sub_score():
    global score1
    global score2
    global turn
    if (turn % 2) == 0:
        score2 -= 0
    else:
        score1 -= 0
    contbutton.configure(state=NORMAL)
    replay_button.configure(state=DISABLED)
    score_sub.configure(state=DISABLED)
    score_add.configure(state=DISABLED)

#####2ND WIDGETS
status3 = Label(frame2, text="Player 1's Score: ", bd=1, relief=SUNKEN, anchor=W)
status3.pack(side=BOTTOM, fill=X)
status5 = Label(frame2, text="Player 2's Score: ", bd=1, relief=SUNKEN, anchor=W)
status5.pack(fill=X, side=BOTTOM)
status2 = Label(frame1, text="", anchor=CENTER, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
status2.pack(fill=X, side=BOTTOM)
statusp = Label(frame3, text="", anchor=CENTER, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
statusp.pack(fill=X, side=BOTTOM)
status_mode = Label(frame4, text="Bloop", anchor=W, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
status_mode.pack(fill=X)
status_type = Label(frame5, text="", anchor=CENTER, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
status_type.pack(fill=X, side=BOTTOM)
status4 = Label(frame2, text="Anime Number: " + str(aninumber1), bd=1, relief=SUNKEN, anchor=W)
status4.pack(fill=X, side=BOTTOM)
status1 = Label(frame2, text="Correct Answer: ", bd=1, relief=SUNKEN, anchor=W)
status1.pack(fill=X, side=BOTTOM)
checkbutton = Button(frame, text="✓", width=8, height=3, command=quiz2)
checkbutton.grid(row=0, column=0)
score_add = Button(frame, text="+", width=7, height=3, command=add_score)
score_add.grid(row=0, column=1)
score_sub = Button(frame, text="-", width=8, height=3, command=sub_score)
score_sub.grid(row=0, column=2)
replay_button = Button(frame, text="⏮", width=7, height=3, command=quizr)
replay_button.grid(row=0, column=3)
contbutton = Button(frame, text="⏭", width=8, height=3, command=loop)
contbutton.grid(row=0, column=4)
end_button = Button(frame, text="X", width=7, height=3, command=end)
end_button.grid(row=0, column=5)

frame_title = Frame(root, bg = "#9fcef5", highlightbackground="black", highlightthickness=1)
frame_title.place(width=150, height=158, x=885, y=465)
frame_title.tkraise()
start_button = Button(frame_title, text="Start", command=raise_frame, height=1)
start_button.pack(fill=X)
easy_button = Button(frame_title, text="Normie", command=easy, height=1)
easy_button.pack(fill=X)
medium_button = Button(frame_title, text="Weeb", command=medium, height=1)
medium_button.pack(fill=X)
hard_button = Button(frame_title, text="Otaku", command=hard, height=1)
hard_button.pack(fill=X)
otaku_button = Button(frame_title, text="Neet", command=otaku, height=1)
otaku_button.pack(fill=X)
all_button = Button(frame_title, text="All", command=diff_all, height=1)
all_button.pack(fill=X)

renew_bgs()
root.mainloop()