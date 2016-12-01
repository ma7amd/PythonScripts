import re, os
def rename_files():
    #get file names  from a folder 
    files_names = os.listdir(r'E:\Programming\Basic Programming Languages\PHP\Courses\PHP Tutorials Playlist') #listdir() changeing the dir to the above level dir
    saved_path = os.getcwd()
    print('Current Working directory is ' + saved_path)
    os.chdir(r'E:\Programming\Basic Programming Languages\PHP\Courses\PHP Tutorials Playlist') #you must change dir to return to the dir that contain files

    #for each file, rename filename
    for file_name in files_names:
        print('Old Name - ' + file_name)
        #print('New Name - ' + re.sub('[0-9]',"", file_name))
        #print('New Name - ' + re.sub("(r'^WWW.DOWNVIDS.NET-Beginner PHP Tutorial - )","", file_name))
        #os.rename(file_name, file_name.translate('0123456789'))
        print(re.sub(r'^([0-9]+. Beginner PHP Tutorial - )',"", file_name))
        os.rename(file_name, re.sub(r'^([0-9]+. Beginner PHP Tutorial - )'," ", file_name))
    os.chdir(saved_path)

rename_files()