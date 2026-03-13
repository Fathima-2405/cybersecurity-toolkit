from flask import Flask, request
import os

app = Flask(__name__)

# HOME PAGE
@app.route("/")
def home():
    return """
    <h1>Cybersecurity Toolkit</h1>
    <p>Select a tool:</p>

    <ul>
    <li><a href="/password">Password Strength Checker</a></li>
    <li><a href="/keylogger">Keylogger Detection</a></li>
    <li><a href="/phishing">Phishing Website Detector</a></li>
    <li><a href="/encryption">File Encryption Tool</a></li>
    <li><a href="/sniffer">Network Packet Sniffer</a></li>
    </ul>
    """

# PASSWORD CHECKER
@app.route("/password", methods=["GET","POST"])
def password():
    result = ""

    if request.method == "POST":
        pwd = request.form["password"]

        if len(pwd) < 6:
            result = "Weak Password"
        elif len(pwd) < 10:
            result = "Medium Password"
        else:
            result = "Strong Password"

    return f"""
    <h2>Password Strength Checker</h2>

    <form method="POST">
        Enter Password:
        <input type="text" name="password">
        <button type="submit">Check</button>
    </form>

    <h3>{result}</h3>

    <br>
    <a href="/">Go Back</a>
    """

# PHISHING DETECTOR
@app.route("/phishing", methods=["GET","POST"])
def phishing():
    result = ""

    if request.method == "POST":
        url = request.form["url"]

        if "login" in url or "bank" in url or "verify" in url:
            result = "⚠ Possible Phishing Website!"
        else:
            result = "✅ Website looks Safe"

    return f"""
    <h2>Phishing Website Detector</h2>

    <form method="POST">
        Enter Website URL:
        <input type="text" name="url">
        <button type="submit">Check</button>
    </form>

    <h3>{result}</h3>

    <br>
    <a href="/">Go Back</a>
    """

# ENCRYPTION TOOL
@app.route("/encryption", methods=["GET","POST"])
def encryption():
    encrypted = ""
    decrypted = ""

    if request.method == "POST":
        message = request.form["message"]

        encrypted = "".join(chr(ord(c)+3) for c in message)
        decrypted = "".join(chr(ord(c)-3) for c in encrypted)

    return f"""
    <h2>File Encryption Tool</h2>

    <form method="POST">
        Enter Message:
        <input type="text" name="message">
        <button type="submit">Encrypt</button>
    </form>

    <p>Encrypted Message: {encrypted}</p>
    <p>Decrypted Message: {decrypted}</p>

    <br>
    <a href="/">Go Back</a>
    """

# KEYLOGGER DETECTION (DEMO)
@app.route("/keylogger")
def keylogger():
    return """
    <h2>Keylogger Detection</h2>
    <p>Scanning system processes...</p>
    <p>✅ No keylogger detected.</p>
    <br>
    <a href="/">Go Back</a>
    """

# PACKET SNIFFER (DEMO)
@app.route("/sniffer")
def sniffer():
    return """
    <h2>Network Packet Sniffer</h2>

    <p>Source IP: 192.168.1.10</p>
    <p>Destination IP: 142.250.183.14</p>
    <p>Protocol: TCP</p>
    <p>Data: Sample Packet Data</p>

    <p>Packet captured successfully!</p>

    <br>
    <a href="/">Go Back</a>
    """

# RUN SERVER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)