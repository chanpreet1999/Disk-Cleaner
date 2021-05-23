import os
import shutil

files_list = []
files_ext = []
main_path = r'E:\Chan\C prac\CPP-test'
exclude_prefixes_dir_tuple = ('New folder', 'Windows', 'Desktop', '.')
exclude_prefixes_file_tuple = ('.', 'settings')
music_set = {'mp3', 'mp4', 'mp4a'}
image_set = {'svg', 'jpg', 'jpeg', 'png'}
video_set = {'wma'}
coding_set = {"c", "java", "py", 'cpp', 'cs', 'class'}

def find_extension(x):
    extension = x.split('.')
    files_list.append(extension[0])
    files_ext.append(extension[1])
    return extension


def get_folder_name_by_ext(file_extension):
    file_extension = file_extension.lower()

    if( file_extension in music_set ):
        return "Music"
    elif (file_extension in video_set):
        return "Videos"
    elif (file_extension in image_set):
        return "Images"
    elif (file_extension in coding_set):
        return "Programs"
    elif (file_extension == 'pdf'):
        return "PDFs"
    elif (file_extension == 'docx'):
        return "DOCs"
    elif (file_extension == 'xlsx' or file_extension == 'tsv' or file_extension == 'csv'):
        return "Excel"
    elif (file_extension == 'txt'):
        return "txt-files"
    else:
        return "Unknown"


def save_to_folder(root_path, file_name, file_extension):
    # get folder_name
    folder_name = get_folder_name_by_ext(file_extension)
    source_path = os.path.join(root_path, file_name)
    destination_path = os.path.join(main_path, folder_name)

    try:
        # create folder with this name
        if not os.path.isdir(destination_path):
            os.mkdir(destination_path)
            print("created folder : ", destination_path)
    except OSError as error:
        print(error)
    # print("SRC:" + fr'{source_path}.{file_extension}'+ " Dest"+  fr'{os.path.join(destination_path, file_name)}.{file_extension}')
    shutil.move(fr'{source_path}.{file_extension}', fr'{os.path.join(destination_path, file_name)}.{file_extension}')



for (root, dirs, files) in os.walk(main_path, topdown=True):
    dirs[:] = [d for d in dirs if not d.startswith(exclude_prefixes_dir_tuple)]
    files[:] = [f for f in files if not f.startswith(exclude_prefixes_file_tuple)]
    for file in files:
        file_name, ext = find_extension(file)
        save_to_folder(root_path=root, file_name=file_name, file_extension=ext)

# print(files_list) #Contains all file names
# print(files_ext)#Contains all extensions
