import os
import re
import pathlib
import numpy
from PIL import Image

def rename(MANGA_DIR = '../dataset'):
    folders = os.listdir(MANGA_DIR)
    for folder in folders:
        id = re.findall("\d+", folder)[-1].zfill(3)
        os.rename(os.path.join(MANGA_DIR, folder), os.path.join(MANGA_DIR, id))

def remove_useless_files(MANGA_DIR = '../dataset'):
    folders = os.listdir(MANGA_DIR)
    for folder in folders:
        chapter_dir = os.path.join(MANGA_DIR, folder)
        for root, subdir, files in os.walk(chapter_dir):
            for file in files:
                # remove ads
                if 'MangaCruzers' in file:
                    print(f"{os.path.join(root, file)} removed.")
                    os.remove(os.path.join(root, file))
                    

    

if __name__=='__main__':
    # rename()
    remove_useless_files()