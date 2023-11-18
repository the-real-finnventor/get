#!python3
import requests
import argparse

parser = argparse.ArgumentParser(
    prog="get",
    description="A program to get stuff from the world wide web."
)

parser.add_argument('url')
parser.add_argument('-o', '--output')
parser.add_argument('-v', '--verbose', action="store_true")

args = parser.parse_args()
if args.url.startswith("http://") == False and args.url.startswith("https://") == False:
    args.url = f"https://{args.url}"
try:
    output = requests.get(args.url).text
except requests.exceptions.ConnectionError:
    exit(f"404: URL not found")


if args.output:
    if args.verbose:
        print(output)
    try:
        open(args.output, 'x')
    except FileExistsError:
        response = input(
            'File exists. Would you like to overwrite it? (y/n): ').lower()
        if response != 'y':
            exit("Writing aborted!")
    with open(args.output, 'w') as f:
        f.write(output)
else:
    print(output)
