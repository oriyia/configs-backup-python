import os
import datetime

def get_current_date_time():
    separator = "-----------------------"
    current_date = datetime.datetime.now()
    current_date_short = current_date.strftime("%d/%m/%Y, %H:%M:%S")
    header_log = separator + current_date_short + separator
    return header_log


list_configs = {
    'zsh': '/home/oriyia/.zshrc',
}


def create_directory():
    os.mkdir('saved_configs')

# mkdir "${PWD}/saved_configs/" &> /dev/null
# target="${PWD}/saved_configs/"
#
# copying_files()
# {
#     for key in "${!list_directories[@]}"
#     do
#         if [[ -d ${list_directories[$key]} ]]
#         then
#             if cp -aT "${list_directories[$key]}" "${target}${key}"
#             then
#                 echo "+++++ ${key}" >> results.txt
#             else
#                 echo "----- ${key}" >> results.txt
#             fi
#         else
#             mkdir "${target}${key}/" &> /dev/null
#             if cp -a "${list_directories[$key]}" "${target}${key}/"
#             then
#                 echo "+++++++ ${key}" >> results.txt
#             else
#                 echo "---------- ${key}" >> results.txt
#             fi
#         fi
#     done
# }
#
# copying_files
# echo -e "\n${itog}" >> results.txt


