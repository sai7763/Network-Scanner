# 🛰️ Network Scanner (Mini Nmap Clone)

A simple Python-based tool that scans a target IP address to find open ports.  
It demonstrates basic networking concepts like socket programming and port scanning.  
⚠️ Use only on networks you own or have permission to test.

---

## 🌟 Features
- Scans common ports (1–1024)
- Detects open ports quickly using multithreading
- Easy to use — beginner-friendly script
- Works on Windows, Linux, and macOS

---

## 🧠 How It Works
The tool tries to connect to each port on the target IP address.  
If the connection is successful, the port is marked **OPEN**, otherwise it is **CLOSED** or filtered by a firewall.

---

## ⚙️ Installation & Run (Step-by-Step)

### 🪜 Step 1: Clone the repository
If you are using Git:
```bash
git clone https://github.com/sai7763/Network-Scanner.git
cd Network-Scanner
```
Or simply **download the ZIP** and extract it.

---

### 🪜 Step 2: (Optional) Create a virtual environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🪜 Step 3: Install dependencies
This project uses only Python’s built-in libraries, so no extra installation is needed.  
But if a `requirements.txt` is provided:
```bash
pip install -r requirements.txt
```

---

### 🪜 Step 4: Run the project
```bash
python scanner.py
```

You’ll be asked to enter the target IP:
```
Enter target IP: 192.168.1.1
```

Then it will start scanning all ports and print open ones.

---

## 🧾 Example Output
```
Scanning target: 192.168.1.1
[+] Port 22 is OPEN
[+] Port 80 is OPEN
[+] Port 443 is OPEN
Scan complete!
```

---

## 💡 Notes
- Run this tool **only on authorized networks**.
- Requires **Python 3.8+**
- You may need administrator privileges for scanning certain ports.
- To stop scanning anytime, press `Ctrl + C`.

---

## 🧰 Requirements
- Python 3.8 or newer
- Internet or LAN connection
- Basic understanding of IP addresses

---

## 🔧 Troubleshooting
- If the script freezes, check your internet/firewall settings.
- For faster results, limit the port range inside the code.
- If you get a “Permission denied” error, run the command prompt as Administrator.

---

## 👨‍💻 Author
**Muvvala Sai (sai7763)**  
GitHub: [https://github.com/sai7763](https://github.com/sai7763)

---

## ⚖️ License
This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it with attribution.

---

### ✅ Summary
| Section | Description |
|----------|--------------|
| Project | Network Scanner |
| Language | Python |
| Type | Cyber Security / Networking |
| License | MIT |
| Created by | Muvvala Sai |

