url = input("Enter website URL: ")

if "https" not in url:
    print("Warning: Website may not be secure!")

elif "login" in url or "verify" in url or "bank" in url:
    print("Possible phishing website detected!")

else:
    print("Website looks safe.")