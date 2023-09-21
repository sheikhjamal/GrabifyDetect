from urllib.parse import urlparse
import tkinter as tk
from tkinter import ttk

linklist = (
    "lovebird.guru", "trulove.guru", "dateing.club", "shrekis.life",
    "headshot.monster", "gaming-at-my.best", "programming.monster",
    "yourmy.monster", "imageshare.best", "screenshot.best",
    "gamingfun.me", "catsnthings.com", "catsnthings.fun",
    "curiouscat.club", "joinmy.site", "fortnitechat.site",
    "fortnight.space", "freegiftcards.co", "stopify.co",
    "leancoding.co", "grabify.link", "photovaults.pics",
    "bathtub.pics", "foot.wiki", "thisdomainislong.lol",
    "gamergirl.pro", "picshost.pics", "pichost.pics",
    "gamertag.shop", "imghost.pics", "imagehost.pics",
    "toldyouso.lol", "toldyouso.pics", "screenshare.pics",
    "myprivate.pics", "noodshare.pics", "cheapcinema.club",
    "shhh.lol", "partpicker.shop", "sportshub.var", "locations.quest"
)


def check_link():
    link = entry.get()
    domain = urlparse(link).netloc.lower()  
    if domain in linklist:
        result_label.config(text=link + " is not a Grabify link")
    else:
        result_label.config(text=link + " is a Grabify link")


window = tk.Tk()
window.title("Grabify Detector")
window.geometry("400x250")  

title_label = ttk.Label(window, text="Grabify Detector", font=("Arial", 16))
title_label.pack(pady=20)

entry = ttk.Entry(window, width=30)
entry.pack(pady=10)

button = ttk.Button(window, text="Check", command=check_link)
button.pack()

result_label = ttk.Label(window, text="")
result_label.pack(pady=10)

credit_label = ttk.Label(window, text="Made by sheikhjamal", font=("Arial", 10))
credit_label.pack(pady=5)

window.mainloop()
