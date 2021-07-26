# -*- coding = utf-8 -*-
# @Time: 2021/7/26 下午 09:09
# @Software: PyCharm

import pyperclip, detectEnglish, transpositionDecrypt

def main():
    cipherTextFile = open('alice.encrypted.txt')
    myMessage = cipherTextFile.read()
    cipherTextFile.close()

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)


def hackTransposition(message):
    print("Hacking...")

    print('(Press Ctrl + C (on Windows) or Ctrl + D (on macOS or Linux) to quit at any time.)')

    for key in range(1, len(message)):
        print('Trying key #%s...'%(key))

        decryptedText = transpositionDecrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            print()
            print('Possible encryption hack:')
            print('Key %s:\n%s'%(key, decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None


if __name__ == '__main__':
    main()