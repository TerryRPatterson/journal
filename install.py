#! /usr/bin/env python3

from os import symlink, mkdir, path, EX_NOPERM, environ
from platform import system
from sys import argv, exit
from shutil import copyfile

PROGRAM_PATH = path.dirname(path.realpath(argv[0]))


def get_user_confirmation(message):
    vaild_postive = ["y", "yes"]
    vaild_negative = ["n", "no"]
    vaild_input_recived = False
    while(not vaild_input_recived):
        user_response = input(message)
        user_response_folded = user_response.casefold()
        if user_response_folded in vaild_postive:
            vaild_input_recived = True
            return True
        elif user_response_folded in vaild_negative:
            vaild_input_recived = True
            return False
        else:
            message += f"\n{user_response} is not vaild please enter  Y or N: "


permission_request = (f"This will install journal to {PROGRAM_PATH} and place"
                      "symbolic links to the exectuable in the user path."
                      "Continue? (Y/N)")

user_permission = get_user_confirmation(permission_request)

if (user_permission is True):
    quest_log_location = f"{PROGRAM_PATH}/save/questLog"
    mkdir(f"{PROGRAM_PATH}/save")
    copyfile(f"{PROGRAM_PATH}/questLogExample", quest_log_location)
    os = system()
    if os != "Windows":
        home = environ["HOME"]
        symlink(f"{PROGRAM_PATH}/journal", f"{home}/bin/journal")
else:
    exit(EX_NOPERM)
