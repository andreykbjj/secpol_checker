from termcolor import colored
from Mappings import local_policy, reg_keys
from Variables import *
import Variables


def checker():
    lines = '-' * 100

    print(colored(f'{lines}', 'yellow'))
    print(colored('Password Policy', 'yellow'))
    print(colored(f'{lines}', 'yellow'))

    if pass_history < 10:
        print(colored(f'{local_policy.get("password_policy")["PasswordHistorySize"]}: {pass_history}', 'red'))
    else:
        print(colored(f'{local_policy.get("password_policy")["PasswordHistorySize"]}: {pass_history}', 'blue'))

    if pass_min < 1:
        print(colored(f'{local_policy.get("password_policy")["MinimumPasswordAge"]}: {pass_min}', 'red'))
    else:
        print(colored(f'{local_policy.get("password_policy")["MinimumPasswordAge"]}: {pass_min}', 'blue'))

    if pass_max == 0 or pass_max > 90:
        print(colored(f'{local_policy.get("password_policy")["MaximumPasswordAge"]}: {pass_max}', 'red'))

    else:
        print(colored(f'{local_policy.get("password_policy")["MaximumPasswordAge"]}: {pass_max}', 'blue'))

    if pass_complex != 1:
        print(colored(f'{local_policy.get("password_policy")["PasswordComplexity"]}: {pass_complex}', 'red'))
    else:
        print(colored(f'{local_policy.get("password_policy")["PasswordComplexity"]}: {pass_complex}', 'blue'))

    if pass_len < 8:
        print(colored(f'{local_policy.get("password_policy")["MinimumPasswordLength"]}: {pass_len}', 'red'))
    else:
        print(colored(f'{local_policy.get("password_policy")["MinimumPasswordLength"]}: {pass_len}', 'blue'))

    print(colored(f'{lines}', 'yellow'))
    print(colored('Account Lockout Policy', 'yellow'))
    print(colored(f'{lines}', 'yellow'))

    if lockout_threshold != 0 and lockout_threshold > 0:
        print(colored(f'{local_policy.get("lockout_policy")["LockoutBadCount"]}: {lockout_threshold}', 'blue'))

        if lockout_duration is not None:
            if lockout_duration < 5:
                print(colored(f'{local_policy.get("lockout_policy")["LockoutDuration"]}: {lockout_duration}', 'red'))
            else:
                print(colored(f'{local_policy.get("lockout_policy")["LockoutDuration"]}: {lockout_duration}', 'blue'))
        else:
            pass

        if reset_lockout_counter_after is not None:
            if reset_lockout_counter_after > 15:
                print(
                    colored(f'{local_policy.get("lockout_policy")["ResetLockoutCount"]}: {reset_lockout_counter_after}',
                            'red'))
            else:
                print(
                    colored(f'{local_policy.get("lockout_policy")["ResetLockoutCount"]}: {reset_lockout_counter_after}',
                            'blue'))
        else:
            pass
    else:
        print(colored(f'{local_policy.get("lockout_policy")["LockoutBadCount"]}: {lockout_threshold}', 'red'))
        print(colored(f'{local_policy.get("lockout_policy")["LockoutDuration"]}: {not_defined}', 'red'))
        print(colored(f'{local_policy.get("lockout_policy")["ResetLockoutCount"]}: {not_defined}', 'red'))

    print(colored(f'{lines}', 'yellow'))
    print(colored('Audit Policy', 'yellow'))
    print(colored(f'{lines}', 'yellow'))

    if account_logon == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountLogon"]}: {account_logon}', 'red'))
    elif account_logon == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountLogon"]}: {account_logon}', 'magenta'))
    elif account_logon == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountLogon"]}: {account_logon}', 'magenta'))
    elif account_logon == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountLogon"]}: {account_logon}', 'blue'))
    else:
        print('Something happened')
        pass

    if account_manage == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountManage"]}: {account_manage}', 'red'))
    elif account_manage == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountManage"]}: {account_manage}', 'magenta'))
    elif account_manage == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountManage"]}: {account_manage}', 'magenta'))
    elif account_manage == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountManage"]}: {account_manage}', 'blue'))
    else:
        print('Something happened')
        pass

    if ds_access == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("audit_dict")["AuditDSAccess"]}: {ds_access}', 'red'))
    elif ds_access == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("audit_dict")["AuditDSAccess"]}: {ds_access}', 'magenta'))
    elif ds_access == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("audit_dict")["AuditDSAccess"]}: {ds_access}', 'magenta'))
    elif ds_access == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("audit_dict")["AuditDSAccess"]}: {ds_access}', 'blue'))
    else:
        print('Something happened')
        pass

    if logon_events == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("audit_dict")["AuditLogonEvents"]}: {logon_events}', 'red'))
    elif logon_events == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("audit_dict")["AuditLogonEvents"]}: {logon_events}', 'magenta'))
    elif logon_events == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("audit_dict")["AuditLogonEvents"]}: {logon_events}', 'magenta'))
    elif logon_events == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("audit_dict")["AuditLogonEvents"]}: {logon_events}', 'blue'))
    else:
        print('Something happened')
        pass

    if object_access == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("audit_dict")["AuditObjectAccess"]}: {object_access}', 'red'))
    elif object_access == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("audit_dict")["AuditObjectAccess"]}: {object_access}', 'magenta'))
    elif object_access == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("audit_dict")["AuditObjectAccess"]}: {object_access}', 'magenta'))
    elif object_access == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("audit_dict")["AuditObjectAccess"]}: {object_access}', 'blue'))
    else:
        print('Something happened')
        pass

    if policy_change == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("audit_dict")["AuditPolicyChange"]}: {policy_change}', 'red'))
    elif policy_change == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("audit_dict")["AuditPolicyChange"]}: {policy_change}', 'magenta'))
    elif policy_change == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("audit_dict")["AuditPolicyChange"]}: {policy_change}', 'magenta'))
    elif policy_change == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("audit_dict")["AuditPolicyChange"]}: {policy_change}', 'blue'))
    else:
        print('Something happened')
        pass

    if privilege_use == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("audit_dict")["AuditPrivilegeUse"]}: {privilege_use}', 'red'))
    elif privilege_use == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("audit_dict")["AuditPrivilegeUse"]}: {privilege_use}', 'magenta'))
    elif privilege_use == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("audit_dict")["AuditPrivilegeUse"]}: {privilege_use}', 'magenta'))
    elif privilege_use == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("audit_dict")["AuditPrivilegeUse"]}: {privilege_use}', 'blue'))
    else:
        print('Something happened')
        pass

    if process_tracking == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("audit_dict")["AuditProcessTracking"]}: {process_tracking}', 'red'))
    elif process_tracking == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("audit_dict")["AuditProcessTracking"]}: {process_tracking}', 'magenta'))
    elif process_tracking == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("audit_dict")["AuditProcessTracking"]}: {process_tracking}', 'magenta'))
    elif process_tracking == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("audit_dict")["AuditProcessTracking"]}: {process_tracking}', 'blue'))
    else:
        print('Something happened')
        pass

    if system_events == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("audit_dict")["AuditSystemEvents"]}: {system_events}', 'red'))
    elif system_events == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("audit_dict")["AuditSystemEvents"]}: {system_events}', 'magenta'))
    elif system_events == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("audit_dict")["AuditSystemEvents"]}: {system_events}', 'magenta'))
    elif system_events == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("audit_dict")["AuditSystemEvents"]}: {system_events}', 'blue'))
    else:
        print('Something happened')
        pass

    # Check Advanced Audit Policy ==>
    # Auditpol /get /category:* | Out-File -FilePath 'C:\adv_audit.txt'

    print(colored(f'{lines}', 'yellow'))
    print(colored('Advanced Audit Policy', 'yellow'))
    print(colored(f'{lines}', 'yellow'))

    print(colored('System', 'yellow'))
    if adv_sys_audit_sec_sys_extension == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][0]}: {adv_sys_audit_sec_sys_extension}', 'red'))
    elif adv_sys_audit_sec_sys_extension == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][0]}: {adv_sys_audit_sec_sys_extension}', 'magenta'))
    elif adv_sys_audit_sec_sys_extension == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][0]}: {adv_sys_audit_sec_sys_extension}', 'magenta'))
    elif adv_sys_audit_sec_sys_extension == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][0]}: {adv_sys_audit_sec_sys_extension}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_sys_audit_sys_integrity == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][1]}: {adv_sys_audit_sys_integrity}', 'red'))
    elif adv_sys_audit_sys_integrity == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][1]}: {adv_sys_audit_sys_integrity}', 'magenta'))
    elif adv_sys_audit_sys_integrity == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][1]}: {adv_sys_audit_sys_integrity}', 'magenta'))
    elif adv_sys_audit_sys_integrity == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][1]}: {adv_sys_audit_sys_integrity}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_sys_audit_ipsec_driver == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][2]}: {adv_sys_audit_ipsec_driver}', 'red'))
    elif adv_sys_audit_ipsec_driver == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][2]}: {adv_sys_audit_ipsec_driver}', 'magenta'))
    elif adv_sys_audit_ipsec_driver == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][2]}: {adv_sys_audit_ipsec_driver}', 'magenta'))
    elif adv_sys_audit_ipsec_driver == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][2]}: {adv_sys_audit_ipsec_driver}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_sys_audit_other_sys_events == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][3]}: {adv_sys_audit_other_sys_events}', 'red'))
    elif adv_sys_audit_other_sys_events == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][3]}: {adv_sys_audit_other_sys_events}', 'magenta'))
    elif adv_sys_audit_other_sys_events == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][3]}: {adv_sys_audit_other_sys_events}', 'magenta'))
    elif adv_sys_audit_other_sys_events == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][3]}: {adv_sys_audit_other_sys_events}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_sys_audit_sec_state_change == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][4]}: {adv_sys_audit_sec_state_change}', 'red'))
    elif adv_sys_audit_sec_state_change == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][4]}: {adv_sys_audit_sec_state_change}', 'magenta'))
    elif adv_sys_audit_sec_state_change == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][4]}: {adv_sys_audit_sec_state_change}', 'magenta'))
    elif adv_sys_audit_sec_state_change == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["System"][4]}: {adv_sys_audit_sec_state_change}', 'blue'))
    else:
        print('Something happened')
        pass

    print(colored('\nLogon/Logoff', 'yellow'))
    if adv_logon_off_audit_logon == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][0]}: {adv_logon_off_audit_logon}', 'red'))
    elif adv_logon_off_audit_logon == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][0]}: {adv_logon_off_audit_logon}', 'magenta'))
    elif adv_logon_off_audit_logon == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][0]}: {adv_logon_off_audit_logon}', 'magenta'))
    elif adv_logon_off_audit_logon == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][0]}: {adv_logon_off_audit_logon}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_logon_off_audit_logoff == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][1]}: {adv_logon_off_audit_logoff}', 'red'))
    elif adv_logon_off_audit_logoff == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][1]}: {adv_logon_off_audit_logoff}', 'magenta'))
    elif adv_logon_off_audit_logoff == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][1]}: {adv_logon_off_audit_logoff}', 'magenta'))
    elif adv_logon_off_audit_logoff == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][1]}: {adv_logon_off_audit_logoff}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_logon_off_audit_logoff == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][2]}: {adv_logon_off_audit_logoff}', 'red'))
    elif adv_logon_off_audit_logoff == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][2]}: {adv_logon_off_audit_logoff}', 'magenta'))
    elif adv_logon_off_audit_logoff == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][2]}: {adv_logon_off_audit_logoff}', 'magenta'))
    elif adv_logon_off_audit_logoff == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][2]}: {adv_logon_off_audit_logoff}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_logon_off_audit_acc_lockout == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][3]}: {adv_logon_off_audit_acc_lockout}', 'red'))
    elif adv_logon_off_audit_acc_lockout == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][3]}: {adv_logon_off_audit_acc_lockout}', 'magenta'))
    elif adv_logon_off_audit_acc_lockout == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][3]}: {adv_logon_off_audit_acc_lockout}', 'magenta'))
    elif adv_logon_off_audit_acc_lockout == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][3]}: {adv_logon_off_audit_acc_lockout}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_logon_off_audit_ipsec_main_mode == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][4]}: {adv_logon_off_audit_ipsec_main_mode}', 'red'))
    elif adv_logon_off_audit_ipsec_main_mode == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][4]}: {adv_logon_off_audit_ipsec_main_mode}', 'magenta'))
    elif adv_logon_off_audit_ipsec_main_mode == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][4]}: {adv_logon_off_audit_ipsec_main_mode}', 'magenta'))
    elif adv_logon_off_audit_ipsec_main_mode == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][4]}: {adv_logon_off_audit_ipsec_main_mode}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_logon_off_audit_ipsec_quick_mode == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][5]}: {adv_logon_off_audit_ipsec_quick_mode}', 'red'))
    elif adv_logon_off_audit_ipsec_quick_mode == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][5]}: {adv_logon_off_audit_ipsec_quick_mode}', 'magenta'))
    elif adv_logon_off_audit_ipsec_quick_mode == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][5]}: {adv_logon_off_audit_ipsec_quick_mode}', 'magenta'))
    elif adv_logon_off_audit_ipsec_quick_mode == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][5]}: {adv_logon_off_audit_ipsec_quick_mode}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_logon_off_audit_ipsec_extended_mode == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][6]}: {adv_logon_off_audit_ipsec_extended_mode}', 'red'))
    elif adv_logon_off_audit_ipsec_extended_mode == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][6]}: {adv_logon_off_audit_ipsec_extended_mode}', 'magenta'))
    elif adv_logon_off_audit_ipsec_extended_mode == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][6]}: {adv_logon_off_audit_ipsec_extended_mode}', 'magenta'))
    elif adv_logon_off_audit_ipsec_extended_mode == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][6]}: {adv_logon_off_audit_ipsec_extended_mode}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_logon_off_audit_special_logon == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][7]}: {adv_logon_off_audit_special_logon}', 'red'))
    elif adv_logon_off_audit_special_logon == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][7]}: {adv_logon_off_audit_special_logon}', 'magenta'))
    elif adv_logon_off_audit_special_logon == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][7]}: {adv_logon_off_audit_special_logon}', 'magenta'))
    elif adv_logon_off_audit_special_logon == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][7]}: {adv_logon_off_audit_special_logon}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_logon_off_audit_other_logon_logoff_events == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][8]}: {adv_logon_off_audit_other_logon_logoff_events}', 'red'))
    elif adv_logon_off_audit_other_logon_logoff_events == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][8]}: {adv_logon_off_audit_other_logon_logoff_events}', 'magenta'))
    elif adv_logon_off_audit_other_logon_logoff_events == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][8]}: {adv_logon_off_audit_other_logon_logoff_events}', 'magenta'))
    elif adv_logon_off_audit_other_logon_logoff_events == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][8]}: {adv_logon_off_audit_other_logon_logoff_events}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_logon_off_audit_network_policy_server == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][9]}: {adv_logon_off_audit_network_policy_server}', 'red'))
    elif adv_logon_off_audit_network_policy_server == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][9]}: {adv_logon_off_audit_network_policy_server}', 'magenta'))
    elif adv_logon_off_audit_network_policy_server == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][9]}: {adv_logon_off_audit_network_policy_server}', 'magenta'))
    elif adv_logon_off_audit_network_policy_server == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][9]}: {adv_logon_off_audit_network_policy_server}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_logon_off_audit_group_membership == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][10]}: {adv_logon_off_audit_group_membership}', 'red'))
    elif adv_logon_off_audit_group_membership == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][10]}: {adv_logon_off_audit_group_membership}', 'magenta'))
    elif adv_logon_off_audit_group_membership == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][10]}: {adv_logon_off_audit_group_membership}', 'magenta'))
    elif adv_logon_off_audit_group_membership == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Logon/Logoff"][10]}: {adv_logon_off_audit_group_membership}', 'blue'))
    else:
        print('Something happened')
        pass

    print(colored('\nObject Access', 'yellow'))

    if adv_object_access_audit_file_system == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][0]}: {adv_object_access_audit_file_system}', 'red'))
    elif adv_object_access_audit_file_system == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][0]}: {adv_object_access_audit_file_system}', 'magenta'))
    elif adv_object_access_audit_file_system == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][0]}: {adv_object_access_audit_file_system}', 'magenta'))
    elif adv_object_access_audit_file_system == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][0]}: {adv_object_access_audit_file_system}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_registry == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][1]}: {adv_object_access_audit_registry}', 'red'))
    elif adv_object_access_audit_registry == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][1]}: {adv_object_access_audit_registry}', 'magenta'))
    elif adv_object_access_audit_registry == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][1]}: {adv_object_access_audit_registry}', 'magenta'))
    elif adv_object_access_audit_registry == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][1]}: {adv_object_access_audit_registry}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_kernel == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][2]}: {adv_object_access_audit_kernel}', 'red'))
    elif adv_object_access_audit_kernel == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][2]}: {adv_object_access_audit_kernel}', 'magenta'))
    elif adv_object_access_audit_kernel == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][2]}: {adv_object_access_audit_kernel}', 'magenta'))
    elif adv_object_access_audit_kernel == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][2]}: {adv_object_access_audit_kernel}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_sam == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][3]}: {adv_object_access_audit_sam}', 'red'))
    elif adv_object_access_audit_sam == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][3]}: {adv_object_access_audit_sam}', 'magenta'))
    elif adv_object_access_audit_sam == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][3]}: {adv_object_access_audit_sam}', 'magenta'))
    elif adv_object_access_audit_sam == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][3]}: {adv_object_access_audit_sam}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_certification_services == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][4]}: {adv_object_access_audit_certification_services}', 'red'))
    elif adv_object_access_audit_certification_services == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][4]}: {adv_object_access_audit_certification_services}', 'magenta'))
    elif adv_object_access_audit_certification_services == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][4]}: {adv_object_access_audit_certification_services}', 'magenta'))
    elif adv_object_access_audit_certification_services == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][4]}: {adv_object_access_audit_certification_services}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_application_generated == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][5]}: {adv_object_access_audit_application_generated}', 'red'))
    elif adv_object_access_audit_application_generated == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][5]}: {adv_object_access_audit_application_generated}', 'magenta'))
    elif adv_object_access_audit_application_generated == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][5]}: {adv_object_access_audit_application_generated}', 'magenta'))
    elif adv_object_access_audit_application_generated == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][5]}: {adv_object_access_audit_application_generated}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_handle_manipulation == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][6]}: {adv_object_access_audit_handle_manipulation}', 'red'))
    elif adv_object_access_audit_handle_manipulation == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][6]}: {adv_object_access_audit_handle_manipulation}', 'magenta'))
    elif adv_object_access_audit_handle_manipulation == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][6]}: {adv_object_access_audit_handle_manipulation}', 'magenta'))
    elif adv_object_access_audit_handle_manipulation == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][6]}: {adv_object_access_audit_handle_manipulation}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_file_share == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][7]}: {adv_object_access_audit_file_share}', 'red'))
    elif adv_object_access_audit_file_share == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][7]}: {adv_object_access_audit_file_share}', 'magenta'))
    elif adv_object_access_audit_file_share == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][7]}: {adv_object_access_audit_file_share}', 'magenta'))
    elif adv_object_access_audit_file_share == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][7]}: {adv_object_access_audit_file_share}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_filtering_platform_packet_drop == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][8]}: {adv_object_access_audit_filtering_platform_packet_drop}', 'red'))
    elif adv_object_access_audit_filtering_platform_packet_drop == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][8]}: {adv_object_access_audit_filtering_platform_packet_drop}', 'magenta'))
    elif adv_object_access_audit_filtering_platform_packet_drop == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][8]}: {adv_object_access_audit_filtering_platform_packet_drop}', 'magenta'))
    elif adv_object_access_audit_filtering_platform_packet_drop == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][8]}: {adv_object_access_audit_filtering_platform_packet_drop}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_filtering_platform_connection == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][9]}: {adv_object_access_audit_filtering_platform_connection}', 'red'))
    elif adv_object_access_audit_filtering_platform_connection == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][9]}: {adv_object_access_audit_filtering_platform_connection}', 'magenta'))
    elif adv_object_access_audit_filtering_platform_connection == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][9]}: {adv_object_access_audit_filtering_platform_connection}', 'magenta'))
    elif adv_object_access_audit_filtering_platform_connection == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][9]}: {adv_object_access_audit_filtering_platform_connection}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_other_object_access_events == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][10]}: {adv_object_access_audit_other_object_access_events}', 'red'))
    elif adv_object_access_audit_other_object_access_events == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][10]}: {adv_object_access_audit_other_object_access_events}', 'magenta'))
    elif adv_object_access_audit_other_object_access_events == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][10]}: {adv_object_access_audit_other_object_access_events}', 'magenta'))
    elif adv_object_access_audit_other_object_access_events == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][10]}: {adv_object_access_audit_other_object_access_events}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_detailed_file_share == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][11]}: {adv_object_access_audit_detailed_file_share}', 'red'))
    elif adv_object_access_audit_detailed_file_share == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][11]}: {adv_object_access_audit_detailed_file_share}', 'magenta'))
    elif adv_object_access_audit_detailed_file_share == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][11]}: {adv_object_access_audit_detailed_file_share}', 'magenta'))
    elif adv_object_access_audit_detailed_file_share == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][11]}: {adv_object_access_audit_detailed_file_share}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_removable_storage == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][12]}: {adv_object_access_audit_removable_storage}', 'red'))
    elif adv_object_access_audit_removable_storage == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][12]}: {adv_object_access_audit_removable_storage}', 'magenta'))
    elif adv_object_access_audit_removable_storage == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][12]}: {adv_object_access_audit_removable_storage}', 'magenta'))
    elif adv_object_access_audit_removable_storage == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][12]}: {adv_object_access_audit_removable_storage}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_object_access_audit_central_policy_staging == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][13]}: {adv_object_access_audit_central_policy_staging}', 'red'))
    elif adv_object_access_audit_central_policy_staging == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][13]}: {adv_object_access_audit_central_policy_staging}', 'magenta'))
    elif adv_object_access_audit_central_policy_staging == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][13]}: {adv_object_access_audit_central_policy_staging}', 'magenta'))
    elif adv_object_access_audit_central_policy_staging == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Object Access"][13]}: {adv_object_access_audit_central_policy_staging}', 'blue'))
    else:
        print('Something happened')
        pass

    print(colored('\nPrivilege Use', 'yellow'))

    if adv_privilege_use_audit_non_sensitive_privilege_use == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][0]}: {adv_privilege_use_audit_non_sensitive_privilege_use}', 'red'))
    elif adv_privilege_use_audit_non_sensitive_privilege_use == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][0]}: {adv_privilege_use_audit_non_sensitive_privilege_use}', 'magenta'))
    elif adv_privilege_use_audit_non_sensitive_privilege_use == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][0]}: {adv_privilege_use_audit_non_sensitive_privilege_use}', 'magenta'))
    elif adv_privilege_use_audit_non_sensitive_privilege_use == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][0]}: {adv_privilege_use_audit_non_sensitive_privilege_use}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_privilege_use_audit_other_privilege_use_events == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][1]}: {adv_privilege_use_audit_other_privilege_use_events}', 'red'))
    elif adv_privilege_use_audit_other_privilege_use_events == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][1]}: {adv_privilege_use_audit_other_privilege_use_events}', 'magenta'))
    elif adv_privilege_use_audit_other_privilege_use_events == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][1]}: {adv_privilege_use_audit_other_privilege_use_events}', 'magenta'))
    elif adv_privilege_use_audit_other_privilege_use_events == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][1]}: {adv_privilege_use_audit_other_privilege_use_events}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_privilege_use_audit_non_sensitive_privilege_use == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][2]}: {adv_privilege_use_audit_non_sensitive_privilege_use}', 'red'))
    elif adv_privilege_use_audit_non_sensitive_privilege_use == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][2]}: {adv_privilege_use_audit_non_sensitive_privilege_use}', 'magenta'))
    elif adv_privilege_use_audit_non_sensitive_privilege_use == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][2]}: {adv_privilege_use_audit_non_sensitive_privilege_use}', 'magenta'))
    elif adv_privilege_use_audit_non_sensitive_privilege_use == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Privilege Use"][2]}: {adv_privilege_use_audit_non_sensitive_privilege_use}', 'blue'))
    else:
        print('Something happened')
        pass

    print(colored('\nDetailed Tracking', 'yellow'))

    if adv_detailed_tracking_audit_process_creation == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_detailed_tracking_audit_process_creation}', 'red'))
    elif adv_detailed_tracking_audit_process_creation == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_detailed_tracking_audit_process_creation}', 'magenta'))
    elif adv_detailed_tracking_audit_process_creation == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_detailed_tracking_audit_process_creation}', 'magenta'))
    elif adv_detailed_tracking_audit_process_creation == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_detailed_tracking_audit_process_creation}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_detailed_tracking_audit_process_termination == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_detailed_tracking_audit_process_termination}', 'red'))
    elif adv_detailed_tracking_audit_process_termination == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_detailed_tracking_audit_process_termination}', 'magenta'))
    elif adv_detailed_tracking_audit_process_termination == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_detailed_tracking_audit_process_termination}', 'magenta'))
    elif adv_detailed_tracking_audit_process_termination == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_detailed_tracking_audit_process_termination}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_detailed_tracking_audit_dpapi_activity == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_detailed_tracking_audit_dpapi_activity}', 'red'))
    elif adv_detailed_tracking_audit_dpapi_activity == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_detailed_tracking_audit_dpapi_activity}', 'magenta'))
    elif adv_detailed_tracking_audit_dpapi_activity == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_detailed_tracking_audit_dpapi_activity}', 'magenta'))
    elif adv_detailed_tracking_audit_dpapi_activity == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_detailed_tracking_audit_dpapi_activity}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_detailed_tracking_audit_rpc_events == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_detailed_tracking_audit_rpc_events}', 'red'))
    elif adv_detailed_tracking_audit_rpc_events == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_detailed_tracking_audit_rpc_events}', 'magenta'))
    elif adv_detailed_tracking_audit_rpc_events == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_detailed_tracking_audit_rpc_events}', 'magenta'))
    elif adv_detailed_tracking_audit_rpc_events == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_detailed_tracking_audit_rpc_events}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_detailed_tracking_audit_plug_and_play == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_detailed_tracking_audit_plug_and_play}', 'red'))
    elif adv_detailed_tracking_audit_plug_and_play == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_detailed_tracking_audit_plug_and_play}', 'magenta'))
    elif adv_detailed_tracking_audit_plug_and_play == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_detailed_tracking_audit_plug_and_play}', 'magenta'))
    elif adv_detailed_tracking_audit_plug_and_play == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_detailed_tracking_audit_plug_and_play}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_detailed_tracking_audit_token_right_adjusted == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_detailed_tracking_audit_token_right_adjusted}', 'red'))
    elif adv_detailed_tracking_audit_token_right_adjusted == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_detailed_tracking_audit_token_right_adjusted}', 'magenta'))
    elif adv_detailed_tracking_audit_token_right_adjusted == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_detailed_tracking_audit_token_right_adjusted}', 'magenta'))
    elif adv_detailed_tracking_audit_token_right_adjusted == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_detailed_tracking_audit_token_right_adjusted}', 'blue'))
    else:
        print('Something happened')
        pass

    print(colored('\nPolicy Change', 'yellow'))

    if adv_policy_change_audit_policy_change == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_policy_change_audit_policy_change}', 'red'))
    elif adv_policy_change_audit_policy_change == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_policy_change_audit_policy_change}', 'magenta'))
    elif adv_policy_change_audit_policy_change == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_policy_change_audit_policy_change}', 'magenta'))
    elif adv_policy_change_audit_policy_change == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_policy_change_audit_policy_change}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_policy_change_audit_authentication_policy_change == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_policy_change_audit_authentication_policy_change}', 'red'))
    elif adv_policy_change_audit_authentication_policy_change == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_policy_change_audit_authentication_policy_change}', 'magenta'))
    elif adv_policy_change_audit_authentication_policy_change == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_policy_change_audit_authentication_policy_change}', 'magenta'))
    elif adv_policy_change_audit_authentication_policy_change == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_policy_change_audit_authentication_policy_change}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_policy_change_audit_authorization_policy_change == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_policy_change_audit_authorization_policy_change}', 'red'))
    elif adv_policy_change_audit_authorization_policy_change == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_policy_change_audit_authorization_policy_change}', 'magenta'))
    elif adv_policy_change_audit_authorization_policy_change == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_policy_change_audit_authorization_policy_change}', 'magenta'))
    elif adv_policy_change_audit_authorization_policy_change == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_policy_change_audit_authorization_policy_change}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_policy_change_audit_mpssvc == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_policy_change_audit_mpssvc}', 'red'))
    elif adv_policy_change_audit_mpssvc == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_policy_change_audit_mpssvc}', 'magenta'))
    elif adv_policy_change_audit_mpssvc == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_policy_change_audit_mpssvc}', 'magenta'))
    elif adv_policy_change_audit_mpssvc == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_policy_change_audit_mpssvc}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_policy_change_audit_filtering_platform_policy_change == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_policy_change_audit_filtering_platform_policy_change}', 'red'))
    elif adv_policy_change_audit_filtering_platform_policy_change == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_policy_change_audit_filtering_platform_policy_change}', 'magenta'))
    elif adv_policy_change_audit_filtering_platform_policy_change == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_policy_change_audit_filtering_platform_policy_change}', 'magenta'))
    elif adv_policy_change_audit_filtering_platform_policy_change == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_policy_change_audit_filtering_platform_policy_change}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_policy_change_audit_other_policy_change == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_policy_change_audit_other_policy_change}', 'red'))
    elif adv_policy_change_audit_other_policy_change == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_policy_change_audit_other_policy_change}', 'magenta'))
    elif adv_policy_change_audit_other_policy_change == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_policy_change_audit_other_policy_change}', 'magenta'))
    elif adv_policy_change_audit_other_policy_change == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_policy_change_audit_other_policy_change}', 'blue'))
    else:
        print('Something happened')
        pass

    print(colored('\nAccount Management', 'yellow'))

    if adv_acc_manage_audit_computer_acc_management == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_acc_manage_audit_computer_acc_management}', 'red'))
    elif adv_acc_manage_audit_computer_acc_management == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_acc_manage_audit_computer_acc_management}', 'magenta'))
    elif adv_acc_manage_audit_computer_acc_management == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_acc_manage_audit_computer_acc_management}', 'magenta'))
    elif adv_acc_manage_audit_computer_acc_management == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_acc_manage_audit_computer_acc_management}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_acc_manage_audit_sec_group_management == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_acc_manage_audit_sec_group_management}', 'red'))
    elif adv_acc_manage_audit_sec_group_management == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_acc_manage_audit_sec_group_management}', 'magenta'))
    elif adv_acc_manage_audit_sec_group_management == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_acc_manage_audit_sec_group_management}', 'magenta'))
    elif adv_acc_manage_audit_sec_group_management == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_acc_manage_audit_sec_group_management}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_acc_manage_audit_distribution_group == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_acc_manage_audit_distribution_group}', 'red'))
    elif adv_acc_manage_audit_distribution_group == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_acc_manage_audit_distribution_group}', 'magenta'))
    elif adv_acc_manage_audit_distribution_group == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_acc_manage_audit_distribution_group}', 'magenta'))
    elif adv_acc_manage_audit_distribution_group == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_acc_manage_audit_distribution_group}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_acc_manage_audit_app == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_acc_manage_audit_app}', 'red'))
    elif adv_acc_manage_audit_app == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_acc_manage_audit_app}', 'magenta'))
    elif adv_acc_manage_audit_app == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_acc_manage_audit_app}', 'magenta'))
    elif adv_acc_manage_audit_app == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_acc_manage_audit_app}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_acc_manage_audit_other_acc_management == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_acc_manage_audit_other_acc_management}', 'red'))
    elif adv_acc_manage_audit_other_acc_management == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_acc_manage_audit_other_acc_management}', 'magenta'))
    elif adv_acc_manage_audit_other_acc_management == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_acc_manage_audit_other_acc_management}', 'magenta'))
    elif adv_acc_manage_audit_other_acc_management == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][4]}: {adv_acc_manage_audit_other_acc_management}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_acc_manage_audit_user_acc_management == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_acc_manage_audit_user_acc_management}', 'red'))
    elif adv_acc_manage_audit_user_acc_management == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_acc_manage_audit_user_acc_management}', 'magenta'))
    elif adv_acc_manage_audit_user_acc_management == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_acc_manage_audit_user_acc_management}', 'magenta'))
    elif adv_acc_manage_audit_user_acc_management == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][5]}: {adv_acc_manage_audit_user_acc_management}', 'blue'))
    else:
        print('Something happened')
        pass

    print(colored('\nDS Access', 'yellow'))

    if adv_ds_access_audit_directory_srv_access == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_ds_access_audit_directory_srv_access}', 'red'))
    elif adv_ds_access_audit_directory_srv_access == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_ds_access_audit_directory_srv_access}', 'magenta'))
    elif adv_ds_access_audit_directory_srv_access == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_ds_access_audit_directory_srv_access}', 'magenta'))
    elif adv_ds_access_audit_directory_srv_access == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_ds_access_audit_directory_srv_access}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_ds_access_audit_directory_srv_changes == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_ds_access_audit_directory_srv_changes}', 'red'))
    elif adv_ds_access_audit_directory_srv_changes == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_ds_access_audit_directory_srv_changes}', 'magenta'))
    elif adv_ds_access_audit_directory_srv_changes == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_ds_access_audit_directory_srv_changes}', 'magenta'))
    elif adv_ds_access_audit_directory_srv_changes == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_ds_access_audit_directory_srv_changes}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_ds_access_audit_directory_srv_replication == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_ds_access_audit_directory_srv_replication}', 'red'))
    elif adv_ds_access_audit_directory_srv_replication == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_ds_access_audit_directory_srv_replication}', 'magenta'))
    elif adv_ds_access_audit_directory_srv_replication == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_ds_access_audit_directory_srv_replication}', 'magenta'))
    elif adv_ds_access_audit_directory_srv_replication == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_ds_access_audit_directory_srv_replication}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_ds_access_audit_detailed_directory_srv_replication == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_ds_access_audit_detailed_directory_srv_replication}', 'red'))
    elif adv_ds_access_audit_detailed_directory_srv_replication == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_ds_access_audit_detailed_directory_srv_replication}', 'magenta'))
    elif adv_ds_access_audit_detailed_directory_srv_replication == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_ds_access_audit_detailed_directory_srv_replication}', 'magenta'))
    elif adv_ds_access_audit_detailed_directory_srv_replication == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_ds_access_audit_detailed_directory_srv_replication}', 'blue'))
    else:
        print('Something happened')
        pass

    print(colored('\nAccount Logon', 'yellow'))

    if adv_acc_logon_audit_kerberos_srv_ticket_operations == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_acc_logon_audit_kerberos_srv_ticket_operations}', 'red'))
    elif adv_acc_logon_audit_kerberos_srv_ticket_operations == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_acc_logon_audit_kerberos_srv_ticket_operations}', 'magenta'))
    elif adv_acc_logon_audit_kerberos_srv_ticket_operations == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_acc_logon_audit_kerberos_srv_ticket_operations}', 'magenta'))
    elif adv_acc_logon_audit_kerberos_srv_ticket_operations == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][0]}: {adv_acc_logon_audit_kerberos_srv_ticket_operations}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_acc_logon_audit_other_acc_logon == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_acc_logon_audit_other_acc_logon}', 'red'))
    elif adv_acc_logon_audit_other_acc_logon == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_acc_logon_audit_other_acc_logon}', 'magenta'))
    elif adv_acc_logon_audit_other_acc_logon == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_acc_logon_audit_other_acc_logon}', 'magenta'))
    elif adv_acc_logon_audit_other_acc_logon == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][1]}: {adv_acc_logon_audit_other_acc_logon}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_acc_logon_audit_kerberos_authentication_srv == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_acc_logon_audit_kerberos_authentication_srv}', 'red'))
    elif adv_acc_logon_audit_kerberos_authentication_srv == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_acc_logon_audit_kerberos_authentication_srv}', 'magenta'))
    elif adv_acc_logon_audit_kerberos_authentication_srv == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_acc_logon_audit_kerberos_authentication_srv}', 'magenta'))
    elif adv_acc_logon_audit_kerberos_authentication_srv == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][2]}: {adv_acc_logon_audit_kerberos_authentication_srv}', 'blue'))
    else:
        print('Something happened')
        pass

    if adv_acc_logon_audit_credential_validation == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_acc_logon_audit_credential_validation}', 'red'))
    elif adv_acc_logon_audit_credential_validation == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_acc_logon_audit_credential_validation}', 'magenta'))
    elif adv_acc_logon_audit_credential_validation == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_acc_logon_audit_credential_validation}', 'magenta'))
    elif adv_acc_logon_audit_credential_validation == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("adv_audit_dict")["Detailed Tracking"][3]}: {adv_acc_logon_audit_credential_validation}', 'blue'))
    else:
        print('Something happened')
        pass

    print(colored(f'{lines}', 'yellow'))
    print(colored('User Rights Assignment', 'yellow'))
    print(colored(f'{lines}', 'yellow'))

    # User rights IF's

    print(colored(f'{lines}', 'yellow'))
    print(colored('Security Options', 'yellow'))
    print(colored(f'{lines}', 'yellow'))

    # Security Options IF's


checker()
