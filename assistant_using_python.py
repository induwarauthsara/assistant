import keyboard, time
item_list = ["notepad", "chrome", "firefox", "calc", "mspaint", "explorer", "wordpad" ]
print("1.notepad\n2.chrome\n3.firefox\n4. Calculator\n5.  Paint\n6. My Compueter (Explorer)\n7. WordPad\n  \n asawa harida dan binath kommlo")
choice = input("enter Your Choice :")
keyboard.press("win+r")
keyboard.release("win")
time.sleep(0.3)
keyboard.write(item_list[int(choice) - 1], delay=0.05)
time.sleep(0.1)
keyboard.press_and_release("enter")
