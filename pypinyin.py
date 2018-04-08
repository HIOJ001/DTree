# coding=utf-8
import pypinyin
import codecs
from hanziconv import HanziConv


def translate_to_pinyi():
    cn_name = codecs.open("cn_user.txt", "r", "gbk")
    en_name = codecs.open("en_user.txt", "w", "gbk")
    names = cn_name.readlines()
    for i in range(len(names)):
        names[i] = names[i].strip()
        # print(HanziConv.toTraditional(names[i]))
        # print(HanziConv.toSimplified(names[i]))
        save_name = ''.join(pypinyin.lazy_pinyin(names[i]))
        if i == len(names) - 1:
            en_name.write(save_name)
            break
        en_name.write(save_name + "\r\n")
    cn_name.close()
    en_name.close()


def generate_mail():
    en_name = codecs.open("en_user.txt", "r", "gbk")
    mail_suffix = codecs.open("mail_suffix.txt", "r", "gbk")
    mail = codecs.open("mail.txt", "w", "gbk")
    users = en_name.readlines()
    suffix = mail_suffix.readlines()
    for i in range(len(users)):
        users[i] = users[i].strip()
        for j in range(len(suffix)):
            suffix[j] = suffix[j].strip()
            if i == len(users) - 1 and j == len(suffix) - 1:
                mail.write(users[i] + suffix[j])
                break
            mail.write(users[i] + suffix[j] + '\r\n')
    en_name.close()
    mail_suffix.close()
    mail.close()


while True:
    choice = raw_input("choice is: ")
    if choice == '0':
        break
    if choice == '1':
        translate_to_pinyi()
        print("translate to pinyi complete")
    if choice == '2':
        generate_mail()
        print("generate mail complete")
