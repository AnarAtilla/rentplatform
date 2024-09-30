import os
import glob

# Укажите путь к вашему проекту
project_path = "D:\\rentfinal\\rentapp"

# Найти все папки с миграциями
migration_folders = glob.glob(os.path.join(project_path, "**", "migrations"), recursive=True)

for folder in migration_folders:
    # Удалить все файлы .py, кроме __init__.py
    for file in glob.glob(os.path.join(folder, "*.py")):
        if not file.endswith("__init__.py"):
            os.remove(file)
    # Удалить все файлы .pyc
    for file in glob.glob(os.path.join(folder, "*.pyc")):
        os.remove(file)

print("Миграции удалены.")