from mappings import sid, local_policy, reg_keys
from termcolor import colored

sec_edit_file = 'this_pc.txt'


def get_line_number(phrase):
    with open(f'{sec_edit_file}', 'r', encoding='utf16') as f:
        for index, line in enumerate(f, 1):
            if phrase in line:
                return index


def privilege_rights_to_dict():
    try:
        raw_local_p_user_right_dict = dict()
        fine_user_right_dict = dict()

        start = get_line_number(phrase="[Privilege Rights]")
        end = get_line_number(phrase="[Version]") - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as user_rights:
            for line in user_rights.readlines()[start:end]:
                line = line.replace(' = *', ':').replace('*', '').replace(' = ', ':').strip('\n').split(':')

                configs = line[0]
                sids = line[1].split(',')
                contains = list()
                for s in sids:
                    if sid.get(s) is None:
                        contains.append(s)  # Translate SID's
                    else:
                        contains.append(sid.get(s))
                new_line_dict = {configs: contains}
                raw_local_p_user_right_dict.update(new_line_dict)

        for conf, value in raw_local_p_user_right_dict.items():
            latest = {local_policy['user_rights_assignment'].get(conf): value}
            fine_user_right_dict.update(latest)

        # for k, v in fine_local_p_user_right_dict.items():
        #     print(k, *v)
        print(colored(fine_user_right_dict, 'blue'))

        return fine_user_right_dict

    except IndexError as index_error:
        print(f'Error: {index_error}')


def security_options_registry_values_to_dict():  # Map Registry Values in reg_keys dict
    try:

        fine_security_options_dict = dict()

        start = get_line_number(phrase="[Registry Values]")
        end = get_line_number(phrase="[Privilege Rights]") - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as sec_options:
            for line in sec_options.readlines()[start:end]:
                line = line.strip('\n').replace('=', ':').split(':')
                configs = line[0]
                status = line[1].split(',')
                for k in local_policy['security_options'].keys():
                    if configs.__contains__(k):
                        index = configs.find(k)
                        if status[0] in reg_keys['Security Options'].keys():
                            status = [reg_keys['Security Options'].get(status[0]), reg_keys['Security Options'].get(status[1])]
                            mapped = {local_policy['security_options'].get(configs[index:]): status}
                            fine_security_options_dict.update(mapped)

        # for keys, values in fine_security_options_dict.items():
        #     print(keys, *values)
        print(colored(fine_security_options_dict, 'red'))

        return fine_security_options_dict

    except IndexError as index_error:
        print(f'Error: {index_error}')


def other_sec_options_policy_to_dict():
    try:

        raw_other_sec_options_dict = dict()

        start = get_line_number(phrase="LockoutDuration")
        end = get_line_number(phrase="[Event Audit]") - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as sys_access:
            for line in sys_access.readlines()[start:end]:
                line = line.strip('\n').replace(' = ', ':').split(':')
                if line[0] in local_policy['other_sec_options_configurations'].keys():
                    keys = local_policy['other_sec_options_configurations'].get(line[0])
                    vals = line[1]
                    new_dict = {keys: vals}
                    raw_other_sec_options_dict.update(new_dict)

        print(colored(raw_other_sec_options_dict, 'red'))

        return

    except IndexError as index_error:
        print(f'Error: {index_error}')


def password_policy_to_dict():
    try:

        raw_password_policy_dict = dict()

        start = get_line_number(phrase="[System Access]")
        end = get_line_number(phrase="LockoutBadCount") - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as sys_access:
            for line in sys_access.readlines()[start:end]:
                line = line.strip('\n').replace(' = ', ':').split(':')
                if line[0] in local_policy['password_policy'].keys():
                    keys = local_policy['password_policy'].get(line[0])
                    vals = line[1]
                    new_dict = {keys: int(vals)}
                    raw_password_policy_dict.update(new_dict)

        print(colored(raw_password_policy_dict, 'blue'))

        return

    except IndexError as index_error:
        print(f'Error: {index_error}')


def lockout_policy_to_dict():
    try:

        raw_lockout_policy_dict = dict()

        start = get_line_number(phrase="PasswordHistorySize")
        end = get_line_number(phrase="RequireLogonToChangePassword") - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as sys_access:
            for line in sys_access.readlines()[start:end]:
                line = line.strip('\n').replace(' = ', ':').split(':')
                if line[0] in local_policy['lockout_policy'].keys():
                    keys = local_policy['lockout_policy'].get(line[0])
                    vals = line[1]
                    new_dict = {keys: int(vals)}
                    raw_lockout_policy_dict.update(new_dict)

        print(colored(raw_lockout_policy_dict, 'blue'))

        return

    except IndexError as index_error:
        print(f'Error: {index_error}')


def event_audit():
    try:

        raw_local_p_user_right_dict = dict()

        start = get_line_number(phrase="[Event Audit]")
        end = get_line_number(phrase="[Registry Values]") - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as audit:
            for line in audit.readlines()[start:end]:
                line = line.strip('\n').replace(' = ', ':').split(':')
                if line[0] in local_policy['audit_dict'].keys():
                    keys = local_policy['audit_dict'].get(line[0])
                    vals = line[1]
                    new_dict = {keys: reg_keys['Audit'].get(int(vals))}
                    raw_local_p_user_right_dict.update(new_dict)
            print(colored(raw_local_p_user_right_dict, 'blue'))

            return

    except IndexError as index_error:
        print(f'Error: {index_error}')


password_policy_to_dict()
lockout_policy_to_dict()
event_audit()
privilege_rights_to_dict()
other_sec_options_policy_to_dict()
security_options_registry_values_to_dict()
