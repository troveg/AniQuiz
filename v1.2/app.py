import glob, os, random, pygame
from configparser import ConfigParser
from tkinter import *
from PIL import Image, ImageTk
from threading import Timer
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

#TK Setup
root = Tk()
root.geometry("1920x1080")
root.title("AniQuiz")
root.state("zoomed")

#Settings
config = ConfigParser()
config.read('settings.ini')
resource_directory = config.get('settings', 'resource_directory')
bg_directory = resource_directory + "Backgrounds\\"
ed_directory = resource_directory + "Endings\\"
icon_directory = resource_directory + "Icons\\"
misc_directory = resource_directory + "Misc\\"
op_directory = resource_directory + "Openings\\"
ost_directory = resource_directory + "OSTs\\"

#Set General Variables
button_01_check = 0
button_02_check = 0
button_03_check = 0
selection_label_modified = 0
difficulty = "easy"
selection_text = "Selection: "
selected_item_groups = []
imported = []
anitype_list = []
total_len = 0
count = 15
anititle = "Anime"
aniseries = "Series"

#Set Background Variables
bg_list = []
bg_title = {}
bg_number = 0
selected_bg = ImageTk.PhotoImage(Image.open(misc_directory + "menu_bg.png"))

#Set Image Variables
logo_image_var = ImageTk.PhotoImage(Image.open(icon_directory + "Tower of God.png"))
menu_bg = ImageTk.PhotoImage(Image.open(misc_directory + "menu_bg.png"))
quiz_button_01_img = ImageTk.PhotoImage(Image.open(misc_directory + "quiz_button_01.png"))
quiz_button_02_img = ImageTk.PhotoImage(Image.open(misc_directory + "quiz_button_02.png"))
quiz_button_03_img = ImageTk.PhotoImage(Image.open(misc_directory + "quiz_button_03.png"))

def load_logo():
    global logo_image_var, aniseries
    logo_image_var = ImageTk.PhotoImage(Image.open(icon_directory + aniseries + ".png"))
    return

def bg_select():
    global selected_bg, bg_directory, bg_number
    os.chdir(bg_directory)
    for file in glob.glob("*.png"):
        bg_number += 1
        bg_title["file{0}".format(bg_number)] = bg_directory + file
        bg_title_01 = (bg_title["file{0}".format(bg_number)])
        bg_title_02 = bg_title_01.replace(bg_directory, "")
        bg_list.append(bg_title_02)
    bg_list_len = len(bg_list) - 1
    selected_bg0 = random.randint(0, bg_list_len)
    selected_bg0 = bg_list[selected_bg0]
    selected_bg = ImageTk.PhotoImage(Image.open(bg_directory + selected_bg0))
    bg_label.configure(image=selected_bg)

def preload():
    #Frame
    menu = Frame(root, highlightbackground="black", highlightthickness=1)
    menu.place(width=530, height=228, x=695, y=300)

    #Widgets
    menu_button_01 = Button(menu, text="Openings", height=2)
    menu_button_02 = Button(menu, text="Endings", height=2)
    menu_button_03 = Button(menu, text="OSTs", height=2)
    menu_button_01.pack(fill=X)
    menu_button_02.pack(fill=X)
    menu_button_03.pack(fill=X)
    selection_label = Label(menu, text="Selection: ", bg="light gray", anchor='w')
    selection_label.pack(fill=X)

    #Button Functions
    def menu_op():
        global button_01_check, selection_text, selection_label_modified
        if button_01_check == 0:
            button_01_check = 1
            text_add = "Openings"
            if selection_label_modified == 1:
                text_add = ", " + text_add
            selection_text = selection_text + text_add
            selection_label_modified = 1
            selection_label.configure(text=selection_text)
            selected_item_groups.append(text_add.replace(", ", ""))
        else:
            return
    def menu_ed():
        global button_02_check, selection_text, selection_label_modified
        if button_02_check == 0:
            button_02_check = 1
            text_add = "Endings"
            if selection_label_modified == 1:
                text_add = ", " + text_add
            selection_text = selection_text + text_add
            selection_label_modified = 1
            selection_label.configure(text=selection_text)
            selected_item_groups.append(text_add.replace(", ", ""))
        else:
            return
    def menu_ost():
        global button_03_check, selection_text, selection_label_modified
        if button_03_check == 0:
            button_03_check = 1
            text_add = "OSTs"
            if selection_label_modified == 1:
                text_add = ", " + text_add
            selection_text = selection_text + text_add
            selection_label_modified = 1
            selection_label.configure(text=selection_text)
            selected_item_groups.append(text_add.replace(", ", ""))
        else:
            return

    def clear_list():
        global button_01_check, button_02_check, button_03_check, selection_text, selection_label_modified, selected_item_groups
        selection_text = "Selection: "
        selection_label.configure(text=selection_text)
        selection_label_modified = 0
        selected_item_groups = []
        button_01_check = 0
        button_02_check = 0
        button_03_check = 0
    def start():
        #Remove Menu
        widget_list = [menu_button_01, menu_button_02, menu_button_03, menu_button_04, menu_button_05, selection_label]
        for item in widget_list:
            item.pack_forget()
        menu.place_forget()

        #Background
        bg_select()

        #Timer Frame
        timer_frame = Frame(root, bg="#9fcef5")
        timer_frame.place(width=150, height=150, x=1750, y=800)
        timer_status = Label(timer_frame, text="", anchor=CENTER, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
        timer_status.pack(fill=X, side=BOTTOM)

        difficulty_select()
        loop()

    #2nd Widgets
    menu_button_04 = Button(menu, text="Clear", height=2, command=clear_list)
    menu_button_05 = Button(menu, text="Start", height=2, command=start)
    menu_button_04.pack(fill=X)
    menu_button_05.pack(fill=X)

    #Link Buttons to Functions
    menu_button_01.configure(command=menu_op)
    menu_button_02.configure(command=menu_ed)
    menu_button_03.configure(command=menu_ost)

def difficulty_select():
    global difficulty
    global total_len
    global anitype_list
    difficulty_var = "Easy"
    difficulty = difficulty_var

    #Type Select
    anitype_list_01 = selection_text.replace("Selection: ", "")
    anitype_list_02 = anitype_list_01.replace(" ", "")
    anitype_list = anitype_list_02.split(",")

    import_mp3()
    total_len = len(imported)

def import_mp3():
    global difficulty
    for item in anitype_list:
        mp3_number = 0
        mp3_title = {}
        os.chdir(resource_directory + item + "\\" + difficulty + "\\")
        for file in glob.glob("*.mp3"):
            mp3_number += 1
            mp3_title["file{0}".format(mp3_number)] = resource_directory + item + "\\" + difficulty + "\\" + file
            mp3_title_01 = (mp3_title["file{0}".format(mp3_number)])
            imported.append(mp3_title_01)

def quiz_01():
    global anititle, aniseries, count
    animax = len(imported) - 1
    select = random.randint(0, animax)
    anifile = imported[select]

    # Quiz Frame
    quiz_frame.place(x=794, y=700)
    quiz_button_01.place(x=-2, y=-2)
    quiz_button_02.place(x=109, y=-2)
    quiz_button_02.configure(state=DISABLED)
    quiz_button_03.place(x=220, y=-2)
    quiz_button_03.configure(state=DISABLED)
    quiz_status_frame.place(x=794, y=678, width=333, height=23)
    quiz_status_label.pack(fill=X)

    #Get AniDifficulty
    if "Easy" in anifile:
        anidifficulty = "Easy"
    else:
        if "Medium" in anifile:
            anidifficulty = "Medium"
        else:
            if "Hard" in anifile:
                anidifficulty = "Hard"
            else:
                anidifficulty = "Otaku"

    #Get AniType
    if "Openings" in anifile:
        anitype = "OP"
    else:
        if "Endings" in anifile:
            anitype = "ED"
        else:
            anitype = "OSTs"

    #Get AniTitle
    anititle_01 = anifile.replace(resource_directory, "")
    anititle_02 = anititle_01.replace("Openings", "")
    anititle_03 = anititle_02.replace("Endings", "")
    anititle_04 = anititle_03.replace("OSTs", "")
    anititle_05 = anititle_04.replace("Easy", "")
    anititle_06 = anititle_05.replace("Medium", "")
    anititle_07 = anititle_06.replace("Hard", "")
    anititle_08 = anititle_07.replace("Otaku", "")
    anititle = anititle_08.replace("\\", "")

    #Get Series
    aniseries0 = anititle.split(" - ")
    aniseries = aniseries0[0]

    #Start Audio
    pygame.mixer.init()
    pygame.mixer.music.load(anifile)
    pygame.mixer.music.play(1)
    imported.remove(anifile)
    timer_frame.tkraise()
    count = 15
    def timer():
        global count
        timer_status.configure(text=str(count))
        if count > 0:
            timer_var = Timer(1, timer)
            count -= 1
            timer_var.start()
        else:
            pygame.mixer.music.fadeout(1000)
    timer()

def quiz_02():
    global count, aniseries
    logo_frame.tkraise()
    count = 0
    quiz_button_02.configure(state=NORMAL)
    quiz_button_03.configure(state=NORMAL)
    logo_frame.place(x=620, y=100)
    logo_label.pack()
    load_logo()
    logo_label.configure(image=logo_image_var)

def loop():
    if len(imported) > 0:
        bg_select()
        logo_frame.lower()
        quiz_01()
    else:
        exit()

#Background
bg_label = Label(root, image=menu_bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#Timer Widgets
timer_frame = Frame(root, bg="#9fcef5", highlightbackground="black", highlightthickness=1)
timer_frame.place(width=150, height=150, x=1700, y=800)
timer_status = Label(timer_frame, text="15", anchor=CENTER, font=("Arial Bold", 96), fg='white', bg="#9fcef5")
timer_status.pack(side=BOTTOM)

#Quiz Widgets
quiz_frame = Frame(root, width=333, height=111, highlightbackground="black", highlightthickness=1)
quiz_button_01 = Button(quiz_frame, width=111, height=111, image=quiz_button_01_img, borderwidth=0, command=quiz_02)
quiz_button_02 = Button(quiz_frame, width=111, height=111, image=quiz_button_02_img, borderwidth=0, state=DISABLED)
quiz_button_03 = Button(quiz_frame, width=111, height=111, image=quiz_button_03_img, borderwidth=0, state=DISABLED, command=loop)
quiz_status_frame = Frame(root, background="white", highlightbackground="black", highlightthickness=1)
quiz_status_label = Label(quiz_status_frame, text="Correct Answer: ", background="white", anchor=W)

#Logo Widgets
logo_frame = Frame(root, width=680, height=300)
logo_label = Label(logo_frame, image=logo_image_var)

#Start
preload()
root.mainloop()