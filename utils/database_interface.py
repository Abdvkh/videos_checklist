import sqlite3
from typing import Dict, List, Union
from pathlib import Path
from .database_connection import DatabaseConnection


#folder = Dict(int, Union(str, str, int))

def create_database(file: str) -> None:
    with DatabaseConnection(file) as connection:
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS checklist(id integer primary key, parent_dirs text, sub_dirs text, seen integer)")


def add_all(file: str, root_path: str) -> None:
    root_items = _get_all_parent_folders(root_path)
    id = 0

    with DatabaseConnection(file) as connection:
        cursor = connection.cursor()

        for folder in root_items['folders']:
            id += 1
            cursor.execute(f'INSERT INTO checklist VALUES(?,?,"None",0)',(int(id), str(folder)))
        for non_folder_item in root_items['non_folder']:
            id += 1
            cursor.execute(f'INSERT INTO checklist VALUES(?,"non_folder_items",?,0)',(int(id), str(non_folder_item)))



def get_all(file: str, root_path: str):# -> List[folder]:
    with DatabaseConnection(file) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM checklist')

        checklist = [{'id': row[0], 'folder': row[1], 'folder_items': row[2], 'seen': row[3]} for row in cursor.fetchall()]

        return checklist


def _get_all_parent_folders(root_path: str):# -> Dict(List[str], List[str]):
    path = Path(root_path)
    folders = [item for item in path.iterdir() if item.is_dir()]
    non_folder = [item for item in path.iterdir() if not item.is_dir()]

    return {'folders': folders, 'non_folder': non_folder}

if __name__ == '__main__':
    # The temporary variables
    file      = 'checklist.db'
    root_path = '/media/user/Локальный диск/Абубакр/Study/Computer Science/Programming languages/Python/python'

    create_database(file)
    checklist = get_all(file, root_path)

    print(checklist)
