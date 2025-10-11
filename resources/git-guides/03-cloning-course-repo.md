# Cloning the Course Repository
# استنساخ مستودع المقرر

## What You'll Learn
## ما ستتعلمه

By the end of this guide, you will have:
- ✅ Cloned the M110 Python course repository to your computer
- ✅ Verified the clone was successful
- ✅ Opened the repository in VS Code
- ✅ Understood the folder structure
- ✅ Made your first safe local change

بنهاية هذا الدليل، ستكون قد:
- ✅ استنسخت مستودع مقرر M110 Python إلى حاسوبك
- ✅ تحققت من نجاح الاستنساخ
- ✅ فتحت المستودع في VS Code
- ✅ فهمت بنية المجلدات
- ✅ أجريت أول تغيير محلي آمن

---

## Why This Matters
## لماذا هذا مهم

Cloning is your first step to accessing all course materials. Once you clone, you'll have:
- All lecture notes and slides references
- Code examples for each week
- Exercises and solutions
- Lab materials
- Setup guides and resources

الاستنساخ هو خطوتك الأولى للوصول إلى جميع مواد المقرر. بمجرد الاستنساخ، سيكون لديك:
- جميع ملاحظات المحاضرات ومراجع الشرائح
- أمثلة الكود لكل أسبوع
- التمارين والحلول
- مواد المختبر
- أدلة الإعداد والموارد

---

## What Does "Cloning" Mean?
## ماذا يعني "الاستنساخ"؟

**Cloning** = Making a complete copy of a repository from GitHub to your computer

**الاستنساخ** = عمل نسخة كاملة من مستودع من GitHub إلى حاسوبك

Think of it like:
- 📥 Downloading a complete folder from the cloud
- 📁 Copying a shared folder to your computer
- 💾 Saving an online project locally

فكر فيه مثل:
- 📥 تحميل مجلد كامل من السحابة
- 📁 نسخ مجلد مشترك إلى حاسوبك
- 💾 حفظ مشروع عبر الإنترنت محليًا

**Important:** You only clone ONCE. After that, you use `git pull` to get updates.

**مهم:** تستنسخ مرة واحدة فقط. بعد ذلك، تستخدم `git pull` للحصول على التحديثات.

---

## Prerequisites
## المتطلبات الأساسية

Before cloning, make sure you have:

قبل الاستنساخ، تأكد من أن لديك:

1. ✅ **Git installed** on your computer
   - Check: Run `git --version` in terminal
   - If not installed: Download from [git-scm.com](https://git-scm.com)

1. ✅ **Git مثبت** على حاسوبك
   - تحقق: شغّل `git --version` في المحطة الطرفية
   - إذا لم يكن مثبتًا: حمّله من [git-scm.com](https://git-scm.com)

2. ✅ **VS Code installed** (recommended editor)
   - Download from [code.visualstudio.com](https://code.visualstudio.com)

2. ✅ **VS Code مثبت** (المحرر الموصى به)
   - حمّله من [code.visualstudio.com](https://code.visualstudio.com)

3. ✅ **Repository URL** from your instructor
   - Example: `https://github.com/YOUR_USERNAME/python-m110.git`

3. ✅ **عنوان URL للمستودع** من مدرسك
   - مثال: `https://github.com/YOUR_USERNAME/python-m110.git`

---

## Step-by-Step Cloning Process
## عملية الاستنساخ خطوة بخطوة

### Step 1: Choose Where to Clone
### الخطوة 1: اختر مكان الاستنساخ

Decide where on your computer you want the course folder. We recommend:

قرر أين على حاسوبك تريد مجلد المقرر. نوصي بـ:

**Recommended Locations:**
**المواقع الموصى بها:**

- **Windows:** `C:\Users\YourName\Documents\AOU\`
- **Mac:** `/Users/YourName/Documents/AOU/`
- **Linux:** `/home/YourName/Documents/AOU/`

**Create the AOU folder first:**
**أنشئ مجلد AOU أولاً:**

Windows (Command Prompt):
```cmd
cd C:\Users\YourName\Documents
mkdir AOU
cd AOU
```

Mac/Linux (Terminal):
```bash
cd ~/Documents
mkdir AOU
cd AOU
```

### Step 2: Open Terminal/Command Prompt
### الخطوة 2: افتح المحطة الطرفية/موجه الأوامر

**Option A: VS Code Terminal (Recommended)**
**الخيار A: محطة VS Code الطرفية (موصى به)**

1. Open VS Code
2. Click `Terminal` → `New Terminal`
3. Or press `Ctrl + ` ` (backtick key)

1. افتح VS Code
2. انقر `Terminal` → `New Terminal`
3. أو اضغط `Ctrl + ` ` (مفتاح backtick)

**Option B: System Terminal**
**الخيار B: محطة النظام الطرفية**

- **Windows:** Press `Win + R`, type `cmd`, press Enter
- **Mac:** Press `Cmd + Space`, type `Terminal`, press Enter

- **Windows:** اضغط `Win + R`، اكتب `cmd`، اضغط Enter
- **Mac:** اضغط `Cmd + Space`، اكتب `Terminal`، اضغط Enter

### Step 3: Navigate to Your Chosen Location
### الخطوة 3: انتقل إلى الموقع المختار

Use the `cd` (change directory) command:

استخدم أمر `cd` (تغيير الدليل):

```bash
cd Documents/AOU
```

Verify you're in the right place:
تحقق من أنك في المكان الصحيح:

```bash
pwd     # Mac/Linux - shows current directory
cd      # Windows - shows current directory
```

### Step 4: Clone the Repository
### الخطوة 4: استنسخ المستودع

Now run the clone command with your repository URL:

الآن شغّل أمر الاستنساخ مع عنوان URL لمستودعك:

```bash
git clone https://github.com/YOUR_USERNAME/python-m110.git
```

**What you'll see:**
**ما ستراه:**

```
Cloning into 'python-m110'...
remote: Enumerating objects: 247, done.
remote: Counting objects: 100% (247/247), done.
remote: Compressing objects: 100% (156/156), done.
remote: Total 247 (delta 89), reused 230 (delta 75)
Receiving objects: 100% (247/247), 3.45 MiB | 2.17 MiB/s, done.
Resolving deltas: 100% (89/89), done.
```

**This means:**
- ✅ "Cloning into 'python-m110'" = Creating the folder
- ✅ "Receiving objects" = Downloading files
- ✅ "Resolving deltas" = Processing file history
- ✅ "done" = Success!

**هذا يعني:**
- ✅ "Cloning into 'python-m110'" = إنشاء المجلد
- ✅ "Receiving objects" = تحميل الملفات
- ✅ "Resolving deltas" = معالجة تاريخ الملفات
- ✅ "done" = نجاح!

### Step 5: Enter the Repository Folder
### الخطوة 5: ادخل مجلد المستودع

```bash
cd python-m110
```

### Step 6: Verify the Clone
### الخطوة 6: تحقق من الاستنساخ

Check that everything worked:

تحقق من أن كل شيء عمل:

```bash
# Check Git status
git status

# Expected output:
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

List the files to see course content:
اسرد الملفات لرؤية محتوى المقرر:

```bash
# Windows
dir

# Mac/Linux
ls -la
```

You should see folders like:
يجب أن ترى مجلدات مثل:

```
lectures/
code-examples/
exercises/
labs/
projects/
resources/
assessments/
student-contributions/
README.md
```

---

## Opening in VS Code
## الفتح في VS Code

### Method 1: From Terminal (Quick)
### الطريقة 1: من المحطة الطرفية (سريع)

While in the python-m110 folder:

أثناء وجودك في مجلد python-m110:

```bash
code .
```

The dot (.) means "current folder"

النقطة (.) تعني "المجلد الحالي"

### Method 2: From VS Code (Visual)
### الطريقة 2: من VS Code (مرئي)

1. Open VS Code
2. Click `File` → `Open Folder`
3. Navigate to `Documents/AOU/python-m110`
4. Click `Select Folder`

1. افتح VS Code
2. انقر `File` → `Open Folder`
3. انتقل إلى `Documents/AOU/python-m110`
4. انقر `Select Folder`

### Method 3: Drag and Drop
### الطريقة 3: السحب والإفلات

1. Open VS Code
2. Find the python-m110 folder in File Explorer/Finder
3. Drag the folder onto the VS Code window

1. افتح VS Code
2. ابحث عن مجلد python-m110 في مستكشف الملفات/Finder
3. اسحب المجلد إلى نافذة VS Code

---

## Understanding the Repository Structure
## فهم بنية المستودع

Once opened in VS Code, you'll see this structure:

بمجرد فتحه في VS Code، سترى هذه البنية:

```
python-m110/
│
├── 📚 lectures/           # Weekly lecture materials
│   ├── week-01-algorithms/
│   ├── week-02-fundamentals/
│   └── ...
│
├── 💻 code-examples/      # Example code for each week
│   ├── week-01-algorithms/
│   ├── week-02-fundamentals/
│   └── ...
│
├── ✏️ exercises/          # Practice problems
│   ├── week-01/
│   ├── week-02/
│   └── ...
│
├── 🧪 labs/              # Lab sessions
│   ├── lab-01-week06/
│   ├── lab-02-week09/
│   └── lab-03-week12/
│
├── 🎯 projects/          # Course projects
│
├── 📖 resources/         # Guides and references
│   ├── setup-guides/
│   ├── git-guides/       # You are here!
│   └── cheatsheets/
│
├── 📝 assessments/       # Exam preparation
│
├── 🌟 student-contributions/  # Student showcase
│
├── 🎮 student-playground/    # YOUR SAFE SPACE!
│
└── 📄 README.md          # Course overview
```

**Important:** The `student-playground/` folder is YOUR space to experiment safely!

**مهم:** مجلد `student-playground/` هو مساحتك للتجربة بأمان!

---

## Your First Local Change (Safe Practice)
## أول تغيير محلي لك (ممارسة آمنة)

Let's make a safe change to practice:

لنجري تغييرًا آمنًا للممارسة:

### Step 1: Create Your Test File
### الخطوة 1: أنشئ ملف الاختبار الخاص بك

In VS Code:
1. Right-click on `student-playground` folder
2. Select `New File`
3. Name it `my_first_file.py`

في VS Code:
1. انقر بزر الماوس الأيمن على مجلد `student-playground`
2. اختر `New File`
3. سمّه `my_first_file.py`

### Step 2: Add Some Code
### الخطوة 2: أضف بعض الكود

Type this in your new file:

اكتب هذا في ملفك الجديد:

```python
"""
My first Python file in the M110 course!
أول ملف Python لي في مقرر M110!

Name: [Your Name]
Date: [Today's Date]
"""

print("Hello, M110!")
print("مرحباً، M110!")

# My learning journey starts here!
# رحلتي التعليمية تبدأ هنا!
```

### Step 3: Save and Check Git Status
### الخطوة 3: احفظ وتحقق من حالة Git

1. Save the file: `Ctrl + S` (Windows/Linux) or `Cmd + S` (Mac)
2. In terminal, run:

1. احفظ الملف: `Ctrl + S` (Windows/Linux) أو `Cmd + S` (Mac)
2. في المحطة الطرفية، شغّل:

```bash
git status
```

You should see:
يجب أن ترى:

```
Untracked files:
  student-playground/my_first_file.py
```

**This is good!** The file is in your playground and won't interfere with course updates.

**هذا جيد!** الملف في ملعبك ولن يتداخل مع تحديثات المقرر.

---

## What NOT to Do
## ما يجب عدم فعله

### ❌ DON'T Push to Main Branch
### ❌ لا تدفع إلى الفرع الرئيسي

Never try to push changes to the main repository. You don't have permission anyway!

لا تحاول أبدًا دفع التغييرات إلى المستودع الرئيسي. ليس لديك الإذن على أي حال!

### ❌ DON'T Modify Course Files
### ❌ لا تعدّل ملفات المقرر

Don't edit files in:
- `lectures/`
- `code-examples/`
- `exercises/` (except for solving them locally)

لا تحرر الملفات في:
- `lectures/`
- `code-examples/`
- `exercises/` (باستثناء حلها محليًا)

### ❌ DON'T Clone Multiple Times
### ❌ لا تستنسخ عدة مرات

One clone is enough! Use `git pull` for updates.

استنساخ واحد كافٍ! استخدم `git pull` للتحديثات.

### ✅ DO Work in student-playground/
### ✅ اعمل في student-playground/

This folder is ignored by Git, so it's safe for all your experiments!

هذا المجلد يتجاهله Git، لذا فهو آمن لجميع تجاربك!

---

## Common Issues and Solutions
## المشاكل الشائعة والحلول

### Issue 1: "destination path already exists"
### المشكلة 1: "destination path already exists"

**Error:**
```
fatal: destination path 'python-m110' already exists and is not an empty directory.
```

**Solution:**
You already cloned! Either:
- Use the existing folder: `cd python-m110`
- Or remove and re-clone: `rm -rf python-m110` then clone again

**الحل:**
لقد استنسخت بالفعل! إما:
- استخدم المجلد الموجود: `cd python-m110`
- أو احذف وأعد الاستنساخ: `rm -rf python-m110` ثم استنسخ مرة أخرى

### Issue 2: "git: command not found"
### المشكلة 2: "git: command not found"

**Solution:**
Git is not installed. Download from [git-scm.com](https://git-scm.com) and install.

**الحل:**
Git غير مثبت. حمّله من [git-scm.com](https://git-scm.com) وثبّته.

### Issue 3: "Permission denied"
### المشكلة 3: "Permission denied"

**Solution:**
Check that you're using HTTPS URL (starts with `https://`), not SSH URL (starts with `git@`).

**الحل:**
تحقق من أنك تستخدم عنوان HTTPS (يبدأ بـ `https://`)، وليس عنوان SSH (يبدأ بـ `git@`).

### Issue 4: Slow cloning
### المشكلة 4: استنساخ بطيء

**Solution:**
This is normal for first clone. The repository has many files. Be patient—it only happens once!

**الحل:**
هذا طبيعي للاستنساخ الأول. المستودع يحتوي على ملفات كثيرة. كن صبورًا—يحدث مرة واحدة فقط!

---

## Verification Checklist
## قائمة التحقق

Make sure you've completed everything:

تأكد من أنك أكملت كل شيء:

- [ ] Git is installed (`git --version` works)
- [ ] Repository is cloned to a good location
- [ ] You can navigate to the folder in terminal
- [ ] `git status` shows "working tree clean"
- [ ] Repository is open in VS Code
- [ ] You can see all course folders
- [ ] You created a test file in `student-playground/`
- [ ] You understand which folders to avoid editing

- [ ] Git مثبت (`git --version` يعمل)
- [ ] المستودع مستنسخ في موقع جيد
- [ ] يمكنك الانتقال إلى المجلد في المحطة الطرفية
- [ ] `git status` يظهر "working tree clean"
- [ ] المستودع مفتوح في VS Code
- [ ] يمكنك رؤية جميع مجلدات المقرر
- [ ] أنشأت ملف اختبار في `student-playground/`
- [ ] تفهم أي المجلدات يجب تجنب تحريرها

---

## Practice Exercises
## تمارين الممارسة

### Exercise 1: Explore the Repository
### التمرين 1: استكشف المستودع

Navigate through the folders and:
1. Find the Week 2 lecture materials
2. Open a code example from Week 1
3. Check what exercises are available

تنقل عبر المجلدات و:
1. ابحث عن مواد محاضرة الأسبوع 2
2. افتح مثال كود من الأسبوع 1
3. تحقق من التمارين المتاحة

### Exercise 2: Practice Git Commands
### التمرين 2: مارس أوامر Git

In the terminal, practice:

في المحطة الطرفية، مارس:

```bash
pwd                    # Where am I?
git status            # Check repository state
git log --oneline -5  # See recent history
git remote -v         # See remote URL
```

### Exercise 3: Create Your Learning Journal
### التمرين 3: أنشئ يومية تعلمك

In `student-playground/`, create `learning_journal.md`:

في `student-playground/`، أنشئ `learning_journal.md`:

```markdown
# My M110 Learning Journal
# يومية تعلمي في M110

## Week 1 Reflections
## تأملات الأسبوع 1

What I learned:
- How to clone a repository
- Basic Git commands
- ...

ما تعلمته:
- كيفية استنساخ مستودع
- أوامر Git الأساسية
- ...
```

---

## Next Steps
## الخطوات التالية

Congratulations! You've successfully cloned the course repository. Next, learn how to stay updated:

تهانينا! لقد نجحت في استنساخ مستودع المقرر. بعد ذلك، تعلم كيفية البقاء محدثًا:

➡️ **[04-staying-updated.md](04-staying-updated.md)** - Learn how to get weekly updates

➡️ **[04-staying-updated.md](04-staying-updated.md)** - تعلم كيفية الحصول على التحديثات الأسبوعية

---

## Quick Summary
## ملخص سريع

You just learned:
- ✅ What cloning means (making a local copy)
- ✅ How to choose a good location for your repository
- ✅ The complete cloning process
- ✅ How to verify successful cloning
- ✅ The repository structure
- ✅ Where to safely make your own changes

لقد تعلمت للتو:
- ✅ ما يعنيه الاستنساخ (عمل نسخة محلية)
- ✅ كيفية اختيار موقع جيد لمستودعك
- ✅ عملية الاستنساخ الكاملة
- ✅ كيفية التحقق من نجاح الاستنساخ
- ✅ بنية المستودع
- ✅ أين تجري تغييراتك الخاصة بأمان

---

## Remember
## تذكر

- 🎯 **Clone once, pull regularly** - Don't clone multiple times
- 📁 **student-playground/ is yours** - Experiment freely there
- 🚫 **Don't modify course files** - Keep them clean for updates
- 💡 **Ask for help if stuck** - We're here to support you

- 🎯 **استنسخ مرة، اسحب بانتظام** - لا تستنسخ عدة مرات
- 📁 **student-playground/ ملكك** - جرّب بحرية هناك
- 🚫 **لا تعدّل ملفات المقرر** - أبقها نظيفة للتحديثات
- 💡 **اطلب المساعدة إذا تعثرت** - نحن هنا لدعمك

---

*Well done! You now have all course materials on your computer!*

*أحسنت! لديك الآن جميع مواد المقرر على حاسوبك!*