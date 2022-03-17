# Windows Notepad automation

Contains a Robocorp robot which automates Windows Notepad.

**Explanation.** _"Robocorp Robot"_ means a directory structure which is runnable with [RCC](https://github.com/robocorp/rcc).

## Robot steps
  
  1. Open test.txt from current directory in Notepad.
  2. Change font settings.
  3. Clear existing text.
  4. Write text into the editor.
  5. Save and exit.
  
## Configuring run with environment variables

  - **FILE_TO_OPEN** (an absolute filepath to file, defaults to current directory's _test.txt_)
  - **NOTEPAD_FONT_NAME** (default with Python is _Comic Sans MS_ and with RFW _Times New roman_)
  - **NOTEPAD_FONT_SIZE** (default is _18_)
  - **NOTEPAD_FONT_STYLE** (default is _Regular_)
 
## Running Robot with the Robot Framework syntax

  ```shell
  > rcc run -t "Notepad with Robot Framework"
  ``` 
  
## Running Robot with the Python syntax

  ```shell
  > rcc run -t "Notepad with Python"
  ```
  
## Links

  - [RCC](https://github.com/robocorp/rcc) (Github)
  - [RCC overview](https://robocorp.com/docs/rcc/overview) (Docs)
  - [Desktop automation](https://robocorp.com/docs/development-guide/desktop) (Docs)
