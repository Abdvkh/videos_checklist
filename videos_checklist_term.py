import utils.database_interface as interface


file      = 'checklist.db'

# You need to put your own path in the future it will take the path itself
root_path = '/media/user/Локальный диск/Абубакр/Study/Computer Science/Programming languages/Python/python'

interface.create_database(file)

interface.add_all(file, root_path)

checklist = interface.get_all(file, root_path)

print(checklist)
