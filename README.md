# example-windows-notepad

Contains Robocorp Robot which automates Windows Notepad.

**explanation.** _"Robocorp Robot"_ means directory structure which is runnable with **rcc** tool (link at the bottom)

## Robot steps
  
  1. open test.txt from current directory and expect that it is opened by Notepad (as .txt associated application)
  2. change font settings
  3. clear existing text
  4. copy text from clipboard into editor
  5. save and exit
  
## Configuring run with environment variables

  - **FILE_TO_OPEN** (absolute filepath to file, defaults to current directory's _test.txt_)
  - **NOTEPAD_FONT_NAME** (default with Python is _Comic Sans MS_ and with RFW _Times New roman_)
  - **NOTEPAD_FONT_SIZE** (default is _18_)
  - **NOTEPAD_FONT_STYLE** (default is _Regular_)
 
## Running Robot with the Robot Framework syntax

  ```shell
  > rcc run -t "Notepad with RFW"
  ``` 
  
## Running Robot with the Python syntax

  ```shell
  > rcc run -t "Notepad with Python"
  ```
  
## Links

  - [RCC](https://github.com/robocorp/rcc) (Github)
  - [RCC overview](https://robocorp.com/docs/rcc/overview) (Docs)
  - [Desktop automation](https://robocorp.com/docs/development-guide/desktop) (Docs)
