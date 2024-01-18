import os
from datetime import datetime
from pathlib import Path

from robocorp import windows
from robocorp.tasks import setup, task


desktop = windows.Desktop()


LOCATOR_NOTEPAD = 'class:"Notepad" subname:"Notepad"'
OPEN_FILE = str(os.getenv("FILE_TO_OPEN", Path("devdata") / "test.txt"))


# @setup
# def open_notepad(task):
#     """Opens Notepad for automation, then closes it at the end."""
#     desktop.windows_run(f"notepad.exe {OPEN_FILE}")
#     yield
#     desktop.close_windows(LOCATOR_NOTEPAD)


def change_font_settings():
    window = windows.find_window(LOCATOR_NOTEPAD)
    # window.send_keys("{LAlt}e")
    # window.send_keys("{LAlt}o")

    family = window.find('id:"FontFamilyComboBox"')
    family.ui_automation_control.Select("Times New Roman")
    style = window.find('id:"FontStyleComboBox"')
    style.ui_automation_control.Select("Regular")
    size = window.find('id:"FontSizeComboBox"')
    size.ui_automation_control.Select(22)
    pass


@task
def automate_notepad():
    """Writes some text in Notepad after changing the font."""
    change_font_settings()
    # write_text_in_editor(f"Timestamp: {datetime.now()}")
