# 🚀 WhatsApp Auto Message Bot

<img src="https://img.icons8.com/color/96/000000/whatsapp.png" alt="WhatsApp Icon" width="60"/>  
A cross-platform Python bot to automate sending WhatsApp messages using GUI automation.  
Perfect for reminders, notifications, or automating repetitive WhatsApp messaging tasks.

---

## ✨ Features

- 🤖 **Automated Messaging**: Send messages to WhatsApp contacts or groups automatically.
- 🖥️ **No API/Browser Required**: Controls the WhatsApp Desktop app using GUI automation.
- ⚙️ **Configurable**: Easily set message content, recipients, and schedule.
- 💻 **Cross-platform**: Works on macOS (with `pyobjc`) and Windows.
- 🧠 **Planned: OpenAI Integration**: Generate smart replies or dynamic messages using OpenAI API (coming soon!)

---

## 🛠️ Requirements

- **WhatsApp Desktop** (must be installed and logged in)
- **Python 3.7+**

### Python Dependencies

Install via pip:

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
PyAutoGUI==0.9.54
PyGetWindow==0.0.9
PyMsgBox==1.0.9
pyobjc-core==11.0
pyobjc-framework-Cocoa==11.0
pyobjc-framework-Quartz==11.0
pyperclip==1.9.0
PyRect==0.2.0
PyScreeze==1.0.1
pytweening==1.2.0
rubicon-objc==0.5.0
```

---

## ⚡ Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/batmanrizz/whatsappautobot.git
   cd whatsappautobot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Open WhatsApp Desktop & Log In**
   - Make sure WhatsApp Desktop is running and you are logged in.

4. **Configure the Bot**
   - Edit the config variables in the script (e.g., contact name, message, schedule).

---

## 💡 Usage

### Simple Example

```python
from whatsappautobot import send_message

send_message(
    contact_name="Mom",
    message="Good morning! This is an automated message.",
)
```

### Scheduled Messaging

You can use Python's `schedule` or `time` modules to send messages at specific times.

---

## 🧩 How It Works

- Uses PyAutoGUI to locate WhatsApp window, search for contacts, and send messages by simulating keyboard and mouse events.
- On macOS, additional accessibility permissions may be required for automation to work.  
  Go to **System Preferences > Security & Privacy > Accessibility** and add Python.

---

## 🧠 OpenAI Integration (Coming Soon)

<img src="https://img.icons8.com/color/96/000000/openai.png" alt="OpenAI Icon" width="40"/>

- The bot will soon support generating smart replies or dynamic messages using OpenAI's API!
- Stay tuned for updates and usage instructions.

---

## ⚠️ Notes & Limitations

- The bot interacts with the WhatsApp Desktop GUI, so avoid using your computer while the script runs.
- Make sure the contact/group name matches exactly as it appears in WhatsApp.
- Works best with the English UI.
- For macOS, ensure all relevant `pyobjc` packages are installed and permissions granted.

---

## 📜 Disclaimer

- Use responsibly and do not spam.
- Respect WhatsApp’s terms of service.
- Provided for educational and personal automation purposes only.

---

## 🪪 License

MIT License

---

**Made with Python ❤️ by [batmanrizz](https://github.com/batmanrizz)**

<p align="left">
  <img src="https://img.icons8.com/color/48/000000/whatsapp.png" width="32"/>
  <img src="https://img.icons8.com/color/48/000000/python--v2.png" width="32"/>
  <img src="https://img.icons8.com/color/48/000000/openai.png" width="32"/>
</p>
