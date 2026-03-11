print("Scanning system for possible keyloggers...")

suspicious_programs = ["keylogger.exe", "spyware.exe", "keylog.exe"]

running_programs = ["chrome.exe", "explorer.exe", "notepad.exe"]

found = False

for program in running_programs:
    if program in suspicious_programs:
        print("Warning! Possible keylogger detected:", program)
        found = True

if not found:
    print("No keylogger detected.")