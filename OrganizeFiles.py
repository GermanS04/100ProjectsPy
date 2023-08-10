import os
import shutil

# Use the path to the folder you want to organize, in this case it is to my download folder
directory = "/Users/germansalas/Downloads"
os.chdir(directory)

files = os.listdir(directory) # Getting a list of the names of the files inside the download folder

"""
    The next part of the code is for the courses of my career,
    mainly organize it by having "S3_CourseAcronym_FileName.ext"
"""

# My school folder directory
schooldir = "/Users/germansalas/Desktop/Tec/Tercer Semestre" 

courseDirs = os.listdir(schooldir) # Having the folder names of the courses
del courseDirs[0] # Eliminate first element of the courses, since it is the .DStore which appears when having the folder in the desktop
courseDirs.sort() # Sort it because in the Finder of macOS the files are in alphanumerical ascending order

coursesShort = ["ED", "DS", "ET", "IP", "SR"] # The acronyms of the courses i'm going to use in the files

# For loop to check which course the file goes into
for file in files:
    for course in coursesShort:
        if file.startswith("S3_" + course):
            # Move the file from the original directory to the new directory of the course by using the index of the coursesShort list in the courseDirs list
            # Because they are in the same index in both lists
            shutil.move(directory+"/"+file, schooldir+"/"+ courseDirs[coursesShort.index(course)] +"/"+file)


"""
    The next lines of code are to organize everything inside
    the Download folder into folders based on the name of the extension
"""

def createFolders(folders, dir):
    # A loop to check if the names of the folders we are going to put in the files exists, and if not then make them
    for folder in folders: 
        if not os.path.isdir(f"{dir}/{folder}"): # If the the path of the folder doesn't exists using the values on the foldernames list
            os.mkdir(f"{dir}/{folder}") # Create a folder with the name of the foldernames list


""" LAST THING WORKING ON 
Basically a way to move files into folder's folders but also into a single folders
 - Maybe 2 functions
"""
def move2folder(extension, directory, file):
    if file.endswith(extension):
        shutil.move(f"{directory}/{file}", f"{directory}/{extension.upper()}/{file}")

# Making the father folders
originfolders = ["Images", "Apps & Stuff", "Audios"]
folderouts = ["PDF", "DOCX", "PPTX", "TXT"] 

#Creating the father folders if they not exist in the Downloads folder
createFolders((originfolders+folderouts), directory)


# Names of the child folders to create or check if they are created
folderimg = ["JPEG", "PNG", "WEBP", "JPG"]
folderaudios = ["MP3", "MP4"]
folderstuff = ["DMG", "ZIP"]

# Creating all folders of images files inside the Images folder
createFolders(folderimg, f"{directory}/Images")

createFolders(folderaudios, f"{directory}/Audios")

createFolders(folderstuff, f"{directory}/Apps & Stuff")


for file in files:
    if file.endswith("pdf"):
        shutil.move(f"{directory}/{file}", f"{directory}/PDF/{file}")

"""
# A loop to move the files to their corresponding folder
for file in files:
    for folder in foldernames2: # Goes through each of the foldernames values
        if file.endswith(folder.lower()): # If the extension name of the file is the same as the folder name
            shutil.move(directory+"/"+file, directory+"/"+folder+"/"+file) # Move the file to the corresponding folder
"""