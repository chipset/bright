REM @echo off
set pds=%1
set fromprofile=%2
set toprofile=%3
set tempdir=%4

REM Create profile.  
bright files create pds %pds% --zosmf-profile %toprofile%

REM Download PDS
bright files dl am %pds% -d %tempdir% --zosmf-profile %fromprofile%

REM Upload PDS to host
bright files upload dtp %tempdir% %pds% --zosmf-profile %toprofile%


