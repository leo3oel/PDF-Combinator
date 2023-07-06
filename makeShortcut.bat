@echo off

set "script_folder=%~dp0"
set "target_file=pdfCombinator.pyw"
set "shortcut_name=pdfCombinator"
set "programFolder=C:\ProgramData\Microsoft\Windows\Start Menu\Programs"

set "shortcut_path=%script_folder%%shortcut_name%"
set "programPath=%programFolder%\%shortcut_name%"

REM Create the shortcut
echo Creating shortcut...
powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%shortcut_path%'); $Shortcut.TargetPath = '%script_folder%%target_file%'; $Shortcut.Save()"

REM Move the shortcut to the desktop
echo Moving shortcut to ProgramPath...
move "%shortcut_path%" "%programPath%"

echo Shortcut created and moved to the ProgramPath.
pause