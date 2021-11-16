import os
import time
# dir_name = 'C:/Program Files/Java/jdk1.8.0_191/'
# dir_name = 'D:/Projects/foto-editor/test/'
dir_name = 'C:/Users/Deluxe/Desktop/Фото/'


# Get list of all files only in the given directory
list_of_files = filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) )

# Sort list of files based on last modification time in ascending order
list_of_files = sorted( list_of_files,
                        key = lambda x: os.path.getmtime(os.path.join(dir_name, x))
                        )

print(list_of_files)

for count, f in enumerate(list_of_files):

    src = dir_name + f
    dst = dir_name + \
          ('photo' if '.JPG' in f.upper() else 'video') + \
          str(count) + ('.jpg' if '.JPG' in f.upper() else '.mp4')
    os.rename(src, dst)
