from termcolor import colored
import Main
from Mappings import local_policy, reg_keys

# Miscellaneous
not_defined = 'Not Defined'

# Functions to Variables
password_policy = Main.password_policy_to_dict()
account_lockout_policy = Main.lockout_policy_to_dict()
event_audit_policy = Main.event_audit()
user_rights_assignment = Main.privilege_rights_to_dict()
security_options = Main.security_options_registry_values_to_dict()

# Password Policy
pass_min = password_policy.get('Minimum password age')
pass_max = password_policy.get('Maximum password age')
pass_len = password_policy.get('Minimum password length')
pass_complex = password_policy.get('Password must meet complexity requirements')
pass_history = password_policy.get('Enforce password history')

# Lockout Policy
lockout_threshold = account_lockout_policy.get('Account lockout threshold')
lockout_duration = account_lockout_policy.get('Account lockout duration')
reset_lockout_counter_after = account_lockout_policy.get('Reset account lockout counter after')

# Event Audit
account_logon = event_audit_policy.get('Audit Account Logon')
account_manage = event_audit_policy.get('Audit Account Manage')
ds_access = event_audit_policy.get('Audit DS Access')
logon_events = event_audit_policy.get('Audit Logon Events')
object_access = event_audit_policy.get('Audit Object Access')
policy_change = event_audit_policy.get('Audit Policy Change')
privilege_use = event_audit_policy.get('Audit Privilege Use')
process_tracking = event_audit_policy.get('Audit Process Tracking')
system_events = event_audit_policy.get('Audit System Events')

# Advanced Audit Policy
# System
adv_sys_audit_sec_sys_extension = event_audit_policy.get('Security System Extension')
adv_sys_audit_sys_integrity = event_audit_policy.get('System Integrity')
adv_sys_audit_ipsec_driver = event_audit_policy.get('IPsec Driver')
adv_sys_audit_other_sys_events = event_audit_policy.get('Other System Events')
adv_sys_audit_sec_state_change = event_audit_policy.get('Security State Change')
# Logon/Logoff
adv_logon_off_audit_logon = event_audit_policy.get('Logon')
adv_logon_off_audit_logoff = event_audit_policy.get('Logoff')
adv_logon_off_audit_ipsec_main_mode = event_audit_policy.get('IPsec Main Mode')
adv_logon_off_audit_ipsec_quick_mode = event_audit_policy.get('IPsec Quick Mode')
adv_logon_off_audit_ipsec_extended_mode = event_audit_policy.get('IPsec Extended Mode')
adv_logon_off_audit_special_logon = event_audit_policy.get('Special Logon')
adv_logon_off_audit_other_logon_logoff_events = event_audit_policy.get('Other Logon/Logoff Events')
adv_logon_off_audit_network_policy_server = event_audit_policy.get('Network Policy Server')
adv_logon_off_audit_user_device_claims = event_audit_policy.get('User / Device Claims')
adv_logon_off_audit_group_membership = event_audit_policy.get('Group Membership')
# Object Access
adv_object_access_audit_file_system = event_audit_policy.get('File System')
adv_object_access_audit_registry = event_audit_policy.get('Registry')
adv_object_access_audit_kernel = event_audit_policy.get('Kernel Object')
adv_object_access_audit_sam = event_audit_policy.get('SAM')
adv_object_access_audit_certification_services = event_audit_policy.get('Certification Services')
adv_object_access_audit_application_generated = event_audit_policy.get('Application Generated')
adv_object_access_audit_handle_manipulation = event_audit_policy.get('Handle Manipulation')
adv_object_access_audit_file_share = event_audit_policy.get('File Share')
adv_object_access_audit_filtering_platform_packet_drop = event_audit_policy.get('Filtering Platform Packet Drop')
adv_object_access_audit_filtering_platform_connection = event_audit_policy.get('Filtering Platform Connection')
adv_object_access_audit_other_object_access_events = event_audit_policy.get('Other Object Access Events')
adv_object_access_audit_detailed_file_share = event_audit_policy.get('Detailed File Share')
adv_object_access_audit_removable_storage = event_audit_policy.get('Removable Storage')
adv_object_access_audit_central_policy_staging = event_audit_policy.get('Central Policy Staging')
# Privilege Use
adv_privilege_use_audit_non_sensitive_privilege_use = event_audit_policy.get('Non Sensitive Privilege Use')
adv_privilege_use_audit_other_privilege_use_events = event_audit_policy.get('Other Privilege Use Events')
adv_privilege_use_audit_sensitive_privilege_use = event_audit_policy.get('Sensitive Privilege Use')
# Detailed Tracking
adv_detailed_tracking_audit_process_creation = event_audit_policy.get('Process Creation')
adv_detailed_tracking_audit_process_termination = event_audit_policy.get('Process Termination')
adv_detailed_tracking_audit_dpapi_activity = event_audit_policy.get('DPAPI Activity')
adv_detailed_tracking_audit_rpc_events = event_audit_policy.get('RPC Events')
adv_detailed_tracking_audit_plug_and_play = event_audit_policy.get('Plug and Play Events')
adv_detailed_tracking_audit_token_right_adjusted = event_audit_policy.get('Token Right Adjusted Events')
# Policy Change
adv_policy_change_audit_policy_change = event_audit_policy.get('Audit Policy Change')
adv_policy_change_audit_authentication_policy_change = event_audit_policy.get('Authentication Policy Change')
adv_policy_change_audit_authorization_policy_change = event_audit_policy.get('Authorization Policy Change')
adv_policy_change_audit_ = event_audit_policy.get('MPSSVC Rule-Level Policy Change')
adv_policy_change_audit_filtering_platform_policy_change = event_audit_policy.get('Filtering Platform Policy Change')
adv_policy_change_audit_other_policy_change = event_audit_policy.get('Other Policy Change Events')
# Account Management
adv_account_manage_audit_computer_account_management = event_audit_policy.get('Computer Account Management')
adv_account_manage_audit_sec_group_management = event_audit_policy.get('Security Group Management')
adv_account_manage_audit_distribution_group_ = event_audit_policy.get('Distribution Group Management')
adv_account_manage_audit_ = event_audit_policy.get('Application Group Management')
adv_account_manage_audit_other_account_management = event_audit_policy.get('Other Account Management Events')
adv_account_manage_audit_user_account_management = event_audit_policy.get('User Account Management')
# DS Access
adv_ds_access_audit_directory_srv_access = event_audit_policy.get('Directory Service Access')
adv_ds_access_audit_directory_srv_changes = event_audit_policy.get('Directory Service Changes')
adv_ds_access_audit_directory_srv_replication = event_audit_policy.get('Directory Service Replication')
adv_ds_access_audit_detailed_directory_srv_replication = event_audit_policy.get('Detailed Directory Service Replication')
# Account Logon
adv_account_logon_audit_kerberos_srv_ticket_operations = event_audit_policy.get('Kerberos Service Ticket Operations')
adv_account_logon_audit_other_account_logon = event_audit_policy.get('Other Account Logon Events')
adv_account_logon_audit_kerberos_authentication_srv = event_audit_policy.get('Kerberos Authentication Service')
adv_account_logon_audit_credential_validation = event_audit_policy.get('Credential Validation')


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

    if adv_account_logon_audit_credential_validation == reg_keys.get('Audit')[0]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountLogon"]}: {adv_account_logon_audit_credential_validation}', 'red'))
    elif adv_account_logon_audit_credential_validation == reg_keys.get('Audit')[1]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountLogon"]}: {adv_account_logon_audit_credential_validation}', 'magenta'))
    elif adv_account_logon_audit_credential_validation == reg_keys.get('Audit')[2]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountLogon"]}: {adv_account_logon_audit_credential_validation}', 'magenta'))
    elif adv_account_logon_audit_credential_validation == reg_keys.get('Audit')[3]:
        print(colored(f'{local_policy.get("audit_dict")["AuditAccountLogon"]}: {adv_account_logon_audit_credential_validation}', 'blue'))
    else:
        print('Something happened')
        pass

    print(colored(f'{lines}', 'yellow'))
    print(colored('User Rights Assignment', 'yellow'))
    print(colored(f'{lines}', 'yellow'))

    print(colored(f'{lines}', 'yellow'))
    print(colored('Security Options', 'yellow'))
    print(colored(f'{lines}', 'yellow'))


checker()
