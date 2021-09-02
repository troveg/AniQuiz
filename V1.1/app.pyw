#####IMPORTS
import random
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import glob, os
from tkinter import *
from threading import Timer
from PIL import Image, ImageTk
from tkinter import ttk
from configparser import ConfigParser

#####VARIABLES
score1 = 0
score2 = 0
score = 0
mode = 0
end_count = 0
aninumber = 1
aninumber1 = 0
aninumber2 = 0
location2used = 0
players = 2
score1_max = 0
score2_max = 0
filenumber = 0
total_len = 0
count = 0
anime_title0 = 0
anime_title000 = 0
turn = 0
filetitle = {}
imported1 = []
imported0 = []
imported = []
sbgs = []
colors = []

#####SETTINGS
config = ConfigParser()
config.read('settings.ini')
directory1 = config.get('section_a', 'directory1')
location = directory1
directory2 = config.get('section_a', 'directory2')
#UPDATE config.set('section_a', 'string_val', 'world')
#ADD config.add_section('section_b') config.set('section_b', 'meal_val', 'spam')
with open('settings.ini', 'w') as configfile:
    config.write(configfile)

#####TK WIDGETS
root = Tk()
root.state('zoomed')
frame = Frame(root, bg="#9fcef5", highlightbackground="black", highlightthickness=1)
frame.place(width=377, height=57, x=800, y=860)
frame1 = Frame(root, bg="#9fcef5")
frame1.place(width=150, height=150, x=1750, y=800)
frame2 = Frame(root, bg="#9fcef5", highlightbackground="black", highlightthickness=1)
frame2.place(width=377, height=21, x=800, y=839)
frame3 = Frame(root, bg="#9fcef5")
frame3.place(width=500, height=150, x=50, y=800)
frame4 = Frame(root, bg="#9fcef5")
frame4.place(width=550, height=150, x=50, y=20)
frame5 = Frame(root, bg="#9fcef5")
frame5.place(width=200, height=150, x=1700, y=20)
frame6 = Frame(root, bg="#9fcef5")
frame6.place(width=480, height=320, x=50, y=450)
pilImage = Image.open("bg.png")
image = ImageTk.PhotoImage(pilImage)
pilImageEnd = Image.open("bgEnd.png")
imageEnd = ImageTk.PhotoImage(pilImageEnd)
background_label = Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#####CHECK FOR IMPORTS
def randomize():
    def zero():
        if len(imported1) > 0:
            importmax = len(imported1) - 1
            aniselect = random.randint(0, importmax)
            anime = imported1[aniselect]
            imported.append(anime)
            imported1.remove(anime)
            zero()
    zero()

def importd():
    global filenumber
    global location2used
    global mode
    def zero():
        if len(imported0) > 0:
            importmax = len(imported0) - 1
            aniselect = random.randint(0, importmax)
            anime = imported0[aniselect]
            imported1.append(anime)
            imported0.remove(anime)
            zero()
        else:
            randomize()
    for file in glob.glob("*.mp3"):
        filenumber += 1
        filetitle["file{0}".format(filenumber)] = location + file
        filetitleA = (filetitle["file{0}".format(filenumber)])
        filetitle3 = filetitleA.replace(".mp3", "")
        filetitleB = filetitle3.replace(location, mode)
        imported0.append(filetitleB)
        location2used = 1
    zero()

def easy():
    global mode
    global total_len
    os.chdir(location + "/easy/")
    mode = "/easy/"
    importd()
    total_len = str(len(imported))
def medium():
    global mode
    global total_len
    os.chdir(location + "/medium/")
    mode = "/medium/"
    importd()
    os.chdir(location + "/easy/")
    mode = "/easy/"
    importd()
    total_len = str(len(imported))
def hard():
    global mode
    global total_len
    os.chdir(location + "/hard/")
    mode = "/hard/"
    importd()
    os.chdir(location + "/medium/")
    mode = "/medium/"
    importd()
    total_len = str(len(imported))
def otaku():
    global mode
    global total_len
    os.chdir(location + "/otaku/")
    mode = "/otaku/"
    importd()
    os.chdir(location + "/hard/")
    mode = "/hard/"
    importd()
    total_len = str(len(imported))
def diff_all():
    otaku()
    medium()
    global total_len
    total_len = str(len(imported))

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
def statcheck():
    global players
    diff0 = difficulty.get()
    diff1 = diff0.replace('Easy', '0')
    diff2 = diff1.replace('Medium', '1')
    diff3 = diff2.replace('Hard', '2')
    diff4 = diff3.replace('Otaku', '3')
    diff5 = diff4.replace('All', '4')
    diff = int(diff5)
    list0 = [easy, medium, hard, otaku, diff_all]
    list0[diff]()
    players = int(player_count.get())
    raise_frame()
def raise_frame():
    frame.tkraise()
    frame1.tkraise()
    frame2.tkraise()
    frame3.tkraise()
    frame4.tkraise()
    frame5.tkraise()
    frame6.tkraise()
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
    status3.configure(bg=color)
    status_max.configure(bg=color)
    sbgs.remove(sbg)
    colors.remove(color)
def loop():
    global score
    global aninumber
    global end_count
    end_count = 0
    if (turn % 2) == 0:
        score = score1
        statusp.config(text="Player 1")
        status3.configure(text=str(score1) + "/" + str(score1_max))
    else:
        if players == 2:
            score = score2
            statusp.config(text="Player 2")
            status3.configure(text=str(score2) + "/" + str(score2_max))
        else:
            score = score1
            statusp.config(text="Player 1")
            status3.configure(text=str(score1) + "/" + str(score1_max))
    bgselect()
    background_label.config(image=imagePic)
    status_max.configure(text = str(total_len))
    status1.configure(text = "Correct Answer: ")
    if len(imported) > 0:
        main()
    else:
        end()
def end_check():
    global end_count
    end_count += 1
    if end_count >= 2:
        end()
def end():
    global count
    global aninumber2
    global aninumber1
    frame.lower()
    frame1.lower()
    frame3.lower()
    frame4.lower()
    frame5.lower()
    frame6.lower()
    aninumber2 -= 1
    count = 0
    pygame.mixer.music.stop()
    total1 = score1
    total2 = score2
    total = total1 + total2
    aninumber3 = aninumber - 2
    end_button.configure(command=exit)
    checkbutton.configure(state=DISABLED)
    contbutton.configure(state=DISABLED)
    score_add.configure(state=DISABLED)
    score_sub.configure(state=DISABLED)
    replay_button.configure(state=DISABLED)
    background_label.configure(image=imageEnd)
    status1.configure(text="Players' Total Score: " + str(total) + "/" + str(aninumber3))
    frame7 = Frame(root, bg="#9fcef5", highlightbackground="black", highlightthickness=1)
    frame7.place(width=377, height=21, x=800, y=860)
    frame8 = Frame(root, bg="#9fcef5", highlightbackground="black", highlightthickness=1)
    score1_final = Label(frame7, text="Player 1's Final Score: " + str(score1) + "/" + str(score1_max), bd=1, relief=SUNKEN, anchor=W)
    score2_final = Label(frame8, text="Player 2's Final Score: " + str(score2) + "/" + str(score2_max), bd=1, relief=SUNKEN, anchor=W)
    if players == 2:
        frame8.place(width=377, height=21, x=800, y=881)
        score1_final.pack(fill=X)
        score2_final.pack(fill=X)
    else:
        score1_final.pack(fill=X)
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
        checkbutton.configure(state = NORMAL)
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
    pygame.mixer.music.fadeout(1000)
    replay_button.configure(state=NORMAL)
def quiz2():
    global score1
    global anime_title000
    global turn
    global count
    global players
    count = 0
    score_add.configure(state = NORMAL)
    score_sub.configure(state = NORMAL)
    checkbutton.configure(state = DISABLED)
    status1.configure(text = "Correct Answer: " + str(anime_title000))
    if players == 1:
        turn = 1
    else:
        turn += 1
def quizr():
    global score1
    global turn
    global anime_title0
    global count
    global aninumber1
    global aninumber2
    global aninumber
    play_anime = location + str(anime_title0) + ".mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(play_anime)
    pygame.mixer.music.play(1)
    checkbutton.configure(state = NORMAL)
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
    global score
    global score1
    global score2
    global turn
    global turn
    global score1_max
    global score2_max
    if (turn % 2) == 0:
        score2 += 1
        score2_max += 1
    else:
        score1 += 1
        score1_max += 1
    contbutton.configure(state=NORMAL)
    replay_button.configure(state=DISABLED)
    score_add.configure(state=DISABLED)
    score_sub.configure(state=DISABLED)
def sub_score():
    global score1
    global score2
    global turn
    global score1_max
    global score2_max
    if (turn % 2) == 0:
        score2 -= 0
        score2_max += 1
    else:
        score1 -= 0
        score1_max += 1
    contbutton.configure(state=NORMAL)
    replay_button.configure(state=DISABLED)
    score_sub.configure(state=DISABLED)
    score_add.configure(state=DISABLED)

#####2ND WIDGETS
status3 = Label(frame6, text="", anchor=CENTER, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
status3.pack(fill=X)
label_underscore1 = Label(frame6, anchor=CENTER, fg='white', bg="white")
label_underscore1.pack(fill=X)
status_max = Label(frame6, text=aninumber1, anchor=CENTER, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
status_max.pack(fill=X, side=BOTTOM)
status2 = Label(frame1, text="", anchor=CENTER, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
status2.pack(fill=X, side=BOTTOM)
statusp = Label(frame3, text="", anchor=CENTER, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
statusp.pack(fill=X, side=BOTTOM)
status_mode = Label(frame4, text="Error", anchor=W, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
status_mode.pack(fill=X)
status_type = Label(frame5, text="", anchor=CENTER, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
status_type.pack(fill=X, side=BOTTOM)
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
end_button = Button(frame, text="X", width=7, height=3, command=end_check)
end_button.grid(row=0, column=5)

frame_title = Frame(root, bg = "#9fcef5", highlightbackground="black", highlightthickness=1)
frame_title.place(width=200, height=70, x=885, y=465)
frame_title.tkraise()
start_button = Button(frame_title, text="Start", command=statcheck, height=1)
start_button.pack(fill=X)
variable = StringVar(root)
variable.set("Difficulty")
variable0 = StringVar(root)
variable0.set("Number of Players")
difficulty = ttk.Combobox(frame_title, textvariable=variable)
difficulty.config(values = ('Easy', 'Medium', 'Hard', 'Otaku', 'All'))
difficulty.pack(fill=X)
player_count = ttk.Combobox(frame_title, textvariable=variable0)
player_count.config(values = ('1', '2'))
player_count.pack(fill=X)

renew_bgs()
root.mainloop()