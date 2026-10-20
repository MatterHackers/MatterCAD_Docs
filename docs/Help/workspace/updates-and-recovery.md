---
title: Updates and Recovery
parent: "Workspace"
nav_order: 24
---
# Updates and Recovery

This page is about the desktop app on Windows, Mac and Linux: keeping MatterCAD up to date, the windows it shows when it starts, crash reports, and getting your work back after MatterCAD closes unexpectedly.

<!-- IMAGE_NEEDED: The Check for Update window showing "There is a recommended update available" with the Download Update button, the Current Build line, and the Update Channel list set to Stable -->

## Check For Update

MatterCAD checks for a newer version when it starts and once a day while it runs. To check yourself:

1. Click **☰ MatterCAD** › **Check For Update** (on a Mac, also **MatterCAD** › **Check For Update** in the menu bar).
2. The **Check for Update** window shows your **Current Build** and what it found:

| Message | What it means |
|---------|---------------|
| **Checking for updates...** | MatterCAD is asking the update server |
| **Your application is up-to-date** | You have the newest version for your update channel |
| **There is a recommended update available** | A newer version is ready. Click **Download Update** |
| **There is a required update available** | You need this update. Click **Download Update** |
| **Downloading updates...** | The download is running, with how far it has got |
| **New updates are ready to install** | The download is done. Click **Install Update** |
| **Oops! Unable to connect to server** | MatterCAD can't reach the update server. Check your internet connection and click the refresh button to try again |

The refresh button (its tooltip says "Check for Update") checks again. Click **Close** when you are done.

### Installing an update

Click **Install Update** once the download is done:

- **Windows** - The installer starts and MatterCAD closes. If you have unsaved changes, MatterCAD asks whether to save them first.
- **Mac** - The MatterCAD disk image opens and MatterCAD closes, asking about unsaved changes first. Drag MatterCAD into your Applications folder, then open it again.
- **Linux** - Your package installer opens the update, and MatterCAD keeps running. When the installer has finished, close MatterCAD and open it again to use the new version.

If you close MatterCAD after downloading but before installing, the next time you open **Check for Update** it says **New updates are ready to install**.

### Update Channel

**Update Channel** in the same window chooses which versions you get. Click **What's this?** beside it for a short explanation.

- **Stable** - The current release version of MatterCAD. This is the recommended choice and the starting one.
- **Beta** - The release candidate: the next version, nearly finished.
- **Alpha** - The version in development, with the newest changes and the most chance of problems.

Choosing a channel checks for an update on that channel at once.

### When MatterCAD tells you itself

- The first time MatterCAD finds a newer version, it asks **Recommended Update Available**: "There is a recommended update available for MatterCAD. Would you like to download it now?" Click **Download Now** to download it and open **Check for Update**, or **Remind Me Later**.
- When an update is available, **Update Available** appears in the tab bar, just right of the **+** button, and flashes briefly. Hover over it to see "Open Check for Update to install the new version", and click it to open **Check for Update**.
- When an update is required, **Check for Update** opens by itself, except in Touch Screen Mode (see [Settings](settings.md#advanced)).

## About MatterCAD

Click **☰ MatterCAD** › **About MatterCAD** (on a Mac, also in the **MatterCAD** menu) to see:

- The **Version** you have. Give this number when you ask for help.
- "Developed By: MatterHackers", and a link to www.matterhackers.com.
- The open source software MatterCAD is made with. Click a name to read its license, or its link button to open its web page.

## The Welcome Page and the Interface Tour

When MatterCAD starts, it shows **Welcome to MatterCAD**: "Let's show you around before you get started."

- Click **Next** to take the Interface Tour.
- Click **Done** to close the window.
- Tick **Don't remind me again** so it doesn't open when MatterCAD starts. You can turn it back on with **Show Welcome Message** in [Settings](settings.md#options).

To take the tour at any time, click **☰ MatterCAD** › **Interface Tour** (on a Mac, also **Help** › **Interface Tour**), then **Next**.

The tour dims the window and points at one part of it at a time, with a short note: the **Application Menu**, **Add to Bed**, **Primitive Shapes**, **Undo & Redo**, the **Tumble Cube**, **Sign In**, **Search MatterCAD**, **Themes** and **Help**. A stop is skipped when that part isn't on screen.

- Click **Next**, or press Enter, to go on. On the last stop the button reads **Done**.
- Click **Prev** to go back.
- Click the **X** on the note, or press Esc, to end the tour.

## What's New

After MatterCAD updates to a new version, it opens the **Help** tab on [What's New](../whats-new.md) once, so you can see what changed. This happens only when you have turned off the welcome page; while the welcome page is on, it opens instead. A first install doesn't show What's New.

## Crash Reports

On Windows and Mac, MatterCAD asks once, when it starts, **Help improve MatterCAD?**: "MatterCAD can send a report when it crashes, so the crash can be fixed." It goes on: "A report contains the error, a stack trace, application state and the recent debug log. Your computer's user name, your AI keys and your GitHub token are taken out; other text, such as file names, is sent as it is. It never includes your design files unless you approve that for a specific report." Click **Allow** or **No thanks**. You can change your answer at any time with **Send Crash Reports** in [Settings](settings.md#options).

If you allowed it and MatterCAD crashes, the next time it starts it asks **Send this crash report?** and shows you the error and exactly what would be sent. When MatterCAD has a debug log, the details go on: "The recent debug log is sent with this report, with the same things taken out. Its last lines:" followed by the end of the log as it would be sent, and "The log files are at:" followed by where they are on your computer, so you can open them and read the whole log.

- Tick **Include the design file that was open** only if you want to send that design too. It starts unticked, and it is only there when the file still exists.
- Click **Send** to send the report, or **Don't send** to delete it.

Nothing is sent without your answer. If the same crash happened several times, its reports are offered once, together. At most three different crashes are offered each time MatterCAD starts. Before a report is sent, your computer's user name is replaced with "[user]", and your AI keys, your AI assistant access token and your GitHub token are taken out. Other text in the report, such as the names of your files, is sent as it is, so read what **Send this crash report?** shows before you click **Send**.

When you click **Send**, MatterCAD's two log files, `debug_log.previous.txt` and `debug_log.txt`, go with the report. MatterCAD takes your user name and those keys and tokens out of every line as it writes it to the log, and again before sending.

MatterCAD for Linux doesn't send crash reports yet. It doesn't ask the question, and the reports it writes after a crash stay on your computer.

## Recover Unsaved Work

If MatterCAD closes before you save, for example after a crash, the next time it starts it asks **Recover Design**. For a design you had saved before, on your computer or in your Cloud Library, it says "Unsaved work was found for '…' from … Recover it as an unsaved design? The original saved file will remain unchanged." For a design you never saved, it says "Unsaved work was found for '…' from … Recover it as an unsaved design?" See [Saving and Exporting](../getting-started/saving-and-exporting.md#recover-unsaved-work) for what **Recover** and **Discard recovery** do.

- If several designs have unsaved work, MatterCAD asks about each one in its own window. Answer them in any order.
- Closing the question with its X, or pressing Esc, is the same as **Discard recovery**.
- When you quit MatterCAD yourself and choose **Discard Changes**, your changes are thrown away and you are not asked about them next time.

## Your Tabs Come Back

When you start MatterCAD, the tabs you had open come back, in the same order, with the tab you were looking at in front:

- Designs saved on your computer reopen from their files. A file that has been moved or deleted is left out.
- Designs with unsaved work, after MatterCAD closed without asking you to save, come back through the recovery question above.
- Designs from your [Cloud Library](../library/cloud-library.md) come back once you are signed in.
- The **Help** tab comes back if you left it open.

If no design comes back, MatterCAD opens one new design so you can start right away.

## If MatterCAD Says the Previous Version Is Open

If the previous version of MatterCAD is still running, MatterCAD shows **Previous Version Is Open** and waits, so your designs and settings stay safe. Close the previous version, then click **Retry**. Click **Quit** to leave.

## Related

- [Saving and Exporting](../getting-started/saving-and-exporting.md) - Save your work and recover unsaved work
- [Settings](settings.md) - Show Welcome Message and Send Crash Reports
- [Menus and Toolbar](menus-and-toolbar.md) - The ☰ MatterCAD menu
- [What's New](../whats-new.md) - What changed in each version
