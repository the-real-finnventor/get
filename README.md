# get

A program to get stuff from the world wide web.

## Quickstart

### Get the repository

-   Open you terminal, command prompt, powershell, etc. and run, `git clone https://github.com/the-real-finnventor/get.git`. If you run `ls` you should see a new folder called `get` on your computer.

### Install requirements

-   Run `cd get` to get into the `get` directory.
-   Run `pip3 install -r requirements.txt`. If you are on Windows, then it is `pip install -r requirements.txt`.

### Add alias to ~/.zprofile

-   Run `echo alias get="$PWD"/get.py >> ~/.zprofile` to be able to use the `get` command anywhere.

## Manual

usage: get [-h] [-o OUTPUT] [-v] url

positional arguments:
url

options:
-h, --help show this help message and exit
-o OUTPUT, --output OUTPUT
-v, --verbose

## Extras

### Add the Manpage

#### Probably does not work for any OS accept MacOS

-   Run `pwd` and remember or copy the output
-   Run `sudo nano /private/etc/man.conf`
-   Enter your password
-   Add to the bottom `MANPATH ` and then put the output from when you ran `pwd` earlier
-   Hold the control key and press `X`. Stop holding control and press `Y`. Press enter.
-   Now you can run `man get` and see the manual page for this program

##### Note that this program has only been tested on MacOS Monterey 12.6.8
