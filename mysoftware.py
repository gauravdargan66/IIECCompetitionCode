import os
import pyttsx3
print()
print("Hey! I'm Seri, Your Personal Desktop Assistant")
print("What's Your Name? ",end="")
name = input()
print()
print("Hey ",name,"!")
print("I'm just there to assist you, I have plenty of Applications from your Desktop.\nYou just have to tell me, What you want me to Launch for You.")
print()
print("-Google Chrome \n-Notepad \n-Microsoft Edge\n-Access\n-Adobe Acrobat Reader\n-Anaconda Navigator\n-Atom\n-GitHub Desktop\n-MySQL\n-Oracle VM Virtualbox\n-Alarms & Clock\n-Calculator\n-Camera\n-Cortana\n-Excel 2016\n-Groove Music\n-Mail\n-Maps\n-Messaging\n-Microsoft News\n-Microsoft Store\n-Movies & TV\n-Paint 3D\n-People\n-Photos\n-Powerpoint 2016\n-Settings\n-Snip & Sketch\n-TeamViewer\n-Tips\n-Weather\n-Windows Defender\n-Word 2016\n-Xbox Console Companion\n-Zoom")
print()
print("****************************************************************************")
print("Please use Run/Launch/Execute/Open keyword while typing application name!!")
print("To terminate, Please write Exit/Quit!! Move Ahead, Have Fun!")
print("****************************************************************************")
print()
t = True
while t:
    print("Which Application you want me to launch(from the list of applications given above)?",end="")
    p = input()
    q = (("run" in p) or ("Run" in p) or ("open" in p) or ("Open" in p) or ("execute" in p) or ("Execute" in p) or ("launch" in p) or ("Launch" in p) or ("start" in p)) 
    
    if q and  (("chrome" in p) or ("Chrome" in p) or ("google" in p) or ("Google" in p) or ("google chrome" in p) or ("Google Chrome" in p)):
        pyttsx3.speak("Launching Chrome, Please wait for a while")
        os.system("chrome")
    elif q and (("notepad" in p) or ("Notepad" in p) or ("editor" in p) or ("Editor" in p)):
        pyttsx3.speak("Launching Notepad, Please wait for a while")
        os.system("notepad")
    elif q and (("edge" in p) or ("Edge" in p) or ("microsoft edge" in p) or ("Microsoft Edge" in p)):
        pyttsx3.speak("Launching Microsoft Edge, Please wait for a while")
        os.system("msedge")
    elif q and (("access" in p) or ("Access" in p)):
        pyttsx3.speak("Launching Access, Please wait for a while")
        os.system("start MSaccess")
    elif q and (("adobe" in p) or ("Adobe" in p) or ("adobe acrobat" in p) or ("Adobe Acrobat" in p) or ("acrobat reader" in p) or ("Acrobat Reader" in p) or ("adobe acrobat reader" in p) or ("Adobe Acrobat Reader" in p)):
        pyttsx3.speak("Launching Acrobat Reader, Please wait for a while")
        os.system("start AcroRd32")
    elif q and (("anaconda" in p) or ("Anaconda" in p) or ("anaconda navigator" in p) or ("Anaconda Navigator" in p)):
        pyttsx3.speak("Launching Anaconda, Please wait for a while")
        os.system("start anaconda-navigator")
    elif q and (("atom" in p) or ("Atom" in p) or ("atom editor" in p) or ("Atom Editor" in p)):
        pyttsx3.speak("Launching Atom, please wait for a while")
        os.system("start atom")
    elif q and (("github" in p) or ("Github" in p) or ("GitHub" in p) or ("github desktop" in p) or ("Github Desktop" in p) or("GitHub Desktop" in p)):
        pyttsx3.speak("Launching GitHub Desktop, Please wait for a while")
        os.system("start GitHubDesktop")
    elif q and (("mysql" in p) or ("MySQL" in p) or ("MySql" in p)):
        pyttsx3.speak("Launching MySQL Workbench, Please wait for a while")
        os.system("start MySQLWorkbench")
    elif q and (("oracle vm virtualbox" in p) or ("Oracle VM Virtualbox" in p)):
        pyttsx3.speak("Launching Oracle VM Virtual Box, Please wait for a while")
        os.system("start VirtualBox")
    elif q and (("alarms and clock" in p) or ("Alarms & Clock" in p) or ("Alarms and Clock" in p)):
        pyttsx3.speak("Launching Alarms and Clock, Please wait for a while")
        os.system("start ms-clock:")
    elif q and (("calculator" in p) or ("Calculator" in p)):
        pyttsx3.speak("Launching Calculator, Please wait for a while")
        os.system("start calculator:")
    elif q and (("calendar" in p) or ("Calendar" in p)):
        pyttsx3.speak("Launching Calendar, Please wait for a while")
        os.system("start outlookcal:")
    elif q and (("camera" in p) or ("Camera" in p)):
        pyttsx3.speak("Launching Camera, Please wait for a while")
        os.system("start microsoft.windows.camera:")
    elif q and (("cortana" in p) or ("Cortana" in p)):
        pyttsx3.speak("Launching Cortana. Please wait for a while")
        os.system("start ms-cortana:")
    elif q and (("eclipse" in p) or ("Eclipse" in p)):
        pyttsx3.speak("Launching Eclipse, Please wait for a while")
        os.system("start eclipse")
    elif q and (("excel" in p) or ("Excel" in p) or ("excel 2016" in p) or ("Excel 2016" in p)):
        pyttsx3.speak("Launching Excel, Please wait for a while")
        os.system("start excel")
    elif q and (("music" in p) or ("groove music" in p) or ("Groove Music" in p)):
        pyttsx3.speak("Launching Groove Music, Please wait for a while")
        os.system("start mswindowsmusic:")
    elif q and (("mail" in p) or ("Mail" in p)):
        pyttsx3.speak("Launching Mail, Please wait for a while")
        os.system("start outlookmail:")
    elif q and (("maps" in p) or ("Maps" in p)):
        pyttsx3.speak("Launching Maps, Please wait for a while")
        os.system("start bingmaps:")
    elif q and (("messaging" in p) or ("Messaging" in p)):
        pyttsx3.speak("Launching Messaging, Please wait for a while")
        os.system("start ms-chat:")
    elif q and (("microsoft news" in p) or ("Microsoft News" in p) or ("news" in p) or ("News" in p)):
        pyttsx3.speak("Launching Microsoft News, Please wait for a while")
        os.system("start bingnews:")
    elif q and (("microsoft store" in p) or ("store" in p) or ("Microsoft Store" in p)):
        pyttsx3.speak("Launching Microsoft Store, Please wait for a while")
        os.system("start ms-windows-store:")
    elif q and (("movies & tv" in p) or ("Movies & TV" in p) or ("movies and tv" in p) or ("Movies and TV" in p)):
        pyttsx3.speak("Launching Movies and TV, Please wait for a while")
        os.system("start mswindowsvideo:")
    elif q and (("onenote" in p) or ("OneNote" in p) or ("Onenote" in p)):
        pyttsx3.speak("Launching Onenote, Please wait for a while")
        os.system("start onenote:")
    elif q and (("paint" in p) or ("Paint" in p) or ("paint 3d" in p) or ("Paint 3D" in p)):
        pyttsx3.speak("Launching Paint 3D, Please wait for a while")
        os.system("start ms-paint:")
    elif q and (("people" in p) or ("People" in p)):
        pyttsx3.speak("Launching People, Please wait for a while")
        os.system("start ms-people:")
    elif q and (("photos" in p) or ("Photos" in p)):
        pyttsx3.speak("Launching Photos, Please wait for a while")
        os.system("start ms-photos:")
    elif q and (("powerpoint" in p) or ("Powerpoint" in p) or ("powerpoint 2016" in p) or ("Powerpoint 2016" in p)):
        pyttsx3.speak("Launching Powerpoint, Please wait for a while")
        os.system("start powerpnt")
    elif q and (("settings" in p) or ("Settings" in p)):
        pyttsx3.speak("Launching Settings, Please wait for a while")
        os.system("start ms-settings:")
    elif q and (("snip and sketch" in p) or ("Snip and Sketch" in p) or ("snip & sketch" in p) or ("Snip & Sketch" in p)):
        pyttsx3.speak("Launching Snip and Sketch, Please wait for a while")
        os.system("start ms.ScreenSketch:")
    elif q and (("teamviewer" in  p) or ("Teamviewer" in p) or ("TeamViewer" in p)):
        pyttsx3.speak("Launching TeamViewer, Please wait for while")
        os.system("start TeamViewer")
    elif q and (("tips" in p) or ("Tips" in p)):
        pyttsx3.speak("Launching Tips, Please wait for a while")
        os.system("start ms-get-started:")
    elif q and (("weather" in p) or ("Weather" in p)):
        pyttsx3.speak("Launching Weather, Please wait for a while")
        os.system("start bingweather:")
    elif q and (("windows defender" in p) or ("Windows Defender" in p)):
        pyttsx3.speak("Launching Windows Defender, Please wait for a while")
        os.system("start windowsdefender:")
    elif q and (("word 2016" in p) or ("Word 2016" in p) or ("word" in p) or ("Word" in p)):
        pyttsx3.speak("Launching Word, Please wait for a while")
        os.system("start winword")
    elif q and (("xbox" in p) or ("Xbox" in p) or ("xbox console companion" in p) or ("Xbox Console Companion" in p)):
        pyttsx3.speak("Launching Xbox Console Companion, Please wait for a while")
        os.system("start xbox:")
    elif q and (("zoom" in p) or ("Zoom" in p)):
        pyttsx3.speak("Launching Zoom, Please wait fro a while")
        os.system("start zoom")
    elif (("exit" in p) or ("quit" in p) or ("Exit" in p) or ("Quit" in p)):
        t = False
        print("Thank You! For using, I hope you have a great time with Me.")
    else:
        print("Sorry! I won't be able to open this application.\nEither You have not downloaded this application or It doesn't supported by me.\nI Hope you have a Great Time with Me!")
        t = False
