# TODO: [] - Correct search engine
#       [] - Make seen marker

import utils.database_interface as interface

# File name for sqlite3 database
file = 'checklist.db'

# You need to put your own path in the future it will take the path itself
# root_path = input("Please enter the path of the folder: ")
root_path = '/media/user/Локальный диск/Абубакр/Study/Computer Science/Programming languages/Python/python'

# Creating sqlite3 database
interface.create_database(file)

# Adding all the items into the database
interface.add_all(file, root_path)

# Getting a dictionary of folders of root path and its items
checklist = interface.get_all(file, root_path)


def change() -> str:
    global root_path

    new_path = input("Enter new path for which video checklist will be created: ")

    confirmation = str(input("Do you confirm new root?(Yes/No)"))

    root_path = new_path if confirmation.lower() == 'yes' else root_path


def search(users_title: str):
    for folder in checklist:
        database_video_item = folder['folder_items'].replace(f"{folder['folder']}/", "")

        if database_video_item == users_title:
            print_video_item(folder)


def print_video_item(folder_in_checklist):
        print(folder_in_checklist['id'], folder_in_checklist['folder'].replace(root_path, "Folder: "), "\n", folder_in_checklist['folder_items'].replace(folder_in_checklist['folder'], "Folder items: "))


def print_all(file: str, root_path: str):
    '''To ge all the folders and its consistence of given root path'''

    print(f"Printing folders of {root_path} and their consistence: \n")
    for folder in checklist:
        print_video_item(folder)


def control_panel():
    txt =    """
Commands:

'c' - change root path,
'f' - searching through videos,
'a' - printing all the directories with items,
'n' - print next(starting) folder with its items,
'p' - previous folder with its items,
's' - change the status of the given video to seen,
'q' - to quit the program

"""

    command = input(txt)

    while command != 'q':
        if command == 'c':
            change()
        elif command == 'f':
            users_title = input("Enter the title of he video you want to find: ")

            search(users_title)
        elif command == 'a':
            print_all(file, root_path)
        elif command == 'n':
            next()
        elif command == 'p':
            previous()
        elif command == 's':
            seen()

        command = input(txt)



if __name__ == '__main__':
    print("Videos checklist program which helps you to track the downloaded videos you have seen.")
    control_panel()
