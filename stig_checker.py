from termcolor import colored
import stig

cats = stig.win_server_2012.get('stig')['findings']

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

main_dict = dict()
new_listing = list()

for k, v in cats.items():
    if v.get('checktext').strip('\n').__contains__(':'):
        testing = list()
        splitted = list()
        # print(colored("*" * 100, 'yellow'))

        testing.append(v.get('checktext').strip('\n'))

        for item in testing:
            # print(item.split('\n'))
            for i in item.split('\n'):
                if i.__contains__('Registry Path'):
                    keys = 'Get-ItemProperty -Path "HKLM:' + i.split(': ')[1].lstrip(' ') + '"'
                    new_listing.append(keys)
                    # print(keys)
                elif i.__contains__('Value Name'):
                    values = i.split(': ')[1]
                    values = ' | fl ' + values + '\n'
                    new_listing.append(values)
                    # print(values)
new_list = (list(filter(None, new_listing)))
print(''.join(new_list).strip('\n'))

