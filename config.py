import os
from pathlib import Path

config = {
    "path_save": Path().home() / Path("yandex/programming/saved_configs"),
    "project_dir": Path(os.path.dirname(os.path.abspath(__file__))),
    "list_backup_files": Path(os.path.dirname(os.path.abspath(__file__))) / 'backup_files.json',
}
