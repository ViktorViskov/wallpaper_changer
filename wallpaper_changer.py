#!/usr/bin/python3

# libs
import requests, os, sys, time

# function for download img file
def load_image():
    # print message
    print("Loading image ...")

    # url
    random_image_link = "https://picsum.photos/1920/1080"

    # return downloaded image
    return requests.get(random_image_link, timeout = 10, allow_redirects=True).content

# function for save image
def save_image(path_to_file, file):
    # print message
    print("Saving image ...")

    # save file
    open(path_to_file, "wb").write(file)

# function for set wallpaper
def set_wallpaper(path_to_file):
    # print message
    print("Set wallpapers ...")

    ### set background for 2 displays xfce4
    # screen_1 = "/backdrop/screen0/monitorDP-0/workspace0/last-image"
    # screen_2 = "/backdrop/screen0/monitorDVI-D-0/workspace0/last-image"
    # os.system("xfconf-query -c xfce4-desktop -p %s -s %s" % (screen_1, path_to_file))
    # os.system("xfconf-query -c xfce4-desktop -p %s -s %s" % (screen_2, path_to_file))

    ### set background using feh
    os.system("feh --bg-fill %s" % (path_to_file))

# function for changing wallpapers
def change_wallpapers():
    # start app
    try:
        # load image
        image = load_image()

        # save image
        save_image("/home/viktor/.config/current_wallpaper.jpg", image)

        # set wallpaper
        set_wallpaper("/home/viktor/.config/current_wallpaper.jpg")

    except:
        # print error
        print("Error. Check your connection or path to file")

# start main script

# change wallpaper if without called without arguments
if (len(sys.argv) == 1):
    change_wallpapers()

# with arguments
else:

    try:
        minuts = int(sys.argv[1])
    except:
        # print error message
        print("Argument must been minuts digit. Default walue 10 minuts")

        # default value
        minuts = 10

    # start loop
    while True:
        # clean screen
        os.system("clear")

        # print message
        print("Changing wallpaper every %s minuts" % minuts)

        # pause 10 min
        time.sleep(minuts * 60)
        
        # change wallpaper
        change_wallpapers()
