import datetime
import os
from RPA.Windows import Windows

windows = Windows()


def open_notepad():
    default_test_file = f'{os.getcwd()}/test.txt'
    test_file = os.getenv("FILE_TO_OPEN", default_test_file)
    windows.windows_run(f'notepad.exe {test_file}')
    windows.control_window("type:WindowControl class:Notepad")

def change_font_settings():
    open_font_settings()
    set_font()
    set_font_style()
    set_font_size()
    windows.click("id:1") # OK

def open_font_settings():
    windows.click("type:MenuItemControl name:Format")
    windows.click("type:MenuItemControl name:Font...")

def set_font():
    windows.select("id:1136", os.getenv("NOTEPAD_FONT_NAME", "Comic Sans MS"))

def set_font_style():
    windows.select("id:1137", os.getenv("NOTEPAD_FONT_STYLE", "Regular"))

def set_font_size():
    windows.select("id:1138", os.getenv("NOTEPAD_FONT_SIZE", "12"))

def write_text_to_editor(text):
    windows.send_keys("id:15", text)

def save():
    windows.send_keys(keys="{CTRL}s")

def automate_notepad():
    open_notepad()
    change_font_settings()
    write_text_to_editor("{CTRL}a{CLEAR}") # Clear text
    write_text_to_editor(f'Timestamp: {datetime.datetime.now()}')
    save()
    windows.close_current_window()

if __name__ == "__main__":
    automate_notepad()
    
