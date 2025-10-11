# Virtual Environment Setup Guide
# دليل إعداد البيئة الافتراضية

⏱️ **Estimated Time:** 10-15 minutes
⏱️ **الوقت المقدر:** 10-15 دقيقة

---

## What is a Virtual Environment?
## ما هي البيئة الافتراضية؟

A virtual environment (venv) is like a separate workspace for each Python project. It keeps your project's packages isolated from other projects and from your system Python installation. Think of it like having separate toolboxes for different projects - tools in one box don't mix with tools in another.

البيئة الافتراضية (venv) هي كمساحة عمل منفصلة لكل مشروع بايثون. تحافظ على حزم مشروعك معزولة عن المشاريع الأخرى وعن تثبيت بايثون على نظامك. فكر فيها كوجود صناديق أدوات منفصلة لمشاريع مختلفة - الأدوات في صندوق لا تختلط مع الأدوات في صندوق آخر.

### Why Use Virtual Environments?
### لماذا نستخدم البيئات الافتراضية؟

- 🔒 **Isolation** - Each project has its own dependencies
- 🔒 **العزل** - كل مشروع له تبعياته الخاصة

- 📦 **Clean system** - Don't clutter your main Python installation
- 📦 **نظام نظيف** - لا تلوث تثبيت بايثون الرئيسي

- 🔄 **Reproducibility** - Others can recreate your exact setup
- 🔄 **إمكانية التكرار** - الآخرون يمكنهم إعادة إنشاء إعدادك بالضبط

- 🚀 **Best practice** - Industry standard for Python development
- 🚀 **أفضل ممارسة** - معيار صناعي لتطوير بايثون

---

## Prerequisites
## المتطلبات الأساسية

Before setting up a virtual environment:
قبل إعداد بيئة افتراضية:

- ✅ Python 3.9+ installed (see [01-python-installation.md](01-python-installation.md))
- ✅ بايثون 3.9+ مثبت (انظر [01-python-installation.md](01-python-installation.md))

- ✅ VS Code installed (see [02-vscode-installation.md](02-vscode-installation.md))
- ✅ VS Code مثبت (انظر [02-vscode-installation.md](02-vscode-installation.md))

- ✅ Course repository cloned (see [06-github-repo-cloning.md](06-github-repo-cloning.md))
- ✅ مستودع المقرر منسوخ (انظر [06-github-repo-cloning.md](06-github-repo-cloning.md))

---

## Part 1: Creating a Virtual Environment
## الجزء 1: إنشاء بيئة افتراضية

### 🪟 For Windows Users
### 🪟 لمستخدمي ويندوز

#### Step 1: Open Terminal in VS Code
#### الخطوة 1: فتح الطرفية في VS Code

1. Open VS Code
   افتح VS Code

2. Open your course repository folder:
   افتح مجلد مستودع المقرر:

   - **File** → **Open Folder**
   - **File** → **Open Folder**

   - Navigate to `python-m110` folder
   - انتقل إلى مجلد `python-m110`

   - Click **Select Folder**
   - انقر **Select Folder**

3. Open the integrated terminal:
   افتح الطرفية المدمجة:

   - **View** → **Terminal** (or press **Ctrl + `**)
   - **View** → **Terminal** (أو اضغط **Ctrl + `**)

4. Make sure you're in the repository root:
   تأكد من أنك في جذر المستودع:

   ```bash
   pwd
   ```

   You should see a path ending with `python-m110`
   يجب أن ترى مساراً ينتهي بـ `python-m110`

📸 **Screenshot location:** VS Code with terminal open showing repository path

#### Step 2: Create the Virtual Environment
#### الخطوة 2: إنشاء البيئة الافتراضية

1. In the terminal, type:
   في الطرفية، اكتب:

   ```bash
   python -m venv venv
   ```

   **Explanation / شرح:**
   - `python` - Run Python
   - `python` - تشغيل بايثون

   - `-m venv` - Use the venv module
   - `-m venv` - استخدام وحدة venv

   - `venv` - Name of the virtual environment folder
   - `venv` - اسم مجلد البيئة الافتراضية

2. Press **Enter** and wait (10-30 seconds)
   اضغط **Enter** وانتظر (10-30 ثانية)

3. You'll see a new folder called `venv` appear in your Explorer
   سترى مجلداً جديداً يسمى `venv` يظهر في المستكشف

✅ **Success!** Your virtual environment is created!
✅ **نجح!** تم إنشاء بيئتك الافتراضية!

#### Step 3: Activate the Virtual Environment
#### الخطوة 3: تفعيل البيئة الافتراضية

1. In the terminal, type:
   في الطرفية، اكتب:

   ```bash
   venv\Scripts\activate
   ```

2. Press **Enter**
   اضغط **Enter**

3. You should see `(venv)` appear at the beginning of your terminal line:
   يجب أن ترى `(venv)` يظهر في بداية سطر الطرفية:

   ```
   (venv) PS C:\Users\YourName\python-m110>
   ```

✅ **The virtual environment is now active!**
✅ **البيئة الافتراضية نشطة الآن!**

📸 **Screenshot location:** Terminal showing (venv) prefix

---

### 🍎 For macOS / Linux Users
### 🍎 لمستخدمي ماك / لينكس

#### Step 1: Open Terminal in VS Code
#### الخطوة 1: فتح الطرفية في VS Code

1. Open VS Code
   افتح VS Code

2. Open your course repository folder:
   افتح مجلد مستودع المقرر:

   - **File** → **Open Folder**
   - **File** → **Open Folder**

   - Navigate to `python-m110` folder
   - انتقل إلى مجلد `python-m110`

   - Click **Open**
   - انقر **Open**

3. Open the integrated terminal:
   افتح الطرفية المدمجة:

   - **View** → **Terminal** (or press **⌘ + `** on Mac, **Ctrl + `** on Linux)
   - **View** → **Terminal** (أو اضغط **⌘ + `** على ماك، **Ctrl + `** على لينكس)

4. Verify you're in the repository root:
   تحقق من أنك في جذر المستودع:

   ```bash
   pwd
   ```

   Should show: `/Users/YourName/python-m110` (Mac) or `/home/yourname/python-m110` (Linux)
   يجب أن يظهر: `/Users/YourName/python-m110` (ماك) أو `/home/yourname/python-m110` (لينكس)

#### Step 2: Create the Virtual Environment
#### الخطوة 2: إنشاء البيئة الافتراضية

1. In the terminal, type:
   في الطرفية، اكتب:

   ```bash
   python3 -m venv venv
   ```

2. Press **Enter** and wait (10-30 seconds)
   اضغط **Enter** وانتظر (10-30 ثانية)

3. A new `venv` folder will appear in your Explorer
   سيظهر مجلد `venv` جديد في المستكشف

#### Step 3: Activate the Virtual Environment
#### الخطوة 3: تفعيل البيئة الافتراضية

1. In the terminal, type:
   في الطرفية، اكتب:

   ```bash
   source venv/bin/activate
   ```

2. Press **Enter**
   اضغط **Enter**

3. You should see `(venv)` at the beginning of your prompt:
   يجب أن ترى `(venv)` في بداية موجه الأوامر:

   ```
   (venv) username@computer python-m110 %
   ```

✅ **Virtual environment is active!**
✅ **البيئة الافتراضية نشطة!**

---

## Part 2: Installing Packages with pip
## الجزء 2: تثبيت الحزم باستخدام pip

Now that your virtual environment is active, let's install packages!
الآن وقد أصبحت بيئتك الافتراضية نشطة، دعنا نثبت الحزم!

### What is pip?
### ما هو pip؟

pip is Python's package installer. It downloads and installs Python libraries from the Python Package Index (PyPI).

pip هو مثبت حزم بايثون. يحمل ويثبت مكتبات بايثون من فهرس حزم بايثون (PyPI).

### Verify pip is Available
### تحقق من توفر pip

1. Make sure your virtual environment is active (you should see `(venv)`)
   تأكد من أن بيئتك الافتراضية نشطة (يجب أن ترى `(venv)`)

2. Check pip version:
   تحقق من إصدار pip:

   ```bash
   pip --version
   ```

   You should see something like:
   يجب أن ترى شيئاً مثل:

   ```
   pip 23.2.1 from .../python-m110/venv/lib/python3.12/site-packages/pip (python 3.12)
   ```

   Notice the path includes `/venv/` - this confirms pip is using your virtual environment!
   لاحظ أن المسار يتضمن `/venv/` - هذا يؤكد أن pip يستخدم بيئتك الافتراضية!

### Upgrade pip (Recommended)
### ترقية pip (موصى به)

It's good practice to upgrade pip to the latest version:
من الممارسات الجيدة ترقية pip إلى أحدث إصدار:

**Windows:**
```bash
python -m pip install --upgrade pip
```

**Mac/Linux:**
```bash
python3 -m pip install --upgrade pip
```

### Installing Individual Packages
### تثبيت الحزم الفردية

To install a single package:
لتثبيت حزمة واحدة:

```bash
pip install package-name
```

Example: Install the `requests` library
مثال: تثبيت مكتبة `requests`

```bash
pip install requests
```

You'll see:
سترى:

```
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.31.0
```

---

## Part 3: Using requirements.txt
## الجزء 3: استخدام requirements.txt

### What is requirements.txt?
### ما هو requirements.txt؟

`requirements.txt` is a file that lists all the packages your project needs. It's like a shopping list for pip!

`requirements.txt` هو ملف يسرد جميع الحزم التي يحتاجها مشروعك. إنه مثل قائمة تسوق لـ pip!

### Installing from requirements.txt
### التثبيت من requirements.txt

Our course repository has a `requirements.txt` file with all necessary packages.
مستودع مقررنا به ملف `requirements.txt` يحتوي على جميع الحزم الضرورية.

1. Make sure you're in the repository root and venv is active `(venv)`
   تأكد من أنك في جذر المستودع وأن venv نشط `(venv)`

2. View the requirements file (optional):
   اعرض ملف المتطلبات (اختياري):

   ```bash
   cat requirements.txt
   ```

3. Install all packages from requirements.txt:
   ثبت جميع الحزم من requirements.txt:

   ```bash
   pip install -r requirements.txt
   ```

   **Explanation / شرح:**
   - `pip install` - Install packages
   - `pip install` - تثبيت الحزم

   - `-r` - Read from file
   - `-r` - القراءة من ملف

   - `requirements.txt` - The file name
   - `requirements.txt` - اسم الملف

4. Wait for all packages to download and install (1-3 minutes)
   انتظر حتى يتم تحميل وتثبيت جميع الحزم (1-3 دقائق)

5. You'll see messages like:
   سترى رسائل مثل:

   ```
   Collecting package1
   Collecting package2
   ...
   Successfully installed package1 package2 package3
   ```

✅ **All course packages are now installed!**
✅ **تم تثبيت جميع حزم المقرر الآن!**

### Viewing Installed Packages
### عرض الحزم المثبتة

To see all packages installed in your virtual environment:
لرؤية جميع الحزم المثبتة في بيئتك الافتراضية:

```bash
pip list
```

You'll see a list like:
سترى قائمة مثل:

```
Package          Version
---------------- -------
pip              23.2.1
requests         2.31.0
setuptools       68.0.0
...
```

---

## Part 4: Deactivating the Virtual Environment
## الجزء 4: إلغاء تفعيل البيئة الافتراضية

When you're done working on your project, you can deactivate the virtual environment.
عندما تنتهي من العمل على مشروعك، يمكنك إلغاء تفعيل البيئة الافتراضية.

### How to Deactivate
### كيفية إلغاء التفعيل

Simply type:
ببساطة اكتب:

```bash
deactivate
```

The `(venv)` prefix will disappear from your terminal prompt.
سيختفي بادئة `(venv)` من موجه الطرفية.

```
# Before deactivation / قبل إلغاء التفعيل
(venv) C:\Users\YourName\python-m110>

# After deactivation / بعد إلغاء التفعيل
C:\Users\YourName\python-m110>
```

### When to Activate/Deactivate
### متى تفعّل/تلغي التفعيل

**Activate when:**
**فعّل عندما:**

- You start working on your Python project
- تبدأ العمل على مشروع بايثون الخاص بك

- You need to install packages
- تحتاج لتثبيت الحزم

- You want to run Python code from this project
- تريد تشغيل كود بايثون من هذا المشروع

**Deactivate when:**
**ألغِ التفعيل عندما:**

- You're done working on the project
- تنتهي من العمل على المشروع

- You want to switch to another project
- تريد التبديل إلى مشروع آخر

- You're closing your terminal/VS Code
- تغلق الطرفية/VS Code

💡 **Note:** You need to activate the venv every time you open a new terminal!
💡 **ملاحظة:** تحتاج إلى تفعيل venv في كل مرة تفتح فيها طرفية جديدة!

---

## Part 5: VS Code Integration
## الجزء 5: التكامل مع VS Code

VS Code can automatically detect and use your virtual environment!
VS Code يمكنه اكتشاف واستخدام بيئتك الافتراضية تلقائياً!

### Select Python Interpreter
### اختيار مفسر بايثون

1. Open VS Code with your repository folder
   افتح VS Code مع مجلد المستودع

2. Press **Ctrl/⌘ + Shift + P** to open Command Palette
   اضغط **Ctrl/⌘ + Shift + P** لفتح لوحة الأوامر

3. Type: **"Python: Select Interpreter"**
   اكتب: **"Python: Select Interpreter"**

4. Select the interpreter that includes `venv`:
   اختر المفسر الذي يتضمن `venv`:

   ```
   Python 3.12.0 ('venv': venv) ./venv/bin/python
   ```

5. Look at the bottom-left of VS Code - you should see:
   انظر إلى الجزء السفلي الأيسر من VS Code - يجب أن ترى:

   ```
   Python 3.12.0 ('venv': venv)
   ```

📸 **Screenshot location:** VS Code status bar showing selected Python interpreter

### Auto-Activation in VS Code
### التفعيل التلقائي في VS Code

Once you select the venv interpreter, VS Code will automatically activate it when you:
بمجرد اختيار مفسر venv، سيفعّله VS Code تلقائياً عندما:

- Open a new terminal
- تفتح طرفية جديدة

- Run a Python file
- تشغّل ملف بايثون

- Debug Python code
- تصحح أخطاء كود بايثون

You'll see `(venv)` appear automatically in new terminals!
سترى `(venv)` يظهر تلقائياً في الطرفيات الجديدة!

---

## Workflow Summary
## ملخص سير العمل

Here's your daily workflow with virtual environments:
إليك سير عملك اليومي مع البيئات الافتراضية:

### Starting Your Work Day
### بدء يوم عملك

1. Open VS Code
   افتح VS Code

2. Open your project folder (`python-m110`)
   افتح مجلد مشروعك (`python-m110`)

3. Open a terminal (**Ctrl/⌘ + `**)
   افتح طرفية (**Ctrl/⌘ + `**)

4. VS Code should auto-activate venv (look for `(venv)`)
   يجب أن يفعّل VS Code الـ venv تلقائياً (ابحث عن `(venv)`)

5. If not auto-activated, activate manually:
   إذا لم يتم التفعيل تلقائياً، فعّل يدوياً:

   - **Windows:** `venv\Scripts\activate`
   - **Mac/Linux:** `source venv/bin/activate`

6. Start coding!
   ابدأ البرمجة!

### During Your Work
### أثناء عملك

- All `pip install` commands use the venv
- جميع أوامر `pip install` تستخدم venv

- All Python scripts run with venv packages
- جميع سكريبتات بايثون تعمل مع حزم venv

- Check active venv: look for `(venv)` in terminal
- تحقق من venv النشط: ابحث عن `(venv)` في الطرفية

### Ending Your Work Day
### إنهاء يوم عملك

1. (Optional) Deactivate: `deactivate`
   (اختياري) ألغِ التفعيل: `deactivate`

2. Close VS Code
   أغلق VS Code

💡 **Tip:** You don't need to deactivate before closing VS Code - it's done automatically!
💡 **نصيحة:** لا تحتاج إلى إلغاء التفعيل قبل إغلاق VS Code - يتم ذلك تلقائياً!

---

## Troubleshooting
## استكشاف الأخطاء وإصلاحها

### ❌ "venv is not recognized" (Windows)
### ❌ "venv is not recognized" (ويندوز)

**Problem:** Python can't find the venv module
**المشكلة:** بايثون لا يمكنه إيجاد وحدة venv

**Solution:**
**الحل:**

1. Make sure Python is properly installed
   تأكد من أن بايثون مثبت بشكل صحيح

2. Try using `python3` instead of `python`:
   حاول استخدام `python3` بدلاً من `python`:

   ```bash
   python3 -m venv venv
   ```

### ❌ "activate cannot be loaded" (Windows PowerShell)
### ❌ "activate cannot be loaded" (Windows PowerShell)

**Problem:** PowerShell execution policy blocks activation
**المشكلة:** سياسة تنفيذ PowerShell تمنع التفعيل

**Solution:**
**الحل:**

1. Open PowerShell as Administrator
   افتح PowerShell كمسؤول

2. Run:
   نفّذ:

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. Type **Y** and press Enter
   اكتب **Y** واضغط Enter

4. Close and reopen VS Code
   أغلق وأعد فتح VS Code

### ❌ "Permission denied" (Mac/Linux)
### ❌ "Permission denied" (ماك/لينكس)

**Solution:**
**الحل:**

```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

### ❌ Packages installing globally instead of in venv
### ❌ الحزم تثبت عالمياً بدلاً من venv

**Problem:** Virtual environment not activated
**المشكلة:** البيئة الافتراضية غير مفعلة

**Check:**
**تحقق:**

1. Look for `(venv)` in terminal - if missing, activate it
   ابحث عن `(venv)` في الطرفية - إذا كان مفقوداً، فعّله

2. Verify with:
   تحقق بـ:

   ```bash
   pip --version
   ```

   The path should include `/venv/`
   المسار يجب أن يتضمن `/venv/`

### ❌ "No module named 'package_name'" when running code
### ❌ "No module named 'package_name'" عند تشغيل الكود

**Problem:** VS Code using wrong Python interpreter
**المشكلة:** VS Code يستخدم مفسر بايثون خاطئ

**Solution:**
**الحل:**

1. Press **Ctrl/⌘ + Shift + P**
   اضغط **Ctrl/⌘ + Shift + P**

2. Type: **"Python: Select Interpreter"**
   اكتب: **"Python: Select Interpreter"**

3. Choose the one with `venv`
   اختر الذي يحتوي على `venv`

4. Restart the terminal
   أعد تشغيل الطرفية

### ❌ Accidentally deleted venv folder
### ❌ حذف مجلد venv عن طريق الخطأ

**Don't panic!** Just recreate it:
**لا داعي للذعر!** فقط أعد إنشاءه:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Best Practices
## أفضل الممارسات

- ✅ **Always activate venv** before working on your project
- ✅ **فعّل venv دائماً** قبل العمل على مشروعك

- ✅ **One venv per project** - don't share venvs between projects
- ✅ **venv واحد لكل مشروع** - لا تشارك venvs بين المشاريع

- ✅ **Add venv to .gitignore** - don't commit venv to Git (already done in our repo)
- ✅ **أضف venv إلى .gitignore** - لا ترسل venv إلى Git (تم بالفعل في مستودعنا)

- ✅ **Use requirements.txt** - document your dependencies
- ✅ **استخدم requirements.txt** - وثّق تبعياتك

- ✅ **Update requirements.txt** when you install new packages:
- ✅ **حدّث requirements.txt** عند تثبيت حزم جديدة:

  ```bash
  pip freeze > requirements.txt
  ```

- ✅ **Keep venv name simple** - use `venv` or `.venv`
- ✅ **احتفظ باسم venv بسيط** - استخدم `venv` أو `.venv`

---

## Quick Reference
## مرجع سريع

### Create venv
### إنشاء venv

**Windows:**
```bash
python -m venv venv
```

**Mac/Linux:**
```bash
python3 -m venv venv
```

### Activate venv
### تفعيل venv

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Deactivate venv
### إلغاء تفعيل venv

```bash
deactivate
```

### Install packages
### تثبيت الحزم

```bash
pip install package-name              # Single package
pip install -r requirements.txt       # From requirements file
```

### List packages
### سرد الحزم

```bash
pip list                              # All packages
pip freeze                            # In requirements.txt format
```

### Save packages to requirements.txt
### حفظ الحزم إلى requirements.txt

```bash
pip freeze > requirements.txt
```

---

## Next Steps
## الخطوات التالية

Great! Your virtual environment is set up! Now continue with:
رائع! تم إعداد بيئتك الافتراضية! الآن تابع مع:

1. **Install Python Extension for VS Code** - [05-python-extension-vscode.md](05-python-extension-vscode.md)
   **تثبيت إضافة Python لـ VS Code** - [05-python-extension-vscode.md](05-python-extension-vscode.md)

2. **Run Your First Program** - [07-running-first-program.md](07-running-first-program.md)
   **تشغيل برنامجك الأول** - [07-running-first-program.md](07-running-first-program.md)

---

## Additional Resources
## موارد إضافية

- 📖 [Python venv Documentation](https://docs.python.org/3/library/venv.html)
- 📖 [وثائق venv لبايثون](https://docs.python.org/3/library/venv.html)

- 📖 [pip User Guide](https://pip.pypa.io/en/stable/user_guide/)
- 📖 [دليل مستخدم pip](https://pip.pypa.io/en/stable/user_guide/)

- 🎥 [Virtual Environments Explained](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)
- 🎥 [شرح البيئات الافتراضية](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)

---

*Last Updated: October 2025*
*آخر تحديث: أكتوبر 2025*
