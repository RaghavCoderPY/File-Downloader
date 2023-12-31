import requests
import argparse
import shutil

def download(url: str, name: str) -> None:
    r = requests.get(url)
    with open(name, "wb") as f:
        f.write(r.content)

arg = argparse.ArgumentParser()
arg.add_argument("file_url", help="file to download")
arg.add_argument("--o", "-o", help="name of the file")
args = arg.parse_args()

url = args.file_url
name = args.o

download(url, name)
shutil.move(name, f"downloaded_images/{name}")
