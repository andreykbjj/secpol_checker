import codecs

regFile = codecs.open("reg_keys.reg", encoding="utf8")
reg = regFile.read()
regFile.close()
print(reg.replace('Windows Registry Editor Version 5.00', '').strip('\n'))
