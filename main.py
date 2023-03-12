#!/usr/bin/env python

import tkinter
import customtkinter
import time
# import os

from threading import Thread


has_button_been_pressed = False


def returnMsg(prefix, sec):
    return f"{prefix}: {sec//60:02d}:{sec%60:02d}"


def pomodoro():
    global has_button_been_pressed
    i = 0
    while i <= 3:
        study(1500)
        break_(300, i)
        i += 1
    long_break(900)
    has_button_been_pressed = False


def study(sec):
    while sec > 0:
        sec -= 1
        app.label.configure(text=returnMsg("Study", sec))
        time.sleep(1)


def break_(sec, i):
    while sec > 0 and i != 3:
        sec -= 1
        app.label.configure(text=returnMsg("Break", sec))
        time.sleep(1)


def long_break(sec):
    while sec > 0:
        sec -= 1
        app.label.configure(text=returnMsg("Long Break", sec))
        time.sleep(1)


def threading():
    global has_button_been_pressed
    if has_button_been_pressed is False:
        has_button_been_pressed = True
        t1 = Thread(target=pomodoro, args=())
        t1.start()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.title("Pomodoro Timer")
        self.minsize(400, 300)

        self.label = customtkinter.CTkLabel(master=self, text="00:00")
        self.label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.button = customtkinter.CTkButton(master=self,
                                              text="Start Timer",
                                              command=threading)
        self.button.pack(padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
