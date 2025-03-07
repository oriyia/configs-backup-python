#!/usr/bin/env python3

# Backup всех важных файлов системы.

import datetime
import json
import os
import shutil
from pathlib import Path

import click
from loguru import logger

from config import config

logger.add("debug.log")

list_backup_files = str(config["list_backup_files"])


def create_directory_save(path_save: Path) -> Path:
    current_date = datetime.datetime.now()
    current_date_short = current_date.strftime("%d_%m_%Y_%H_%M_%S")
    full_name_path_directory = path_save / Path(current_date_short)
    os.mkdir(str(full_name_path_directory))
    return full_name_path_directory


def create_backup_copy_file_list():
    path_list_file = os.path.dirname(os.path.abspath(__file__))
    old_name_file = "backup_files.json"
    new_name_file = str(Path(old_name_file).stem) + "_bc.json"
    source = Path(path_list_file) / Path(old_name_file)
    target = Path(path_list_file) / Path(new_name_file)
    shutil.copyfile(str(source), str(target))


def add_new_file_to_list(new_file: str) -> int:
    path_new_file = Path(new_file)
    name_new_file = path_new_file.name
    full_path_new_file = Path.cwd() / path_new_file
    create_backup_copy_file_list()
    if not full_path_new_file.exists():
        click.echo(f"Такого файла не существует: {str(full_path_new_file)}")
        return 1
    else:
        with open(list_backup_files) as file:
            list_object = json.load(file)
        while True:
            name_directory = input("Имя директории: ")
            if name_directory in list_object:
                click.echo(f"Директория '{name_directory}' уже есть. Укажите другое.")
                continue
            list_object[str(name_new_file)] = str(full_path_new_file)
            with open(list_backup_files, "w") as json_file:
                json.dump(list_object, json_file)
            click.echo(f"Новая запись: '{name_directory}':'{str(full_path_new_file)}'")
            return 0


@logger.catch
def copy_object(source: str, target: str):
    try:
        if Path(source).is_dir():
            shutil.copytree(source, str(target))
        else:
            shutil.copy2(source, str(target))
    except FileNotFoundError as FN:
        logger.debug(f"Не удалось скопировать: {source}")
        logger.debug(f"Error: {FN}")
    else:
        logger.info(f"(+) {source}")


@logger.catch
def dictionary_parsing(files: dict, full_name_path_dir: Path):
    for key, value_dict in files.items():
        current_directory = Path(full_name_path_dir)
        new_current_directory = Path(current_directory, key)
        new_current_directory.mkdir()
        if type(value_dict) == str:
            source = value_dict
            name_file = Path(source).name
            target = new_current_directory / name_file
            copy_object(source, str(target))
        elif type(value_dict) == list:
            for value_list in value_dict:
                if type(value_list) == str:
                    source = value_list
                    name_file = Path(source).name
                    target = new_current_directory / name_file
                    copy_object(source, str(target))
                elif type(value_list) == dict:
                    dictionary_parsing(value_list, new_current_directory)
        elif type(value_dict) == dict:
            dictionary_parsing(value_dict, new_current_directory)


@click.command()
@click.option(
    "-nf", "--new-file", default=None, help="Добавить в список новый сохраняемый файл"
)
def backup_files(new_file):
    """Function save important files"""
    logger.info("НАЧАЛО ОТЛАДКИ")
    if new_file:
        if add_new_file_to_list(new_file) != 0:
            return
    full_name_created_dir = create_directory_save(config["path_save"])
    with open(list_backup_files) as file:
        conservation_objects = json.load(file)
    dictionary_parsing(conservation_objects, full_name_created_dir)


if __name__ == "__main__":
    backup_files()
