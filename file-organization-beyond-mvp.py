
import os
import getpass
import shutil




# tuples of file-extensions 
pictures = (".png",".jpg",".JPG")
audio = (".wav",".mp3")
video = (".mp4",".mov",".AVCHD",".wmv")
documents = (".pdf",".html",".doc",".docx",".py",".js",".html",".css")




# Get the username of the computer(1) 
current_user = getpass.getuser()
print("Welcome to the Desktop Organization Program!")
user_input = input( current_user +"," + " Do you want to organize your Desktop? Yes or no? ").lower()


# function that makes the folders
def makefolders():
    for make in list_folderNames:
         os.mkdir(make)

 

if user_input == "yes":

    # Changes current directory to desktop 
    list_Files = os.chdir('/Users/'+ current_user +'/desktop/')
    # Asks the user what folders they want included 
    folders_input = input("What folders do you want included? (Include commas please): ")
    # Folders are then turned into a list 
    list_folderNames = folders_input.split(",")
    makefolders()
    print(list_folderNames)
    dir_list = os.listdir(list_Files)


    # Ask the users where to send files 
    send_pictures = input("Where do you want to send pictures: ")
    send_videos = input("Where do you want to send videos: ")
    send_documents = input("Where do you want to send documents: ")
    send_audio = input("Where do you want to send audio: ")
   
    # Loops through list of files on desktop and sends files 
    for files in dir_list:
        if files.endswith(pictures) == True:
            shutil.move(files,send_pictures)
        if files.endswith(documents)== True:
            shutil.move(files,send_documents)
        if files.endswith(video)== True:   
            shutil.move(files,send_videos)
        if files.endswith(audio)== True:
            shutil.move(files,send_audio)

else: 
    print("Thank you, have a great day")


