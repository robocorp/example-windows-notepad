*** Settings ***
Documentation     Copy text from clipboard to Notepad and change font settings.
Library           String
Library           RPA.Desktop.Windows
Library           RPA.FileSystem

*** Keywords ***
Format text
    [Arguments]    ${text}
    ${text}=    Replace String    ${text}    ${SPACE}    {VK_SPACE}
    ${text}=    Replace String    ${text}    \n    {ENTER}
    [Return]    ${text}

*** Keywords ***
Change font settings
    Set Task Variable    ${fontname}    %{NOTEPAD_FONT_NAME=Times New Roman}
    Set Task Variable    ${fontsize}    %{NOTEPAD_FONT_SIZE=12}
    Set Task Variable    ${fontstyle}    %{NOTEPAD_FONT_STYLE=Regular}
    Menu Select    Format->Font
    Refresh Window    # because UI changed
    Wait For Element    name:\'Font style:\' and type:Edit
    Mouse Click    name:\'Font style:\' and type:Edit
    Send Keys    ${fontstyle}
    Mouse Click    name:Size: and class:Edit
    Send Keys    ${fontsize}
    ${fontname}=    Format Text    ${fontname}
    Send Keys    %f${fontname}
    Mouse Click    name:OK and type:Button
    Wait For Element    class:Edit

*** Keywords ***
Write Notepad message
    [Arguments]    ${message}
    ${message}=    Format Text    ${message}
    Type Into    class:Edit    ${message}

*** Keywords ***
Save and exit
    Menu Select    File->Save
    Sleep    1s    # For demo purpose
    Menu Select    File->Exit

Run teardown
    Run Keyword If Test Failed
    ...    Screenshot
    ...    ${OUTPUT_DIR}${/}fail.png
    ...    desktop=True
    Close All Applications

*** Tasks ***
Notepad Font menu
    Set Task Variable    ${workfile}    %{FILE_TO_OPEN=test.txt}
    Open File    ${workfile}    Notepad    wildcard=True
    Change font settings
    Write Notepad message    ^a{VK_CLEAR}    # Clear Notepad editor
    Send Keys    ^v{ENTER}
    Write Notepad message    \nTimestamp: ${{ datetime.datetime.now() }}\n
    Screenshot    output/success.png    desktop=True
    Save and exit
    [Teardown]    Run Teardown
