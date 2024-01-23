import os
import platform
from datetime import datetime
from pathlib import Path

from robocorp import windows
from robocorp.tasks import setup, task


desktop = windows.Desktop()
window = None  # Notepad window object after being controlled

LOCATOR_NOTEPAD = 'class:"Notepad" subname:"Notepad"'
TEXT_FILE = str(os.getenv("FILE_TO_OPEN", Path("devdata") / "test.txt").absolute())
FONT_FAMILY = os.getenv("NOTEPAD_FONT_NAME", "Times New Roman")
FONT_STYLE = os.getenv("NOTEPAD_FONT_STYLE", "Regular")
FONT_SIZE = os.getenv("NOTEPAD_FONT_SIZE", "12")


def get_win_version() -> str:
    """Windows only utility which returns the current Windows major version."""
    # Windows terminal `ver` command is bugged, until that's fixed, check by build
    #  number. (the same applies for `platform.version()`)
    WINDOWS_10_VERSION = "10"
    WINDOWS_11_BUILD = 22000
    version_parts = platform.version().split(".")
    major = version_parts[0]
    if major == WINDOWS_10_VERSION and int(version_parts[2]) >= WINDOWS_11_BUILD:
        major = "11"

    return major


@setup
def open_close_notepad(task):
    """Opens Notepad for automation, then closes it at the end."""
    desktop.windows_run(f"notepad.exe {TEXT_FILE}")
    yield
    desktop.close_windows(LOCATOR_NOTEPAD)


def _set_property(unique_id: str, value: str):
    field = window.find(f'id:"{unique_id}"')
    field.click()
    field.send_keys("{DOWN}", wait_time=0.5)
    desktop.send_keys(value, send_enter=True, wait_time=0.5)


def _select_property(unique_id: str, value: str):
    field = window.find(f'id:"{unique_id}"')
    field.select(value)


def change_font_settings(family: str, style: str, size: str):
    ver = get_win_version()  # slightly different automation based on Windows version

    # Opens the Edit menu and goes into Font.
    if ver == "11":
        window.send_keys("{LAlt}e")
        window.send_keys("{LAlt}o", wait_time=3)  # wait for the settings to load
    else:
        window.send_keys("{LAlt}of", wait_time=1)

    # Now set different values for the font family, style and size.
    if ver == "11":
        _set_property("FontFamilyComboBox", family)  # doesn't work with selection
        _select_property("FontStyleComboBox", style)
        _set_property("FontSizeComboBox", size)  # doesn't work with selection
        window.click('name:"Back"')  # goes back and automatically saves the settings
    else:
        # Selection works everywhere now.
        _select_property("1136", family)
        _select_property("1137", style)
        _select_property("1138", size)
        desktop.send_keys("{Enter}")  # saves the new settings


def write_text_in_editor(text: str):
    # Sets text directly inside the text editing box of Notepad.
    text_edit = window.find('regex:"Text (E|e)ditor"')
    text_edit.set_value(text)


@task
def automate_notepad():
    """Writes some text in Notepad after changing the font."""
    global window
    window = windows.find_window(LOCATOR_NOTEPAD)
    change_font_settings(FONT_FAMILY, FONT_STYLE, FONT_SIZE)
    write_text_in_editor(f"Timestamp: {datetime.now()}")
    window.send_keys("{Ctrl}s")  # saves the new content
