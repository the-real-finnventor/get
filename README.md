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

#### MacOS

From the `get` directory, run:
```
echo "MANPATH $PWD" | sudo tee -a /private/etc/man.conf
```

##### Note that this program has only been tested on MacOS Monterey 12.6.8
