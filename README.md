# Batch project export for DaVinci Resolve

This script allows the user to queue the export of multiple projects that are located in the same folder in Resolve's project manager.

## Installation

### Requirements

This script requires Python 3.6.

Using the script from the workspace menu requires the Studio version of Resolve, version 16.2+.

### Script location

To enable the execution of the script from the `Workspace / Scripts` menu, you need to copy the repository content to a specific location depending on your operating system.

```
MacOS:      /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp/
Windows:    %APPDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp\
Linux:      /opt/resolve/Fusion/Scripts/Comp/   (or /home/resolve/Fusion/Scripts/Comp/ depending on installation)
```

### Settings in Resolve

Make sure to enable External scripting by going in `Preferences`, `System`, `General`.
Then set the `External script using` option to `Local` or `Network`.

In the Fusion page, go to the `Fusion` menu, and open `Fusion Settings...`. 
Then navigate to the `Script` category, and select `Python 3.6`. 
Finally, save the settings, and quit Resolve for the settings to apply.

## Using the script

To execute the script, make sure you have opened a project in the folder you want to use the script from, then open the `Workspace` menu and navigate to `Script / resolve_drp_exporter` and select `resolve_drp_exporter.py`

In the settings window that opens, select the projects you want to export.
Then, choose the destination folder for the exports.
Finally, you can choose to append a date and time at the end of the export file name.

Once you validate, the exports will start. You can check the progress using the console.