from termcolor import colored

import stig

cats = stig.win_server_2012_r2.get('stig')['findings']


def read_pulled_txt(file_name: str):
    only_configs = list()
    pulled_configs_dict = dict()
    with open(file_name, 'r') as pulled:
        for line in pulled.readlines():
            only_configs.append(line.strip('\n').split(' : '))
    # print(only_configs)
    for item in only_configs:
        if item != ['']:
            if len(item) > 1:
                key = item[0].lower()
                value = item[1]
                config_dict = {key: value}
                pulled_configs_dict.update(config_dict)

    # print(pulled_configs_dict)
    return pulled_configs_dict


def combine_checks():
    new_listing = list()
    total_dict = dict()
    for k, v in cats.items():

        if v.get('checktext').strip('\n').__contains__(':'):
            raw_list = list()
            raw_list.append(v.get('checktext').strip('\n'))

            for item in raw_list:
                for i in item.split('\n'):
                    if i.__contains__('Value Name'):
                        values = i.split(': ')[1]
                        values = values.lstrip(' ').lower()
                        new_listing.append(values)
                        combo = {values: v.get('title').strip('.')}
                        total_dict.update(combo)

    return total_dict


combine_checks()
text = read_pulled_txt(file_name='pulled.txt')

values = {'0': 'Disabled', '1': 'Enabled'}

# Test Loop

for k in combine_checks().keys():
    if k in text.keys():
        if values.get(text.get(k)) is None:
            print(combine_checks().get(k), text.get(k))
            print(colored("*" * len(combine_checks().get(k)), 'yellow'))
        else:
            print(combine_checks().get(k), '-', colored(values.get(text.get(k)), 'red'))
            print(colored("*" * len(combine_checks().get(k)), 'yellow'))
