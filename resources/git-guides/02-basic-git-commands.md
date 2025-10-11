# Basic Git Commands
# أوامر Git الأساسية

## What You'll Learn
## ما ستتعلمه

By the end of this guide, you'll know how to use:
- ✅ `git clone` - Get a copy of the course repository
- ✅ `git status` - Check what's happening in your repository
- ✅ `git pull` - Get updates from the instructor
- ✅ `git log` - View the history of changes
- ✅ `git diff` - See what changed in files

بنهاية هذا الدليل، ستعرف كيفية استخدام:
- ✅ `git clone` - الحصول على نسخة من مستودع المقرر
- ✅ `git status` - التحقق مما يحدث في مستودعك
- ✅ `git pull` - الحصول على التحديثات من المدرس
- ✅ `git log` - عرض تاريخ التغييرات
- ✅ `git diff` - رؤية ما تغير في الملفات

---

## Why This Matters
## لماذا هذا مهم

These five commands are all you need to succeed in this course! Master these, and you'll be able to:
- Stay updated with course materials
- Track your own progress
- Understand what's changing in the code

هذه الأوامر الخمسة هي كل ما تحتاجه للنجاح في هذا المقرر! أتقنها، وستتمكن من:
- البقاء محدثًا مع مواد المقرر
- تتبع تقدمك الخاص
- فهم ما يتغير في الكود

---

## Before You Start: The Terminal
## قبل أن تبدأ: المحطة الطرفية (Terminal)

### What is the Terminal?
### ما هي المحطة الطرفية؟

The terminal (also called command line or console) is where you type Git commands. Think of it as texting with your computer!

المحطة الطرفية (تسمى أيضًا سطر الأوامر أو وحدة التحكم) هي حيث تكتب أوامر Git. فكر فيها كالمراسلة النصية مع حاسوبك!

### Opening the Terminal
### فتح المحطة الطرفية

**Windows:**
- Press `Windows + R`, type `cmd`, press Enter
- Or use Git Bash (installed with Git)

**Windows:**
- اضغط `Windows + R`، اكتب `cmd`، اضغط Enter
- أو استخدم Git Bash (مثبت مع Git)

**Mac:**
- Press `Cmd + Space`, type `Terminal`, press Enter
- Or find Terminal in Applications → Utilities

**Mac:**
- اضغط `Cmd + Space`، اكتب `Terminal`، اضغط Enter
- أو ابحث عن Terminal في Applications → Utilities

**VS Code (Recommended):**
- Open VS Code
- Press `Ctrl + ` ` (backtick) or `View → Terminal`

**VS Code (موصى به):**
- افتح VS Code
- اضغط `Ctrl + ` ` أو `View → Terminal`

---

## Command 1: git clone
## الأمر 1: git clone

### What It Does
### ما يفعله

Creates a copy of a repository from GitHub to your computer. You only do this ONCE per repository.

ينشئ نسخة من مستودع من GitHub إلى حاسوبك. تفعل هذا مرة واحدة فقط لكل مستودع.

### When to Use It
### متى تستخدمه

- First time getting the course materials
- When you want a fresh copy of any GitHub project

- أول مرة للحصول على مواد المقرر
- عندما تريد نسخة جديدة من أي مشروع GitHub

### How to Use It
### كيفية استخدامه

```bash
git clone https://github.com/YOUR_USERNAME/python-m110.git
```

### Command Breakdown
### تفصيل الأمر

```
git clone [URL]
│    │      │
│    │      └── The GitHub repository address
│    │          عنوان مستودع GitHub
│    └── The clone command
│        أمر النسخ
└── The Git program
    برنامج Git
```

### Example with Output
### مثال مع المخرجات

```bash
$ git clone https://github.com/YOUR_USERNAME/python-m110.git
Cloning into 'python-m110'...
remote: Enumerating objects: 150, done.
remote: Counting objects: 100% (150/150), done.
remote: Compressing objects: 100% (89/89), done.
Receiving objects: 100% (150/150), 2.34 MiB | 1.23 MiB/s, done.
```

**What this means:**
- ✅ "Cloning into..." = Creating a new folder
- ✅ "Receiving objects..." = Downloading files
- ✅ "done" = Success!

**ماذا يعني هذا:**
- ✅ "Cloning into..." = إنشاء مجلد جديد
- ✅ "Receiving objects..." = تحميل الملفات
- ✅ "done" = نجاح!

### Common Errors and Solutions
### الأخطاء الشائعة والحلول

**Error:** `fatal: destination path 'python-m110' already exists`

**Solution:** The folder already exists. Either delete it or clone to a different location.

**الخطأ:** `fatal: destination path 'python-m110' already exists`

**الحل:** المجلد موجود بالفعل. احذفه أو انسخ في موقع مختلف.

---

## Command 2: git status
## الأمر 2: git status

### What It Does
### ما يفعله

Shows the current state of your repository. Like asking "What's going on here?"

يعرض الحالة الحالية لمستودعك. مثل السؤال "ماذا يحدث هنا؟"

### When to Use It
### متى تستخدمه

- Before doing anything (to see current state)
- After making changes (to see what changed)
- When confused (it always helps!)

- قبل فعل أي شيء (لرؤية الحالة الحالية)
- بعد إجراء تغييرات (لرؤية ما تغير)
- عند الارتباك (دائمًا ما يساعد!)

### How to Use It
### كيفية استخدامه

```bash
git status
```

### Example with Output
### مثال مع المخرجات

**Clean repository (no changes):**
**مستودع نظيف (لا تغييرات):**

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

**With changes:**
**مع تغييرات:**

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  modified:   exercises/week-02/practice.py

Untracked files:
  student-playground/my_test.py
```

### Understanding the Output
### فهم المخرجات

| Status Message | What It Means | Arabic |
|---------------|---------------|---------|
| `working tree clean` | No changes, all good! | لا تغييرات، كل شيء جيد! |
| `modified:` | You changed this file | قمت بتغيير هذا الملف |
| `Untracked files:` | New files Git doesn't know about | ملفات جديدة لا يعرفها Git |
| `Your branch is up to date` | No new updates available | لا تحديثات جديدة متاحة |
| `Your branch is behind` | Updates available! Run git pull | تحديثات متاحة! شغّل git pull |

### Pro Tip
### نصيحة احترافية

Run `git status` frequently! It's impossible to break anything with this command.

شغّل `git status` بكثرة! من المستحيل كسر أي شيء بهذا الأمر.

---

## Command 3: git pull
## الأمر 3: git pull

### What It Does
### ما يفعله

Downloads the latest changes from GitHub to your computer. Like refreshing a webpage!

يحمّل أحدث التغييرات من GitHub إلى حاسوبك. مثل تحديث صفحة ويب!

### When to Use It
### متى تستخدمه

- Every Sunday before lecture
- Every Thursday before lab
- Whenever instructor announces new materials
- When `git status` says "Your branch is behind"

- كل يوم أحد قبل المحاضرة
- كل يوم خميس قبل المختبر
- كلما أعلن المدرس عن مواد جديدة
- عندما يقول `git status` "Your branch is behind"

### How to Use It
### كيفية استخدامه

```bash
git pull
```

Or more specifically:
أو بشكل أكثر تحديدًا:

```bash
git pull origin main
```

### Command Breakdown
### تفصيل الأمر

```
git pull origin main
│    │     │     │
│    │     │     └── The branch name (usually 'main')
│    │     │         اسم الفرع (عادة 'main')
│    │     └── The remote name (usually 'origin')
│    │         اسم البعيد (عادة 'origin')
│    └── The pull command
│        أمر السحب
└── The Git program
    برنامج Git
```

### Example with Output
### مثال مع المخرجات

**When there are updates:**
**عندما توجد تحديثات:**

```bash
$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
Unpacking objects: 100% (3/3), done.
From https://github.com/YOUR_USERNAME/python-m110
   a1b2c3d..e4f5g6h  main     -> origin/main
Updating a1b2c3d..e4f5g6h
Fast-forward
 lectures/week-03/README.md | 125 +++++++++++++++++++
 exercises/week-03/loops.py |  45 +++++++
 2 files changed, 170 insertions(+)
```

**What this tells you:**
- ✅ Files updated: `lectures/week-03/README.md` and `exercises/week-03/loops.py`
- ✅ 170 new lines added
- ✅ Successfully updated!

**ماذا يخبرك هذا:**
- ✅ الملفات المحدثة: `lectures/week-03/README.md` و `exercises/week-03/loops.py`
- ✅ تم إضافة 170 سطرًا جديدًا
- ✅ تم التحديث بنجاح!

**When already up to date:**
**عندما تكون محدثًا بالفعل:**

```bash
$ git pull
Already up to date.
```

### Common Errors and Solutions
### الأخطاء الشائعة والحلول

**Error:** `error: Your local changes would be overwritten`

**Solution:** You have local changes. Save them first or stash them:
```bash
git stash        # Temporarily save changes
git pull         # Get updates
git stash pop    # Restore your changes
```

**الخطأ:** `error: Your local changes would be overwritten`

**الحل:** لديك تغييرات محلية. احفظها أولاً أو خزّنها:
```bash
git stash        # حفظ التغييرات مؤقتًا
git pull         # الحصول على التحديثات
git stash pop    # استعادة تغييراتك
```

---

## Command 4: git log
## الأمر 4: git log

### What It Does
### ما يفعله

Shows the history of all commits (changes) in the repository. Like viewing a timeline!

يعرض تاريخ جميع الالتزامات (التغييرات) في المستودع. مثل عرض خط زمني!

### When to Use It
### متى تستخدمه

- To see what's been added recently
- To understand project history
- To find when something was changed

- لرؤية ما تم إضافته مؤخرًا
- لفهم تاريخ المشروع
- للعثور على متى تم تغيير شيء ما

### How to Use It
### كيفية استخدامه

Basic log:
السجل الأساسي:

```bash
git log
```

Simpler one-line format:
تنسيق أبسط في سطر واحد:

```bash
git log --oneline
```

Last 5 commits only:
آخر 5 التزامات فقط:

```bash
git log --oneline -5
```

### Example with Output
### مثال مع المخرجات

```bash
$ git log --oneline -5
e4f5g6h (HEAD -> main, origin/main) Add week 3 exercises
a1b2c3d Update lecture notes for week 2
7h8i9j0 Fix typo in README
k1l2m3n Add installation guide
o4p5q6r Initial course setup
```

### Understanding the Output
### فهم المخرجات

```
e4f5g6h (HEAD -> main) Add week 3 exercises
│        │       │      └── Commit message (what changed)
│        │       │          رسالة الالتزام (ما تغير)
│        │       └── Current branch
│        │           الفرع الحالي
│        └── You are here
│            أنت هنا
└── Commit ID (unique identifier)
    معرف الالتزام (معرف فريد)
```

### Exiting git log
### الخروج من git log

Press `q` to quit viewing the log.

اضغط `q` للخروج من عرض السجل.

---

## Command 5: git diff
## الأمر 5: git diff

### What It Does
### ما يفعله

Shows exactly what changed in files. Like "Track Changes" in Microsoft Word!

يعرض بالضبط ما تغير في الملفات. مثل "تتبع التغييرات" في Microsoft Word!

### When to Use It
### متى تستخدمه

- Before saving changes (to review what you did)
- To understand what instructor changed
- To compare versions

- قبل حفظ التغييرات (لمراجعة ما فعلته)
- لفهم ما غيّره المدرس
- لمقارنة الإصدارات

### How to Use It
### كيفية استخدامه

See all changes:
رؤية جميع التغييرات:

```bash
git diff
```

See changes in specific file:
رؤية التغييرات في ملف محدد:

```bash
git diff exercises/week-02/practice.py
```

### Example with Output
### مثال مع المخرجات

```diff
$ git diff exercises/week-02/practice.py
diff --git a/exercises/week-02/practice.py b/exercises/week-02/practice.py
index a1b2c3d..e4f5g6h 100644
--- a/exercises/week-02/practice.py
+++ b/exercises/week-02/practice.py
@@ -10,7 +10,7 @@ def calculate_average(numbers):
     total = sum(numbers)
     count = len(numbers)

-    return total / count
+    return round(total / count, 2)  # Added rounding

 # Test the function
 scores = [85, 90, 78, 92, 88]
```

### Understanding the Output
### فهم المخرجات

- **Red lines (-)**: Lines that were removed
- **Green lines (+)**: Lines that were added
- **White lines**: Unchanged context

- **الأسطر الحمراء (-)**: الأسطر التي تم حذفها
- **الأسطر الخضراء (+)**: الأسطر التي تم إضافتها
- **الأسطر البيضاء**: السياق غير المتغير

### Exiting git diff
### الخروج من git diff

Press `q` to quit viewing the diff.

اضغط `q` للخروج من عرض الفروقات.

---

## Command Summary Cheatsheet
## ملخص الأوامر

| Command | Purpose | When to Use | Arabic |
|---------|---------|-------------|---------|
| `git clone [URL]` | Get repository | Once, at the beginning | مرة واحدة، في البداية |
| `git status` | Check current state | Anytime, frequently | في أي وقت، بكثرة |
| `git pull` | Get updates | Weekly (Sun & Thu) | أسبوعيًا (الأحد والخميس) |
| `git log` | View history | To see what's new | لرؤية ما هو جديد |
| `git diff` | See changes | To review modifications | لمراجعة التعديلات |

---

## Your Weekly Git Routine
## روتين Git الأسبوعي

### Sunday (Before Lecture)
### الأحد (قبل المحاضرة)

```bash
cd python-m110          # Go to course folder
git pull               # Get latest materials
git status             # Verify everything is clean
```

### Thursday (Before Lab)
### الخميس (قبل المختبر)

```bash
cd python-m110          # Go to course folder
git pull               # Get lab materials
git log --oneline -3   # See what's new
```

### After Making Your Own Changes
### بعد إجراء تغييراتك الخاصة

```bash
git status             # See what you changed
git diff               # Review your changes
```

---

## Common Questions
## الأسئلة الشائعة

### Q: What if I forget a command?
### س: ماذا لو نسيت أمرًا؟

**A:** Use `git --help` or refer back to this guide. Keep this guide bookmarked!

**ج:** استخدم `git --help` أو ارجع إلى هذا الدليل. احتفظ بهذا الدليل في المفضلة!

### Q: Can I break something with these commands?
### س: هل يمكنني كسر شيء بهذه الأوامر؟

**A:** No! These commands are all read-only except `git pull`, which only updates files.

**ج:** لا! هذه الأوامر كلها للقراءة فقط باستثناء `git pull`، الذي يحدث الملفات فقط.

### Q: What if git pull gives an error?
### س: ماذا لو أعطى git pull خطأ؟

**A:** Usually means you have local changes. Ask for help or use `git stash` as shown above.

**ج:** عادة يعني أن لديك تغييرات محلية. اطلب المساعدة أو استخدم `git stash` كما هو موضح أعلاه.

### Q: Do I need to memorize these commands?
### س: هل أحتاج لحفظ هذه الأوامر؟

**A:** No! Keep this guide handy. With practice, you'll remember the common ones naturally.

**ج:** لا! احتفظ بهذا الدليل في متناول اليد. مع الممارسة، ستتذكر الأوامر الشائعة بشكل طبيعي.

---

## Troubleshooting
## استكشاف الأخطاء وإصلاحها

### Problem: "git is not recognized as a command"
### المشكلة: "git غير معترف به كأمر"

**Solution:** Git is not installed. Download from [git-scm.com](https://git-scm.com)

**الحل:** Git غير مثبت. حمّله من [git-scm.com](https://git-scm.com)

### Problem: "Permission denied (publickey)"
### المشكلة: "Permission denied (publickey)"

**Solution:** Use HTTPS URL instead of SSH, or set up SSH keys (advanced)

**الحل:** استخدم عنوان HTTPS بدلاً من SSH، أو قم بإعداد مفاتيح SSH (متقدم)

### Problem: "fatal: not a git repository"
### المشكلة: "fatal: not a git repository"

**Solution:** You're not in the right folder. Use `cd` to navigate to python-m110 folder

**الحل:** لست في المجلد الصحيح. استخدم `cd` للانتقال إلى مجلد python-m110

### Problem: Changes disappear after git pull
### المشكلة: التغييرات تختفي بعد git pull

**Solution:** Git pull updates files. Save your work in `student-playground/` folder which is ignored by Git

**الحل:** git pull يحدث الملفات. احفظ عملك في مجلد `student-playground/` الذي يتجاهله Git

---

## Practice Exercises
## تمارين الممارسة

### Exercise 1: Check Your Setup
### التمرين 1: تحقق من إعدادك

Run these commands and verify they work:

شغّل هذه الأوامر وتحقق من أنها تعمل:

```bash
git --version      # Should show version number
cd python-m110     # Navigate to course folder
git status         # Should show repository status
```

### Exercise 2: Explore History
### التمرين 2: استكشف التاريخ

Try these variations of git log:

جرّب هذه الاختلافات من git log:

```bash
git log --oneline          # Compact view
git log --oneline --graph  # Visual branch structure
git log --since="1 week"   # Recent commits only
```

### Exercise 3: Practice the Weekly Routine
### التمرين 3: مارس الروتين الأسبوعي

Simulate your weekly workflow:

حاكي سير عملك الأسبوعي:

1. Check status: `git status`
2. Pull updates: `git pull`
3. View recent changes: `git log --oneline -5`
4. Check status again: `git status`

---

## Next Steps
## الخطوات التالية

Now that you know the basic commands, let's clone the course repository:

الآن بعد أن تعرف الأوامر الأساسية، لنستنسخ مستودع المقرر:

➡️ **[03-cloning-course-repo.md](03-cloning-course-repo.md)** - Step-by-step cloning guide

➡️ **[03-cloning-course-repo.md](03-cloning-course-repo.md)** - دليل الاستنساخ خطوة بخطوة

---

## Quick Reference Card
## بطاقة مرجعية سريعة

Print this and keep it handy:

اطبع هذا واحتفظ به في متناول اليد:

```
┌─────────────────────────────────────┐
│         ESSENTIAL GIT COMMANDS       │
│         أوامر Git الأساسية          │
├─────────────────────────────────────┤
│ Clone (once):                       │
│   git clone [URL]                   │
│                                     │
│ Check status:                       │
│   git status                        │
│                                     │
│ Get updates:                        │
│   git pull                          │
│                                     │
│ View history:                       │
│   git log --oneline                │
│                                     │
│ See changes:                        │
│   git diff                          │
│                                     │
│ Help:                               │
│   git --help                        │
└─────────────────────────────────────┘
```

---

## Remember
## تذكر

- 📚 **These 5 commands are enough** for this course
- 🔄 **git pull regularly** to stay updated
- ✅ **git status is your friend** - use it often
- 🆘 **Ask for help** when stuck - we're here to support you

- 📚 **هذه الأوامر الـ 5 كافية** لهذا المقرر
- 🔄 **git pull بانتظام** للبقاء محدثًا
- ✅ **git status صديقك** - استخدمه كثيرًا
- 🆘 **اطلب المساعدة** عند التعثر - نحن هنا لدعمك

---

*You're doing great! These commands will become second nature with practice!*

*أنت تبلي بلاءً حسنًا! ستصبح هذه الأوامر طبيعة ثانية مع الممارسة!*