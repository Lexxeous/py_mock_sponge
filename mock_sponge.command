#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]; then
	cd $( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) # change to the location of the executable source
	python "src/mock_sponge.py" # start the application and run terminal in background
	# osascript -e 'tell application "Terminal" to close first window' & exit # close the terminal
	killall Terminal
fi

# Windows OS type could be msys, cygwin, win32, win64, etc...