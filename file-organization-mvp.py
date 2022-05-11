
import os
import getpass
import shutil



# Get current user of the computer (1)
current_user = getpass.getuser()

# Change current directory of user(2)
os.chdir('/Users/'+ current_user+'/desktop/')





# Make Folders (3)
os.mkdir("Video")
os.mkdir("Music")
os.mkdir("Documents")
os.mkdir("Pictures")


# # # Store list of files in a variable (4)
list_Files = "/Users/" + current_user +"/desktop/"
dir_list = os.listdir(list_Files)
print(dir_list)




for files in dir_list:
    if files.endswith(".png") == True:
        shutil.move(files,"Pictures")
    elif files.endswith(".jpg") == True:
         shutil.move(files,"Pictures")
    elif files.endswith(".MP4") == True:
        shutil.move(files,"Video")
    elif files.endswith(".mp3") == True:
        shutil.move(files,"Music")
    elif files.endswith(".pdf") == True:
        shutil.move(files,"Documents")
    elif files.endswith(".wav") == True:
        shutil.move(files,"Music")
    elif files.endswith(".mov") == True:
        shutil.move(files,"Video")

