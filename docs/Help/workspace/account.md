---
title: Signing In
parent: "Workspace"
nav_order: 23
---
# Signing In

You don't need an account to design in MatterCAD. Sign in to your MatterHackers account when you want to use your [Cloud Library](../library/cloud-library.md), open designs others have [shared](../library/sharing.md) with you, or use MatterHackers AI.

<!-- IMAGE_NEEDED: The right end of the tab bar while signed in, with the account menu open under the user's name showing AI Assistant Access..., Enter Share Code... and Sign Out -->

## Sign In

1. Click **(sign in)** at the far right of the tab bar. Hover over it and it says "Sign in to your MatterHackers account".
2. In **Sign in to my account**, type your **Username or Email** and your **Password**. Tick **Show Password** to see what you typed.
3. Click **Sign in**, or press Enter in the password box.

While MatterCAD checks, it shows "Please wait. Signing in...". Once you are in, **(sign in)** changes to your name, and the cloud designs you had open when you last signed out come back in their tabs.

MatterCAD stays signed in when you close and reopen it, until you sign out.

Opening the **Cloud Library** in the library while signed out opens the same sign-in window.

If signing in doesn't work, the window says why:

- "Oops! Invalid username, email or password." - Check what you typed, or use **Forgot Password**.
- "Sorry! Unable to connect to server. Please try again later." - MatterCAD can't reach the internet or the MatterHackers server.
- "Sorry! Too many sign in attempts. Please try again later." - Wait a while before you try again.

## Create an Account

1. Click **(sign in)**, then click **Create An Account** at the bottom of the window (beside "New User?").
2. In **Sign Up for an Account**, fill in **Username**, **Email**, **Password** and **Re-enter Password**.
3. Click **Create Account**.

When the account is made, MatterCAD shows "Success! Your account has been created." Click **Continue** to go back to the sign-in window with your username filled in, and sign in.

If the name or email is already in use, the window tells you which, for example "Sorry! Looks like an account already exists for that email address."

## Forgot Password

1. Click **(sign in)**, then click **Forgot Password** beside the **Password** box.
2. In **What was my password again?**, type your **Email Address** and click **Reset Password**. MatterCAD emails you a six-digit reset code.
3. In **Update my password**, type the **Password Reset Code** from the email, then your **New Password** twice (**Re-enter New Password**).
4. Click **Change Password**. When you see "Success! Your password has been updated.", click **Continue** and sign in with the new password.

If the code is wrong or too old, the window says "Sorry! Looks like that reset code is invalid." or "Sorry! Looks like that reset code has expired." Start again from step 2 to get a new code.

## The Account Menu

While you are signed in, click your name at the right of the tab bar for:

| Item | What it does |
|------|--------------|
| **AI Assistant Access...** | Opens the panel that lets AI tools outside MatterCAD work on your designs. You don't have to be signed in for this: the same item is on the globe in the status bar. See [Using AI Assistants](../getting-started/ai-assistants.md). Desktop app only |
| **Enter Share Code...** | Opens a design someone shared with you. See below |
| **Sign Out** | Signs you out. See below |

### Enter a share code

1. Choose **Enter Share Code...**.
2. In **Library - Enter Share Code**, type the code you were given in the **Enter Share Code:** box and click **Continue**. The note under the box says "This code will provide read-only access."
3. When MatterCAD says "Your code has been redeemed. Please check your 'Shared with Me' folder in your Library.", click **Done**.

The shared design is in the **Shared with Me** folder of your Library. You can open and use it, but you can't change the original. If the code is wrong, MatterCAD says "Oops! Invalid code."; click **Try Again** to fix it.

## Sign Out

1. Click your name at the right of the tab bar and choose **Sign Out**.
2. MatterCAD asks "Are you sure you want to sign out? You will not have access to your cloud library until you sign in again." Click **Sign Out**, or **Cancel** to stay signed in.

Signing out closes every tab that holds a design from your Cloud Library. Designs saved on your computer and new designs stay open. The closed cloud designs come back the next time you sign in.

If a cloud design has changes you have not saved, MatterCAD asks first, for example "You have unsaved changes in the cloud design 'Bracket'. Signing out closes it. Save the changes before signing out?"

- **Save Changes** saves the designs, waits for them to finish uploading, and then signs you out. If a design doesn't finish saving, MatterCAD stays signed in and tells you, so you can save it again.
- **Sign Out Anyway** signs out and throws the unsaved changes away.
- **Cancel** keeps you signed in.

After you sign out, **Shared with Me** and **Purchased** disappear from the Library until you sign in again, and the status bar's globe shows **Disconnected**.

## Related

- [Cloud Library](../library/cloud-library.md) - Keep designs online
- [Sharing](../library/sharing.md) - Share designs with share codes
- [Settings](settings.md#ai-providers) - The AI connection and MatterHackers AI
- [Tabs, Search and the Status Bar](tabs-and-search.md) - The tab bar and the status bar
