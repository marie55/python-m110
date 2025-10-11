# Troubleshooting Common Issues
# استكشاف المشاكل الشائعة وإصلاحها

⏱️ **Estimated Time:** As needed
⏱️ **الوقت المقدر:** حسب الحاجة

---

## Overview
## نظرة عامة

This guide covers solutions to common problems you might encounter while setting up and using your Python development environment. Use this as a reference when something isn't working correctly.

يغطي هذا الدليل حلولاً للمشاكل الشائعة التي قد تواجهها أثناء إعداد واستخدام بيئة تطوير Python الخاصة بك. استخدم هذا كمرجع عندما لا يعمل شيء بشكل صحيح.

### How to Use This Guide
### كيفية استخدام هذا الدليل

1. **Find your problem** - Use the table of contents
   **ابحث عن مشكلتك** - استخدم جدول المحتويات

2. **Try the solutions** - Follow steps in order
   **جرب الحلول** - اتبع الخطوات بالترتيب

3. **Still stuck?** - Contact your instructor
   **لا تزال عالقاً؟** - اتصل بمدرسك

---

## Table of Contents
## جدول المحتويات

- [Python Installation Issues](#python-installation-issues)
- [VS Code Problems](#vs-code-problems)
- [Git and GitHub Issues](#git-and-github-issues)
- [Virtual Environment Problems](#virtual-environment-problems)
- [Python Extension Issues](#python-extension-issues)
- [File and Path Problems](#file-and-path-problems)
- [Terminal and Command Line Issues](#terminal-and-command-line-issues)
- [Running Code Problems](#running-code-problems)
- [Package Installation Issues](#package-installation-issues)
- [Character Encoding Problems](#character-encoding-problems)
- [Permission and Access Errors](#permission-and-access-errors)
- [Performance and Speed Issues](#performance-and-speed-issues)

---

## Python Installation Issues
## مشاكل تثبيت Python

### ❌ Problem: "python is not recognized" (Windows)
### ❌ المشكلة: "python is not recognized" (ويندوز)

**Symptom:** When you type `python` in Command Prompt, you see:
**العَرَض:** عندما تكتب `python` في موجه الأوامر، ترى:

```
'python' is not recognized as an internal or external command
```

**Cause:** Python is not in your system PATH
**السبب:** Python ليس في PATH النظام الخاص بك

**Solution 1: Reinstall Python with PATH**
**الحل 1: أعد تثبيت Python مع PATH**

1. Uninstall Python:
   أزل Python:

   - Control Panel → Programs → Uninstall a program
   - Control Panel → Programs → Uninstall a program

   - Find Python → Uninstall
   - ابحث عن Python → أزل

2. Reinstall Python:
   أعد تثبيت Python:

   - Download from python.org
   - حمّل من python.org

   - **IMPORTANT:** Check "Add Python to PATH" during installation
   - **مهم:** حدد "Add Python to PATH" أثناء التثبيت

**Solution 2: Add Python to PATH Manually**
**الحل 2: أضف Python إلى PATH يدوياً**

1. Find Python installation location:
   ابحث عن موقع تثبيت Python:

   - Usually: `C:\Users\YourName\AppData\Local\Programs\Python\Python312\`
   - عادةً: `C:\Users\YourName\AppData\Local\Programs\Python\Python312\`

2. Add to PATH:
   أضف إلى PATH:

   - Search Windows for "Environment Variables"
   - ابحث في ويندوز عن "Environment Variables"

   - Click "Edit the system environment variables"
   - انقر "Edit the system environment variables"

   - Click "Environment Variables"
   - انقر "Environment Variables"

   - Under "System variables", find and select "Path"
   - تحت "System variables"، ابحث واختر "Path"

   - Click "Edit"
   - انقر "Edit"

   - Click "New"
   - انقر "New"

   - Add two paths (replace Python312 with your version):
   - أضف مسارين (استبدل Python312 بإصدارك):

     ```
     C:\Users\YourName\AppData\Local\Programs\Python\Python312\
     C:\Users\YourName\AppData\Local\Programs\Python\Python312\Scripts\
     ```

3. Click "OK" on all windows
   انقر "OK" على جميع النوافذ

4. **Restart Command Prompt** and try again
   **أعد تشغيل موجه الأوامر** وحاول مرة أخرى

### ❌ Problem: "python3: command not found" (Mac/Linux)
### ❌ المشكلة: "python3: command not found" (ماك/لينكس)

**Cause:** Python 3 is not installed
**السبب:** Python 3 غير مثبت

**Solution:**

**Mac:**
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Or download from python.org
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### ❌ Problem: Old Python Version
### ❌ المشكلة: إصدار Python قديم

**Check version:**
**تحقق من الإصدار:**

```bash
python --version    # Windows
python3 --version   # Mac/Linux
```

**If version is older than 3.9:**
**إذا كان الإصدار أقدم من 3.9:**

1. Uninstall old version
   أزل الإصدار القديم

2. Download latest from python.org
   حمّل الأحدث من python.org

3. Install following the guide
   ثبت باتباع الدليل

---

## VS Code Problems
## مشاكل VS Code

### ❌ Problem: VS Code Won't Open
### ❌ المشكلة: VS Code لا يفتح

**Windows:**
**ويندوز:**

1. Right-click VS Code icon → "Run as administrator"
   انقر بالزر الأيمن على أيقونة VS Code → "Run as administrator"

2. If still doesn't work, reinstall VS Code
   إذا لم يعمل، أعد تثبيت VS Code

**Mac:**
**ماك:**

1. Check Security & Privacy settings:
   تحقق من إعدادات الأمان والخصوصية:

   - System Preferences → Security & Privacy
   - System Preferences → Security & Privacy

   - Click "Open Anyway" if prompted
   - انقر "Open Anyway" إذا طُلب

**Linux:**
**لينكس:**

```bash
# Try running from terminal
code

# If error, reinstall
sudo snap remove code
sudo snap install code --classic
```

### ❌ Problem: "code" Command Not Found (Terminal)
### ❌ المشكلة: أمر "code" غير موجود (الطرفية)

**Mac:**
**ماك:**

1. Open VS Code
   افتح VS Code

2. Press **⌘ + Shift + P**
   اضغط **⌘ + Shift + P**

3. Type: "Shell Command: Install 'code' command in PATH"
   اكتب: "Shell Command: Install 'code' command in PATH"

4. Press Enter
   اضغط Enter

**Linux:**
**لينكس:**

Add to your `.bashrc` or `.zshrc`:
أضف إلى `.bashrc` أو `.zshrc`:

```bash
export PATH="$PATH:/usr/share/code/bin"
```

Then restart terminal.
ثم أعد تشغيل الطرفية.

### ❌ Problem: VS Code Extensions Not Installing
### ❌ المشكلة: إضافات VS Code لا تثبت

**Solution:**
**الحل:**

1. Check internet connection
   تحقق من اتصال الإنترنت

2. Clear extension cache:
   امسح ذاكرة التخزين المؤقت للإضافات:

   ```bash
   # Close VS Code first
   # Windows
   rd /s %USERPROFILE%\.vscode\extensions

   # Mac/Linux
   rm -rf ~/.vscode/extensions
   ```

3. Restart VS Code
   أعد تشغيل VS Code

4. Try installing again
   حاول التثبيت مرة أخرى

---

## Git and GitHub Issues
## مشاكل Git و GitHub

### ❌ Problem: "git is not recognized" (Windows)
### ❌ المشكلة: "git is not recognized" (ويندوز)

**Cause:** Git not in PATH or not installed
**السبب:** Git ليس في PATH أو غير مثبت

**Solution:**
**الحل:**

1. Restart computer (PATH updates need restart)
   أعد تشغيل الكمبيوتر (تحديثات PATH تحتاج إعادة تشغيل)

2. If still not working, reinstall Git:
   إذا لم يعمل، أعد تثبيت Git:

   - Download from git-scm.com
   - حمّل من git-scm.com

   - During installation, select "Git from the command line and also from 3rd-party software"
   - أثناء التثبيت، اختر "Git from the command line and also from 3rd-party software"

### ❌ Problem: "Permission denied (publickey)" when cloning
### ❌ المشكلة: "Permission denied (publickey)" عند النسخ

**Cause:** Trying to use SSH without SSH keys
**السبب:** محاولة استخدام SSH بدون مفاتيح SSH

**Solution: Use HTTPS instead**
**الحل: استخدم HTTPS بدلاً من ذلك**

Make sure your clone URL starts with `https://`:
تأكد من أن رابط النسخ يبدأ بـ `https://`:

```bash
# Correct
git clone https://github.com/username/repo.git

# Wrong (requires SSH keys)
git clone git@github.com:username/repo.git
```

### ❌ Problem: "Authentication failed" when cloning
### ❌ المشكلة: "Authentication failed" عند النسخ

**For private repositories:**
**للمستودعات الخاصة:**

**Windows:** Git Credential Manager will pop up
**ويندوز:** سيظهر Git Credential Manager

- Sign in with your GitHub account
- سجل دخول بحساب GitHub الخاص بك

**Mac/Linux:** Use Personal Access Token
**ماك/لينكس:** استخدم رمز الوصول الشخصي

1. Generate token at: https://github.com/settings/tokens
   أنشئ رمزاً في: https://github.com/settings/tokens

2. Use token as password when prompted
   استخدم الرمز ككلمة مرور عند الطلب

### ❌ Problem: "Merge conflict" when pulling
### ❌ المشكلة: "تعارض دمج" عند السحب

**Cause:** Local changes conflict with remote changes
**السبب:** التغييرات المحلية تتعارض مع التغييرات البعيدة

**Solution 1: Discard local changes**
**الحل 1: تجاهل التغييرات المحلية**

```bash
git reset --hard
git pull
```

⚠️ **Warning:** This deletes all your local changes!
⚠️ **تحذير:** هذا يحذف جميع تغييراتك المحلية!

**Solution 2: Save changes first**
**الحل 2: احفظ التغييرات أولاً**

```bash
git stash        # Save changes temporarily
git pull         # Get remote changes
git stash pop    # Reapply your changes
```

---

## Virtual Environment Problems
## مشاكل البيئة الافتراضية

### ❌ Problem: "venv is not recognized" (Windows)
### ❌ المشكلة: "venv is not recognized" (ويندوز)

**Solution:**
**الحل:**

Try using `python3` instead of `python`:
حاول استخدام `python3` بدلاً من `python`:

```bash
python3 -m venv venv
```

Or use full path:
أو استخدم المسار الكامل:

```bash
py -m venv venv
```

### ❌ Problem: "activate cannot be loaded" (Windows PowerShell)
### ❌ المشكلة: "activate cannot be loaded" (Windows PowerShell)

**Error message:**
**رسالة الخطأ:**

```
venv\Scripts\activate : File cannot be loaded because running scripts is disabled
```

**Cause:** PowerShell execution policy
**السبب:** سياسة تنفيذ PowerShell

**Solution:**
**الحل:**

1. Open PowerShell **as Administrator**
   افتح PowerShell **كمسؤول**

2. Run:
   نفّذ:

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. Type `Y` and press Enter
   اكتب `Y` واضغط Enter

4. Close and reopen PowerShell (normal mode)
   أغلق وأعد فتح PowerShell (الوضع العادي)

5. Try activating again
   حاول التفعيل مرة أخرى

### ❌ Problem: venv activated but pip installs globally
### ❌ المشكلة: venv مفعّل لكن pip يثبت عالمياً

**Check if venv is really active:**
**تحقق إذا كان venv نشطاً فعلاً:**

```bash
pip --version
```

**Should show path with venv:**
**يجب أن يظهر مساراً مع venv:**

```
pip 23.2.1 from .../python-m110/venv/lib/... (python 3.12)
```

**If path doesn't include venv:**
**إذا لم يتضمن المسار venv:**

1. Deactivate and reactivate:
   ألغِ التفعيل وأعد التفعيل:

   ```bash
   deactivate
   # Then activate again based on your OS
   ```

2. Check Python interpreter in VS Code:
   تحقق من مفسر Python في VS Code:

   - Ctrl/⌘ + Shift + P → "Python: Select Interpreter"
   - Ctrl/⌘ + Shift + P → "Python: Select Interpreter"

   - Choose the one with venv
   - اختر الذي يحتوي على venv

### ❌ Problem: "Permission denied" when creating venv (Mac/Linux)
### ❌ المشكلة: "Permission denied" عند إنشاء venv (ماك/لينكس)

**Solution:**
**الحل:**

```bash
# Make sure you're in a directory you own
cd ~/Documents/Dev

# Create venv
python3 -m venv venv

# If still fails, check permissions
ls -la

# Fix permissions if needed
chmod +x venv/bin/activate
```

---

## Python Extension Issues
## مشاكل إضافة Python

### ❌ Problem: No Python interpreter found
### ❌ المشكلة: لم يتم العثور على مفسر Python

**Solution:**
**الحل:**

1. Make sure Python is installed:
   تأكد من تثبيت Python:

   ```bash
   python --version
   ```

2. Reload VS Code:
   أعد تحميل VS Code:

   - Ctrl/⌘ + Shift + P
   - Ctrl/⌘ + Shift + P

   - Type: "Developer: Reload Window"
   - اكتب: "Developer: Reload Window"

3. Manually select interpreter:
   اختر المفسر يدوياً:

   - Ctrl/⌘ + Shift + P
   - Ctrl/⌘ + Shift + P

   - Type: "Python: Select Interpreter"
   - اكتب: "Python: Select Interpreter"

   - Choose from list or enter path
   - اختر من القائمة أو أدخل المسار

### ❌ Problem: IntelliSense not working
### ❌ المشكلة: IntelliSense لا يعمل

**Solution:**
**الحل:**

1. Check Pylance is installed:
   تحقق من تثبيت Pylance:

   - Extensions → Search "Pylance"
   - Extensions → ابحث عن "Pylance"

   - Install if not present
   - ثبت إذا لم يكن موجوداً

2. Wait 10-20 seconds after opening file
   انتظر 10-20 ثانية بعد فتح الملف

3. Check Output panel:
   تحقق من لوحة المخرجات:

   - View → Output
   - View → Output

   - Select "Python" from dropdown
   - اختر "Python" من القائمة المنسدلة

   - Look for errors
   - ابحث عن أخطاء

4. Restart Python language server:
   أعد تشغيل خادم لغة Python:

   - Ctrl/⌘ + Shift + P
   - Ctrl/⌘ + Shift + P

   - Type: "Python: Restart Language Server"
   - اكتب: "Python: Restart Language Server"

### ❌ Problem: Linter not showing errors
### ❌ المشكلة: فاحص الكود لا يعرض الأخطاء

**Solution:**
**الحل:**

1. Install pylint in venv:
   ثبت pylint في venv:

   ```bash
   pip install pylint
   ```

2. Enable linting:
   مكّن فحص الكود:

   - File → Preferences → Settings
   - File → Preferences → Settings

   - Search: "python.linting.enabled"
   - ابحث عن: "python.linting.enabled"

   - Check the box
   - حدد المربع

3. Select linter:
   اختر فاحص الكود:

   - Ctrl/⌘ + Shift + P
   - Ctrl/⌘ + Shift + P

   - Type: "Python: Select Linter"
   - اكتب: "Python: Select Linter"

   - Choose "pylint"
   - اختر "pylint"

---

## File and Path Problems
## مشاكل الملفات والمسارات

### ❌ Problem: "No such file or directory"
### ❌ المشكلة: "No such file or directory"

**Cause:** Wrong current directory or file doesn't exist
**السبب:** المجلد الحالي خاطئ أو الملف غير موجود

**Solution:**
**الحل:**

1. Check current directory:
   تحقق من المجلد الحالي:

   ```bash
   pwd     # Mac/Linux
   cd      # Windows
   ```

2. List files:
   سرد الملفات:

   ```bash
   ls      # Mac/Linux
   dir     # Windows
   ```

3. Navigate to correct directory:
   انتقل إلى المجلد الصحيح:

   ```bash
   cd path/to/directory
   ```

4. Use tab completion to avoid typos
   استخدم الإكمال التلقائي لتجنب الأخطاء الإملائية

### ❌ Problem: Spaces in File Paths
### ❌ المشكلة: مسافات في مسارات الملفات

**Error:**
**خطأ:**

```bash
# This fails
cd My Documents/Projects

# This works
cd "My Documents/Projects"
```

**Solution: Always quote paths with spaces**
**الحل: اقتبس دائماً المسارات التي بها مسافات**

```bash
# Correct
python "my file.py"
cd "C:\Users\My Name\Projects"

# Wrong
python my file.py
cd C:\Users\My Name\Projects
```

### ❌ Problem: File not found (case sensitivity on Mac/Linux)
### ❌ المشكلة: الملف غير موجود (حساسية حالة الأحرف على ماك/لينكس)

**Remember:** Mac/Linux are case-sensitive!
**تذكر:** ماك/لينكس حساسان لحالة الأحرف!

```bash
# These are DIFFERENT files on Mac/Linux:
hello.py
Hello.py
HELLO.py

# But SAME file on Windows
```

**Solution: Match exact case**
**الحل: طابق الحالة الدقيقة**

Use tab completion to get the right case automatically.
استخدم الإكمال التلقائي للحصول على الحالة الصحيحة تلقائياً.

---

## Terminal and Command Line Issues
## مشاكل الطرفية وسطر الأوامر

### ❌ Problem: Terminal shows gibberish or weird characters
### ❌ المشكلة: الطرفية تعرض كلاماً غير مفهوم أو رموزاً غريبة

**Cause:** Wrong character encoding
**السبب:** ترميز أحرف خاطئ

**Solution (Windows):**
**الحل (ويندوز):**

```bash
# Run in Command Prompt
chcp 65001
```

**For VS Code terminal:**
**لطرفية VS Code:**

1. Settings (Ctrl/⌘ + ,)
   الإعدادات (Ctrl/⌘ + ,)

2. Search: "terminal.integrated.defaultProfile.windows"
   ابحث عن: "terminal.integrated.defaultProfile.windows"

3. Set to "Command Prompt" or "PowerShell"
   اضبط على "Command Prompt" أو "PowerShell"

### ❌ Problem: Can't copy/paste in terminal
### ❌ المشكلة: لا يمكن النسخ/اللصق في الطرفية

**VS Code Terminal:**
**طرفية VS Code:**

- **Copy:** Ctrl/⌘ + C (with text selected)
- **نسخ:** Ctrl/⌘ + C (مع تحديد النص)

- **Paste:** Ctrl/⌘ + V
- **لصق:** Ctrl/⌘ + V

**Windows Command Prompt:**
**موجه أوامر ويندوز:**

- Right-click → Properties → Enable "Use Ctrl+Shift+C/V as Copy/Paste"
- النقر بالزر الأيمن → Properties → مكّن "Use Ctrl+Shift+C/V as Copy/Paste"

### ❌ Problem: Terminal freezes or hangs
### ❌ المشكلة: الطرفية تتجمد أو تتوقف

**Solution:**
**الحل:**

1. Try pressing Ctrl + C to cancel current operation
   حاول الضغط على Ctrl + C لإلغاء العملية الحالية

2. If frozen, kill the terminal:
   إذا تجمدت، أنهِ الطرفية:

   - Click trash icon in terminal panel
   - انقر أيقونة القمامة في لوحة الطرفية

   - Open new terminal
   - افتح طرفية جديدة

3. Restart VS Code if needed
   أعد تشغيل VS Code إذا لزم الأمر

---

## Running Code Problems
## مشاكل تشغيل الكود

### ❌ Problem: Code runs but no output appears
### ❌ المشكلة: الكود يعمل لكن لا تظهر مخرجات

**Check:**
**تحقق:**

1. Look in TERMINAL tab (not OUTPUT or PROBLEMS)
   انظر في تبويب TERMINAL (وليس OUTPUT أو PROBLEMS)

2. Scroll up in terminal to see output
   مرر لأعلى في الطرفية لرؤية المخرجات

3. Make sure code has print() statements
   تأكد من أن الكود يحتوي على جمل print()

### ❌ Problem: "SyntaxError: invalid syntax"
### ❌ المشكلة: "SyntaxError: invalid syntax"

**Common causes:**
**الأسباب الشائعة:**

1. **Missing quotes:**
   **علامات اقتباس مفقودة:**

   ```python
   # Wrong
   print(Hello)

   # Correct
   print("Hello")
   ```

2. **Mismatched quotes:**
   **علامات اقتباس غير متطابقة:**

   ```python
   # Wrong
   print("Hello')

   # Correct
   print("Hello")
   ```

3. **Missing colon:**
   **نقطتان مفقودتان:**

   ```python
   # Wrong
   if x > 5
       print("Big")

   # Correct
   if x > 5:
       print("Big")
   ```

4. **Wrong indentation:**
   **مسافة بادئة خاطئة:**

   ```python
   # Wrong
   def hello():
   print("Hi")

   # Correct
   def hello():
       print("Hi")
   ```

### ❌ Problem: "IndentationError"
### ❌ المشكلة: "IndentationError"

**Cause:** Mixing tabs and spaces or wrong indentation
**السبب:** خلط التبويبات والمسافات أو مسافة بادئة خاطئة

**Solution:**
**الحل:**

1. VS Code settings:
   إعدادات VS Code:

   - File → Preferences → Settings
   - File → Preferences → Settings

   - Search: "tab size"
   - ابحث عن: "tab size"

   - Set to 4
   - اضبط على 4

   - Search: "insert spaces"
   - ابحث عن: "insert spaces"

   - Check the box
   - حدد المربع

2. Fix existing code:
   أصلح الكود الموجود:

   - Select all (Ctrl/⌘ + A)
   - حدد الكل (Ctrl/⌘ + A)

   - Format document (Shift + Alt/⌥ + F)
   - نسّق المستند (Shift + Alt/⌥ + F)

### ❌ Problem: "NameError: name 'X' is not defined"
### ❌ المشكلة: "NameError: name 'X' is not defined"

**Cause:** Using a variable before defining it
**السبب:** استخدام متغير قبل تعريفه

```python
# Wrong - using before defining
print(name)
name = "Ahmed"

# Correct - define first
name = "Ahmed"
print(name)
```

---

## Package Installation Issues
## مشاكل تثبيت الحزم

### ❌ Problem: "ModuleNotFoundError: No module named 'X'"
### ❌ المشكلة: "ModuleNotFoundError: No module named 'X'"

**Cause:** Package not installed or wrong Python interpreter
**السبب:** الحزمة غير مثبتة أو مفسر Python خاطئ

**Solution:**
**الحل:**

1. Make sure venv is active (look for `(venv)`)
   تأكد من أن venv نشط (ابحث عن `(venv)`)

2. Install the package:
   ثبت الحزمة:

   ```bash
   pip install package-name
   ```

3. If you installed but still get error:
   إذا ثبتت لكن لا تزال تحصل على خطأ:

   - Check VS Code is using venv interpreter
   - تحقق من أن VS Code يستخدم مفسر venv

   - Restart VS Code
   - أعد تشغيل VS Code

### ❌ Problem: pip install fails with permissions error
### ❌ المشكلة: pip install يفشل بخطأ أذونات

**DON'T use sudo with pip in venv!**
**لا تستخدم sudo مع pip في venv!**

**Solution:**
**الحل:**

1. Make sure venv is activated
   تأكد من تفعيل venv

2. Check pip is from venv:
   تحقق من أن pip من venv:

   ```bash
   pip --version
   # Should show path with 'venv'
   ```

3. If not, deactivate and reactivate venv
   إذا لم يكن، ألغِ التفعيل وأعد التفعيل لـ venv

### ❌ Problem: "Could not find a version that satisfies the requirement"
### ❌ المشكلة: "Could not find a version that satisfies the requirement"

**Cause:** Package name misspelled or doesn't exist
**السبب:** اسم الحزمة مكتوب بشكل خاطئ أو غير موجود

**Solution:**
**الحل:**

1. Check spelling at: https://pypi.org
   تحقق من الإملاء في: https://pypi.org

2. Make sure you have internet connection
   تأكد من اتصال الإنترنت

3. Update pip:
   حدّث pip:

   ```bash
   python -m pip install --upgrade pip
   ```

---

## Character Encoding Problems
## مشاكل ترميز الأحرف

### ❌ Problem: Arabic text shows as boxes or question marks
### ❌ المشكلة: النص العربي يظهر كمربعات أو علامات استفهام

**Cause:** Wrong file encoding
**السبب:** ترميز ملف خاطئ

**Solution in VS Code:**
**الحل في VS Code:**

1. Look at bottom-right corner
   انظر إلى الزاوية السفلية اليمنى

2. Click on encoding (e.g., "ASCII" or "Windows-1256")
   انقر على الترميز (مثل "ASCII" أو "Windows-1256")

3. Select **"Save with Encoding"**
   اختر **"Save with Encoding"**

4. Choose **"UTF-8"**
   اختر **"UTF-8"**

5. Save file
   احفظ الملف

**For new files:**
**للملفات الجديدة:**

Settings → Search "files.encoding" → Set to "UTF-8"
الإعدادات → ابحث عن "files.encoding" → اضبط على "UTF-8"

### ❌ Problem: Code with Arabic comments causes syntax errors
### ❌ المشكلة: الكود بتعليقات عربية يسبب أخطاء بنية

**Solution: Add encoding declaration at top of file**
**الحل: أضف إعلان ترميز في أعلى الملف**

```python
# -*- coding: utf-8 -*-

# الآن يمكنك استخدام العربية في التعليقات
print("Hello, World!")
```

---

## Permission and Access Errors
## أخطاء الأذونات والوصول

### ❌ Problem: "Permission denied" (General)
### ❌ المشكلة: "Permission denied" (عامة)

**Windows:**
**ويندوز:**

1. Run VS Code or terminal as Administrator
   شغّل VS Code أو الطرفية كمسؤول

2. Check file/folder is not read-only:
   تحقق من أن الملف/المجلد ليس للقراءة فقط:

   - Right-click → Properties
   - النقر بالزر الأيمن → Properties

   - Uncheck "Read-only"
   - ألغِ تحديد "Read-only"

**Mac/Linux:**
**ماك/لينكس:**

```bash
# Check permissions
ls -la filename

# Fix permissions
chmod +x filename

# For directories
chmod -R 755 directory/
```

### ❌ Problem: Can't delete or modify files in repository
### ❌ المشكلة: لا يمكن حذف أو تعديل ملفات في المستودع

**Cause:** File might be in use or locked by Git
**السبب:** الملف قد يكون قيد الاستخدام أو مغلق من Git

**Solution:**
**الحل:**

1. Close VS Code and any programs using the file
   أغلق VS Code وأي برامج تستخدم الملف

2. Try again
   حاول مرة أخرى

3. If still locked on Windows:
   إذا لا يزال مغلقاً على ويندوز:

   - Restart computer
   - أعد تشغيل الكمبيوتر

---

## Performance and Speed Issues
## مشاكل الأداء والسرعة

### ❌ Problem: VS Code is slow or laggy
### ❌ المشكلة: VS Code بطيء أو متقطع

**Solution:**
**الحل:**

1. Disable extensions you don't need:
   عطّل الإضافات التي لا تحتاجها:

   - Extensions → Click gear icon → Disable
   - Extensions → انقر أيقونة الترس → Disable

2. Close other applications
   أغلق التطبيقات الأخرى

3. Disable minimap:
   عطّل الخريطة المصغرة:

   - Settings → Search "minimap" → Uncheck
   - الإعدادات → ابحث عن "minimap" → ألغِ التحديد

4. Increase memory (Windows):
   زد الذاكرة (ويندوز):

   - Close and restart VS Code
   - أغلق وأعد تشغيل VS Code

### ❌ Problem: Python scripts run slowly
### ❌ المشكلة: سكريبتات Python تعمل ببطء

**For beginners, this is usually normal!**
**للمبتدئين، هذا عادة طبيعي!**

**But check:**
**لكن تحقق:**

1. Are you in debug mode? Run normally instead
   هل أنت في وضع التصحيح؟ شغّل بشكل طبيعي بدلاً من ذلك

2. Infinite loops in code?
   حلقات لا نهائية في الكود؟

3. Large files being processed?
   ملفات كبيرة تتم معالجتها؟

---

## Getting Additional Help
## الحصول على مساعدة إضافية

### When to Ask for Help
### متى تطلب المساعدة

Ask your instructor if:
اسأل مدرسك إذا:

- You tried all solutions here
- جربت جميع الحلول هنا

- Error persists after restarting
- الخطأ مستمر بعد إعادة التشغيل

- You don't understand the error message
- لا تفهم رسالة الخطأ

- Problem is blocking your progress
- المشكلة تمنع تقدمك

### How to Report Issues Effectively
### كيفية الإبلاغ عن المشاكل بفعالية

When asking for help, provide:
عند طلب المساعدة، وفّر:

1. **What you were trying to do**
   **ما كنت تحاول فعله**

   - "I was trying to run my Week 1 exercise"
   - "كنت أحاول تشغيل تمرين الأسبوع 1"

2. **Exact error message**
   **رسالة الخطأ الدقيقة**

   - Copy and paste the full error
   - انسخ والصق الخطأ الكامل

3. **What you tried**
   **ما جربته**

   - "I restarted VS Code and checked venv is active"
   - "أعدت تشغيل VS Code وتحققت من أن venv نشط"

4. **Screenshots** (if visual issue)
   **لقطات شاشة** (إذا كانت مشكلة بصرية)

5. **System info**
   **معلومات النظام**

   - Windows 11, macOS 14, Ubuntu 22.04, etc.
   - Windows 11، macOS 14، Ubuntu 22.04، إلخ.

### Useful Resources
### موارد مفيدة

- 📖 Python Official Docs: https://docs.python.org
- 📖 وثائق Python الرسمية: https://docs.python.org

- 📖 VS Code Docs: https://code.visualstudio.com/docs
- 📖 وثائق VS Code: https://code.visualstudio.com/docs

- 🔍 Stack Overflow: https://stackoverflow.com
- 🔍 Stack Overflow: https://stackoverflow.com

- 💬 Python Discord: https://discord.gg/python
- 💬 Python Discord: https://discord.gg/python

---

## Quick Diagnostic Checklist
## قائمة التحقق التشخيصية السريعة

When something isn't working, check:
عندما لا يعمل شيء، تحقق:

- [ ] Is Python installed? `python --version`
- [ ] هل Python مثبت؟ `python --version`

- [ ] Is venv activated? Look for `(venv)` in terminal
- [ ] هل venv مفعّل؟ ابحث عن `(venv)` في الطرفية

- [ ] Is VS Code using correct interpreter? Check bottom-left
- [ ] هل VS Code يستخدم المفسر الصحيح؟ تحقق من أسفل اليسار

- [ ] Did you save the file? Ctrl/⌘ + S
- [ ] هل حفظت الملف؟ Ctrl/⌘ + S

- [ ] Are you in the right directory? `pwd` or `cd`
- [ ] هل أنت في المجلد الصحيح؟ `pwd` أو `cd`

- [ ] Is the file name correct? (case-sensitive on Mac/Linux)
- [ ] هل اسم الملف صحيح؟ (حساس لحالة الأحرف على ماك/لينكس)

- [ ] Did you restart VS Code?
- [ ] هل أعدت تشغيل VS Code؟

- [ ] Did you restart your computer?
- [ ] هل أعدت تشغيل حاسوبك؟

---

## Remember
## تذكر

- 🔄 **Restart fixes many problems** - Try restarting VS Code or your computer
- 🔄 **إعادة التشغيل تحل مشاكل عديدة** - حاول إعادة تشغيل VS Code أو حاسوبك

- 📖 **Read error messages carefully** - They usually tell you what's wrong
- 📖 **اقرأ رسائل الأخطاء بعناية** - عادة ما تخبرك بما هو خاطئ

- 🎯 **One change at a time** - Don't change multiple things at once
- 🎯 **تغيير واحد في كل مرة** - لا تغير أشياء متعددة في وقت واحد

- 💾 **Save often** - Ctrl/⌘ + S is your friend
- 💾 **احفظ كثيراً** - Ctrl/⌘ + S صديقك

- 🙋 **Ask for help** - Don't spend hours stuck on one problem
- 🙋 **اطلب المساعدة** - لا تقضِ ساعات عالقاً في مشكلة واحدة

- 📝 **Document your solutions** - If you fix something, note how for next time
- 📝 **وثّق حلولك** - إذا أصلحت شيئاً، سجّل كيف للمرة القادمة

---

*Last Updated: October 2025*
*آخر تحديث: أكتوبر 2025*
