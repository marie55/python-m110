# GitHub Repository Cloning Guide
# دليل نسخ مستودع GitHub

⏱️ **Estimated Time:** 10-15 minutes
⏱️ **الوقت المقدر:** 10-15 دقيقة

---

## What is Cloning?
## ما هو النسخ (Cloning)؟

Cloning means creating a local copy of a GitHub repository on your computer. Think of it like downloading a folder from the cloud, but with special Git powers - you can track changes, get updates, and see the full history of the project.

النسخ يعني إنشاء نسخة محلية من مستودع GitHub على حاسوبك. فكر فيه كتحميل مجلد من السحابة، ولكن مع قوى Git الخاصة - يمكنك تتبع التغييرات، والحصول على التحديثات، ورؤية التاريخ الكامل للمشروع.

### Why Clone the Course Repository?
### لماذا ننسخ مستودع المقرر؟

- 📚 **Access all course materials** - Lectures, code examples, exercises
- 📚 **الوصول إلى جميع مواد المقرر** - المحاضرات، أمثلة الكود، التمارين

- 🔄 **Get weekly updates** - Pull new materials as they're added
- 🔄 **الحصول على تحديثات أسبوعية** - سحب المواد الجديدة عند إضافتها

- 💻 **Work offline** - Everything is on your computer
- 💻 **العمل بدون إنترنت** - كل شيء على حاسوبك

- 🎯 **Follow along** - Run code examples locally
- 🎯 **المتابعة** - تشغيل أمثلة الكود محلياً

---

## Prerequisites
## المتطلبات الأساسية

Before cloning the repository:
قبل نسخ المستودع:

- ✅ Git installed (see [03-git-installation.md](03-git-installation.md))
- ✅ Git مثبت (انظر [03-git-installation.md](03-git-installation.md))

- ✅ VS Code installed (see [02-vscode-installation.md](02-vscode-installation.md))
- ✅ VS Code مثبت (انظر [02-vscode-installation.md](02-vscode-installation.md))

- ✅ GitHub account created (see [03-git-installation.md](03-git-installation.md))
- ✅ حساب GitHub منشأ (انظر [03-git-installation.md](03-git-installation.md))

---

## Part 1: Finding the Repository URL
## الجزء 1: إيجاد رابط المستودع

### Step 1: Navigate to the Repository
### الخطوة 1: الانتقال إلى المستودع

1. Open your web browser
   افتح متصفح الإنترنت

2. Go to the course repository on GitHub:
   اذهب إلى مستودع المقرر على GitHub:

   🔗 **[Your instructor will provide the repository URL]**
   🔗 **[سيوفر مدرسك رابط المستودع]**

   Example format: `https://github.com/username/python-m110`
   صيغة المثال: `https://github.com/username/python-m110`

### Step 2: Get the Clone URL
### الخطوة 2: الحصول على رابط النسخ

1. On the repository page, look for the green **Code** button
   في صفحة المستودع، ابحث عن الزر الأخضر **Code**

2. Click the **Code** button
   انقر زر **Code**

3. You'll see a dropdown with three tabs: **HTTPS**, **SSH**, and **GitHub CLI**
   سترى قائمة منسدلة بثلاثة تبويبات: **HTTPS**، **SSH**، و **GitHub CLI**

4. Make sure **HTTPS** is selected (it's the default)
   تأكد من اختيار **HTTPS** (إنه الافتراضي)

5. You'll see a URL like:
   سترى رابطاً مثل:

   ```
   https://github.com/username/python-m110.git
   ```

6. Click the **📋 Copy** icon to copy the URL
   انقر أيقونة **📋 Copy** لنسخ الرابط

📸 **Screenshot location:** GitHub repository page with Code button and HTTPS URL highlighted

💡 **Tip:** Keep this browser tab open - you might need it!
💡 **نصيحة:** احتفظ بهذا التبويب مفتوحاً - قد تحتاجه!

---

## Part 2: Choosing a Location for Your Repository
## الجزء 2: اختيار موقع لمستودعك

Before cloning, decide where to save the repository on your computer.
قبل النسخ، قرر أين ستحفظ المستودع على حاسوبك.

### Recommended Locations
### المواقع الموصى بها

**Windows:**
```
C:\Users\YourName\Documents\Courses\
C:\Users\YourName\Dev\
```

**Mac:**
```
/Users/YourName/Documents/Courses/
/Users/YourName/Dev/
```

**Linux:**
```
/home/yourname/Documents/Courses/
/home/yourname/Dev/
```

### Create a Parent Folder (If Needed)
### إنشاء مجلد أب (إذا لزم الأمر)

It's a good idea to have a dedicated folder for your coding projects:
إنها فكرة جيدة أن يكون لديك مجلد مخصص لمشاريع البرمجة:

**Windows (using File Explorer):**
1. Open File Explorer
2. Navigate to `Documents`
3. Right-click → New → Folder
4. Name it `Dev` or `Courses`

**Mac (using Finder):**
1. Open Finder
2. Go to your home folder
3. Right-click → New Folder
4. Name it `Dev` or `Courses`

**Using Terminal (All platforms):**

```bash
# Windows
mkdir C:\Users\YourName\Dev

# Mac/Linux
mkdir ~/Dev
```

---

## Part 3: Cloning the Repository
## الجزء 3: نسخ المستودع

Now let's clone the repository! We'll cover three methods.
الآن دعنا ننسخ المستودع! سنغطي ثلاث طرق.

### Method 1: Clone Using VS Code (Recommended for Beginners)
### الطريقة 1: النسخ باستخدام VS Code (موصى به للمبتدئين)

This is the easiest method!
هذه هي الطريقة الأسهل!

1. Open VS Code
   افتح VS Code

2. Press **Ctrl + Shift + P** (Windows/Linux) or **⌘ + Shift + P** (Mac)
   اضغط **Ctrl + Shift + P** (ويندوز/لينكس) أو **⌘ + Shift + P** (ماك)

3. Type: **"Git: Clone"**
   اكتب: **"Git: Clone"**

4. Press **Enter**
   اضغط **Enter**

5. Paste the repository URL you copied earlier:
   الصق رابط المستودع الذي نسخته سابقاً:

   ```
   https://github.com/username/python-m110.git
   ```

6. Press **Enter**
   اضغط **Enter**

7. A file browser will open. Navigate to where you want to save the repository
   سيفتح متصفح ملفات. انتقل إلى حيث تريد حفظ المستودع

   Example: `C:\Users\YourName\Dev` or `~/Dev`
   مثال: `C:\Users\YourName\Dev` أو `~/Dev`

8. Click **Select Repository Location**
   انقر **Select Repository Location**

9. Wait for cloning to complete (10-60 seconds depending on repository size)
   انتظر اكتمال النسخ (10-60 ثانية حسب حجم المستودع)

10. VS Code will ask: **"Would you like to open the cloned repository?"**
    سيسأل VS Code: **"Would you like to open the cloned repository?"**

11. Click **Open**
    انقر **Open**

✅ **Success! The repository is now cloned and open in VS Code!**
✅ **نجح! تم نسخ المستودع وفتحه في VS Code الآن!**

📸 **Screenshot locations:**
- Command Palette with "Git: Clone"
- File browser selecting location
- VS Code with cloned repository open

### Method 2: Clone Using Terminal in VS Code
### الطريقة 2: النسخ باستخدام الطرفية في VS Code

For those comfortable with command line:
لأولئك المرتاحين مع سطر الأوامر:

1. Open VS Code
   افتح VS Code

2. Open the integrated terminal: **View** → **Terminal** (or Ctrl/⌘ + `)
   افتح الطرفية المدمجة: **View** → **Terminal** (أو Ctrl/⌘ + `)

3. Navigate to where you want to clone (your parent folder):
   انتقل إلى حيث تريد النسخ (مجلد الأب):

   **Windows:**
   ```bash
   cd C:\Users\YourName\Dev
   ```

   **Mac/Linux:**
   ```bash
   cd ~/Dev
   ```

4. Run the clone command:
   نفذ أمر النسخ:

   ```bash
   git clone https://github.com/username/python-m110.git
   ```

   Replace the URL with your actual repository URL
   استبدل الرابط برابط المستودع الفعلي

5. Press **Enter**
   اضغط **Enter**

6. You'll see output like:
   سترى مخرجات مثل:

   ```
   Cloning into 'python-m110'...
   remote: Enumerating objects: 150, done.
   remote: Counting objects: 100% (150/150), done.
   remote: Compressing objects: 100% (95/95), done.
   remote: Total 150 (delta 45), reused 120 (delta 30)
   Receiving objects: 100% (150/150), 2.5 MiB | 1.2 MiB/s, done.
   Resolving deltas: 100% (45/45), done.
   ```

7. Once complete, navigate into the cloned folder:
   بمجرد الانتهاء، انتقل إلى المجلد المنسوخ:

   ```bash
   cd python-m110
   ```

8. Open it in VS Code:
   افتحه في VS Code:

   ```bash
   code .
   ```

   The `.` means "current directory"
   الـ `.` تعني "المجلد الحالي"

### Method 3: Clone Using System Terminal
### الطريقة 3: النسخ باستخدام طرفية النظام

Same as Method 2, but using your system's terminal instead of VS Code's:
نفس الطريقة 2، لكن باستخدام طرفية نظامك بدلاً من طرفية VS Code:

**Windows (Command Prompt or PowerShell):**
1. Press **Windows + R**
2. Type `cmd` or `powershell`, press Enter
3. Navigate to your desired folder
4. Run `git clone` command

**Mac (Terminal):**
1. Press **⌘ + Space**, type "Terminal"
2. Navigate to your desired folder
3. Run `git clone` command

**Linux:**
1. Press **Ctrl + Alt + T**
2. Navigate to your desired folder
3. Run `git clone` command

---

## Part 4: Exploring the Cloned Repository
## الجزء 4: استكشاف المستودع المنسوخ

Let's explore what you just cloned!
دعنا نستكشف ما نسخته للتو!

### Repository Structure
### بنية المستودع

In VS Code's Explorer (left sidebar), you should see:
في مستكشف VS Code (الشريط الجانبي الأيسر)، يجب أن ترى:

```
python-m110/
├── .git/                    # Git internals (don't touch!)
├── .gitignore              # Files Git should ignore
├── README.md               # Course overview
├── requirements.txt        # Python packages needed
├── lectures/               # Weekly lecture notes
├── code-examples/          # Runnable Python examples
├── exercises/              # Practice problems
├── labs/                   # Lab sessions
├── projects/               # Semester projects
├── resources/              # Setup guides and cheatsheets
├── assessments/            # Exam prep materials
└── student-contributions/  # Student work showcase
```

### Opening Files
### فتح الملفات

1. Click on any folder in the Explorer to expand it
   انقر على أي مجلد في المستكشف لتوسيعه

2. Click on a file to open it
   انقر على ملف لفتحه

3. Try opening `README.md` - it shows the course overview
   حاول فتح `README.md` - يعرض نظرة عامة على المقرر

📸 **Screenshot location:** VS Code Explorer showing repository structure

### Understanding the .git Folder
### فهم مجلد .git

The `.git` folder contains all Git history and metadata.
مجلد `.git` يحتوي على كل تاريخ Git والبيانات الوصفية.

⚠️ **Important:** Never delete or modify the `.git` folder manually!
⚠️ **مهم:** لا تحذف أو تعدل مجلد `.git` يدوياً أبداً!

If you don't see `.git` in VS Code:
إذا لم ترَ `.git` في VS Code:

- It's hidden by default (which is fine!)
- إنه مخفي افتراضياً (وهذا جيد!)

- Git can still access it
- Git لا يزال يمكنه الوصول إليه

---

## Part 5: Pulling Updates
## الجزء 5: سحب التحديثات

Your instructor will add new materials weekly. Here's how to get them!
سيضيف مدرسك مواد جديدة أسبوعياً. إليك كيفية الحصول عليها!

### What is Pulling?
### ما هو السحب (Pulling)؟

Pulling downloads the latest changes from GitHub and merges them into your local repository.
السحب يحمل أحدث التغييرات من GitHub ويدمجها في مستودعك المحلي.

### Method 1: Pull Using VS Code UI (Easiest)
### الطريقة 1: السحب باستخدام واجهة VS Code (الأسهل)

1. Open your repository in VS Code
   افتح مستودعك في VS Code

2. Look at the **bottom-left** of the window
   انظر إلى **أسفل اليسار** في النافذة

3. You'll see a sync icon (🔄) with numbers
   سترى أيقونة مزامنة (🔄) مع أرقام

4. Click the **🔄 Sync** icon
   انقر أيقونة **🔄 Sync**

5. VS Code will pull new changes automatically
   سيسحب VS Code التغييرات الجديدة تلقائياً

6. You'll see a notification: **"Successfully pulled X commits"**
   سترى إشعاراً: **"Successfully pulled X commits"**

📸 **Screenshot location:** VS Code status bar with sync icon

### Method 2: Pull Using Source Control Panel
### الطريقة 2: السحب باستخدام لوحة التحكم بالمصدر

1. Click the **Source Control** icon (🌿) in the Activity Bar
   انقر أيقونة **Source Control** (🌿) في شريط النشاط

2. Click the **⋯** (three dots) at the top
   انقر **⋯** (ثلاث نقاط) في الأعلى

3. Select **Pull** from the menu
   اختر **Pull** من القائمة

4. Wait for the pull to complete
   انتظر اكتمال السحب

### Method 3: Pull Using Terminal
### الطريقة 3: السحب باستخدام الطرفية

1. Open the terminal in VS Code (Ctrl/⌘ + `)
   افتح الطرفية في VS Code (Ctrl/⌘ + `)

2. Make sure you're in the repository folder:
   تأكد من أنك في مجلد المستودع:

   ```bash
   pwd
   ```

   Should show path ending with `python-m110`
   يجب أن يظهر مسار ينتهي بـ `python-m110`

3. Run the pull command:
   نفذ أمر السحب:

   ```bash
   git pull
   ```

4. You'll see output like:
   سترى مخرجات مثل:

   ```
   remote: Enumerating objects: 10, done.
   remote: Counting objects: 100% (10/10), done.
   remote: Compressing objects: 100% (5/5), done.
   remote: Total 8 (delta 3), reused 6 (delta 1)
   Unpacking objects: 100% (8/8), done.
   From https://github.com/username/python-m110
      abc1234..def5678  main       -> origin/main
   Updating abc1234..def5678
   Fast-forward
    lectures/week-02/README.md | 50 +++++++++++++++++++++++++++++++++
    1 file changed, 50 insertions(+)
   ```

### When to Pull
### متى تسحب

- 📅 **Weekly** - At the start of each week to get new lecture materials
- 📅 **أسبوعياً** - في بداية كل أسبوع للحصول على مواد محاضرات جديدة

- 🔔 **When notified** - When your instructor announces new materials
- 🔔 **عند الإشعار** - عندما يعلن مدرسك عن مواد جديدة

- 🐛 **Before reporting issues** - Make sure you have the latest version
- 🐛 **قبل الإبلاغ عن مشاكل** - تأكد من أن لديك أحدث إصدار

💡 **Tip:** Get in the habit of pulling before you start working each day!
💡 **نصيحة:** اعتد على السحب قبل أن تبدأ العمل كل يوم!

---

## Part 6: Understanding .gitignore
## الجزء 6: فهم .gitignore

### What is .gitignore?
### ما هو .gitignore؟

`.gitignore` is a file that tells Git which files to ignore (not track). This keeps your repository clean.

`.gitignore` هو ملف يخبر Git بأي الملفات يتجاهل (لا يتتبع). هذا يحافظ على مستودعك نظيفاً.

### What's Ignored in Our Repository?
### ما الذي يُتجاهل في مستودعنا؟

Open `.gitignore` in VS Code to see:
افتح `.gitignore` في VS Code لترى:

```gitignore
# Virtual environment / البيئة الافتراضية
venv/
.venv/

# Python cache / ذاكرة التخزين المؤقت لبايثون
__pycache__/
*.pyc
*.pyo

# IDE settings / إعدادات IDE
.vscode/
.idea/

# OS files / ملفات نظام التشغيل
.DS_Store
Thumbs.db

# Personal notes / ملاحظات شخصية
*.personal.md
```

### Why These Files?
### لماذا هذه الملفات؟

- **venv/** - Virtual environment is recreated locally, no need to share
- **venv/** - البيئة الافتراضية تُعاد محلياً، لا حاجة لمشاركتها

- **__pycache__/** - Python temporary files, different per system
- **__pycache__/** - ملفات بايثون المؤقتة، مختلفة لكل نظام

- **.vscode/** - Personal editor settings
- **.vscode/** - إعدادات المحرر الشخصية

- **.DS_Store** - Mac system files
- **.DS_Store** - ملفات نظام ماك

You don't need to modify `.gitignore` for this course!
لا تحتاج لتعديل `.gitignore` في هذا المقرر!

---

## Part 7: Read-Only Workflow (For Students)
## الجزء 7: سير العمل للقراءة فقط (للطلاب)

As a student, you'll use a **read-only workflow** - you can view and pull updates, but won't push changes back to the main repository.
كطالب، ستستخدم **سير عمل للقراءة فقط** - يمكنك العرض وسحب التحديثات، لكن لن ترسل التغييرات إلى المستودع الرئيسي.

### Your Workflow
### سير عملك

1. **Clone once** - At the start of the semester
   **انسخ مرة واحدة** - في بداية الفصل الدراسي

2. **Pull regularly** - Weekly or when notified
   **اسحب بانتظام** - أسبوعياً أو عند الإشعار

3. **Explore and run code** - Experiment with examples
   **استكشف وشغّل الكود** - جرب الأمثلة

4. **Make local changes** - Edit files for practice
   **أجرِ تغييرات محلية** - عدّل الملفات للممارسة

5. **Don't push** - Changes stay on your computer
   **لا ترسل** - التغييرات تبقى على حاسوبك

### Making Local Changes
### إجراء تغييرات محلية

You can freely modify files for practice:
يمكنك تعديل الملفات بحرية للممارسة:

- Edit code examples
- عدّل أمثلة الكود

- Add your own comments
- أضف تعليقاتك الخاصة

- Create new files for experimentation
- أنشئ ملفات جديدة للتجربة

- Solve exercises and save solutions
- حل التمارين واحفظ الحلول

### What If I Break Something?
### ماذا لو أتلفت شيئاً؟

Don't worry! You can easily restore files:
لا تقلق! يمكنك استعادة الملفات بسهولة:

**Restore a single file:**
**استعادة ملف واحد:**

```bash
git checkout filename.py
```

**Restore everything to original state:**
**استعادة كل شيء إلى الحالة الأصلية:**

```bash
git reset --hard
```

⚠️ **Warning:** This will delete all your local changes!
⚠️ **تحذير:** هذا سيحذف جميع تغييراتك المحلية!

---

## Troubleshooting
## استكشاف الأخطاء وإصلاحها

### ❌ "Repository not found" error
### ❌ خطأ "Repository not found"

**Problem:** Wrong URL or private repository
**المشكلة:** رابط خاطئ أو مستودع خاص

**Solution:**
**الحل:**

1. Double-check the repository URL
   تحقق مرة أخرى من رابط المستودع

2. Make sure you're logged into GitHub
   تأكد من أنك مسجل دخول إلى GitHub

3. Contact your instructor if the repository is private
   اتصل بمدرسك إذا كان المستودع خاصاً

### ❌ "Authentication failed" error
### ❌ خطأ "Authentication failed"

**Problem:** GitHub credentials needed
**المشكلة:** بيانات اعتماد GitHub مطلوبة

**Solution (Windows):**
**الحل (ويندوز):**

1. Git Credential Manager will pop up
   سيظهر Git Credential Manager

2. Sign in with your GitHub account
   سجل دخول بحساب GitHub الخاص بك

**Solution (Mac/Linux):**
**الحل (ماك/لينكس):**

1. Use a Personal Access Token instead of password
   استخدم رمز وصول شخصي بدلاً من كلمة المرور

2. Create one at: Settings → Developer settings → Personal access tokens
   أنشئ واحداً في: Settings → Developer settings → Personal access tokens

### ❌ "already exists" error
### ❌ خطأ "already exists"

**Problem:** Folder with same name already exists
**المشكلة:** مجلد بنفس الاسم موجود بالفعل

**Solution:**
**الحل:**

1. Delete or rename the existing folder
   احذف أو أعد تسمية المجلد الموجود

2. Clone to a different location
   انسخ إلى موقع مختلف

3. Or specify a different name:
   أو حدد اسماً مختلفاً:

   ```bash
   git clone <url> python-m110-backup
   ```

### ❌ "Merge conflict" when pulling
### ❌ "تعارض دمج" عند السحب

**Problem:** Your local changes conflict with remote updates
**المشكلة:** تغييراتك المحلية تتعارض مع التحديثات البعيدة

**Solution 1 - Keep remote version (discard your changes):**
**الحل 1 - احتفظ بالنسخة البعيدة (تجاهل تغييراتك):**

```bash
git reset --hard
git pull
```

**Solution 2 - Keep your changes (stash them):**
**الحل 2 - احتفظ بتغييراتك (خبّئها):**

```bash
git stash
git pull
git stash pop
```

### ❌ Clone is very slow
### ❌ النسخ بطيء جداً

**Problem:** Large repository or slow internet
**المشكلة:** مستودع كبير أو إنترنت بطيء

**Solution:**
**الحل:**

1. Use a wired connection if possible
   استخدم اتصالاً سلكياً إن أمكن

2. Close other internet-heavy applications
   أغلق التطبيقات الأخرى كثيفة الاستخدام للإنترنت

3. Try cloning with depth limit (gets recent history only):
   حاول النسخ بحد عمق (يحصل على التاريخ الحديث فقط):

   ```bash
   git clone --depth 1 <url>
   ```

### ❌ "Permission denied" error
### ❌ خطأ "Permission denied"

**Solution:**
**الحل:**

1. Make sure you have write permissions to the target folder
   تأكد من أن لديك أذونات الكتابة إلى المجلد الهدف

2. Don't clone into system folders
   لا تنسخ إلى مجلدات النظام

3. Use your Documents or home folder instead
   استخدم مجلد Documents أو المنزل بدلاً من ذلك

---

## Quick Reference
## مرجع سريع

### Essential Git Commands
### أوامر Git الأساسية

```bash
# Clone a repository / نسخ مستودع
git clone <repository-url>

# Check repository status / التحقق من حالة المستودع
git status

# Pull latest changes / سحب أحدث التغييرات
git pull

# View commit history / عرض تاريخ الـ commits
git log

# Restore a file to original / استعادة ملف إلى الأصل
git checkout <filename>

# Discard all local changes / تجاهل جميع التغييرات المحلية
git reset --hard
```

### VS Code Git Actions
### إجراءات Git في VS Code

- **Clone:** Ctrl/⌘ + Shift + P → "Git: Clone"
- **نسخ:** Ctrl/⌘ + Shift + P → "Git: Clone"

- **Pull:** Click sync icon (🔄) in status bar
- **سحب:** انقر أيقونة المزامنة (🔄) في شريط الحالة

- **View changes:** Source Control panel (🌿)
- **عرض التغييرات:** لوحة التحكم بالمصدر (🌿)

---

## Next Steps
## الخطوات التالية

Perfect! You've cloned the course repository! Now:
ممتاز! لقد نسخت مستودع المقرر! الآن:

1. **Set up Virtual Environment** - [04-venv-setup.md](04-venv-setup.md)
   **إعداد البيئة الافتراضية** - [04-venv-setup.md](04-venv-setup.md)

2. **Run Your First Program** - [07-running-first-program.md](07-running-first-program.md)
   **تشغيل برنامجك الأول** - [07-running-first-program.md](07-running-first-program.md)

3. **Explore Week 1 Materials** - Check `lectures/week-01/`
   **استكشف مواد الأسبوع 1** - راجع `lectures/week-01/`

---

## Additional Resources
## موارد إضافية

- 📖 [Git Clone Documentation](https://git-scm.com/docs/git-clone)
- 📖 [وثائق Git Clone](https://git-scm.com/docs/git-clone)

- 📖 [GitHub Quickstart](https://docs.github.com/en/get-started/quickstart)
- 📖 [بداية سريعة GitHub](https://docs.github.com/en/get-started/quickstart)

- 🎥 [Git Clone Tutorial](https://www.youtube.com/watch?v=CKcqniGu3tA)
- 🎥 [درس Git Clone](https://www.youtube.com/watch?v=CKcqniGu3tA)

---

*Last Updated: October 2025*
*آخر تحديث: أكتوبر 2025*
