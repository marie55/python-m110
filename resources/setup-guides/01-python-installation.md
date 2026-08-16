# Python Installation Guide
# دليل تثبيت بايثون

⏱️ **Estimated Time:** 15-20 minutes
⏱️ **الوقت المقدر:** 15-20 دقيقة

---

## Overview
## نظرة عامة

Python is the programming language we'll use throughout this course. Installing Python means you can write and run Python programs on your computer. We'll install Python 3.9 or newer, which includes everything you need to start programming.

بايثون هي لغة البرمجة التي سنستخدمها طوال هذا المقرر. تثبيت بايثون يعني أنك تستطيع كتابة وتشغيل برامج بايثون على حاسوبك. سنقوم بتثبيت بايثون 3.9 أو أحدث، والذي يتضمن كل ما تحتاجه للبدء في البرمجة.

---

## Prerequisites
## المتطلبات الأساسية

Before starting, make sure you have:
قبل البدء، تأكد من أن لديك:

- ✅ A computer with Windows 10/11, macOS 10.15+, or Linux
- ✅ حاسوب يعمل بنظام ويندوز 10/11، أو ماك 10.15+، أو لينكس

- ✅ Internet connection for downloading (about 30MB)
- ✅ اتصال بالإنترنت للتحميل (حوالي 30 ميجابايت)

- ✅ Administrator/admin access to install software
- ✅ صلاحيات المسؤول (Administrator) لتثبيت البرامج

- ✅ About 100MB free disk space
- ✅ حوالي 100 ميجابايت مساحة فارغة على القرص الصلب

---

## Installation Steps
## خطوات التثبيت

### 🪟 For Windows Users
### 🪟 لمستخدمي ويندوز

#### Step 1: Download Python
#### الخطوة 1: تحميل بايثون

1. Open your web browser and visit the official Python website:
   افتح متصفح الإنترنت وقم بزيارة موقع بايثون الرسمي:

   🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Click the large yellow button that says **"Download Python 3.x.x"** (the x.x will be the latest version number)
   انقر على الزر الأصفر الكبير الذي يقول **"Download Python 3.x.x"** (حيث x.x هو رقم أحدث إصدار)

3. The download will start automatically. Save the file to your **Downloads** folder
   سيبدأ التحميل تلقائياً. احفظ الملف في مجلد **التنزيلات**

📸 **Screenshot location:** Python.org homepage with the yellow download button highlighted

#### Step 2: Run the Installer
#### الخطوة 2: تشغيل برنامج التثبيت

⚠️ **CRITICAL STEP - READ CAREFULLY!**
⚠️ **خطوة حرجة - اقرأ بعناية!**

1. Navigate to your **Downloads** folder and find the file named `python-3.x.x.exe`
   انتقل إلى مجلد **التنزيلات** وابحث عن الملف المسمى `python-3.x.x.exe`

2. **Right-click** on the file and select **"Run as administrator"**
   **انقر بزر الماوس الأيمن** على الملف واختر **"Run as administrator"**

3. **BEFORE CLICKING ANYTHING ELSE:**
   **قبل النقر على أي شيء آخر:**

   ✅ **CHECK THE BOX** that says **"Add Python 3.x to PATH"** at the bottom of the window
   ✅ **حدد المربع** الذي يقول **"Add Python 3.x to PATH"** في أسفل النافذة

   This is the most important step! Without this, Python won't work properly.
   هذه هي الخطوة الأكثر أهمية! بدون هذا، لن يعمل بايثون بشكل صحيح.

4. Click **"Install Now"** (not "Customize installation")
   انقر على **"Install Now"** (وليس "Customize installation")

5. If Windows asks for permission, click **"Yes"**
   إذا طلب ويندوز الإذن، انقر على **"Yes"**

6. Wait for installation to complete (this takes 2-5 minutes)
   انتظر حتى يكتمل التثبيت (يستغرق هذا 2-5 دقائق)

7. When you see **"Setup was successful"**, click **"Close"**
   عندما ترى **"Setup was successful"**، انقر على **"Close"**

📸 **Screenshot locations:**
- Python installer with "Add Python to PATH" checkbox highlighted in red
- Installation progress bar
- "Setup was successful" screen

#### Step 3: Verify Installation
#### الخطوة 3: التحقق من التثبيت

1. Press **Windows key + R** to open the Run dialog
   اضغط على **مفتاح Windows + R** لفتح نافذة التشغيل

2. Type `cmd` and press **Enter** to open Command Prompt
   اكتب `cmd` واضغط **Enter** لفتح موجه الأوامر

3. In the black window that appears, type:
   في النافذة السوداء التي تظهر، اكتب:

   ```bash
   python --version
   ```

4. Press **Enter**. You should see something like:
   اضغط **Enter**. يجب أن ترى شيئاً مثل:

   ```
   Python 3.12.0
   ```

5. Also verify pip (Python's package installer) is working:
   تحقق أيضاً من أن pip (مثبت حزم بايثون) يعمل:

   ```bash
   pip --version
   ```

   You should see:
   يجب أن ترى:

   ```
   pip 23.2.1 from ... (python 3.12)
   ```

🎉 **Congratulations! Python is now installed on your Windows computer!**
🎉 **تهانينا! تم تثبيت بايثون الآن على حاسوبك الويندوز!**

---

### 🍎 For macOS Users
### 🍎 لمستخدمي ماك

#### Step 1: Check if Python is Already Installed
#### الخطوة 1: التحقق من وجود بايثون مسبقاً

macOS comes with Python 2.7, but we need Python 3.9+. Let's check:
يأتي نظام ماك مع بايثون 2.7، لكننا نحتاج بايثون 3.9+. دعنا نتحقق:

1. Press **Command ⌘ + Space** to open Spotlight search
   اضغط **Command ⌘ + Space** لفتح بحث Spotlight

2. Type **Terminal** and press **Enter**
   اكتب **Terminal** واضغط **Enter**

3. In Terminal, type:
   في Terminal، اكتب:

   ```bash
   python3 --version
   ```

4. If you see `Python 3.9` or higher, skip to verification. Otherwise, continue.
   إذا رأيت `Python 3.9` أو أعلى، انتقل إلى التحقق. وإلا، تابع.

#### Step 2: Download Python
#### الخطوة 2: تحميل بايثون

1. Visit the official Python website:
   قم بزيارة موقع بايثون الرسمي:

   🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Click **"Download Python 3.x.x"** button
   انقر على زر **"Download Python 3.x.x"**

3. Save the `.pkg` file to your **Downloads** folder
   احفظ ملف `.pkg` في مجلد **التنزيلات**

#### Step 3: Install Python
#### الخطوة 3: تثبيت بايثون

1. Open **Finder** and go to **Downloads**
   افتح **Finder** واذهب إلى **التنزيلات**

2. Double-click the `python-3.x.x-macos.pkg` file
   انقر مرتين على ملف `python-3.x.x-macos.pkg`

3. The installer will open. Click **"Continue"** through the introduction screens
   سيفتح المثبت. انقر **"Continue"** عبر شاشات المقدمة

4. **Read and agree** to the license (click **"Agree"**)
   **اقرأ ووافق** على الرخصة (انقر **"Agree"**)

5. Click **"Install"** (you may need to enter your Mac password)
   انقر **"Install"** (قد تحتاج لإدخال كلمة مرور الماك)

6. Wait for installation (2-5 minutes)
   انتظر التثبيت (2-5 دقائق)

7. Click **"Close"** when complete
   انقر **"Close"** عند الانتهاء

#### Step 4: Install Certificates (macOS Only)
#### الخطوة 4: تثبيت الشهادات (ماك فقط)

1. In Finder, press **Command ⌘ + Shift + G**
   في Finder، اضغط **Command ⌘ + Shift + G**

2. Type `/Applications/Python 3.x/` and press **Enter**
   اكتب `/Applications/Python 3.x/` واضغط **Enter**

3. Double-click **"Install Certificates.command"**
   انقر مرتين على **"Install Certificates.command"**

4. A Terminal window will open and run the command. Wait for it to finish.
   ستفتح نافذة Terminal وتنفذ الأمر. انتظر حتى ينتهي.

#### Step 5: Verify Installation
#### الخطوة 5: التحقق من التثبيت

1. Open Terminal (Command ⌘ + Space, type Terminal)
   افتح Terminal (Command ⌘ + Space، اكتب Terminal)

2. Type:
   اكتب:

   ```bash
   python3 --version
   ```

   You should see:
   يجب أن ترى:

   ```
   Python 3.12.0
   ```

3. Verify pip:
   تحقق من pip:

   ```bash
   pip3 --version
   ```

🎉 **Excellent! Python is now installed on your Mac!**
🎉 **ممتاز! تم تثبيت بايثون الآن على جهاز الماك الخاص بك!**

---

### 🐧 For Linux Users (Ubuntu/Debian)
### 🐧 لمستخدمي لينكس (Ubuntu/Debian)

#### Step 1: Update Package List
#### الخطوة 1: تحديث قائمة الحزم

1. Open Terminal (Ctrl + Alt + T)
   افتح Terminal (Ctrl + Alt + T)

2. Update your package list:
   حدث قائمة الحزم:

   ```bash
   sudo apt update
   ```

3. Enter your password when prompted
   أدخل كلمة المرور عند الطلب

#### Step 2: Install Python
#### الخطوة 2: تثبيت بايثون

1. Install Python 3 and pip:
   ثبت بايثون 3 و pip:

   ```bash
   sudo apt install python3 python3-pip python3-venv
   ```

2. Type **Y** and press **Enter** when asked to confirm
   اكتب **Y** واضغط **Enter** عند طلب التأكيد

3. Wait for installation (3-5 minutes)
   انتظر التثبيت (3-5 دقائق)

#### Step 3: Verify Installation
#### الخطوة 3: التحقق من التثبيت

1. Check Python version:
   تحقق من إصدار بايثون:

   ```bash
   python3 --version
   ```

2. Check pip version:
   تحقق من إصدار pip:

   ```bash
   pip3 --version
   ```

🎉 **Great! Python is installed on your Linux system!**
🎉 **رائع! تم تثبيت بايثون على نظام لينكس الخاص بك!**

---

## Testing Python
## اختبار بايثون

Let's make sure everything works by running a simple Python program:
دعنا نتأكد من أن كل شيء يعمل بتشغيل برنامج بايثون بسيط:

1. Open your terminal/command prompt
   افتح terminal/موجه الأوامر

2. Type `python` (Windows) or `python3` (Mac/Linux) and press Enter
   اكتب `python` (ويندوز) أو `python3` (ماك/لينكس) واضغط Enter

3. You should see something like:
   يجب أن ترى شيئاً مثل:

   ```
   Python 3.12.0 (main, Oct  2 2023, 00:00:00)
   [GCC 11.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

4. Type this Python code and press Enter:
   اكتب كود بايثون هذا واضغط Enter:

   ```python
   print("Hello, M110!")
   ```

5. You should see:
   يجب أن ترى:

   ```
   Hello, M110!
   ```

6. Type `exit()` or press **Ctrl + D** (Mac/Linux) or **Ctrl + Z then Enter** (Windows) to quit
   اكتب `exit()` أو اضغط **Ctrl + D** (ماك/لينكس) أو **Ctrl + Z ثم Enter** (ويندوز) للخروج

---

## Troubleshooting
## استكشاف الأخطاء وإصلاحها

### ❌ Problem: "python is not recognized" (Windows)
### ❌ المشكلة: "python is not recognized" (ويندوز)

This means Python wasn't added to PATH. Here's how to fix it:
هذا يعني أن بايثون لم يُضف إلى PATH. إليك كيفية إصلاحه:

1. Search for **"Environment Variables"** in Windows search
   ابحث عن **"Environment Variables"** في بحث ويندوز

2. Click **"Edit the system environment variables"**
   انقر على **"Edit the system environment variables"**

3. Click **"Environment Variables..."** button
   انقر على زر **"Environment Variables..."**

4. Under "System variables", find and select **"Path"**, then click **"Edit..."**
   تحت "System variables"، ابحث واختر **"Path"**، ثم انقر **"Edit..."**

5. Click **"New"** and add these two paths (replace X with your Python version):
   انقر **"New"** وأضف هذين المسارين (استبدل X بإصدار بايثون):

   ```
   C:\Users\YourUsername\AppData\Local\Programs\Python\Python3X\
   C:\Users\YourUsername\AppData\Local\Programs\Python\Python3X\Scripts\
   ```

6. Click **"OK"** on all windows
   انقر **"OK"** على جميع النوافذ

7. **Restart** Command Prompt and try again
   **أعد تشغيل** موجه الأوامر وحاول مرة أخرى

### ❌ Problem: "Permission denied" (Mac/Linux)
### ❌ المشكلة: "Permission denied" (ماك/لينكس)

Use `sudo` before the command:
استخدم `sudo` قبل الأمر:

```bash
sudo python3 your_script.py
```

### ❌ Problem: Old Python version
### ❌ المشكلة: إصدار بايثون قديم

If you have Python older than 3.9:
إذا كان لديك بايثون أقدم من 3.9:

- **Windows**: Uninstall old version from Control Panel first, then install new
  **ويندوز**: أزل الإصدار القديم من لوحة التحكم أولاً، ثم ثبت الجديد

- **Mac**: The new version will be available as `python3`
  **ماك**: الإصدار الجديد سيكون متاحاً كـ `python3`

- **Linux**: Update using your package manager
  **لينكس**: حدث باستخدام مدير الحزم

---

## Next Steps
## الخطوات التالية

✅ Python is installed! Now you're ready to:
✅ تم تثبيت بايثون! الآن أنت جاهز لـ:

1. **Install VS Code** - See [02-vscode-installation.md](02-vscode-installation.md)
   **تثبيت VS Code** - انظر [02-vscode-installation.md](02-vscode-installation.md)

2. **Set up Git** - See [03-git-installation.md](03-git-installation.md)
   **إعداد Git** - انظر [03-git-installation.md](03-git-installation.md)

3. **Create your first Python program!**
   **إنشاء أول برنامج بايثون لك!**

---

## Useful Links
## روابط مفيدة

- 📖 [Official Python Documentation](https://docs.python.org/3/)
- 📖 [وثائق بايثون الرسمية](https://docs.python.org/3/)

- 🎓 [Python for Beginners](https://www.python.org/about/gettingstarted/)
- 🎓 [بايثون للمبتدئين](https://www.python.org/about/gettingstarted/)

- 💬 [Python Community Discord](https://discord.gg/python)
- 💬 [مجتمع بايثون على Discord](https://discord.gg/python)

---

## Need Help?
## تحتاج مساعدة؟

If you encounter any issues:
إذا واجهت أي مشاكل:

1. Check the [Troubleshooting Guide](10-troubleshooting-common-issues.md)
   راجع [دليل استكشاف الأخطاء](10-troubleshooting-common-issues.md)

2. Ask Dr. Laila
   اسأل الدكتورة ليلى

3. Open a GitHub issue on the course repository
   افتح GitHub issue على مستودع المقرر

Remember: Everyone encounters installation issues. It's part of learning! Don't hesitate to ask for help.
تذكر: الجميع يواجه مشاكل في التثبيت. إنها جزء من التعلم! لا تتردد في طلب المساعدة.

---

*Last Updated: October 2025*
*آخر تحديث: أكتوبر 2025*