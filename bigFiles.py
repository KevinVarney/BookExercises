#! python3
# Find the big files.

import os

for foldername, subfolders, filenames in os.walk('/'):
    for filename in filenames:
        file = os.path.join(foldername,filename)
        size = os.path.getsize(file)
        if size > 100000:
            print(file + ': ' + str(size) + ' MB')
