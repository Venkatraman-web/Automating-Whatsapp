import pyautogui


# 4th step done
i = 0
while i<=10:
    pyautogui.sleep(4)
    # 1st step done
    pyautogui.click(x=700, y=1046)
    # 2nd step done
    pyautogui.typewrite('Automated Message from Python', interval=0.010)
    # 3rd step done
    pyautogui.press('enter')
    i+=1

