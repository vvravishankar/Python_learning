from plyer import notification
import time

if __name__ == '__main__':
    image = 'C://Users//VVRAVISH//Downloads//Graphicloads-100-Flat-Clock.256.png'
    while True:
                notification.notify(

                    title="**** TAKE REST *****",
                    message="Take a break for a while",
                    #app_icon=image,
                    timeout=5)

                time.sleep(10)

