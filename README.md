# 🔒 SafeSight  
**SafeSight** is a lightweight Website Security Header Checker written in Python. Designed for students, developers, and cybersecurity enthusiasts, it helps you quickly verify if critical HTTP security headers are present on a website, providing insights into web security posture.  

---

## 🌐 What is SafeSight?  

SafeSight allows you to analyze HTTP response headers from any website and check whether important security headers are implemented. It highlights which headers are present and which are missing, giving users a clear understanding of potential security risks. Results can also be saved for future reference.  

---

## 🚀 Features  
- Check for commonly expected security headers:  
  - Content-Security-Policy  
  - X-Frame-Options  
  - X-Content-Type-Options  
  - Strict-Transport-Security  
  - Referrer-Policy  
  - Permissions-Policy  
  - Expect-CT  
  - Feature-Policy (deprecated but still detected)  
- Supports custom header checks (user-defined).  
- Color-coded terminal output for easy readability.  
- Save results in **JSON** format.  
- Beginner-friendly and interactive terminal interface.  
- Works on Linux, macOS, and Windows.  

---

## 📥 Installation  

**Prerequisites**  

Make sure Python 3 and the required libraries are installed:  

```bash
sudo apt update
sudo apt install python3 pip
pip install requests colorama pyfiglet
```
### Clone the repository
```git clone https://github.com/FathimaLamia/SafeSight.git
cd SafeSight
```

### Run the tool
```python 
python3 safesight.py
```
---

## 📝 Usage Instructions

1. Start the tool:
   Run `python3 safesight.py`
   
3. Enter the target website (include http:// or https://).
   
4. Choose options:
   - View the default security headers being checked.
   - Add your own custom headers to test.
   - Save results to a file in JSON format.

---

# 🔍 Output Sample

## SafeSight

 🌐 👁  Website Header Checker  🔒 🛡

- Enter website URL (with http:// or https://): https://example.com

- Do you want to see the default security headers that will be checked? (y/n):

- Checked headers for https://example.com:
    Present headers (3):
     - X-Frame-Options
     - Referrer-Policy
     - Strict-Transport-Security

- Missing headers (5):
   - Content-Security-Policy
   - X-Content-Type-Options
   - Permissions-Policy
   - Expect-CT
   - Feature-Policy

📁 Files saved as:
`header_check_results.json`

---

## 🛠️ How It Works
| Feature               | Description                                              |
| --------------------- | -------------------------------------------------------- |
| Header detection      | Fetches website response headers using HEAD/GET requests |
| Security headers list | Verifies presence of key HTTP security headers           |
| Custom header checks  | Allows user to specify additional headers                |
| JSON output           | Saves results to structured file for reuse               |
| Interactive CLI       | Simple prompts for flexible scanning                     |

---

## ⚠️ Legal & Ethical Notice

Ethical Usage: Use SafeSight only on websites you own or have explicit permission to test.

Liability: The author is not responsible for misuse or illegal activities.

---

## 🧑‍💻 Author
Lamia Lathif
A passionate developer building simple yet powerful cybersecurity tools.

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome! Feel free to fork this project and help enhance SafeSight.
