---
title: Settings
parent: "Workspace"
nav_order: 22
description: Change MatterCAD's language, text size, color theme, see-through drawing and AI connection.
keywords: preferences, dark mode, light mode, font size, color scheme, api key
---
# Settings

**MatterCAD Settings** holds the choices that apply to the whole app: language, text size, colors, how see-through parts are drawn, and the AI connection.

To open it, click **☰ MatterCAD** › **Settings**. On a Mac you can also choose **MatterCAD** › **Settings** in the menu bar, or press ⌘, (Command and comma).

Every change takes effect when you make it; there is no Save button. Click **Close** when you are done. Some changes reload the window, which takes a moment and keeps your open designs.

The page has five sections: **General**, **Theme**, **Options**, **Advanced** and **AI Providers**. **Options**, **Advanced** and **AI Providers** start closed: click a heading to open it. MatterCAD remembers which ones you left open.

In the browser, Settings has no **AI Providers** section, and **Advanced** has no **Application Storage** or **Application Cache** rows.

<!-- IMAGE_NEEDED: The MatterCAD Settings window with the General and Theme sections showing (Language, Number format, Thumbnails, the Text Size slider, and the row of theme previews with the accent color swatches) and the Options, Advanced and AI Providers headings closed below them -->

## General

| Setting | What it does |
|---------|--------------|
| **Language** | The language MatterCAD shows its menus and messages in. The list shows the language in use; pick another and the window reloads in that language. The first time MatterCAD starts, it picks your computer's language if MatterCAD has it |
| **Number format** | How numbers are shown and typed: **System** (follow your computer's region setting), **1234.5** (a point before the decimals) or **1234,5** (a comma before the decimals). The window reloads |
| **Thumbnails** | **Reset Thumbnails** deletes the small pictures the library shows for your designs and makes them again. MatterCAD asks first: click **Reset** to go ahead or **No** to stop. The library may be slower for a while as the pictures are remade |
| **Text Size** | Makes everything in the window bigger or smaller, from 0.3 to 2.5 (1.0 is normal). The row's name shows the size, for example "Text Size : 1.2". Move the slider, then click **Apply** to use the new size (the window reloads). If you close Settings without clicking **Apply**, the new size is used the next time you start MatterCAD |

## Theme

The **Theme** section shows a small picture of each color theme: **Classic Dark**, **Classic Light**, **Light White** (the starting theme), **Modern Dark**, **Solarized Dark** and **Solarized Light**. The theme in use has a check mark.

- Click a picture to switch to that theme.
- The colored squares at the right of the **Theme** heading are the accent colors, used for highlights and selected buttons. Hover over one to preview it on the current theme, and click it to use it.

The window reloads after each change. You can also change the theme without opening Settings: click the theme button in the status bar at the bottom of the window.

## Options

| Setting | What it does |
|---------|--------------|
| **Depth Peeling Layers** | How carefully see-through parts are drawn where they overlap: **Off**, **4**, **6** (the starting value) or **8**. More layers draw overlapping see-through parts more accurately but take more work from your graphics card. **Off** uses a quicker approximation. Open designs follow the change at once |
| **Show Welcome Message** | When on (the starting setting), the welcome window opens each time MatterCAD starts. Ticking **Don't remind me again** in the welcome window turns this off. See [Updates and Recovery](updates-and-recovery.md#the-welcome-page-and-the-interface-tour) |
| **Send Crash Reports** | When on, MatterCAD offers to send a report after it crashes, and shows you exactly what would be sent before anything goes. It turns on when you choose **Allow** in the one-time question "Help improve MatterCAD?" that MatterCAD asks when it starts, or when you turn it on here. Until you answer that question it shows off. The question says what a report leaves out: "Your computer's user name, your AI keys and your GitHub token are taken out; other text, such as file names, is sent as it is." A report also carries MatterCAD's recent debug log, with the same things taken out. Once you have turned it off, MatterCAD never asks or offers. Crash reports are sent from MatterCAD for Windows and Mac; MatterCAD for Linux doesn't send them yet, and keeps its crash reports on your computer. See [Updates and Recovery](updates-and-recovery.md#crash-reports) |

## Advanced

| Setting | What it does |
|---------|--------------|
| **Touch Screen Mode** | For a computer with a touch screen. When on, the starting text size is 1.3 instead of 1.0, unless you have already chosen a text size. The window reloads |
| **Snap baselines to whole pixels** | Lines text up on whole screen pixels, which makes it look sharper on an ordinary screen. On a high-resolution screen (such as a Mac's Retina screen) it makes no visible difference. It starts on. The window reloads |
| **Enable LCD subpixel rendering** | Uses the separate red, green and blue parts of each pixel on an LCD screen to make text sharper. On Windows it starts out following your computer's ClearType setting; on Mac and Linux it starts off |
| **Application Storage** | **Open Folder** (the link button) opens the folder where MatterCAD keeps your settings, your library and its other data. See [Frequently Asked Questions](../frequently-asked-questions.md#how-do-i-clear-the-application-data) for where it is. Desktop app only |
| **Application Cache** | **Clear Cache** (the X button) deletes temporary files MatterCAD no longer needs, such as update installers older than 30 days. It does not ask first. Desktop app only |
| **GitHub Personal Access Token** | Only needed if you browse designs stored on GitHub in the Library a lot. GitHub limits how often a program may read from it without signing in; paste a GitHub personal access token here to raise that limit. While it is empty, the box says "Enter Personal Access Token". The box hides what you paste, the token is saved as soon as it is in the box, and it is kept on this computer and taken out of crash reports |

## AI Providers

This section sets up MatterCAD's own AI chat, in the **AI** tab of the side panel (see [The AI Tab](../getting-started/ai-tab.md)). It is in the desktop app only.

At the top it says: "Your API keys are kept in MatterCAD's settings on this computer, and each is sent only to its own provider."

| Setting | What it does |
|---------|--------------|
| **AI connection** | Where the AI chat sends your messages. See below |
| **Anthropic API key** | Your own key for Claude, from Anthropic. Used for chat |
| **OpenAI API key** | Your own key for OpenAI. Used for GPT chat, making pictures and turning speech into text |
| **Meshy API key** | Your own key for Meshy. Used to make 3D meshes with Meshy's service |
| **AI Assistant Access** | **Open** opens the panel that lets AI tools outside MatterCAD, such as Claude Code, work on your designs. See [Using AI Assistants](../getting-started/ai-assistants.md) |

### AI connection

- **Automatic** (the starting choice) - Uses your own keys if you have entered an Anthropic or OpenAI key. Otherwise it uses MatterHackers AI when you are signed in. A Meshy key alone doesn't count.
- **MatterHackers AI** - Uses the MatterHackers AI service. You need to [sign in](account.md), and your MatterHackers account needs an AI subscription.
- **My own API keys** - Always sends your messages straight to Anthropic or OpenAI with your own keys.

If the chat can't connect the way you chose, the **AI** tab tells you what is missing, for example "Sign in to use MatterHackers AI, or add your own API key in Settings."

### Entering a key

1. Open **AI Providers**.
2. Click in the key's box and paste your key. The box hides what you paste. The key is saved as soon as it is in the box.
3. To take a key out, click **Remove key** beside it.

Your keys stay on this computer, saved with MatterCAD's other settings. Each key is sent only to its own company's service (Anthropic, OpenAI or Meshy), never to MatterHackers, and it is removed from crash reports.

## Related

- [Menus and Toolbar](menus-and-toolbar.md) - The ☰ MatterCAD menu
- [Signing In](account.md) - Your MatterHackers account
- [Updates and Recovery](updates-and-recovery.md) - Updates, crash reports and the welcome window
