#!/bin/sh

# /etc/X11/xinit/xinitrc
#
# global xinitrc file, used by all X sessions started by xinit (startx)

# invoke global X session script
#. /etc/X11/Xsession

# change wallpapers one time in hour
while :
do
    feh --bg-fill ~/.config/current_wallpaper.jpg
    sleep 3600
    wallpaper_changer.py
done &

# loop for status panel
while :
do
    xsetroot -name `statusBar.sh foo`
    sleep 15
done &

# turn off screeen after 60 second (change dpms)
xset dpms 0 0 60 &

#background light 50%
xbacklight -set 50 &

# start dwm
exec dwm
