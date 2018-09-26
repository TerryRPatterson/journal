#! /usr/bin/env python3

import zipfile
from glob import glob
from os import chdir, remove, EX_IOERR
from sys import exit


OUTPUT_FILE = "QuestLog.zip"


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


def create_new_archive():
    with zipfile.ZipFile(OUTPUT_FILE, mode="x") as builtArchive:
        chdir("dist")
        for file in glob("**", recursive=True):
            builtArchive.write(file)


try:
    create_new_archive()
except FileExistsError:
    user_response = get_user_confirmation("The distribution zip archive "
                                          "already exists would you like to "
                                          "overwrite it?(Y/N)\n")
    if user_response is True:
        remove(OUTPUT_FILE)
        create_new_archive()
    else:
        print("File not removed")
        exit(EX_IOERR)
