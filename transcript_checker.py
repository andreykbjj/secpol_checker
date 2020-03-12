from reg_value_names import reg_values


def check_duplicates(_list: list):
    duplicates = []
    for item in _list:
        if _list.count(item) > 1:
            duplicates.append(item)
    print(duplicates)

new_list = list()
with open('transcript.txt', 'r', encoding='utf8') as transcript:
    for line in transcript.readlines():
        new_list.append(list(filter(None, line.strip('\n').replace(' ', '').split(':'))))


super_new = list(filter(None, new_list))
new_dict = dict()

for i in super_new:
    if len(i) > 1:
        # print(i)
        keys = i[0]
        values = i[1]
        test = {keys: values}
        new_dict.update(test)

for k, v in new_dict.items():
    for reg in reg_values:
        if k == reg:
            print(k, v)
