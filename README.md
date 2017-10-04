# Aenea Setup

My setup for aenea

Follow the `aenea` submodule setup instructions

## Updating the grammars easily

Make the `MacroSystem` directory a Shared Folder in VirtualBox. This will allow
the `scripts/copy-scripts.py` file to cause the VM to see the updated grammars.

You can use the `scripts/copy-scripts.py` to update the MacroSystem folder with
new grammars. After running the script, in Dragon turn the microphone off then
on again (the grammars are reloaded when they microphone is turned on, or when
you say `force natlink to reload all grammars`).
