# Unit 001 - Lesson 005

In this lesson we are going to download and install the powerful VS Code editor from Microsoft &trade;. This lesson will cover how to download and install the software on the Windows, macOS, and Linux (Debian) operating systems. Once installed we will introduce this powerful editor and just a few of its many features. IDLE is a fine editor, but for larger coding projects and more control over efficiency and multiple file management, VS Code wins hands down! Let's get started!

Biblical integration for this type of a lesson is difficult because the things we are doing are very detailed and intricate, but asking our Father in heaven for help and understanding is always a good place to begin.

::: prayer

"Dear Father, who created all things, I am now learning myself how to use what You have given me, the creative desire, to learn something new and try to excel at it. Take this lesson, open my eyes, mind, and heart. If there is anything of Christ that You can show me, then show me, yet still, help me to use all that I learn for Your glory. In Jesus' name, the name You love. Amen."

:::

## Downloading, Installing, and Introducing VS Code

To download VS Code on Window, macOS, or even Linux, open a web browser and navigate to the following page..

::: link
<a href="https://code.visualstudio.com/download">https://code.visualstudio.com/download</a>
:::

::: center-img
![VS Code Download Page](../static/images/unit_001/vs%20code%20download%20image.png)
:::

*Depending on any new updates on the page, the download page should look, more or less, like this..*

## Windows and macOS

The downloading and installation of VS Code for Windows and macOS will be straight forward. Below the Windows logo and macOS logo there are blue boxes with the *download arrow*  (pointing downwards). If you are on Windows or macOS, click on the respective box that represents your operating system and the download will begin.

On Windows, once the download is complete you will have an executable file (*.exe) in your Downloads folder (or where-ever you download your files by default). On macOS you will have a (.pkg) file. Double click on your downloaded file and this will open the installation wizard.

> **Wizard** A wizard is a user interface in software that gives a step-by-step guide for the user to complete a task or set of tasks. In this case our task is the installation of VS Code.

Follow these steps directly and VS Code will install on your system.

## Linux (Debian)

Installing software on Linux, can be, a more detailed process. This step by step process has been provided for Linux users at the VS Code site.

::: link
<a href="https://code.visualstudio.com/docs/setup/linux">https://code.visualstudio.com/docs/setup/linux</a>
:::

## Launching VS Code

Once you have VS Code installed on your system go ahead and launch the application (launch = start the app).

### Windows

In the taskbar at the bottom of the screen, in the search box type: Code. VS Code and it's icon will appear from the search. Click on this item to launch the application.

### macOS

Press the **Command (&#8984;) key** and tap the **Space bar** to bring up Spotlight search. Type: Code and you will see the VS Code icon appear. Click on this icon and the application will launch.

### Linux

Press the **Super key** (the Windows logo key on most keyboards, often called ⊞). Immediately start typing: code or visual or vs.
This will instantly show Visual Studio Code as the top result. Press Enter to launch it.

::: page-break :::

## VS Code

On first launch you will get a window on your screen that should look, more or less, like this..

![VS Code First Launch](../static/images/unit_001/vs%20code%20first%20launch.png)

*VS Code upon first launch.*

#### Close Agent Mode

Unless you are a more advanced user, collapse the **Agent Mode** panel on the right by clicking on the corresponding &times; to close this panel.

#### The Activity Bar

On the left hand side of the screen is a vertical bar with several icons on it. This is known as the VS Code Activity bar. At this point, there are only two icons we are interested in. The explorer, and extensions icons.

![Explorer Icon](../static/images/unit_001/explorer.png) is the explorer icon. Right now, we do not have any projects open or any files to work with. When we begin building applications with VS Code this will change. The explorer icon will show us all our project files and allow us to manage them more directly. This is one of the main features of VS Code that stands out from IDLE. In IDLE, you can only work with one file at a time.

![Extensions Icon](../static/images/unit_001/extensions.png) is the extensions icon. VS Code extensions are mini-programs that extend the functionality of your development experience.

### Open the Extensions MarketPlace

Click on the extensions icon and you will load the default extensions marketplace.

In the marketplace you are going to see a search bar. **Type:** "Python" and hit Enter. The marketplace page will load.

![Extensions MarketPlace](../static/images/unit_001/extensions%20marketplace.png)

Upon loading any particular extension available you will see several important and relevant items.

1. The number of users currently using the extension.
2. The current evaluation of the extension based upon a five star rating. &#x2B50;
3. An installation button. (When an extension is already installed, the button options then become "Disable" and "Uninstall")

### The Minimum Extensions Needed

Here is a list of the minimum extensions I would like you to install at this time.

1. Python (not the programming language, the extension)
2. Pylance
3. Python indent
4. Jupyter
5. Ruff
6. Python Debugger
7. Sourcery or GitHub Copilot (Copilot can be used for free in a limited way. If you want full access, you will have to get the paid version).

::: note
**Trusting the Author** When you install each extension you may get a dialogue box asking whether or not to trust the author of that particular extension. The extensions that I have provided for you are trustworthy so go ahead and select Yes/Ok. 

However, you do want to take time to investigate how many people trust a given extension and its rating. Some extensions (sadly to say) are written with malicious intent. This means that in some way they will try to get personal information from your computer. These types of extensions are removed from the marketplace when discovered, but they do pop up from time to time.
:::

### Extension MarketPlace Best Practices

* Stick to trusted publishers: (Microsoft, GitHub) and popular extensions with many downloads/reviews.
* Check the details: Look at install counts, rating, publisher verification, and recent updates.
* Minimize extensions: Only what you need.
* Review before installing.
* Use Workspace Trust: Restricts untrusted folder from running risky code.
* Enable Restriction.
* Keep your extensions up to date.
* Tools like ExtensionTotal can scan for risks.

## Creating a Root Project Folder

Now let's create a project root folder. We are not going to build any serious applications because we are still new in our learning, but it is important to know the steps involved to create and work from a root project folder.

**Step 1:** Create the following folders and sub-folders on your computer system. We suggest you go to your `Documents` folder and build them from there.

`compsci` &rarr; `unit_001` &rarr; `lesson_005`

**Step 2:** In VS Code go to the **File** menu and choose **Open Folder**: `File` &rarr; `Open Folder`. Navigate to the `lesson_005` folder and choose `Select`. The `lesson_005` folder is now your root project folder.

At the top of the explorer window in VS Code you should now see the following.

<div class="container">
<img src="../static/images/unit_001/lesson 5 root project folder.png" alt="Lesson 5 Root Project Folder">
<p>
    Notice that the root project folder is in ALL CAPS. Next, we will learn how to create Python files and even sub-folders inside our project. Now that we have our root project folder, let's learn how to create our first Python file.
</p>
</div>

### Creating Files and Folders

There are two icons that we want to familiarize ourselves with. They are: ![create icons vs code](../static/images/unit_001/create%20new%20file%20and%20create%20new%20folder.png). The first icon is the create file icon, the second is the create folder icon.

**Alternative**: Alternatively you can create new files by going to the **File** menu and choosing the **New File** option. If you want to create a new folder alternatively, then you will have to follow the same steps you did before to create the `lesson_005` folder.

**Step 3:** Click on the new file icon and type in `temp.py` then hit enter. The following empty Python file is created.

![temp.py](../static/images/unit_001/temp.py.png) the little blue Python logo appears to the right of the file name. 

How does VS Code know that this is a Python file? Answer: Because all Python files end with the `*.py` extension.

### Writing and Running

**Step 4:** Inside the `temp.py` file, write the following script.

```python
print("Welcome to VS Code and Python!")
```

**Step 5:** Save the file. To save the file you can type: (CTRL + S) Windows/Linux, or (&#x2318; + S) macOS.

**Step 6:** To run the file click on the `Run` button in the upper right hand corner of the editor window. Here is what *should* happen..

![running temp.py](../static/images/unit_001/running%20temp%20file.png)

This is what ***should*** happen.

::: page-break :::

There are typically two problems that some students encounter. If this is not you, then skip these next two sub-sections.

---

### I Don't See A Run Button!

The reason for this *could* be a rather simple reason. There are two things which must happen for the `Run` button to appear. 

1. VS Code does not see this file as a Python file, in which case you have not named it with the `*.py` file extension.
2. The Official Python extension from Microsoft has not been downloaded and installed yet from the VS Code Extensions marketplace.

If you need to redo any of these steps, go ahead and do so now, then save your file. Close VS Code and reopen it. This should remedy the problem.

### I Don't See The Output or Terminal Does Not Open!

Here is how to fix this is a few quick steps.

1. Open the `temp.py` file in VS Code.
2. Look at the top-right corner for the ▶ button.
3. **Click the small dropdown arrow** next to the ▶ (if there's no arrow, just click the button -- it wil show the menu.)
4. Choose **Run Python File in Terminal**.
---

## The Integrated Terminal

When you run the program the integrated terminal window pane should appear at the bottom of your VS Code window. How cool is that!? 😎 VS Code has its own built in terminal just for you. Here are some extra features of the integrated terminal that I will let you research on your own.

1. Open multiple terminals in VS Code
2. Remove or Trash a terminal session in VS Code
3. Change the type of shell (bash or other) in VS Code
4. How to open the terminal window directly in VS Code with the `Terminal` menu item.

::: page-break :::

## Opening a Python Shell Session

If you researched how to open another terminal in VS Code, then go ahead and type `python` for Windows users, or `python3` for macOS and Linux users.

A Python shell should open for you to use. You will see the three chevrons `>>>`. Do you remember how to close or exit a Python shell session?

This terminal based shell comes with a few more features, however. Here is one. If you type (CTRL + L) on all systems, the terminal session will clear, but the Python shell will still be running. This is a feature we did not have in IDLE.

## Version Syncing

Sometimes, if you have multiple versions of Python installed on your system, the version you run with the `Run` button will be out of sync with the version of Python you run in the integrated terminal. This is pretty simple to fix.

For example, I have both Python3.13.5 and Python3.14.0 installed on my Debian Linux system, and my VS Code is out of sync. To fix this I will open the **Command Palette** in VS Code.

When you type CTRL + SHIFT + P (Windows and Linux), or (Command + Shift + P) macOS, the command palette opens.

![command palette](../static/images/unit_001/command%20palette.png)

In the text box, type: **Python: Select Interpreter** and then choose the version of Python from the list that corresponds to the version used in your terminal. Hit `Enter` and you are all synced up!

::: note
**Note:** If at any time you want to see what version of Python your terminal window is running (or allows to run) type the command `python --version` on Windows and `python3 --version` on macOS and Linux.
:::

::: page-break :::

::: warning-box
**Warning to Linux Users:** If you are a Linux user we highly recommend you do not alter the native Python version your system uses. The Linux operating system you are using depends very heavily upon the Python version that came installed with it. Changing this version system wide can break your computer. 

If you do wish to install multiple versions on your Linux system, we recommend you research how to do an `alternative install` for Python online. There are multiple resources out there to help you get the version you want without breaking your system.
:::

## Creating a new folder

Finally, let's conclude this lesson by creating a new sub-folder in our root project folder. For now, we will create a dummy folder named `temp`.

**Step 7:** Click on the `new Folder` icon ![create new files and folders vs code](../static/images/unit_001/create%20new%20file%20and%20create%20new%20folder.png), next to the `new File` icon you used earlier and type `temp`. Hit the **Enter** key. You should now see a `temp` folder inside your project alongside the `temp.py` file.

### Moving Files with the mouse

When you create a file and folder you can use your mouse to move the file inside and outside of the folder you created. It is easier to see how to do this than to read about it, but I will try to give a brief description of how to do that here.

If you click on the `temp.py` file and hold on the left mouse key you can drag the temp.py file into your `temp` folder. Release the mouse key and you will see the file slightly *indent* a little. This means that it belongs to or is inside of the`temp` folder.

To drag a file out of the folder, click and hold the left mouse key down on the file and pull down in the explorer pane until the background becomes a dull gray/blue with a border. This means that the file has been moved to the root project folder. Release the mouse button and you will see the file indented at the same level as the `temp` folder.

## Video Tutorial

For a chance to see the file and folder creation process for yourself, try the following video link.

::: link
<a href="https://vimeo.com/1150164776?share=copy&fl=sv&fe=ci" target="_blank">&#9654;&#65039; VS Code: Creating new files and folders tutorial</a>
:::