
import os
import getpass
import shutil




# tuples of file-extensions 
pictures = (".png",".jpg")
audio = (".wav",".mp3")
video = (".MP4",".mov",".AVCHD",".wmv")
documents = (".pdf",".html",".doc",".docx")




# Get the username (1) 
current_user = getpass.getuser()
user_input = input("Hello "+ current_user + "! Do you want to organize your Desktop? Yes or no? ").lower()



def makefolders():
    for make in list_folderNames:
         os.mkdir(make)

 

if user_input == "yes":
    list_Files = os.chdir('/Users/'+ current_user +'/desktop/')
    folders_input = input("What folders do you want included? (Include commas please): ")
    list_folderNames = folders_input.split(",")
    makefolders()
    print(list_folderNames)
    dir_list = os.listdir(list_Files)
    send_pictures = input("Where do you want to send pictures: ").replace(" ","")

    send_videos = input("Where do you want to send videos: ").replace(" ","")

    send_documents = input("Where do you want to send documents: ").replace(" ","")

    send_audio = input("Where do you want to send audio: ").replace(" ","")

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







