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
print("****************************HERE IS THE LIST OF APPLICATIONS*******************************")
print("-Google Chrome \n-Notepad \n-Microsoft Edge\n-MS Access\n-Adobe Acrobat Reader\n-Anaconda Navigator\n-Atom\n-GitHub Desktop\n-MySQL\n-Oracle VM Virtualbox\n-Alarms & Clock\n-Calculator\n-Camera\n-Candy Crush Saga\n-Cortana\n-MS Excel 2016\n-Groove Music\n-Mail\n-Maps\n-Messaging\n-Microsoft News\n-Microsoft Store\n-Movies & TV\n-Paint 3D\n-People\n-Photos\n-MS Powerpoint 2016\n-Settings\n-Snip & Sketch\n-Spotify Music\n-TeamViewer\n-Tips\n-Weather\n-Windows Defender\n-MS Word 2016\n-Xbox Console Companion\n-Zoom")
print()
print("*******************************************************************************************")
print("Please use Run/Launch/Execute/Open keyword while typing application name!!")
print("To terminate, Please write Exit/Quit!! Move Ahead, Have Fun!")
print("*******************************************************************************************")
print()
while True:
    print("Which Application you want me to launch(from the list of applications given above)?",end="")
    p = input()
    q = (("run" in p) or ("Run" in p) or ("open" in p) or ("Open" in p) or ("execute" in p) or ("Execute" in p) or ("launch" in p) or ("Launch" in p) or ("start" in p)) 
    
    if q and  (("chrome" in p) or ("Chrome" in p) or ("google" in p) or ("Google" in p) or ("google chrome" in p) or ("Google Chrome" in p)):
        pyttsx3.speak("Launching Chrome, Please wait for a while")
        os.system("chrome")
    
    elif q and (("notepad" in p) or ("Notepad" in p) or ("editor" in p) or ("Editor" in p)):
        pyttsx3.speak("Launching Notepad, Please wait for a while")
        os.system("notepad")
    
    elif q and (("microsoft" in p) or ("Microsoft" in p)):
        if (("edge" in p) or ("Edge" in p)):
            pyttsx3.speak("Launching Microsoft Edge, Please wait for a while")
            os.system("msedge")
        
        elif (("news" in p) or ("News" in p)):
            pyttsx3.speak("Launching Microsoft News, Please wait for a while")
            os.system("start bingnews:")
        
        elif (("store" in p) or ("Store" in p)):
            pyttsx3.speak("Launching Microsoft Store, Please wait for a while")
            os.system("start ms-windows-store:")

        else:
            print("Sorry! I won't be able to launch this application.\n-Either You have not downloaded this application\n-Or It doesn't configured in me.\n-And it might be possible that you are not putting the correct name\nI Hope you have a Great Time with Me!")
    
    elif q and (("ms" in p) or ("MS" in p) or ("microsoft" in p) or ("Microsoft" in p)):
        if (("access" in p) or ("Access" in p)):
            pyttsx3.speak("Launching MS Access, Please wait for a while")
            os.system("start MSaccess")
        
        elif (("excel" in p) or ("Excel" in p) or ("excel 2016" in p) or ("Excel 2016" in p)):
            pyttsx3.speak("Launching MS Excel, Please wait for a while")
            os.system("start excel")
        
        elif (("powerpoint" in p) or ("Powerpoint" in p) or ("powerpoint 2016" in p) or ("Powerpoint 2016" in p)):
            pyttsx3.speak("Launching MS Powerpoint, Please wait for a while")
            os.system("start powerpnt")
        
        elif (("word 2016" in p) or ("Word 2016" in p) or ("word" in p) or ("Word" in p)):
            pyttsx3.speak("Launching MS Word, Please wait for a while")
            os.system("start winword")

        else:
            print("Sorry! I won't be able to launch this application.\n-Either You have not downloaded this application\n-Or It doesn't configured in me.\n-And it might be possible that you are not putting the correct name\nI Hope you have a Great Time with Me!")

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
    
    elif q and (("candy crush saga" in p) or ("Candy Crush Saga" in p) or ("candy crush" in p) or ("Candy Crush" in p)):
        pyttsx3.speak("Launching Candy Crush Saga, Please wait for a while")
        os.system("start candycrushsaga:")
    
    elif q and (("cortana" in p) or ("Cortana" in p)):
        pyttsx3.speak("Launching Cortana. Please wait for a while")
        os.system("start ms-cortana:")
    
    elif q and (("eclipse" in p) or ("Eclipse" in p)):
        pyttsx3.speak("Launching Eclipse, Please wait for a while")
        os.system("start eclipse")
    
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
    
    elif q and (("settings" in p) or ("Settings" in p)):
        pyttsx3.speak("Launching Settings, Please wait for a while")
        os.system("start ms-settings:")
    
    elif q and (("snip and sketch" in p) or ("Snip and Sketch" in p) or ("snip & sketch" in p) or ("Snip & Sketch" in p)):
        pyttsx3.speak("Launching Snip and Sketch, Please wait for a while")
        os.system("start ms.ScreenSketch:")
    
    elif q and (("spotify music" in p) or ("Spotify Music" in p) or ("spotify" in p) or ("Spotify" in p)):
        pyttsx3.speak("Launching Spotify, Please wait for a while")
        os.system("start spotify")
    
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
    
    elif q and (("xbox" in p) or ("Xbox" in p) or ("xbox console companion" in p) or ("Xbox Console Companion" in p)):
        pyttsx3.speak("Launching Xbox Console Companion, Please wait for a while")
        os.system("start xbox:")
    
    elif q and (("zoom" in p) or ("Zoom" in p)):
        pyttsx3.speak("Launching Zoom, Please wait fro a while")
        os.system("start zoom")
    
    elif (("exit" in p) or ("quit" in p) or ("Exit" in p) or ("Quit" in p)):
        break
    
    else:
        print("Sorry! I won't be able to launch this application.\n-Either You have not downloaded this application\n-Or It doesn't configured in me.\n-And it might be possible that you are not putting the correct name\nI Hope you have a Great Time with Me!")
        t = False
print("Thank You! For using, I hope you have a great time with Me.")