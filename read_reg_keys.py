import codecs

with codecs.open("reg_keys.reg", encoding="utf8") as regFile:
    reg = regFile.read()
    print(reg.replace('Windows Registry Editor Version 5.00', '').strip('\n'))
