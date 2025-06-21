# **Hare Apparent Calculator**
#### * For use with Preston, the Vanisher decks in Magic the Gathering

Want to make hundreds or even thousands of rabbits but don't want to be that guy at the commander pod taking 30 minutes to calculate how much is made after multiple flicker and repeat triggers? Then this calculator is for you!

![Example](/example.png "Example")

# **Installing/Running**
Very verbose to help out all the non-nerds out there.
## Desktop (Windows, Mac, Linux)</br>
1. Download `hare_apparent_calc.py` from this repo and move to wherever you'd like to keep it</br>
2. Install the latest version of [Python](https://www.python.org/downloads/)
3. Open your favorite terminal application (Command Prompt, Powershell, etc.)</br>
4. (Only for first run) Install dependencies using the terminal with the following commands:</br>
`python -m pip install rich` *Used to display a pretty output in the terminal*</br>
5. Change the directory of your terminal to wherever you downloaded `hare_apparent_calc.py` using the following command:</br>
`cd "C:\Your\Path\Here"` (do not include the file name)
6. Run the file with the command and enjoy!:</br>
`python hare_apparent_calc.py`</br>
## Android</br>
1. Download `hare_apparent_calc.py` from this repo and move to wherever you'd like to keep it</br>
2. Install [Termux](https://termux.dev/en/).</br>
*DO NOT INSTALL THROUGH PLAY STORE. The easiest way would be through [F-Droid](https://f-droid.org/en/packages/com.termux/) which will auto-update for you as well as handle the install of the APK. If you're comfortable installing your own APK files, follow their instructions on their [GitHub](https://github.com/termux/termux-app#github)*
3. (Only for first run) Open Termux and run the following commands:</br>
`pkg install python` *Installs Python (Fair warning: ~600 MB of space)*</br>
`pkg up openssl` *Fixes an issue I ran into running the next command where it wouldn't install. When coming up to any prompts during this command running regarding updating configs. Input `N`*</br>
`python -m pip install rich` *Used to display a pretty output in the terminal*</br>
4. Exit Termux and kill the process in your notifaction tray.</br>
*More advanced users, change the directory using `cd` to wherever you have downloaded `hare_apparent_calc.py` and go to Step 7.</br>
However, the directions below are faster after these initial setup instructions.*</br>
5. Open your Android file manager and navigate to wherever you downloaded `hare_apparent_calc.py`</br>
*"Files" on Samsung phones for example*</br>
6. Open `hare_apparent_calc.py` and select "Termux" when asked what app to open with. Then select "Open Directory".</br>
7. Run the file with the command and enjoy!:</br>
`python hare_apparent_calc.py`</br>
*Remember to exit the Termux session from the notification panel when done*
## iPhone</br>
*Warning: I have not tested this because I don't have an iPhone*
1. Download `hare_apparent_calc.py` from this repo and move to wherever you'd like to keep it</br>
2. Install [iSH Shell](https://apps.apple.com/us/app/ish-shell/id1436902243)
3. Open iSH Shell and run the following commands:</br>
(Only for first run) `apk add python3` *Installs Python (Fair warning: ~600 MB of space)*</br>
(Only for first run) `apk add py3-pip` *Installs pip which Python uses to install dependency packages*</br>
(Only for first run) `python3 -m pip install rich` *Used to display a pretty output in the terminal*</br>
`mkdir app_dir` *Makes a directory which we will then use...*</br>
`mount -t ios . app_dir` *...to find our file we downloaded*</br>
5. The last command should open up the GUI to choose a directory from the Files app. Navigate to the directory where `hare_apparent_calc.py` is and select it.</br>
7. Run the file with the command and enjoy!:</br>
`python3 hare_apparent_calc.py`</br>