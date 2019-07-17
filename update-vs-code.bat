
REM Update Visual Studio Code configuration

REM Get setttings.json, keybindings.json, javascript.json, and extensions.txt
call python curl.py 

REM Copy .json files.
call copy settings.json    C:\Users\roger\AppData\Roaming\Code\User\settings.json
call copy keybindings.json C:\Users\roger\AppData\Roaming\Code\User\keybindings.json
call copy javascript.json  C:\Users\roger\AppData\Roaming\Code\User\snippets\javascript.json

REM Build and run install-extensions.bat file
call python build-extension-batchfile.py 
call install-extensions.bat 
