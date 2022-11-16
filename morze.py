import os
from time import sleep

L = 1000
S = 100

MORSE = {
    "A":(S,L,),
    "B":(L,S,S,S,),
    "C":(L,S,L,S,),
    "D":(L,S,S,),
    "E":(S,),
    "F":(S,S,L,S,),
    "G":(L,L,S,),
    "H":(S,S,S,S,),
    "I":(S,S,),
    "J":(S,L,L,L,),
    "K":(L,S,L,),
    "L":(S,L,S,S,),
    "M":(L,L,),
    "N":(L,S,),
    "O":(L,L,L,),
    "P":(S,L,L,S,),
    "Q":(L,L,S,L,),
    "R":(S,L,S,),
    "S":(S,S,S,),
    "T":(L,),
    "U":(S,S,L,),
    "V":(S,S,S,L,),
    "W":(S,L,L,),
    "X":(L,S,S,L,),
    "Y":(L,S,L,L,),
    "Z":(L,L,S,S,),
    "0":(L,L,L,L,L,),
    "1":(S,L,L,L,L,),
    "2":(S,S,L,L,L,),
    "3":(S,S,S,L,L,),
    "4":(S,S,S,S,L,),
    "5":(S,S,S,S,S,),
    "6":(L,S,S,S,S,),
    "7":(L,L,S,S,S,),
    "8":(L,L,L,S,S,),
    "9":(L,L,L,L,S,),
}

def vibro(d: int) -> None:
    os.system(
        f"termux-vibrate -d {d} -f"
    )
    sleep(1)


def torch(d: int) -> None:
    os.system("termux-torch on")
    sleep(d / 1000)
    os.system("termux-torch off")
    sleep(.1)

def to_morze(signal_type: str, text:str) -> None:
    method = torch if signal_type == "t" else vibro
    for letter in text.upper():
        try:
            for d in MORSE[letter]:
                method(d)
        except KeyError:
            pass


signal = input("input signal type(t - torch, v - vibro):\n")
msg = input("input message:\n")
to_morze(signal, msg)
