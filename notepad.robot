*** Settings ***
Documentation     Automate Notepad.
...               Expects Windows 10, English.
Library           RPA.Windows
Library           String
Task Teardown     Close Current Window

*** Variables ***
${DEFAULT_TEST_FILE}=    ${CURDIR}${/}test.txt

*** Tasks ***
Automate Notepad
    Open Notepad
    Change font settings
    Write text to editor    {CTRL}a{CLEAR}    # Clear text
    Write text to editor    Timestamp: ${{ datetime.datetime.now() }}
    Save

*** Keywords ***
Open Notepad
    Windows Run    notepad.exe %{FILE_TO_OPEN=${DEFAULT_TEST_FILE}}
    Control Window    type:WindowControl class:Notepad

Change font settings
    Open font settings
    Set font
    Set font style
    Set font size
    Click    id:1    # OK

Open font settings
    Click    type:MenuItemControl name:Format
    Click    type:MenuItemControl name:Font...

Set font
    Select    id:1136    %{NOTEPAD_FONT_NAME=Times New Roman}

Set font style
    Select    id:1137    %{NOTEPAD_FONT_STYLE=Regular}

Set font size
    Select    id:1138    %{NOTEPAD_FONT_SIZE=12}

Write text to editor
    [Arguments]    ${text}
    Send Keys    id:15    ${text}    # Text Editor

Save
    Send Keys    keys={CTRL}s
