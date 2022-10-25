import subprocess
import vlc

prevUsb = subprocess.run('lsusb', capture_output=True, text=True)

try:
    while True:
        usb = subprocess.run('lsusb', capture_output=True, text=True)

        if prevUsb.stdout == usb.stdout:
            pass
        else:
            p = vlc.MediaPlayer("/home/keped/Desktop/usb.mp3")
            prevUsb = usb
except Exception as e:
    print(e)

