from termcolor import colored
import stig

cats = stig.win_server_2012_r2.get('stig')['findings']

insides = [
    "checkid"
    "checktext"
    "description"
    "fixid"
    "fixtext"
    "iacontrols"
    "id"
    "ruleID"
    "severity"
    "title"
    "version"
]


def get_item_property():
    new_listing = list()
    for k, v in cats.items():

        if v.get('checktext').strip('\n').__contains__(':'):
            raw_list = list()
            # print(colored("*" * 100, 'yellow'))
            raw_list.append(v.get('checktext').strip('\n'))

            for item in raw_list:
                for i in item.split('\n'):
                    if i.__contains__('Registry Path'):
                        keys = 'Get-ItemProperty -Path "HKLM:' + i.split(': ')[1].lstrip(' ') + '"'
                        new_listing.append(keys)
                    elif i.__contains__('Value Name'):
                        values = i.split(': ')[1]
                        values = ' | fl ' + values + '\n'
                        new_listing.append(values)

    new_list = (list(filter(None, new_listing)))

    # print(''.join(new_list).strip('\n'))
    return ''.join(new_list).strip('\n')


def read_pulled_txt(file_name: str):
    only_configs = list()
    pulled_configs_dict = dict()
    with open(file_name, 'r') as pulled:
        for line in pulled.readlines():
            only_configs.append(line.strip('\n').split(' : '))
    for item in only_configs:
        if item != ['']:
            if len(item) > 1:
                key = item[0].lower()
                value = item[1]
                config_dict = {key: value}
                pulled_configs_dict.update(config_dict)

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

translate = {'0': 'Disabled', '1': 'Enabled'}

# Test Loop
for k in combine_checks().keys():
    if k in text.keys():
        # print(combine_checks().get(k), values.get(text.get(k)))
        print(combine_checks().get(k), translate.get(text.get(k)))
        print(colored("*" * len(combine_checks().get(k)), 'yellow'))
