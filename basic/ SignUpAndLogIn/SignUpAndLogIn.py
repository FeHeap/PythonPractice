# -*- coding = utf-8 -*-
# @Time: 2021/7/11 下午 09:27
# @Software: PyCharm

import re

findname = re.compile(r'(.+)(?=:)')

findpassword = re.compile(r'(?<=:)(.+)')

namerule = re.compile(r'[^_0-9a-zA-Z]+')

passwordrule = re.compile(r'[^0-9a-zA-Z]+')


def main():
    print('*' * 20)
    print("操作編碼     操作")
    print("[0]         註冊")
    print("[1]         登錄")
    print('*' * 20)
    instruction = input("請輸入你要進行的操作編碼：")
    if instruction == "0":
        signup()
    elif instruction == "1":
        login()
    else:
        print("error!")

def signup():
    print("\n"*10)
    print("-"*10 + "註冊" + "-"*10)
    fptr = open("user.txt", "r")
    users = fptr.read().splitlines();
    fptr.close()
    if(len(users) == 0):
        userData = ""
    else:
        userData = "\n"
    for index,user in enumerate(users):
        users[index] = findname.search(user)[0].strip()

    name = input("請輸入用戶名(只能包含字母,數字,_)：").strip()
    if name in users or namerule.search(name) is not None or len(name) == 0:
        while True:
            if len(name) == 0:
                print("未輸入用戶名")
            elif namerule.search(name) is not None:
                print("用戶名不符合規則")
            elif name in users:
                print("用戶名已存在")
            name = input("請重新輸入用戶名(只能包含字母,數字,_)：")
            if name not in users and namerule.search(name) is None and len(name) != 0:
                break
    userData += (name + ":")

    password = input("請輸入密碼(只能包含字母,數字,且長度不能超過8)：")
    if passwordrule.search(password) is not None or len(password) > 8 or len(password) == 0:
        while True:
            if len(password) == 0:
                print("未輸入密碼")
            elif passwordrule.search(password) is not None:
                print("密碼不符合規則")
            elif len(password) > 8:
                print("密碼長度不能超過8")
            password = input("請重新輸入密碼(只能包含字母,數字,且長度不能超過8)：")
            if passwordrule.search(password) is None and len(password) <= 8 and len(password) != 0:
                break
    while True:
        passwordAgain = input("請再次輸入密碼：")
        if passwordAgain != password:
            print("密碼不一致")
        else:
            break
    userData += password

    fptr = open("user.txt", "a")
    fptr.write(userData)
    fptr.close()


def login():
    print("\n" * 10)
    print("-"*10 + "登錄" + "-"*10)

    fptr = open("user.txt", "r")
    users = fptr.read().splitlines();
    fptr.close()
    fptr = open("blacklist.txt", "r")
    blacklist = fptr.read().splitlines();
    fptr.close()

    names = users.copy()
    passwords = users.copy()
    for index,name in enumerate(names):
        names[index] = findname.search(name)[0].strip()
    for index,password in enumerate(passwords):
        passwords[index] = findpassword.search(password)[0].strip()

    while True:
        name = input("請輸入用戶名：")
        if name not in names:
            print("此用戶不存在")
        elif name in blacklist:
            print("此用戶已被鎖")
        else:
            break
    password = passwords[names.index(name)]

    inputPassword = input("請輸入密碼：")
    if inputPassword == password:
        print("登錄成功")
    else:
        print("密碼不正確")
        inputPassword = input("請再次輸入密碼：")
        if (inputPassword == password):
            print("登錄成功")
        else:
            print("密碼不正確")
            print("您還有1次機會")
            inputPassword = input("請再次輸入密碼：")
            if inputPassword == password:
                print("登錄成功")
            else:
                print("密碼3次錯誤，禁止登錄，請聯繫管理員。")
                fptr = open("blacklist.txt", "a")
                if len(blacklist) != 0:
                    name = "\n" + name
                fptr.write(name)
                fptr.close()


if __name__ == "__main__":
    main()