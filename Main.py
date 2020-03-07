from termcolor import colored
from Mappings import sid, local_policy, reg_keys

sec_edit_file = 'secedit.txt'
advanced_audit_policy_file = 'advanced_audit.txt'


def get_line_number(phrase, file):
    with open(f'{file}', 'r', encoding='utf16') as f:
        for index, line in enumerate(f, 1):
            if phrase in line:
                return int(index)


def privilege_rights_to_dict():
    try:
        raw_local_p_user_right_dict = dict()
        fine_user_right_dict = dict()

        start = get_line_number(phrase="[Privilege Rights]", file='secedit.txt')
        end = get_line_number(phrase="[Version]", file='secedit.txt') - 1

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
        # print(colored(fine_user_right_dict, 'blue'))

        return fine_user_right_dict

    except IndexError as index_error:
        print(f'Error: {index_error}')


def security_options_registry_values_to_dict():  # Map Registry Values in reg_keys dict
    try:

        fine_security_options_dict = dict()

        start = get_line_number(phrase="[Registry Values]", file='secedit.txt')
        end = get_line_number(phrase="[Privilege Rights]", file='secedit.txt') - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as sec_options:
            for line in sec_options.readlines()[start:end]:
                line = line.strip('\n').replace('=', ':').split(':')
                configs = line[0]
                status = line[1].split(',')
                stats = status[1]
                for k in local_policy['security_options'].keys():
                    if configs.__contains__(k):
                        index = configs.find(k)
                        if stats in reg_keys['Security Options'].keys():
                            status = [reg_keys['Security Options'].get(stats)]
                            mapped = {local_policy['security_options'].get(configs[index:]): status}
                            fine_security_options_dict.update(mapped)
                        elif stats not in reg_keys['Security Options'].keys():
                            mapped = {local_policy['security_options'].get(configs[index:]): status[1:]}
                            fine_security_options_dict.update(mapped)

        fine_security_options_dict.update(other_sec_options_policy_to_dict())

        # for keys, values in fine_security_options_dict.items():
        #     print(keys, '\t', *values)
        # print(colored(fine_security_options_dict, 'red'))

        return fine_security_options_dict

    except IndexError as index_error:
        print(f'Error: {index_error}')


def other_sec_options_policy_to_dict():
    try:

        raw_other_sec_options_dict = dict()

        start = get_line_number(phrase="LockoutDuration", file='secedit.txt')
        end = get_line_number(phrase="[Event Audit]", file='secedit.txt') - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as sys_access:
            for line in sys_access.readlines()[start:end]:
                line = line.strip('\n').replace(' = ', ':').split(':')
                if line[0] in local_policy['other_sec_options_configurations'].keys():
                    keys = local_policy['other_sec_options_configurations'].get(line[0])
                    vals = line[1]
                    if reg_keys['Security Options'].get(vals) is None:
                        new_dict = {keys: vals}
                        raw_other_sec_options_dict.update(new_dict)
                    elif reg_keys['Security Options'].get(vals) is not None:
                        new_dict = {keys: reg_keys['Security Options'].get(vals)}
                        raw_other_sec_options_dict.update(new_dict)

        # print(colored(raw_other_sec_options_dict, 'blue'))

        return raw_other_sec_options_dict

    except IndexError as index_error:
        print(f'Error: {index_error}')


def password_policy_to_dict():
    try:

        raw_password_policy_dict = dict()

        start = get_line_number(phrase="[System Access]", file='secedit.txt')
        end = get_line_number(phrase="LockoutBadCount", file='secedit.txt') - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as sys_access:
            for line in sys_access.readlines()[start:end]:
                line = line.strip('\n').replace(' = ', ':').split(':')
                if line[0] in local_policy['password_policy'].keys():
                    keys = local_policy['password_policy'].get(line[0])
                    vals = line[1]
                    new_dict = {keys: int(vals)}
                    raw_password_policy_dict.update(new_dict)

        # print(colored(raw_password_policy_dict, 'blue'))

        return raw_password_policy_dict

    except IndexError as index_error:
        print(f'Error: {index_error}')


def lockout_policy_to_dict():
    try:

        raw_lockout_policy_dict = dict()

        start = get_line_number(phrase="PasswordHistorySize", file='secedit.txt')
        end = get_line_number(phrase="RequireLogonToChangePassword", file='secedit.txt') - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as sys_access:
            for line in sys_access.readlines()[start:end]:
                line = line.strip('\n').replace(' = ', ':').split(':')
                if line[0] in local_policy['lockout_policy'].keys():
                    keys = local_policy['lockout_policy'].get(line[0])
                    vals = line[1]
                    new_dict = {keys: int(vals)}
                    raw_lockout_policy_dict.update(new_dict)

        # print(colored(raw_lockout_policy_dict, 'blue'))

        return raw_lockout_policy_dict

    except IndexError as index_error:
        print(f'Error: {index_error}')


def event_audit():
    try:

        raw_event_audit_dict = dict()

        start = get_line_number(phrase="[Event Audit]", file='secedit.txt')
        end = get_line_number(phrase="[Registry Values]", file='secedit.txt') - 1

        with open(f'{sec_edit_file}', 'r', encoding='utf16') as audit:
            for line in audit.readlines()[start:end]:
                line = line.strip('\n').replace(' = ', ':').split(':')
                if line[0] in local_policy['audit_dict'].keys():
                    keys = local_policy['audit_dict'].get(line[0])
                    vals = line[1]
                    new_dict = {keys: reg_keys['Audit'].get(int(vals))}
                    raw_event_audit_dict.update(new_dict)

            raw_event_audit_dict.update(advanced_audit())
            # print(colored(raw_event_audit_dict, 'blue'))

            return raw_event_audit_dict

    except IndexError as index_error:
        print(f'Error: {index_error}')


def advanced_audit():       # Need to extract config & value to dictionary return

    system_start = get_line_number(phrase="Category/Subcategory", file='advanced_audit.txt') + 1
    system_end = get_line_number(phrase="Logon/Logoff", file='advanced_audit.txt') - 1

    logon_logoff_start = get_line_number(phrase="Logon/Logoff", file='advanced_audit.txt')
    logon_logoff_end = get_line_number(phrase="Object Access", file='advanced_audit.txt') - 1

    object_access_start = get_line_number(phrase="Object Access", file='advanced_audit.txt')
    object_access_end = get_line_number(phrase="Privilege Use", file='advanced_audit.txt') - 1

    privilege_use_start = get_line_number(phrase="Privilege Use", file='advanced_audit.txt')
    privilege_use_end = get_line_number(phrase="Detailed Tracking", file='advanced_audit.txt') - 1

    detailed_tracking_start = get_line_number(phrase="Detailed Tracking", file='advanced_audit.txt')
    detailed_tracking_end = get_line_number(phrase="Policy Change", file='advanced_audit.txt') - 1

    policy_change_start = get_line_number(phrase="Policy Change", file='advanced_audit.txt')
    policy_change_end = get_line_number(phrase="Account Management", file='advanced_audit.txt') - 1

    account_management_start = get_line_number(phrase="Account Management", file='advanced_audit.txt')
    account_management_end = get_line_number(phrase="DS Access", file='advanced_audit.txt') - 1

    ds_access_start = get_line_number(phrase="DS Access", file='advanced_audit.txt')
    ds_access_end = get_line_number(phrase="Account Logon", file='advanced_audit.txt') - 1

    account_logon_start = get_line_number(phrase="Account Logon", file='advanced_audit.txt')

    with open(f'{advanced_audit_policy_file}', 'r', encoding='utf16') as advanced:
        for line in advanced.readlines()[system_start:system_end]:
            line = line.strip('\n').strip('').split('  ')
            line = list(filter(None, line))
            lines = dict()
            if len(line) != 0:
                keys_values = {line[0]: line[1].strip(" ").replace('Auditing', 'auditing')}
                lines.update(keys_values)
                # print(lines)

                return lines
