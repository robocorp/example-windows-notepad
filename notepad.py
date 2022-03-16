import datetime
import os
from RPA.Desktop.Windows import Windows

windows = Windows()


def format_text(message:str):
    message = message.replace(" ", "{VK_SPACE}")
    message = message.replace("\n", "{ENTER}")
    return message


def change_font_settings():
    NOTEPAD_FONT_NAME = os.getenv("NOTEPAD_FONT_NAME", "Comic Sans MS")
    NOTEPAD_FONT_SIZE = os.getenv("NOTEPAD_FONT_SIZE", "18")
    NOTEPAD_FONT_STYLE = os.getenv("NOTEPAD_FONT_STYLE", "Regular")

    NOTEPAD_FONT_NAME = format_text(NOTEPAD_FONT_NAME.strip().replace('"', ""))
    NOTEPAD_FONT_STYLE = format_text(NOTEPAD_FONT_STYLE.strip().replace('"', ""))

    windows.menu_select("Format->Font")
    windows.refresh_window()
    windows.mouse_click("name:'Font style:' and type:Edit")
    windows.send_keys(NOTEPAD_FONT_STYLE)
    windows.mouse_click("name:Size: and class:Edit")
    windows.send_keys(NOTEPAD_FONT_SIZE)
    windows.send_keys("%f" + NOTEPAD_FONT_NAME)
    windows.mouse_click("name:OK and type:Button")
    windows.wait_for_element("class:Edit")


def write_notepad_message(message):
    windows.type_into("class:Edit", format_text(message))


def save_and_exit():
    windows.menu_select("File->Save")
    windows.menu_select("File->Exit")


def notepad_task():
    FILE_TO_OPEN = os.getenv("FILE_TO_OPEN", "test.txt")
    windows.open_file(FILE_TO_OPEN, "Notepad", wildcard=True)
    change_font_settings()
    write_notepad_message("^a{VK_CLEAR}")
    windows.send_keys("^v{ENTER}")
    write_notepad_message("\nTimestamp: %s\n" % datetime.datetime.now())
    save_and_exit()


if __name__ == "__main__":
    notepad_task()
