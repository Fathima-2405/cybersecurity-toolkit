print("=== Cybersecurity Toolkit ===")
print("1. Password Strength Checker")
print("2. Keylogger Detection")
print("3. Phishing Website Detector")
print("4. File Encryption / Decryption")
print("5. Network Packet Sniffer")
print("6. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    import password_checker
elif choice == "2":
    import keylogger_detection
elif choice == "3":
    import phishing_detector
elif choice == "4":
    import encryption
elif choice == "5":
    import packet_sniffer
else:
    print("Exiting...")