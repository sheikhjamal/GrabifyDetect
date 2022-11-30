from urllib.parse import urlparse 
linklist = ("lovebird.guru", "trulove.guru", "dateing.club", "shrekis.life", "headshot.monster", "gaming-at-my.best", "programing.monster", "yourmy.monster", "imageshare.best", "screenshot.best", "gamingfun.me", "catsnthings.com", "catsnthings.fun", "curiouscat.club", "joinmy.site", "fortnitechat.site", "fortnight.space", "freegiftcards.co", "stopify.co", "leancoding.co", "grabify.link", "photovaults.pics", "bathtub.pics", "foot.wiki", "thisdomainislong.lol","gamergirl.pro","picshost.pics", "pichost.pics", "gamertag.shop","imghost.pics","imagehost.pics","toldyouso.lol","toldyouso.pics","screenshare.pics", "myprivate.pics", "noodshare.pics", "cheapcinema.club", "cheapcinema.club", "shhh.lol","partpicker.shop","sportshub.var","locations.quest")

print("GrabifyDetect by sheikhjamal")
while True:
  link = input("Enter the link: ")
  domain = urlparse(link).netloc
  if domain in linklist:
    print(link + " is from Grabify")
  else:
    print(link + " is not from Grabify")
