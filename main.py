import pyautogui
import time
import pyperclip

# Step 0: Click WhatsApp icon to open it (double click to ensure it opens)
pyautogui.moveTo(1268, 912)
pyautogui.click()
time.sleep(0.2)
pyautogui.click()
time.sleep(6)

# Step 1: Drag to reveal messages
pyautogui.moveTo(471, 244)
pyautogui.dragTo(1176, 832, duration=0.7, button='left')

# Step 2: Copy selected text
pyautogui.hotkey('command', 'c')
time.sleep(0.6)

# Step 3: Click elsewhere to deselect
pyautogui.click(1172, 828)

# Step 4: Read and print conversation
convo = pyperclip.paste()
print("Conversation:\n", convo)

# Step 5: Click on message input box
pyautogui.click(597, 870)

# Step 6: Match & Respond
lst = ["Hey wassup!", "Money", "Plans", "return book", "EAT", "Mummy"]
r_dict = {
    lst[0]: "I am good",               #We r using lst[i] here
    lst[1]: "No bro I dont have it",
    lst[2]: "Busy",
    lst[3]: "Okay",
    lst[4]: "lets goo",
    lst[5]: "Can i go and play basketball?"
}

matched = False
for key in lst:
    if key in convo or key.capitalize() in convo or key.upper() in convo or key.lower() in convo:
        pyautogui.write(r_dict[key], interval=1)
        matched = True
        break  # stop after first match to avoid confusion

if not matched:
    pyautogui.write("hi", interval=1)

# Optional: Send it
# pyautogui.press('enter')
