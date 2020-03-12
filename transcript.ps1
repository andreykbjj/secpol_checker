$hostname=hostname
$ErrorActionPreference= 'silentlycontinue'

Start-Transcript -Path "K:\$hostname.txt" -NoClobber

Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\grouppolicy\{35378eac-683f-11d2-a89a-00c04fbbcfa2}
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\wdi\{9c5a40da-b965-4fc3-8781-88dd50a6299d}
Get-ItemProperty -Path HKLM:\software\policies\microsoft\power\powersettings\0e796bdb-100d-47d6-a2d5-f7d2daa51f51
Get-ItemProperty -Path HKLM:\software\policies\microsoft\assistance\client\1.0
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\securepipeservers\winreg\allowedexactpaths
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\securepipeservers\winreg\allowedpaths
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\appcompat
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\eventlog\application
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\appx
Get-ItemProperty -Path HKLM:\software\microsoft\windows\currentversion\policies\attachments
Get-ItemProperty -Path HKLM:\software\microsoft\windows\currentversion\policies\system\audit
Get-ItemProperty -Path HKLM:\software\policies\microsoft\biometrics
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\winrm\client
Get-ItemProperty -Path HKLM:\software\microsoft\windows\currentversion\policies\credui
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\credui
Get-ItemProperty -Path HKLM:\software\policies\microsoft\cryptography
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\controlpanel\desktop
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\devicemetadata
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\driversearching
Get-ItemProperty -Path HKLM:\system\currentcontrolset\policies\earlylaunch
Get-ItemProperty -Path HKLM:\software\policies\microsoft\eventviewer
Get-ItemProperty -Path HKLM:\software\microsoft\windows\currentversion\policies\explorer
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\explorer
Get-ItemProperty -Path HKLM:\software\policies\microsoft\internetexplorer\feeds
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\lsa\fipsalgorithmpolicy
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\handwritingerrorreports
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\installer
Get-ItemProperty -Path HKLM:\software\policies\microsoft\controlpanel\international
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\tcpip\v6transition\iphttps\iphttpsinterface
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\ipsec
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\sessionmanager\kernel
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\lanmanworkstation
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\ldap
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\lltd
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\locationandsensors
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\lsa
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\mrxsmb10
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\lsa\msv1_0
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\networkconnections
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\tcpip\parameters
Get-ItemProperty -Path HKLM:\software\microsoft\windows\currentversion\policies\system\kerberos\parameters
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\netbt\parameters
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\lanmanworkstation\parameters
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\tcpip6\parameters
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\netlogon\parameters
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\lanmanserver\parameters
Get-ItemProperty -Path HKLM:\software\policies\microsoft\peernet
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\personalization
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\lsa\pku2u
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\scripteddiagnosticsprovider\policy
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windowsnt\printers
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\currentversion\pushnotifications
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\wcn\registrars
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windowsnt\rpc
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\powershell\scriptblocklogging
Get-ItemProperty -Path HKLM:\system\currentcontrolset\services\eventlog\security
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\eventlog\security
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\print\providers\lanmanprintservices\servers
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\winrm\service
Get-ItemProperty -Path HKLM:\software\microsoft\windows\currentversion\policies\servicing
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\sessionmanager
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\deviceinstall\settings
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\eventlog\setup
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windowsdefender\spynet
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\sessionmanager\subsystems
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\system
Get-ItemProperty -Path HKLM:\software\microsoft\windows\currentversion\policies\system
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\eventlog\system
Get-ItemProperty -Path HKLM:\software\microsoft\windows\currentversion\policies\system
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windowsnt\terminalservices
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\wcn\ui
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windows\tcpip\v6transition
Get-ItemProperty -Path HKLM:\system\currentcontrolset\control\securityproviders\wdigest
Get-ItemProperty -Path HKLM:\software\policies\microsoft\sqmclient\windows
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windowsmediaplayer
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windowsstore
Get-ItemProperty -Path HKLM:\software\policies\microsoft\windowsstore\windowsupdate
Get-ItemProperty -Path HKLM:\software\microsoft\windowsnt\currentversion\winlogon
Get-ItemProperty -Path HKLM:\software\policies\microsoft\wmdrm

Stop-Transcript

