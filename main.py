import cv2
import subprocess


def adb(command):
    proc = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, shell=True)
    (out, _) = proc.communicate()
    return out.decode('utf-8')


running = True
option = 0


def switch_phone_on_off():
    adb("adb shell input keyevent 26")


def swipe(start_x, start_y, end_x, end_y, duration_ms):
    adb("adb shell input swipe {} {} {} {} {}".format(start_x, start_y, end_x, end_y, duration_ms))


def passcode_unlock():
    passcode = int(input("Enter your phones passcode: "))
    adb(f'adb shell input text "{passcode}"')
    adb("adb shell input keyevent 22")
    adb("adb shell input keyevent 20")
    adb("adb shell input keyevent 20")
    adb("adb shell input keyevent 20")
    adb("adb shell input keyevent 66")


def open_url():
    url = input("Enter the url you want to browse: ")
    adb(f'adb shell am start -a android.intent.action.VIEW -d {url}')


def call():
    number = input("Enter the number you want to call: ")
    adb(f"adb shell am start -a android.intent.action.CALL -d tel:{number}")


def send_whatsapp_message():
    std_code = input("Enter country code: ")
    phone_number = input("Enter Phone Number: ")
    phone = "+" + std_code + phone_number
    message = input("Enter the text you want to send: ")
    adb(f'adb shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone={phone}"') # Opening whatsapp url
    adb('ping 127.0.0.1 -n 2 > nul') # delay
    adb(f'adb shell input text "{message}"')  # entering message
    adb('adb shell keyevent 22') # Right arrow
    adb('adb shell keyevent 22') # Right arrow
    adb('adb shell input keyevent 22') # Right arrow
    adb('adb shell input keyevent 22') # Right arrow
    adb('adb shell input keyevent 66') # Enter Key


def exit():
    switch_phone_on_off()


def options_check(option):
    if option == 1:
        switch_phone_on_off()
    if option == 2:
        swipe(-700, 0, 700, 0, 0)
    if option == 3:
        passcode_unlock()
    if option == 4:
        open_url()
    if option == 5:
        call()
    if option == 6:
        send_whatsapp_message()
    if option == 7:
        exit()


while(running):
    print('WelCome to Mobile controller')
    print('[1] Power On')
    print('[2] Swipe Up')
    print('[3] Enter Passcode')
    print('[4] Open a Url')
    print('[5] Call A person')
    print('[6] Send A whats app Message')
    print('[7] Exit')
    option = int(input("Enter your Option: "))
    options_check(option)


