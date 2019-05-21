from zipfile import ZipFile
import os
from shutil import copyfile

for root, folders, files in os.walk("sample"):
    for filename in files:
        if filename.endswith(".xlsx"):
            copyfile("sample/" + filename, "excel/" + filename)

def main():

    directory = './'
    file_paths = get_all_file_paths(directory)

    with ZipFile('excel.zip','w') as file:
        for file in file_paths:
            zip.write(file)
        print('All files zipped successfully!')
if __name__ == "__main__":
    main()

import shutil
shutil.make_archive("excel","zip","folders")