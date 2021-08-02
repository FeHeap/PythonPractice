# -*- coding = utf-8 -*-
# @Time: 2021/8/2 下午 01:00
# @Software: PyCharm

import detectEnglish, vigenereCipher, pyperclip


def main():
    ciphertext = 'Tzx isnz eccjxkg nfq lol mys bbqq I lxcz.'
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackVigenereDictionary(ciphertext):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip()
        decryptedtext = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedtext, wordPercentage=40):
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ': ' + decryptedtext[:100])
            print()
            print('Enter D for done, or just press Enter to continue breaking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedtext

if __name__ == '__main__':
    main()