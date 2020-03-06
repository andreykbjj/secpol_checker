from termcolor import colored
import Main
from Mappings import local_policy


password_policy = Main.password_policy_to_dict()
account_lockout_policy = Main.lockout_policy_to_dict()
event_audit_policy = Main.event_audit()
user_rights_assignment = Main.privilege_rights_to_dict()
security_options = Main.security_options_registry_values_to_dict()

pass_min = password_policy.get('Minimum password age')
pass_max = password_policy.get('Maximum password age')
pass_len = password_policy.get('Minimum password length')
pass_complex = password_policy.get('Password must meet complexity requirements')
pass_history = password_policy.get('Enforce password history')

lockout_threshold = account_lockout_policy.get('Account lockout threshold')
lockout_duration = account_lockout_policy.get('Account lockout duration')
reset_lockout_counter_after = account_lockout_policy.get('Reset account lockout counter after')

account_logon = event_audit_policy.get('Audit Account Logon')
ds_access = event_audit_policy.get('Audit DS Access')
process_tracking = event_audit_policy.get('Audit Process Tracking')
account_manage = event_audit_policy.get('Audit Account Manage')
policy_change = event_audit_policy.get('Audit Policy Change')
privilege_use = event_audit_policy.get('Audit Privilege Use')
object_access = event_audit_policy.get('Audit Object Access')
logon_events = event_audit_policy.get('Audit Logon Events')
system_events = event_audit_policy.get('Audit System Events')


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
        print(colored(f'{local_policy.get("password_policy")["MinimumPasswordAge"]}: {pass_history}', 'red'))
    else:
        print(colored(f'{local_policy.get("password_policy")["MinimumPasswordAge"]}: {pass_history}', 'blue'))

    if pass_max == 0 or pass_max > 90:
        print(colored(f'{local_policy.get("password_policy")["MaximumPasswordAge"]}: {pass_history}', 'red'))

    else:
        print(colored(f'{local_policy.get("password_policy")["MaximumPasswordAge"]}: {pass_history}', 'blue'))

    if pass_complex != 1:
        print(colored(f'{local_policy.get("password_policy")["PasswordComplexity"]}: {pass_history}', 'red'))
    else:
        print(colored(f'{local_policy.get("password_policy")["PasswordComplexity"]}: {pass_history}', 'blue'))

    if pass_len < 8:
        print(colored(f'{local_policy.get("password_policy")["MinimumPasswordLength"]}: {pass_history}', 'red'))
    else:
        print(colored(f'{local_policy.get("password_policy")["MinimumPasswordLength"]}: {pass_history}', 'blue'))

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
                print(colored(f'{local_policy.get("lockout_policy")["ResetLockoutCount"]}: {reset_lockout_counter_after}', 'red'))
            else:
                print(colored(f'{local_policy.get("lockout_policy")["ResetLockoutCount"]}: {reset_lockout_counter_after}', 'blue'))
        else:
            pass
    else:
        print(colored(f'{local_policy.get("lockout_policy")["LockoutBadCount"]}: {lockout_threshold}', 'red'))
        print(colored(f'{local_policy.get("lockout_policy")["LockoutDuration"]}: Not Defined', 'red'))
        print(colored(f'{local_policy.get("lockout_policy")["ResetLockoutCount"]}: Not Defined', 'red'))

    print(colored(f'{lines}', 'yellow'))
    print(colored('Audit Policy', 'yellow'))
    print(colored(f'{lines}', 'yellow'))

    if account_logon == 3:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountLogon"]}: {account_logon}', 'red'))
    else:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountLogon"]}: {account_logon}', 'blue'))
    if ds_access == 0:
        print(colored(f'{local_policy.get("audit_dict")["AuditDSAccess"]}: {ds_access}', 'red'))
    else:
        print(colored(f'{local_policy.get("audit_dict")["AuditDSAccess"]}: {ds_access}', 'blue'))
    if account_manage == 0:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountManage"]}: {account_manage}', 'red'))
    else:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountManage"]}: {account_manage}', 'blue'))
    if policy_change == 0:
        print(colored(f'{local_policy.get("audit_dict")["AuditPolicyChange"]}: {policy_change}', 'red'))
    else:
        print(colored(f'{local_policy.get("audit_dict")["AuditPolicyChange"]}: {policy_change}', 'blue'))
    if privilege_use == 0:
        print(colored(f'{local_policy.get("audit_dict")["AuditPrivilegeUse"]}: {privilege_use}', 'red'))
    else:
        print(colored(f'{local_policy.get("audit_dict")["AuditPrivilegeUse"]}: {privilege_use}', 'blue'))
    if object_access == 0:
        print(colored(f'{local_policy.get("audit_dict")["AuditObjectAccess"]}: {object_access}', 'red'))
    else:
        print(colored(f'{local_policy.get("audit_dict")["AuditObjectAccess"]}: {object_access}', 'blue'))
    if logon_events == 0:
        print(colored(f'{local_policy.get("audit_dict")["AuditLogonEvents"]}: {logon_events}', 'red'))
    else:
        print(colored(f'{local_policy.get("audit_dict")["AuditLogonEvents"]}: {logon_events}', 'blue'))
    if system_events == 0:
        print(colored(f'{local_policy.get("audit_dict")["AuditSystemEvents"]}: {system_events}', 'red'))
    else:
        print(colored(f'{local_policy.get("audit_dict")["AuditSystemEvents"]}: {system_events}', 'blue'))
    if process_tracking == 0:
        print(colored(f'{local_policy.get("audit_dict")["AuditSystemEvents"]}: {process_tracking}', 'red'))
    else:
        print(colored(f'{local_policy.get("audit_dict")["AuditSystemEvents"]}: {process_tracking}', 'blue'))

    print(colored(f'{lines}', 'yellow'))
    print(colored('User Rights Assignment', 'yellow'))
    print(colored(f'{lines}', 'yellow'))

    print(colored(f'{lines}', 'yellow'))
    print(colored('Security Options', 'yellow'))
    print(colored(f'{lines}', 'yellow'))


checker()
