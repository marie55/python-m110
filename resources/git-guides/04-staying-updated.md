# Staying Updated with Git Pull
# البقاء محدثًا مع Git Pull

## What You'll Learn
## ما ستتعلمه

By the end of this guide, you'll know:
- ✅ Why pulling updates regularly is important
- ✅ When to pull updates (course schedule)
- ✅ How to pull updates safely
- ✅ How to handle conflicts with your local changes
- ✅ How to set up a weekly update routine

بنهاية هذا الدليل، ستعرف:
- ✅ لماذا سحب التحديثات بانتظام مهم
- ✅ متى تسحب التحديثات (جدول المقرر)
- ✅ كيفية سحب التحديثات بأمان
- ✅ كيفية التعامل مع التعارضات مع تغييراتك المحلية
- ✅ كيفية إعداد روتين تحديث أسبوعي

---

## Why This Matters
## لماذا هذا مهم

Your instructor adds new materials every week:
- 📚 New lecture notes every Sunday
- 💻 Code examples for each topic
- ✏️ Practice exercises with solutions
- 🧪 Lab materials before lab sessions
- 📢 Important announcements and updates

مدرسك يضيف مواد جديدة كل أسبوع:
- 📚 ملاحظات محاضرة جديدة كل أحد
- 💻 أمثلة كود لكل موضوع
- ✏️ تمارين تدريبية مع الحلول
- 🧪 مواد المختبر قبل جلسات المختبر
- 📢 إعلانات وتحديثات مهمة

**Without regular pulls, you'll miss important content!**

**بدون السحب المنتظم، ستفوتك محتويات مهمة!**

---

## The Update Cycle
## دورة التحديث

### Your Instructor's Schedule
### جدول مدرسك

```
Saturday Evening: Instructor prepares materials
السبت مساءً: المدرس يحضر المواد
        ↓
Sunday Morning: Materials pushed to GitHub
الأحد صباحًا: المواد تُدفع إلى GitHub
        ↓
Sunday (You): Pull updates before lecture
الأحد (أنت): اسحب التحديثات قبل المحاضرة
        ↓
Wednesday Evening: Lab materials added
الأربعاء مساءً: مواد المختبر تُضاف
        ↓
Thursday (You): Pull updates before lab
الخميس (أنت): اسحب التحديثات قبل المختبر
```

### Visual Timeline
### الخط الزمني المرئي

```
Week Schedule / جدول الأسبوع:

Sat | Sun | Mon | Tue | Wed | Thu | Fri
السبت | الأحد | الإثنين | الثلاثاء | الأربعاء | الخميس | الجمعة
     | 📚  |     |     |      | 🧪  |
     | PULL |     |     |      | PULL|
     | سحب  |     |     |      | سحب |
```

---

## When to Pull Updates
## متى تسحب التحديثات

### Essential Pull Times (Required)
### أوقات السحب الأساسية (مطلوبة)

1. **Sunday Morning** - Before lecture
2. **Thursday Morning** - Before lab

1. **الأحد صباحًا** - قبل المحاضرة
2. **الخميس صباحًا** - قبل المختبر

### Additional Pull Times (Recommended)
### أوقات سحب إضافية (موصى بها)

3. **When instructor announces updates** via email/LMS
4. **Before starting homework** to get latest exercises
5. **When you see classmates discussing new content**

3. **عندما يعلن المدرس عن تحديثات** عبر البريد الإلكتروني/نظام إدارة التعلم
4. **قبل بدء الواجبات المنزلية** للحصول على أحدث التمارين
5. **عندما ترى زملاءك يناقشون محتوى جديدًا**

### Set Reminders!
### اضبط التذكيرات!

Add these to your phone:
- 📱 "Git Pull - M110" every Sunday at 8:00 AM
- 📱 "Git Pull - M110" every Thursday at 8:00 AM

أضف هذه إلى هاتفك:
- 📱 "Git Pull - M110" كل أحد الساعة 8:00 صباحًا
- 📱 "Git Pull - M110" كل خميس الساعة 8:00 صباحًا

---

## How to Pull Updates
## كيفية سحب التحديثات

### The Basic Pull Process
### عملية السحب الأساسية

```bash
# 1. Navigate to your repository
cd ~/Documents/AOU/python-m110

# 2. Check current status
git status

# 3. Pull updates
git pull

# 4. Check what's new
git log --oneline -5
```

### Step-by-Step with Explanations
### خطوة بخطوة مع الشروحات

#### Step 1: Open Terminal
#### الخطوة 1: افتح المحطة الطرفية

In VS Code: Press `Ctrl + ` ` (backtick)

في VS Code: اضغط `Ctrl + ` ` (backtick)

#### Step 2: Navigate to Repository
#### الخطوة 2: انتقل إلى المستودع

```bash
cd ~/Documents/AOU/python-m110
```

**Tip:** Use Tab key for auto-completion!

**نصيحة:** استخدم مفتاح Tab للإكمال التلقائي!

#### Step 3: Check Current Status
#### الخطوة 3: تحقق من الحالة الحالية

```bash
git status
```

**What to look for:**
**ما تبحث عنه:**

✅ **Good to pull:**
```
On branch main
Your branch is behind 'origin/main' by 3 commits
nothing to commit, working tree clean
```

⚠️ **Need to handle local changes first:**
```
Changes not staged for commit:
  modified: exercises/week-02/practice.py
```

#### Step 4: Pull the Updates
#### الخطوة 4: اسحب التحديثات

```bash
git pull
```

Or be more specific:
أو كن أكثر تحديدًا:

```bash
git pull origin main
```

#### Step 5: Review What Changed
#### الخطوة 5: راجع ما تغير

```bash
# See commit messages
git log --oneline -5

# See which files changed
git diff HEAD~1 --name-only

# Open VS Code to explore
code .
```

---

## Understanding Pull Output
## فهم مخرجات السحب

### Scenario 1: Smooth Update
### السيناريو 1: تحديث سلس

```bash
$ git pull
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (8/8), done.
Unpacking objects: 100% (8/8), done.
From https://github.com/YOUR_USERNAME/python-m110
   abc123d..def456e  main -> origin/main
Updating abc123d..def456e
Fast-forward
 lectures/week-03/README.md      |  89 +++++++++++
 code-examples/week-03/loops.py  |  45 ++++++
 exercises/week-03/practice.py   |  32 ++++
 3 files changed, 166 insertions(+)
```

**What this means:**
**ماذا يعني هذا:**

| Line | Meaning | Arabic |
|------|---------|--------|
| `Fast-forward` | Clean update, no conflicts | تحديث نظيف، لا تعارضات |
| `3 files changed` | Three files were updated | تم تحديث ثلاثة ملفات |
| `166 insertions(+)` | 166 new lines added | تم إضافة 166 سطرًا جديدًا |
| File paths | Shows exactly what changed | يظهر بالضبط ما تغير |

### Scenario 2: Already Updated
### السيناريو 2: محدث بالفعل

```bash
$ git pull
Already up to date.
```

**This means:** No new updates available. You have the latest version!

**هذا يعني:** لا تحديثات جديدة متاحة. لديك أحدث إصدار!

### Scenario 3: Local Changes Conflict
### السيناريو 3: تعارض التغييرات المحلية

```bash
$ git pull
error: Your local changes to the following files would be overwritten by merge:
    exercises/week-02/practice.py
Please commit your changes or stash them before you merge.
```

**This means:** You modified files that also changed on GitHub.

**هذا يعني:** عدّلت ملفات تغيرت أيضًا على GitHub.

---

## Handling Local Changes
## التعامل مع التغييرات المحلية

### Option 1: Stash (Temporary Save)
### الخيار 1: التخزين المؤقت (Stash)

Best when you want to keep your changes but get updates first:

الأفضل عندما تريد الاحتفاظ بتغييراتك لكن الحصول على التحديثات أولاً:

```bash
# Save your changes temporarily
git stash save "My work on exercise 2"

# Pull updates
git pull

# Restore your changes
git stash pop
```

**Visual explanation:**
**شرح مرئي:**

```
Your Work → [Stash Box] → Pull Updates → [Restore from Box] → Continue
عملك ← [صندوق التخزين] ← سحب التحديثات ← [استعادة من الصندوق] ← استمر
```

### Option 2: Save to Different File
### الخيار 2: حفظ في ملف مختلف

Best for important work you don't want to lose:

الأفضل للعمل المهم الذي لا تريد فقدانه:

```bash
# Copy your modified file
cp exercises/week-02/practice.py student-playground/my_practice_backup.py

# Discard local changes
git checkout exercises/week-02/practice.py

# Pull updates
git pull
```

### Option 3: Commit Locally (Advanced)
### الخيار 3: الالتزام محليًا (متقدم)

Only if you're comfortable with Git:

فقط إذا كنت مرتاحًا مع Git:

```bash
# Commit your changes locally
git add exercises/week-02/practice.py
git commit -m "My solution to exercise 2"

# Pull and merge
git pull
```

---

## The Student-Playground Strategy
## استراتيجية Student-Playground

### Best Practice: Work in Your Playground
### أفضل الممارسات: اعمل في ملعبك

To avoid ALL conflicts, do your work in `student-playground/`:

لتجنب جميع التعارضات، اعمل في `student-playground/`:

```bash
# Copy exercise to your playground
cp exercises/week-02/practice.py student-playground/my_practice.py

# Work on your copy
code student-playground/my_practice.py

# Pull updates without worry!
git pull  # Never conflicts with student-playground!
```

**Why this works:**
**لماذا يعمل هذا:**

The `.gitignore` file contains:
```
student-playground/
```

This means Git completely ignores this folder!

هذا يعني أن Git يتجاهل هذا المجلد تمامًا!

---

## Weekly Workflow Routine
## روتين سير العمل الأسبوعي

### Sunday Morning Routine
### روتين صباح الأحد

```bash
# 1. Morning coffee ☕
# 1. قهوة الصباح ☕

# 2. Open terminal
cd ~/Documents/AOU/python-m110

# 3. Check and pull
git status
git pull

# 4. See what's new
git log --oneline -3
ls lectures/  # See new lecture folder

# 5. Open in VS Code
code .

# 6. Review new materials before class!
```

### Thursday Morning Routine
### روتين صباح الخميس

```bash
# 1. Before lab
cd ~/Documents/AOU/python-m110

# 2. Pull lab materials
git pull

# 3. Check lab folder
ls labs/

# 4. Open specific lab
code labs/lab-01-week06/

# 5. Read instructions first!
```

---

## Checking for Updates Without Pulling
## التحقق من التحديثات دون السحب

### See If Updates Are Available
### معرفة ما إذا كانت التحديثات متاحة

```bash
# Fetch information without downloading files
git fetch

# Check if behind
git status
```

Output if updates available:
المخرجات إذا كانت التحديثات متاحة:

```
Your branch is behind 'origin/main' by 5 commits
```

This means: 5 updates waiting for you!

هذا يعني: 5 تحديثات تنتظرك!

### Preview What Will Change
### معاينة ما سيتغير

```bash
# See what commits are coming
git log HEAD..origin/main --oneline

# See what files will change
git diff HEAD..origin/main --name-only
```

---

## Common Problems and Solutions
## المشاكل الشائعة والحلول

### Problem 1: "Not a git repository"
### المشكلة 1: "Not a git repository"

```bash
fatal: not a git repository
```

**Solution:** You're in the wrong folder!
```bash
pwd  # Check where you are
cd ~/Documents/AOU/python-m110  # Go to correct folder
```

**الحل:** أنت في المجلد الخطأ!

### Problem 2: "Connection timeout"
### المشكلة 2: "Connection timeout"

```bash
fatal: unable to access 'https://github.com/...': Connection timeout
```

**Solution:** Check your internet connection. Try again later.

**الحل:** تحقق من اتصالك بالإنترنت. حاول مرة أخرى لاحقًا.

### Problem 3: "Merge conflict"
### المشكلة 3: "Merge conflict"

```bash
CONFLICT (content): Merge conflict in exercises/week-02/practice.py
Automatic merge failed; fix conflicts and then commit the result.
```

**Solution:** This is complex for beginners. Best approach:
```bash
# Cancel the merge
git merge --abort

# Save your work elsewhere
cp exercises/week-02/practice.py student-playground/backup.py

# Reset to clean state
git reset --hard origin/main
```

**الحل:** هذا معقد للمبتدئين. أفضل نهج هو الحفظ والإعادة.

### Problem 4: Accidentally modified course files
### المشكلة 4: تعديل ملفات المقرر بالخطأ

**Solution:** Reset the modified files:
```bash
# See what you changed
git status

# Undo changes to specific file
git checkout -- lectures/week-02/README.md

# Or undo ALL changes (careful!)
git checkout -- .

# Now pull safely
git pull
```

**الحل:** أعد تعيين الملفات المعدلة.

---

## Pro Tips for Smooth Updates
## نصائح احترافية للتحديثات السلسة

### Tip 1: Always Status First
### النصيحة 1: دائمًا الحالة أولاً

```bash
git status  # ALWAYS run this before pull
git pull    # Only if status is clean
```

### Tip 2: Create Aliases
### النصيحة 2: أنشئ اختصارات

Add to your `.bashrc` or `.zshrc`:

أضف إلى `.bashrc` أو `.zshrc`:

```bash
alias m110='cd ~/Documents/AOU/python-m110'
alias update='git pull && git log --oneline -5'
```

Now you can just type:
الآن يمكنك فقط كتابة:
```bash
m110     # Goes to course folder
update   # Pulls and shows what's new
```

### Tip 3: Use VS Code Git Integration
### النصيحة 3: استخدم تكامل Git في VS Code

1. Open VS Code
2. Click Source Control icon (or `Ctrl+Shift+G`)
3. Click "..." menu → Pull

### Tip 4: Check Before Sleeping
### النصيحة 4: تحقق قبل النوم

Sunday & Thursday nights: Quick pull before bed ensures you're ready for next day!

ليالي الأحد والخميس: سحب سريع قبل النوم يضمن أنك جاهز لليوم التالي!

---

## Practice Exercises
## تمارين الممارسة

### Exercise 1: Simulate Weekly Routine
### التمرين 1: حاكي الروتين الأسبوعي

Practice the commands even when no updates:

مارس الأوامر حتى عند عدم وجود تحديثات:

```bash
# Monday practice
cd ~/Documents/AOU/python-m110
git fetch
git status
git log --oneline -3

# Tuesday practice
git pull
ls lectures/
ls exercises/
```

### Exercise 2: Handle a Stash
### التمرين 2: تعامل مع التخزين المؤقت

1. Create a test file in exercises
2. Modify it
3. Try to pull (will fail)
4. Stash changes
5. Pull successfully
6. Restore from stash

### Exercise 3: Set Up Your Routine
### التمرين 3: أعد روتينك

1. Add phone reminders for Sunday & Thursday
2. Create a checklist note
3. Practice the workflow 3 times

---

## Update Checklist
## قائمة تحقق التحديث

Print and keep this handy:

اطبع واحتفظ بهذا في متناول اليد:

```
┌─────────────────────────────────────┐
│     WEEKLY GIT PULL CHECKLIST       │
│    قائمة تحقق السحب الأسبوعية      │
├─────────────────────────────────────┤
│ ☐ Open terminal/VS Code             │
│ ☐ Navigate to python-m110           │
│ ☐ Run: git status                   │
│ ☐ Check: working tree clean?        │
│ ☐ Run: git pull                     │
│ ☐ Check: successful?                │
│ ☐ Run: git log --oneline -3         │
│ ☐ Review: what's new?               │
│ ☐ Open: new materials in VS Code    │
└─────────────────────────────────────┘
```

---

## Next Steps
## الخطوات التالية

Now learn the complete student workflow for the course:

الآن تعلم سير العمل الكامل للطالب في المقرر:

➡️ **[05-git-workflow-for-students.md](05-git-workflow-for-students.md)** - Complete workflow guide

➡️ **[05-git-workflow-for-students.md](05-git-workflow-for-students.md)** - دليل سير العمل الكامل

---

## Summary
## الملخص

You've learned:
- 📅 **When to pull:** Sundays & Thursdays minimum
- 🔄 **How to pull:** `git status` then `git pull`
- 💾 **Handling conflicts:** Stash or save elsewhere
- 🎯 **Best practice:** Work in student-playground/
- ⏰ **Routine:** Set reminders and stick to schedule

لقد تعلمت:
- 📅 **متى تسحب:** الأحد والخميس كحد أدنى
- 🔄 **كيف تسحب:** `git status` ثم `git pull`
- 💾 **معالجة التعارضات:** خزّن أو احفظ في مكان آخر
- 🎯 **أفضل الممارسات:** اعمل في student-playground/
- ⏰ **الروتين:** اضبط التذكيرات والتزم بالجدول

---

## Remember
## تذكر

- 🔄 **Pull regularly** - Don't fall behind on materials
- 🛡️ **Check status first** - Avoid conflicts
- 📁 **Use student-playground/** - Your safe space
- 📱 **Set reminders** - Make it a habit
- 🆘 **Ask for help** - When something seems wrong

- 🔄 **اسحب بانتظام** - لا تتأخر عن المواد
- 🛡️ **تحقق من الحالة أولاً** - تجنب التعارضات
- 📁 **استخدم student-playground/** - مساحتك الآمنة
- 📱 **اضبط التذكيرات** - اجعلها عادة
- 🆘 **اطلب المساعدة** - عندما يبدو شيء خاطئًا

---

*Stay updated, stay ahead! Regular pulls ensure you never miss important content!*

*ابق محدثًا، ابق في المقدمة! السحب المنتظم يضمن عدم تفويت محتوى مهم!*