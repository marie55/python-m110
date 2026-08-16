# Terminal Commands Cheatsheet
# ورقة مرجع أوامر الطرفية

**For**: M110 Python Programming Students | **لـ**: طلاب برمجة بايثون M110
**Platforms**: Windows (CMD/PowerShell), macOS/Linux (Terminal) | **المنصات**: ويندوز، ماك، لينكس

---

## 🖥️ Opening Terminal
## 🖥️ فتح الطرفية

| Platform | How to Open | Alternative |
|----------|-------------|-------------|
| **Windows** | `Win + R` → type `cmd` → Enter | PowerShell: `Win + X` → PowerShell |
| **macOS** | `Cmd + Space` → type `Terminal` → Enter | Finder → Applications → Utilities → Terminal |
| **Linux** | `Ctrl + Alt + T` | Search for "Terminal" |
| **VS Code** | `` Ctrl/Cmd + ` `` | View → Terminal |

---

## 📁 Navigation Commands
## 📁 أوامر التنقل

| Command | Windows | macOS/Linux | Purpose | Example |
|---------|---------|-------------|---------|---------|
| **Current location** / **الموقع الحالي** | | | | |
| Print working directory | `cd` | `pwd` | Where am I? / أين أنا؟ | `/Users/student/python-m110` |
| **List files** / **قائمة الملفات** | | | | |
| List directory | `dir` | `ls` | See files / رؤية الملفات | Shows all files |
| List detailed | `dir /a` | `ls -la` | Show hidden files / إظهار الملفات المخفية | Detailed list |
| **Change directory** / **تغيير المجلد** | | | | |
| Enter folder | `cd folder` | `cd folder` | Go into folder / دخول مجلد | `cd exercises` |
| Go back | `cd ..` | `cd ..` | Up one level / مستوى أعلى | Back to parent |
| Home directory | `cd %USERPROFILE%` | `cd ~` | Go home / المجلد الرئيسي | User's home |
| Root/Drive | `cd \` | `cd /` | Go to root / الجذر | C:\ or / |

---

## 📂 File & Folder Operations
## 📂 عمليات الملفات والمجلدات

| Command | Windows | macOS/Linux | Purpose | Example |
|---------|---------|-------------|---------|---------|
| **Create** / **إنشاء** | | | | |
| Make directory | `mkdir folder` | `mkdir folder` | Create folder / إنشاء مجلد | `mkdir my-project` |
| Create file | `type nul > file.txt` | `touch file.txt` | Create empty file / إنشاء ملف فارغ | `touch homework.py` |
| **Copy** / **نسخ** | | | | |
| Copy file | `copy source dest` | `cp source dest` | Copy file / نسخ ملف | `cp exercise.py backup.py` |
| Copy folder | `xcopy /s source dest` | `cp -r source dest` | Copy folder / نسخ مجلد | `cp -r chapter1 chapter1-backup` |
| **Move/Rename** / **نقل/إعادة تسمية** | | | | |
| Move/rename | `move old new` | `mv old new` | Move or rename / نقل أو إعادة تسمية | `mv test.py final.py` |
| **Delete** / **حذف** | | | | |
| Delete file | `del file` | `rm file` | Remove file / حذف ملف | `rm temp.py` |
| Delete folder | `rmdir folder` | `rm -r folder` | Remove folder / حذف مجلد | `rm -r old-project` |

⚠️ **Warning**: Delete commands are permanent! / **تحذير**: أوامر الحذف دائمة!

---

## 🐍 Python Commands
## 🐍 أوامر بايثون

| Command | Purpose | Example |
|---------|---------|---------|
| **Check Python** / **فحص بايثون** | | |
| `python --version` | Check Python version / فحص إصدار بايثون | `Python 3.9.7` |
| `python3 --version` | macOS/Linux version / إصدار ماك/لينكس | `Python 3.9.7` |
| **Run Python** / **تشغيل بايثون** | | |
| `python file.py` | Run Python file / تشغيل ملف بايثون | `python homework.py` |
| `python3 file.py` | macOS/Linux / ماك/لينكس | `python3 homework.py` |
| `python` | Interactive mode / الوضع التفاعلي | `>>> ` (Python prompt) |
| `exit()` or `Ctrl+Z` | Exit Python / الخروج من بايثون | Back to terminal |
| **Package Management** / **إدارة الحزم** | | |
| `pip install package` | Install package / تثبيت حزمة | `pip install numpy` |
| `pip list` | List packages / قائمة الحزم | Shows installed packages |
| `pip freeze` | Show versions / إظهار الإصدارات | Package versions |

---

## 📝 File Viewing & Editing
## 📝 عرض وتحرير الملفات

| Command | Windows | macOS/Linux | Purpose | Example |
|---------|---------|-------------|---------|---------|
| **View file** / **عرض ملف** | | | | |
| Display content | `type file` | `cat file` | Show file content / عرض محتوى الملف | `cat homework.py` |
| View with pages | `more file` | `less file` | Page by page / صفحة بصفحة | `less long-file.txt` |
| First lines | `type file \| more` | `head file` | Show beginning / عرض البداية | `head -10 file.py` |
| Last lines | `powershell -command "Get-Content file -Tail 10"` | `tail file` | Show end / عرض النهاية | `tail -10 log.txt` |
| **Simple edit** / **تحرير بسيط** | | | | |
| Nano editor | - | `nano file` | Simple editor / محرر بسيط | `nano homework.py` |
| VS Code | `code file` | `code file` | Open in VS Code / فتح في VS Code | `code homework.py` |

---

## 🔍 Search & Find
## 🔍 البحث والإيجاد

| Command | Windows | macOS/Linux | Purpose | Example |
|---------|---------|-------------|---------|---------|
| **Find files** / **إيجاد الملفات** | | | | |
| Find by name | `dir /s *.py` | `find . -name "*.py"` | Find Python files / إيجاد ملفات بايثون | Lists all .py files |
| **Search in files** / **البحث في الملفات** | | | | |
| Search text | `findstr "text" file` | `grep "text" file` | Find in file / بحث في ملف | `grep "def" homework.py` |
| Search all files | `findstr /s "text" *.py` | `grep -r "text" .` | Search everywhere / بحث شامل | Find "text" in all files |

---

## 🌐 Network & System
## 🌐 الشبكة والنظام

| Command | Windows | macOS/Linux | Purpose |
|---------|---------|-------------|---------|
| **System info** / **معلومات النظام** | | | |
| Clear screen | `cls` | `clear` | Clear terminal / مسح الطرفية |
| System info | `systeminfo` | `uname -a` | System details / تفاصيل النظام |
| Disk usage | `dir` | `df -h` | Disk space / مساحة القرص |
| **Network** / **الشبكة** | | | |
| Test connection | `ping google.com` | `ping google.com` | Check internet / فحص الإنترنت |
| Download file | `curl -O url` | `curl -O url` | Download / تحميل |

---

## ⌨️ Terminal Shortcuts
## ⌨️ اختصارات الطرفية

| Shortcut | Windows | macOS/Linux | Purpose |
|----------|---------|-------------|---------|
| **Navigation** / **التنقل** | | | |
| Previous command | `↑` | `↑` | Command history / سجل الأوامر |
| Next command | `↓` | `↓` | Forward in history / التقدم في السجل |
| Beginning of line | `Home` | `Ctrl+A` | Start of line / بداية السطر |
| End of line | `End` | `Ctrl+E` | End of line / نهاية السطر |
| **Editing** / **التحرير** | | | |
| Cancel command | `Ctrl+C` | `Ctrl+C` | Stop execution / إيقاف التنفيذ |
| Clear line | `Esc` | `Ctrl+U` | Clear current line / مسح السطر الحالي |
| Exit terminal | `exit` | `exit` or `Ctrl+D` | Close terminal / إغلاق الطرفية |
| **Copy/Paste** / **نسخ/لصق** | | | |
| Copy | `Ctrl+C` or Right-click | `Cmd+C` | Copy text / نسخ النص |
| Paste | `Ctrl+V` or Right-click | `Cmd+V` | Paste text / لصق النص |

---

## 📚 Common Student Tasks
## 📚 مهام الطلاب الشائعة

### Task 1: Navigate to project and run Python
### المهمة 1: التنقل للمشروع وتشغيل بايثون
```bash
cd ~/python-m110/code-examples/chapter-01-algorithms
python3 01_sequence_average.py    # Windows: python 01_sequence_average.py
```

### Task 2: Create new project folder
### المهمة 2: إنشاء مجلد مشروع جديد
```bash
mkdir my-homework
cd my-homework
touch homework.py     # or: type nul > homework.py (Windows)
code homework.py      # Open in VS Code
```

### Task 3: Copy exercise for practice
### المهمة 3: نسخ تمرين للممارسة
```bash
cp exercise.py my-solution.py     # or: copy exercise.py my-solution.py (Windows)
python3 my-solution.py            # Windows: python my-solution.py
```

### Task 4: Find all Python files
### المهمة 4: إيجاد جميع ملفات بايثون
```bash
# Windows
dir /s *.py

# macOS/Linux
find . -name "*.py"
```

---

## ⚠️ Common Mistakes
## ⚠️ أخطاء شائعة

| Mistake | Problem | Solution |
|---------|---------|----------|
| **Spaces in paths** / **مسافات في المسارات** | `cd my folder` ❌ | `cd "my folder"` ✅ |
| **Wrong slash** / **شرطة خاطئة** | `cd folder/subfolder` (Windows) ❌ | `cd folder\subfolder` ✅ |
| **Case sensitive** / **حساسية الأحرف** | `CD` instead of `cd` (Linux) ❌ | Use lowercase `cd` ✅ |
| **Python vs Python3** / **بايثون مقابل بايثون3** | `python` not found (Mac) | Use `python3` |

---

## ✅ Pro Tips
## ✅ نصائح احترافية

- 🔄 **Tab completion**: Press `Tab` to auto-complete file names
  **الإكمال التلقائي**: اضغط `Tab` للإكمال التلقائي

- 📝 **Command history**: Use `↑` arrow to repeat commands
  **سجل الأوامر**: استخدم السهم `↑` لتكرار الأوامر

- 🎯 **Drag & drop**: Drag files to terminal to get path
  **السحب والإفلات**: اسحب الملفات للطرفية للحصول على المسار

- 💡 **Multiple commands**: Use `&&` to chain commands
  **أوامر متعددة**: استخدم `&&` لربط الأوامر
  ```bash
  mkdir project && cd project && touch main.py
  ```

---

**📌 Keep this reference while learning terminal commands!**
**📌 احتفظ بهذا المرجع أثناء تعلم أوامر الطرفية!**

---

*M110 Python Programming - Arab Open University, Amman*
*برمجة بايثون M110 - الجامعة العربية المفتوحة، عمان*