import os
from datetime import datetime
from pathlib import Path

from robocorp import windows
from robocorp.tasks import setup, task
from robocorp.windows import WindowElement


desktop = windows.Desktop()
window = None  # Notepad window object after being controlled

LOCATOR_NOTEPAD = 'class:"Notepad" subname:"Notepad"'
OPEN_FILE = str(os.getenv("FILE_TO_OPEN", Path("devdata") / "test.txt").absolute())


@setup
def open_notepad(task):
    """Opens Notepad for automation, then closes it at the end."""
    desktop.windows_run(f"notepad.exe {OPEN_FILE}")
    yield
    desktop.close_windows(LOCATOR_NOTEPAD)


def _set_property(unique_id: str, value: str):
    field = window.find(f'id:"{unique_id}"')
    field.click()
    field.send_keys("{DOWN}", wait_time=0.5)
    desktop.send_keys(value, send_enter=True, wait_time=0.5)


def _select_property(unique_id: str, value: str):
    field = window.find(f'id:"{unique_id}"')
    field.ui_automation_control.Select(value)


def change_font_settings():
    # Opens the Edit menu and goes into Font.
    window.send_keys("{LAlt}e")
    window.send_keys("{LAlt}o", wait_time=3)  # wait a while for the settings to load

    # Now set different values for the font family, style and size.
    _set_property("FontFamilyComboBox", "Times New Roman")
    _select_property("FontStyleComboBox", "Regular")
    _set_property("FontSizeComboBox", "12")
    window.click('name:"Back"')


def write_text_in_editor(text: str):
    # Sets text directly inside the text editing text box of Notepad.
    text_edit = window.find('name:"Text editor"')
    text_edit.set_value(text)


@task
def automate_notepad():
    """Writes some text in Notepad after changing the font."""
    global window
    window = windows.find_window(LOCATOR_NOTEPAD)
    change_font_settings()
    write_text_in_editor(f"Timestamp: {datetime.now()}")
    window.send_keys("{Ctrl}s")
