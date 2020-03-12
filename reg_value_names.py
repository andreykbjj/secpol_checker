reg_values = [
    'ShutdownWithoutLogon',
    'LegalNoticeText',
    'CachedLogonsCount',
    'RestrictAnonymous',
    'EnableForcedLogoff',
    'EnablePlainTextPassword',
    'AutoAdminLogon',
    'AddPrinterDrivers',
    'LmCompatibilityLevel',
    'DisableCAD',
    'SCRemoveOption',
    'EnableSecuritySignature',
    'SealSecureChannel',
    'SignSecureChannel',
    'DisablePasswordChange',
    'EnableSecuritySignature',
    'AllocateDASD',
    'PasswordExpiryWarning',
    'ProtectionMode',
    'autodisconnect',
    'DontDisplayLastUserName',
    'AuditBaseObjects',
    'FullPrivilegeAuditing',
    'SCENoApplyLegacyAuditPolicy',
    'NoDefaultExempt',
    'FilterAdministratorToken',
    'ConsentPromptBehaviorAdmin',
    'ConsentPromptBehaviorUser',
    'EnableInstallerDetection',
    'EnableSecureUIAPaths',
    'EnableLUA',
    'PromptOnSecureDesktop',
    'EnableVirtualization',
    'EnumerateAdministrators',
    'DisablePasswordSaving',
    'fDisableCdm',
    'RestrictRemoteClients',
    'DisableHTTPPrinting',
    'DisableWebPnPDownload',
    'DontSearchWindowsUpdate',
    'SaveZoneInformation',
    'HideZoneInfoOnProperties',
    'ScanWithAntiVirus',
    'Disabled',
    'NC_AllowNetBridge_NLA',
    'MicrosoftEventVwrDisableLinks',
    'NoInternetOpenWith',
    'LogonType',
    'DisableEnclosureDownload',
    'PreXPSP2ShellProtocolBehavior',
    'SafeForScripting',
    'EnableUserControl',
    'DisableLUAPatching',
    'GroupPrivacyAcceptance',
    'AllowLLTDIOOndomain',
    'AllowLLTDIOOnPublicNet',
    'EnableLLTDIO',
    'ProhibitLLTDIOOnPrivateNet',
    'AllowRspndrOndomain',
    'AllowRspndrOnPublicNet',
    'EnableRspndr',
    'ProhibitRspndrOnPrivateNet',
    'DisableFlashConfigRegistrar',
    'DisableInBand802DOT11Registrar',
    'DisableUPnPRegistrar',
    'DisableWPDRegistrar',
    'EnableRegistrars',
    'DisableWcnUi',
    'AllowRemoteRPC',
    'DisableSystemRestore',
    'DisableSendGenericDriverNotFoundToWER',
    'DontPromptForWindowsUpdate',
    'PreventHandwritingErrorReports',
    'DCSettingIndex',
    'ACSettingIndex',
    'LoggingEnabled',
    'SpyNetReporting',
    'NoHeapTerminationOnCorruption',
    'DisableOnline',
    'NoInPlaceSharing',
    'EnableUIADesktopToggle',
    'fDisableCcm',
    'fDisableLPT',
    'fDisablePNPRedir',
    'fEnableSmartCard',
    'ValidateAdminCodeSignatures',
    'CEIPEnable',
    'NoImplicitFeedback',
    'NoExplicitFeedback',
    'SmbServerNameHardeningLevel',
    'UseMachineId',
    'allowNonesessionfallback',
    'AllowOnlineID',
    'SupportedEncryptionTypes',
    'DisableIPSourceRouting',
    'TcpMaxDataRetransmissions',
    'NC_StdDomainUserSetLocation',
    'Force_Tunneling',
    'DoNotInstallCompatibleDriverFromWindowsUpdate',
    'PreventDeviceMetadataFromNetwork',
    'SearchOrderConfig',
    'DisableQueryRemoteServer',
    'EnableQueryRemoteServer',
    'ScenarioExecutionEnabled',
    'DisableInventory',
    'NoAutoplayfornonVolume',
    'NoDataExecutionPrevention',
    'NoAutorun',
    'NoDriveTypeAutoRun',
    'RestrictAnonymousSAM',
    'LegalNoticeCaption',
    '6to4_State',
    'IPHTTPS_ClientState',
    'ISATAP_State',
    'Teredo_State',
    'MaxSize',
    'MaxSize',
    'MaxSize',
    'MaxSize',
    'DisableSendRequestAdditionalSoftwareToWER',
    'NoneSessionPipes',
    'Machine',
    'NoneSessionShares',
    'fAllowToGetHelp',
    'LimitBlankPasswordUse',
    'MaximumPasswordAge',
    'RequireStrongKey',
    'DisableDomainCreds',
    'EveryoneIncludesAnonymous',
    'ForceGuest',
    'NoLMHash',
    'LDAPClientIntegrity',
    'NTLMMinClientSec',
    'Enabled',
    'ObCaseInsensitive',
    'fSingleSessionPerUser',
    'fPromptForPassword',
    'MinEncryptionLevel',
    'PerSessionTempDir',
    'DeleteTempDirsOnExit',
    'DisableBkGndGroupPolicy',
    'fAllowUnsolicited',
    'SafeDllSearchMode',
    'DisableAutoupdate',
    'PreventCodecDownload',
    'AlwaysInstallElevated',
    'LocalAccountTokenFilterPolicy',
    'ScreenSaveActive',
    'ScreenSaverIsSecure',
    'NTLMMinServerSec',
    'EnableIPAutoConfigurationLimits',
    'UseWindowsUpdate',
    'DriverServerSelection',
    'DriverLoadPolicy',
    'NoUseStoreOpenWith',
    'BlockUserInputMethodsForSignIn',
    'EnumerateLocalUsers',
    'DisableLockScreenAppNotifications',
    'DisablePcaUI',
    'AllowAllTrustedApps',
    'Enabled',
    'DisablePasswordReveal',
    'EnableSmartScreen',
    'DisableLocation',
    'AllowBasicAuthInClear',
    'AutoDownload',
    'AutoDownload',
    'RemoveWindowsStore',
    'AllowBasic',
    'AllowUnencryptedTraffic',
    'AllowDigest',
    'AllowBasic',
    'AllowUnencryptedTraffic',
    'DisableRunAs',
    'InactivityTimeoutSecs',
    'NoCloudApplicationNotification',
    'NoToastApplicationNotificationOnLockScreen',
    'RedirectOnlyDefaultClientPrinter',
    'WarningLevel',
    'DisableIPSourceRouting',
    'EnableICMPRedirect',
    'PerformRouterDiscovery',
    'KeepAliveTime',
    'NoNameReleaseOnDemand',
    'NoLockScreenSlideshow',
    'ProcessCreationIncludeCmdLine_Enabled',
    'DontDisplayNetworkSelectionUI',
    'MSAOptional',
    'DisableAutomaticRestartSignOn',
    'TcpMaxDataRetransmissions',
    'ScreenSaverGracePeriod',
    'Machine',
    'Optional',
    'fEncryptRPCTraffic',
    'NoGPOListChanges',
    'ForceKeyProtection',
    'RequireSignOrSeal',
    'RequireSecuritySignature',
    'RequireSecuritySignature',
    'RestrictNoneSessAccess',
    'UseLogonCredential',
    'SMB1',
    'Start',
    'DependOnService',
    'EnableScriptBlockLogging',
]
