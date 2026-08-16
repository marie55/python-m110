# Terminal in VS Code
# الطرفية في VS Code

⏱️ **Estimated Time:** 20 minutes
⏱️ **الوقت المقدر:** 20 دقيقة

## What You'll Learn
## ما ستتعلمه

By the end of this guide, you'll be able to:
- ✅ Understand what a terminal/command line is and why it matters
- ✅ Open and use the integrated terminal in VS Code
- ✅ Navigate directories using terminal commands
- ✅ Run Python scripts from the terminal
- ✅ Activate and use virtual environments
- ✅ Work with multiple terminals simultaneously
- ✅ Customize your terminal appearance
- ✅ Troubleshoot common terminal errors

بنهاية هذا الدليل، ستكون قادرًا على:
- ✅ فهم ما هي الطرفية/سطر الأوامر ولماذا هي مهمة
- ✅ فتح واستخدام الطرفية المدمجة في VS Code
- ✅ التنقل بين المجلدات باستخدام أوامر الطرفية
- ✅ تشغيل سكريبتات بايثون من الطرفية
- ✅ تفعيل واستخدام البيئات الافتراضية
- ✅ العمل مع طرفيات متعددة في وقت واحد
- ✅ تخصيص مظهر الطرفية
- ✅ حل مشاكل الطرفية الشائعة

## Why This Matters
## لماذا هذا مهم

The terminal (also called command line or console) is a powerful tool that:
- **Runs programs directly** without clicking through menus
- **Automates tasks** with scripts and commands
- **Manages packages** and dependencies
- **Works with Git** for version control
- **Provides detailed output** and error messages
- **Is used by all professional developers** - it's an essential skill!

الطرفية (تُسمى أيضًا سطر الأوامر أو وحدة التحكم) هي أداة قوية:
- **تشغل البرامج مباشرة** دون النقر عبر القوائم
- **تؤتمت المهام** بالسكريبتات والأوامر
- **تدير الحزم** والتبعيات
- **تعمل مع Git** للتحكم في الإصدارات
- **توفر مخرجات مفصلة** ورسائل خطأ
- **يستخدمها جميع المطورين المحترفين** - إنها مهارة أساسية!

## Prerequisites
## المتطلبات الأساسية

- VS Code installed and running
- Python installed and configured ([see Python guide](./03-python-development-in-vscode.md))
- Basic familiarity with VS Code interface

- VS Code مثبت ويعمل
- بايثون مثبت ومُعد ([انظر دليل بايثون](./03-python-development-in-vscode.md))
- معرفة أساسية بواجهة VS Code

---

## What is a Terminal?
## ما هي الطرفية؟

### Terminal vs GUI
### الطرفية مقابل الواجهة الرسومية

Think of it this way:
- **GUI (Graphical User Interface)**: Click buttons and menus with your mouse
- **Terminal**: Type commands with your keyboard

فكر في الأمر بهذه الطريقة:
- **الواجهة الرسومية (GUI)**: انقر الأزرار والقوائم بالماوس
- **الطرفية**: اكتب الأوامر بلوحة المفاتيح

**Example - Creating a new folder:**
- GUI way: Right-click → New → Folder → Type name → Enter (5 steps)
- Terminal way: `mkdir my_folder` → Enter (2 steps)

**مثال - إنشاء مجلد جديد:**
- طريقة الواجهة الرسومية: نقر بزر الماوس الأيمن → جديد → مجلد → اكتب الاسم → Enter (5 خطوات)
- طريقة الطرفية: `mkdir my_folder` → Enter (خطوتان)

### Terminal Names by Platform
### أسماء الطرفية حسب المنصة

Different operating systems call it different names:
- **Windows**: Command Prompt (cmd), PowerShell, Windows Terminal
- **Mac**: Terminal, iTerm2
- **Linux**: Terminal, Console, Shell

أنظمة التشغيل المختلفة تسميها بأسماء مختلفة:
- **ويندوز**: موجه الأوامر (cmd)، PowerShell، Windows Terminal
- **ماك**: Terminal، iTerm2
- **لينكس**: Terminal، Console، Shell

**Good news:** VS Code's integrated terminal works the same on all platforms!

**أخبار جيدة:** الطرفية المدمجة في VS Code تعمل بنفس الطريقة على جميع المنصات!

---

## Opening the Terminal in VS Code
## فتح الطرفية في VS Code

### Method 1: Keyboard Shortcut (Fastest)
### الطريقة 1: اختصار لوحة المفاتيح (الأسرع)

Press `` Ctrl+` `` (Mac: `` Cmd+` ``)

The backtick (`` ` ``) key is usually above the Tab key on your keyboard.

اضغط `` Ctrl+` `` (Mac: `` Cmd+` ``)

مفتاح backtick (`` ` ``) عادة فوق مفتاح Tab على لوحة المفاتيح.

### Method 2: Menu
### الطريقة 2: القائمة

**View → Terminal**

### Method 3: Panel Buttons
### الطريقة 3: أزرار اللوحة

Click "TERMINAL" tab in the bottom panel if it's already visible.

انقر على تبويب "TERMINAL" في اللوحة السفلية إذا كانت مرئية بالفعل.

### What You Should See
### ما يجب أن تراه

When the terminal opens, you'll see something like:

عندما تفتح الطرفية، سترى شيئًا مثل:

**Windows (PowerShell):**
```
Windows PowerShell
Copyright (c) Microsoft Corporation. All rights reserved.

(venv) PS C:\Users\YourName\python-m110>
```

**Mac/Linux (Bash/Zsh):**
```
(venv) username@computer python-m110 %
```

Important parts:
- `(venv)`: Your virtual environment is active! ✅
- `C:\Users\YourName\python-m110`: Current directory
- `>` or `%` or `$`: Prompt (waiting for your command)

الأجزاء المهمة:
- `(venv)`: بيئتك الافتراضية نشطة! ✅
- `C:\Users\YourName\python-m110`: المجلد الحالي
- `>` أو `%` أو `$`: المحث (ينتظر أمرك)

---

## Essential Terminal Commands
## أوامر الطرفية الأساسية

Learn these 10 commands and you'll handle 90% of terminal tasks!

تعلم هذه الأوامر العشرة وستتعامل مع 90% من مهام الطرفية!

### 1. Where Am I? (pwd)
### 1. أين أنا؟ (pwd)

**Command:** `pwd` (Print Working Directory)

Shows your current location in the file system.

**الأمر:** `pwd` (طباعة دليل العمل)

يظهر موقعك الحالي في نظام الملفات.

```bash
pwd
# Output: /Users/YourName/python-m110
```

**Windows alternative:** `cd` (without arguments)

**بديل ويندوز:** `cd` (بدون معاملات)

### 2. List Files (ls)
### 2. سرد الملفات (ls)

**Command:** `ls` (Mac/Linux) or `dir` (Windows)

Shows all files and folders in current directory.

**الأمر:** `ls` (ماك/لينكس) أو `dir` (ويندوز)

يظهر جميع الملفات والمجلدات في المجلد الحالي.

```bash
ls
# Output:
# code-examples/
# exercises/
# lectures/
# README.md
```

**Useful variations:**
- `ls -la` (Mac/Linux): Show hidden files and details
- `dir /a` (Windows): Show all files including hidden

**تنويعات مفيدة:**
- `ls -la` (ماك/لينكس): إظهار الملفات المخفية والتفاصيل
- `dir /a` (ويندوز): إظهار جميع الملفات بما في ذلك المخفية

### 3. Change Directory (cd)
### 3. تغيير المجلد (cd)

**Command:** `cd [folder_name]`

Navigate to different folders.

**الأمر:** `cd [اسم_المجلد]`

التنقل إلى مجلدات مختلفة.

```bash
# Go into a folder / الدخول إلى مجلد
cd code-examples

# Go back one level / العودة مستوى واحد
cd ..

# Go to home directory / الذهاب للمجلد الرئيسي
cd ~

# Go to specific path / الذهاب لمسار محدد
cd /Users/YourName/python-m110
```

**💡 Pro tip:** Use Tab key to auto-complete folder names!

**💡 نصيحة احترافية:** استخدم مفتاح Tab للإكمال التلقائي لأسماء المجلدات!

### 4. Clear Screen
### 4. مسح الشاشة

**Command:** `clear` (Mac/Linux) or `cls` (Windows)

Cleans up the terminal screen.

**الأمر:** `clear` (ماك/لينكس) أو `cls` (ويندوز)

ينظف شاشة الطرفية.

### 5. Create Directory (mkdir)
### 5. إنشاء مجلد (mkdir)

**Command:** `mkdir [folder_name]`

Creates a new folder.

**الأمر:** `mkdir [اسم_المجلد]`

ينشئ مجلدًا جديدًا.

```bash
mkdir my_project
# Creates folder called 'my_project'
# ينشئ مجلد يسمى 'my_project'
```

### 6. Create File (touch/echo)
### 6. إنشاء ملف (touch/echo)

**Mac/Linux:**
```bash
touch my_file.py
```

**Windows:**
```bash
echo. > my_file.py
```

Creates an empty file.

ينشئ ملفًا فارغًا.

### 7. Remove File (rm/del)
### 7. حذف ملف (rm/del)

**Mac/Linux:**
```bash
rm file.py
```

**Windows:**
```bash
del file.py
```

⚠️ **Warning:** Deleted files don't go to trash - they're gone forever!

⚠️ **تحذير:** الملفات المحذوفة لا تذهب لسلة المهملات - تختفي للأبد!

### 8. Copy Files (cp/copy)
### 8. نسخ الملفات (cp/copy)

**Mac/Linux:**
```bash
cp source.py destination.py
```

**Windows:**
```bash
copy source.py destination.py
```

### 9. Move/Rename (mv/move)
### 9. نقل/إعادة تسمية (mv/move)

**Mac/Linux:**
```bash
mv old_name.py new_name.py  # Rename / إعادة تسمية
mv file.py folder/          # Move / نقل
```

**Windows:**
```bash
move old_name.py new_name.py  # Rename / إعادة تسمية
move file.py folder\          # Move / نقل
```

### 10. View File Contents (cat/type)
### 10. عرض محتويات الملف (cat/type)

**Mac/Linux:**
```bash
cat README.md
```

**Windows:**
```bash
type README.md
```

Shows file contents in terminal.

يظهر محتويات الملف في الطرفية.

---

## Running Python in the Terminal
## تشغيل بايثون في الطرفية

### Check Python Installation
### التحقق من تثبيت بايثون

```bash
python --version
# or / أو
python3 --version

# Output: Python 3.11.2
```

### Run a Python File
### تشغيل ملف بايثون

```bash
python my_script.py      # Windows
python3 my_script.py     # Mac/Linux
```

### Run Python Interactive Mode
### تشغيل وضع بايثون التفاعلي

```bash
python    # or python3
```

You'll see:
```python
Python 3.11.2 (main, date, time)
>>>
```

Now you can type Python code directly:
```python
>>> print("Hello from terminal!")
Hello from terminal!
>>> 2 + 2
4
>>> exit()  # Exit interactive mode / الخروج من الوضع التفاعلي
```

### Run Python with Arguments
### تشغيل بايثون مع معاملات

```bash
python script.py argument1 argument2
```

Example script that uses arguments:
```python
# greet.py
import sys
name = sys.argv[1] if len(sys.argv) > 1 else "World"
print(f"Hello, {name}!")
```

Run it:
```bash
python greet.py Mohammad
# Output: Hello, Mohammad!
```

---

## Virtual Environment in Terminal
## البيئة الافتراضية في الطرفية

### Understanding Virtual Environments
### فهم البيئات الافتراضية

A virtual environment is like a bubble for your Python project:
- Keeps project dependencies separate
- Prevents version conflicts
- Makes your project portable

البيئة الافتراضية مثل فقاعة لمشروع بايثون:
- تبقي تبعيات المشروع منفصلة
- تمنع تضارب الإصدارات
- تجعل مشروعك قابلاً للنقل

### Activate Virtual Environment
### تفعيل البيئة الافتراضية

**Windows:**
```bash
.\venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

**Success indicators:**
- `(venv)` appears before your prompt
- `which python` shows path with `venv`

**مؤشرات النجاح:**
- `(venv)` يظهر قبل المحث
- `which python` يظهر المسار مع `venv`

### Deactivate Virtual Environment
### إلغاء تفعيل البيئة الافتراضية

```bash
deactivate
```

The `(venv)` prefix disappears.

البادئة `(venv)` تختفي.

### Install Packages with pip
### تثبيت الحزم باستخدام pip

With virtual environment active:
```bash
pip install package_name

# Examples / أمثلة:
pip install requests
pip install numpy
pip install -r requirements.txt  # Install from file / التثبيت من ملف
```

### List Installed Packages
### سرد الحزم المثبتة

```bash
pip list
```

---

## Terminal vs Run Button
## الطرفية مقابل زر التشغيل

When should you use each?

متى يجب استخدام كل منهما؟

### Use Run Button (▶️) When:
### استخدم زر التشغيل (▶️) عندما:

- Running simple scripts without arguments
- Quick testing
- Learning and practicing
- You want clean output

- تشغيل سكريبتات بسيطة بدون معاملات
- اختبار سريع
- التعلم والممارسة
- تريد مخرجات نظيفة

### Use Terminal When:
### استخدم الطرفية عندما:

- Script needs command-line arguments
- Installing packages with pip
- Running multiple scripts
- Using Git commands
- Need more control over execution
- Debugging complex issues

- السكريبت يحتاج معاملات سطر الأوامر
- تثبيت الحزم باستخدام pip
- تشغيل سكريبتات متعددة
- استخدام أوامر Git
- تحتاج مزيد من التحكم في التنفيذ
- تصحيح مشاكل معقدة

---

## Working with Multiple Terminals
## العمل مع طرفيات متعددة

VS Code lets you run multiple terminals at once!

VS Code يتيح لك تشغيل طرفيات متعددة في وقت واحد!

### Create New Terminal
### إنشاء طرفية جديدة

Click the **+** button in terminal panel or press `Ctrl+Shift+`` ` ``

انقر على زر **+** في لوحة الطرفية أو اضغط `Ctrl+Shift+`` ` ``

### Switch Between Terminals
### التبديل بين الطرفيات

- Click terminal names in dropdown
- Or use `Ctrl+PageUp/PageDown`

- انقر على أسماء الطرفيات في القائمة المنسدلة
- أو استخدم `Ctrl+PageUp/PageDown`

### Split Terminal
### تقسيم الطرفية

Click the split icon (⊞) to see two terminals side by side.

انقر على أيقونة التقسيم (⊞) لرؤية طرفيتين جنبًا إلى جنب.

### Why Multiple Terminals?
### لماذا طرفيات متعددة؟

Use cases:
1. **Terminal 1:** Run your Python script
2. **Terminal 2:** Run tests
3. **Terminal 3:** Git commands
4. **Terminal 4:** Install packages

حالات الاستخدام:
1. **الطرفية 1:** تشغيل سكريبت بايثون
2. **الطرفية 2:** تشغيل الاختبارات
3. **الطرفية 3:** أوامر Git
4. **الطرفية 4:** تثبيت الحزم

---

## Terminal Customization
## تخصيص الطرفية

Make the terminal yours!

اجعل الطرفية ملكك!

### Change Terminal Type
### تغيير نوع الطرفية

**Windows users can choose:**
- Command Prompt
- PowerShell (recommended)
- Git Bash
- WSL (Windows Subsystem for Linux)

**مستخدمو ويندوز يمكنهم الاختيار:**
- موجه الأوامر
- PowerShell (موصى به)
- Git Bash
- WSL (نظام ويندوز الفرعي للينكس)

To change: Click dropdown arrow next to + button → Select Default Profile

للتغيير: انقر على السهم المنسدل بجانب زر + → اختر الملف الافتراضي

### Change Font Size
### تغيير حجم الخط

1. Open Settings: `Ctrl+,` (Mac: `Cmd+,`)
2. Search: "terminal font size"
3. Adjust "Terminal › Integrated: Font Size"

<!-- -->

1. افتح الإعدادات: `Ctrl+,` (Mac: `Cmd+,`)
2. ابحث: "terminal font size"
3. اضبط "Terminal › Integrated: Font Size"

### Change Colors
### تغيير الألوان

1. Open Settings
2. Search: "terminal color"
3. Modify colors or choose a theme

<!-- -->

1. افتح الإعدادات
2. ابحث: "terminal color"
3. عدّل الألوان أو اختر مظهرًا

### Terminal Position
### موضع الطرفية

Right-click terminal tab → Move Panel:
- Bottom (default)
- Right
- Left

انقر بزر الماوس الأيمن على تبويب الطرفية → نقل اللوحة:
- أسفل (افتراضي)
- يمين
- يسار

---

## Common Terminal Errors
## أخطاء الطرفية الشائعة

### "Command not found" / "is not recognized"
### "الأمر غير موجود" / "غير معترف به"

**Problem:**
```bash
python: command not found  # Mac/Linux
'python' is not recognized...  # Windows
```

**Solution:**
- Make sure Python is installed
- Try `python3` instead of `python`
- Check PATH environment variable

**الحل:**
- تأكد من تثبيت بايثون
- جرب `python3` بدلاً من `python`
- تحقق من متغير البيئة PATH

### "Permission denied"
### "الإذن مرفوض"

**Problem:**
```bash
bash: ./script.py: Permission denied
```

**Solution (Mac/Linux):**
```bash
chmod +x script.py  # Make executable / جعله قابل للتنفيذ
./script.py         # Now run it / الآن شغّله
```

### "No such file or directory"
### "لا يوجد ملف أو مجلد"

**Problem:**
```bash
python: can't open file 'script.py': No such file or directory
```

**Solution:**
- Check you're in the right directory (`pwd`)
- Check spelling and capitalization
- Use `ls` to see available files

**الحل:**
- تحقق أنك في المجلد الصحيح (`pwd`)
- تحقق من التهجئة والأحرف الكبيرة
- استخدم `ls` لرؤية الملفات المتاحة

### Virtual Environment Not Activating
### البيئة الافتراضية لا تُفعّل

**Problem:** No `(venv)` prefix after activation command

**Solution:**
1. Make sure venv exists: `ls venv/`
2. Use correct activation command for your OS
3. Try creating new terminal
4. Restart VS Code

**الحل:**
1. تأكد من وجود venv: `ls venv/`
2. استخدم أمر التفعيل الصحيح لنظامك
3. جرب إنشاء طرفية جديدة
4. أعد تشغيل VS Code

---

## Hands-On Practice
## ممارسة عملية

Let's practice terminal commands!

لنمارس أوامر الطرفية!

### Exercise 1: Basic Navigation
### التمرين 1: التنقل الأساسي

Try these commands in order:
```bash
# 1. Check where you are / تحقق من مكانك
pwd

# 2. List files / اسرد الملفات
ls  # or dir on Windows

# 3. Go to code-examples / اذهب إلى code-examples
cd code-examples

# 4. List what's there / اسرد ما هناك
ls

# 5. Go back / ارجع
cd ..

# 6. Clear screen / امسح الشاشة
clear  # or cls on Windows
```

### Exercise 2: Create and Run Script
### التمرين 2: أنشئ وشغّل سكريبت

```bash
# 1. Create new folder / أنشئ مجلد جديد
mkdir my_terminal_test

# 2. Go into it / ادخل إليه
cd my_terminal_test

# 3. Create Python file / أنشئ ملف بايثون
echo 'print("Hello from terminal!")' > hello_terminal.py

# 4. Run it / شغّله
python hello_terminal.py

# 5. Clean up - go back and remove folder / نظف - ارجع واحذف المجلد
cd ..
# Be careful with rm/rmdir commands! / كن حذرًا مع أوامر rm/rmdir!
```

### Exercise 3: Virtual Environment Practice
### التمرين 3: ممارسة البيئة الافتراضية

```bash
# 1. Check if venv is active / تحقق إذا كانت venv نشطة
which python  # Mac/Linux
where python  # Windows

# 2. If not active, activate it / إذا لم تكن نشطة، فعّلها
# Windows: .\venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# 3. Install a package / ثبّت حزمة
pip install requests

# 4. List installed packages / اسرد الحزم المثبتة
pip list

# 5. Create requirements file / أنشئ ملف المتطلبات
pip freeze > my_requirements.txt

# 6. View the file / اعرض الملف
cat my_requirements.txt  # Mac/Linux
type my_requirements.txt  # Windows
```

### Exercise 4: Multiple Terminals
### التمرين 4: طرفيات متعددة

1. Create 3 terminals using the + button
2. In Terminal 1: Run `python` for interactive mode
3. In Terminal 2: Navigate to `exercises` folder
4. In Terminal 3: List pip packages
5. Switch between them using the dropdown

<!-- -->

1. أنشئ 3 طرفيات باستخدام زر +
2. في الطرفية 1: شغّل `python` للوضع التفاعلي
3. في الطرفية 2: انتقل إلى مجلد `exercises`
4. في الطرفية 3: اسرد حزم pip
5. تبدّل بينها باستخدام القائمة المنسدلة

---

## Tips & Tricks
## نصائح وحيل

### Auto-Complete with Tab
### الإكمال التلقائي مع Tab

Start typing a filename/folder and press Tab:
```bash
cd cod[TAB]  # Completes to 'cd code-examples/'
```

ابدأ بكتابة اسم ملف/مجلد واضغط Tab:
```bash
cd cod[TAB]  # يكمل إلى 'cd code-examples/'
```

### Command History
### سجل الأوامر

- **Up Arrow ↑**: Previous command
- **Down Arrow ↓**: Next command
- `history`: Show all previous commands

- **السهم لأعلى ↑**: الأمر السابق
- **السهم لأسفل ↓**: الأمر التالي
- `history`: إظهار جميع الأوامر السابقة

### Drag and Drop Files
### سحب وإفلات الملفات

Drag a file from Explorer to terminal to insert its path!

اسحب ملفًا من المستكشف إلى الطرفية لإدراج مساره!

### Copy and Paste
### النسخ واللصق

- **Copy**: Select text → `Ctrl+C` (or `Cmd+C`)
- **Paste**: `Ctrl+V` (or `Cmd+V`)
- Some terminals: Right-click to paste

- **النسخ**: حدد النص → `Ctrl+C` (أو `Cmd+C`)
- **اللصق**: `Ctrl+V` (أو `Cmd+V`)
- بعض الطرفيات: انقر بزر الماوس الأيمن للصق

### Stop Running Process
### إيقاف العملية الجارية

Press `Ctrl+C` to stop a running program.

اضغط `Ctrl+C` لإيقاف برنامج قيد التشغيل.

### Terminal Aliases (Advanced)
### الأسماء المستعارة للطرفية (متقدم)

Create shortcuts for common commands:
```bash
# Add to .bashrc or .zshrc (Mac/Linux)
alias py='python3'
alias activate='source venv/bin/activate'

# Now you can just type:
py script.py
activate
```

أنشئ اختصارات للأوامر الشائعة:
```bash
# أضف إلى .bashrc أو .zshrc (ماك/لينكس)
alias py='python3'
alias activate='source venv/bin/activate'

# الآن يمكنك كتابة:
py script.py
activate
```

---

## Next Steps
## الخطوات التالية

Congratulations! You've mastered the VS Code terminal. You're now ready to:

1. Start coding Python projects efficiently
2. Use Git for version control
3. Install and manage packages
4. Work like a professional developer

تهانينا! لقد أتقنت طرفية VS Code. أنت الآن جاهز لـ:

1. بدء برمجة مشاريع بايثون بكفاءة
2. استخدام Git للتحكم في الإصدارات
3. تثبيت وإدارة الحزم
4. العمل مثل مطور محترف

---

## Additional Resources
## موارد إضافية

- [VS Code Terminal Documentation](https://code.visualstudio.com/docs/editor/integrated-terminal)
- [Command Line Crash Course](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Windows Terminal Guide](https://docs.microsoft.com/en-us/windows/terminal/)
- [Mac Terminal User Guide](https://support.apple.com/guide/terminal/welcome/mac)

- [وثائق طرفية VS Code](https://code.visualstudio.com/docs/editor/integrated-terminal)
- [دورة مكثفة في سطر الأوامر](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line)
- [البيئات الافتراضية لبايثون](https://docs.python.org/3/tutorial/venv.html)
- [دليل Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/)
- [دليل مستخدم Mac Terminal](https://support.apple.com/guide/terminal/welcome/mac)

---

## Quick Reference Card
## بطاقة مرجعية سريعة

### Essential Commands Cheat Sheet
### ورقة غش للأوامر الأساسية

```bash
# Navigation / التنقل
pwd                     # Where am I? / أين أنا؟
ls / dir               # List files / سرد الملفات
cd folder_name         # Enter folder / دخول المجلد
cd ..                  # Go back / الرجوع
clear / cls            # Clear screen / مسح الشاشة

# Files & Folders / الملفات والمجلدات
mkdir folder_name      # Create folder / إنشاء مجلد
touch file.py          # Create file (Mac/Linux) / إنشاء ملف
echo. > file.py        # Create file (Windows) / إنشاء ملف
rm / del file.py       # Delete file / حذف ملف
cp / copy src dst      # Copy file / نسخ ملف
mv / move old new      # Rename/move / إعادة تسمية/نقل

# Python / بايثون
python --version       # Check version / التحقق من الإصدار
python script.py       # Run script / تشغيل سكريبت
pip install package    # Install package / تثبيت حزمة
pip list              # List packages / سرد الحزم
pip freeze            # Show versions / إظهار الإصدارات

# Virtual Environment / البيئة الافتراضية
.\venv\Scripts\activate     # Activate (Windows) / التفعيل
source venv/bin/activate    # Activate (Mac/Linux) / التفعيل
deactivate                  # Deactivate / إلغاء التفعيل

# Control / التحكم
Ctrl+C                # Stop running / إيقاف التشغيل
Tab                   # Auto-complete / إكمال تلقائي
↑ ↓                   # Command history / سجل الأوامر
```

---

**Remember:** The terminal might seem intimidating at first, but with practice, it becomes second nature. Every professional developer uses the terminal daily - you're learning an essential skill!

**تذكر:** قد تبدو الطرفية مخيفة في البداية، لكن مع الممارسة، تصبح طبيعة ثانية. كل مطور محترف يستخدم الطرفية يوميًا - أنت تتعلم مهارة أساسية!

💻 **Master the terminal, master development!** | **أتقن الطرفية، أتقن التطوير!** 💻