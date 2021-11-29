from datetime import datetime

from os import path


def indexOf(str: str, serch):
    try:
        return str.index(serch)
    except:
        return -1


def get_account_from_file(accont_path):
    file = open(accont_path)
    file = file.readline()
    splited = file.split(":")
    cokei = splited[2].split(";")
    return (splited[0], splited[1], cokei)


def set_done_accout(done_account_path, account):
    file = open(done_account_path, "r+")
    lines = file.readlines()
    file.seek(0)
    file.truncate()
    file.writelines(lines)
    file.writelines(account)


def checked_account(check_acconts_path, account):
    file = open(check_acconts_path, "r+")
    lines = file.readlines()
    file.seek(0)
    file.truncate()
    file.writelines(lines)
    file.writelines(account)


def set_fill_account(fill_accounts_path, account):
    file = open(fill_accounts_path, "r+")
    lines = file.readlines()
    file.seek(0)
    file.truncate()
    file.writelines(lines)
    file.writelines(account)


def remove_account(accont_path):
    file = open(accont_path, "r+")
    lines = file.readlines()
    file.seek(0)
    file.truncate()
    file.writelines(lines[1:])


def create_files(folder_path):
    today = str(datetime.date(datetime.now())).replace('-', '_')
    files_name = [
        'done_' + today,
        'check_' + today,
        'fill_' + today,
        'unknow_' + today
    ]
    new_files = []
    for file in files_name:
        if not path.exists("{}/{}.txt".format(folder_path, file)):
            f = open("{}/{}.txt".format(folder_path, file), 'w+')
        new_files.append("{}/{}.txt".format(folder_path, file))
    return new_files


def get_files_inf(files: list):
    files_info = []
    for file in files:
        if path.exists(file):
            files_info.append(len(open(file, 'r').readlines()))
        else:
            files_info.append(0)
    return files_info
