import subprocess, time, xml.etree.ElementTree as ET
from playsound import playsound

def check_and_accept():
    subprocess.run(["adb", "shell", "uiautomator", "dump", "/sdcard/view.xml"])
    subprocess.run(["adb", "pull", "/sdcard/view.xml", "view.xml"])
    tree = ET.parse("view.xml")
    playsound('O:/Programming Files/Python/ADB Appointment Checker/notification_sound.mp3')
    for node in tree.iter("node"):
        text = node.attrib.get("text", "")
        if "OSI" in text:
            parts = text.split("|")
            count = int(parts[1].strip()) if len(parts) > 1 else 0
            #if count > 0:
            print("Number of OSI appointments:", count)
        if "VRI" in text:
                    parts = text.split("|")
                    count = int(parts[1].strip()) if len(parts) > 1 else 0
                    #if count > 0:
                    print("Number of VRI appointments:", count)
        if "OPI" in text:
                            parts = text.split("|")
                            count = int(parts[1].strip()) if len(parts) > 1 else 0
                            #if count > 0:
                            print("Number of OPI appointments:", count)
        if node.attrib.get("text") == "Accept":
            bounds = node.attrib["bounds"]  # "[x1,y1][x2,y2]"
            x1, y1, x2, y2 = map(int, bounds.replace("[", "").replace("]", ",").split(",")[:4])
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            subprocess.run(["adb", "shell", "input", "tap", str(cx), str(cy)])
            print("Accepted appointment, tapped:", cx, cy)
            return True
    return False

#while True:
#    check_and_accept()
#    time.sleep(30)
check_and_accept()

#adb shell input tap  1074 159 refresh
#adb shell input tap 1142 162 foward
#adb shell input tap 11 162 back