# Windows Notepad automation

This example demonstrates a basic Notepad app automation, compatible with both Windows
11 and Server 2019.

## How it works

1. Opens the provided [*test.txt*](devdata/test.txt) in Notepad using the Windows Run
     widget.
2. Initially it configures the font.
3. Then it sets a text (current timestamp) in the already opened file.
4. Saves the new content in the file, then closes the app.

### Configuring the run with environment variables

- `FILE_TO_OPEN`: An absolute filepath to a file, defaults to
 [*test.txt*](devdata/test.txt) found in *devdata*.
- `NOTEPAD_FONT_NAME`: Defaults to "Times New Roman".
- `NOTEPAD_FONT_STYLE`: Defaults to "Regular".
- `NOTEPAD_FONT_SIZE`: Defaults to "12".

## Links

- [Windows library](https://robocorp.com/docs/python/robocorp/robocorp-windows)
- [Windows locators](https://robocorp.com/docs/development-guide/locators/windows)
- [Windows setup](https://robocorp.com/docs/control-room/unattended/worker-setups/windows-desktop)
- [Desktop automation](https://robocorp.com/docs/development-guide/desktop)
