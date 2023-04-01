#!/usr/bin/env python3

# backup всех важных конфигов системы

import os
import datetime
import shutil


def get_current_date_time():
    separator = "-----------------------"
    current_date = datetime.datetime.now()
    current_date_short = current_date.strftime("%d/%m/%Y, %H:%M:%S")
    header_log = separator + current_date_short + separator
    return header_log


list_configs = {
    "zsh": "/home/oriyia/.zshrc",
    "alacritty": "/home/oriyia/.config/alacritty/",
    "i3": "/home/oriyia/.config/i3/config",
    "betterlockscreen": "/home/oriyia/.config/betterlockscreenrc",
    "nvim": "/home/oriyia/.config/nvim/",
    "bash_history": "/home/oriyia/.bash_history",
    "bashrc": "/home/oriyia/.bashrc",
    "bash_profile": "/home/oriyia/.profile",
    "python_history": "/home/oriyia/.python_history",
    "xinitrc": "/home/oriyia/.xinitrc",
    "xmodmap": "/home/oriyia/.Xmodmap",
    "xprofile": "/home/oriyia/.xprofile",
    "xresources": "/home/oriyia/.Xresources",
    "polybar": "/home/oriyia/.config/polybar/",
    "ranger": "/home/oriyia/.config/ranger/",
    "pygments": "/usr/lib/python3/dist-packages/pygments/styles/my.py",
    "zathura": "/home/oriyia/.config/zathura/zathurarc",
    "ppa": "/etc/apt/sources.list",
    "rofi": "/home/oriyia/.config/rofi/config.rasi",
    "rofi_theme": "/home/oriyia/.local/share/rofi/themes/rofi_mytheme_onedark.rasi",
    "zsh_history": "/home/oriyia/.zsh_history",
    "zshrc": "/home/oriyia/.zshrc",
    "starship": "/home/oriyia/.config/starship.toml",
    "lsd": "/home/oriyia/.config/lsd/config.yaml",
    "lsd_themes": "/home/oriyia/.config/lsd/themes/lsd_theme.yaml",
    "vivid": "/home/oriyia/.config/vivid/vivid_mytheme_onedark.yml",
    "glow": "/home/oriyia/.config/glow/glow.yml",
    "glamour": "/home/oriyia/.config/glow/myconf.json",
    "ipython_config": "/home/oriyia/.ipython/profile_default/ipython_config.py",
    "autojump": "/home/oriyia/.local/share/autojump/autojump.txt",
    "bat_config": "/home/oriyia/.config/bat/config",
    "bat_theme": "/home/oriyia/.config/bat/themes/sublime-snazzy/NewBatThemeLight.tmTheme",
    "systemd_yandex_disk": "/etc/systemd/system/yandex-disk.service",
    "delta": "/home/oriyia/.config/themes.gitconfig",
    "lazygit": "/home/oriyia/.config/lazygit/config.yml"
}

log_file = open("results.txt", "a")


def create_directory(target_path):
    if not os.path.exists(target_path):
        os.mkdir(target_path)


def write_info_log_file(log_message):
    log_message = log_message + "\n"
    log_file.write(log_message)


def backup_files(key, path_object):
    target_path = os.environ["PWD"] + "/saved_configs/" + key + "/"
    create_directory(target_path)
    if os.path.isdir(path_object):
        try:
            log_message = '+++++ ' + key
            shutil.copytree(path_object, target_path,
                            copy_function=shutil.copy2, dirs_exist_ok=True)
            write_info_log_file(log_message)
        except BaseException:
            log_message = '---- ' + key
            write_info_log_file(log_message)
    else:
        try:
            log_message = '+++++ ' + key
            shutil.copy2(path_object, target_path)
            write_info_log_file(log_message)
        except BaseException:
            log_message = '---------- ' + key
            write_info_log_file(log_message)


current_date = get_current_date_time()
write_info_log_file(current_date)

configs_directory = "saved_configs"
create_directory(configs_directory)


for key, value in list_configs.items():
    backup_files(key, value)


log_file.close()
