# Git Workflow for M110 Students
# سير عمل Git لطلاب M110

## What You'll Learn
## ما ستتعلمه

This guide brings everything together:
- ✅ Complete Git workflow for the course
- ✅ Progressive learning path (Week 1-12)
- ✅ Read-only vs. experimental workflows
- ✅ How to safely experiment with code
- ✅ Optional: Contributing back to the course
- ✅ Building your portfolio on GitHub

هذا الدليل يجمع كل شيء معًا:
- ✅ سير عمل Git الكامل للمقرر
- ✅ مسار التعلم التدريجي (الأسبوع 1-12)
- ✅ سير العمل للقراءة فقط مقابل التجريبي
- ✅ كيفية التجربة بأمان مع الكود
- ✅ اختياري: المساهمة في المقرر
- ✅ بناء محفظتك على GitHub

---

## Why This Matters
## لماذا هذا مهم

Understanding the complete workflow helps you:
- Focus on learning Python without Git confusion
- Know exactly what to do each week
- Safely experiment without breaking anything
- Build professional habits early
- Prepare for real-world development

فهم سير العمل الكامل يساعدك على:
- التركيز على تعلم Python دون ارتباك Git
- معرفة بالضبط ما يجب فعله كل أسبوع
- التجربة بأمان دون كسر أي شيء
- بناء عادات مهنية مبكرًا
- الاستعداد للتطوير في العالم الحقيقي

---

## Course Timeline & Git Skills
## الجدول الزمني للمقرر ومهارات Git

### Phase 1: Read-Only (Weeks 1-5)
### المرحلة 1: القراءة فقط (الأسابيع 1-5)

Focus: Learning Python basics, getting comfortable with Git

التركيز: تعلم أساسيات Python، الارتياح مع Git

| Week | Python Topic | Git Skills |
|------|-------------|------------|
| 1 | Algorithms | Clone repository |
| 1 | الخوارزميات | استنساخ المستودع |
| 2 | Fundamentals | Pull updates, navigate folders |
| 2 | الأساسيات | سحب التحديثات، التنقل بين المجلدات |
| 3 | Decision Structures | Regular pull routine |
| 3 | هياكل القرار | روتين السحب المنتظم |
| 4 | Loops | Check status, view logs |
| 4 | الحلقات | التحقق من الحالة، عرض السجلات |
| 5 | Lists & Tuples | Understand diffs |
| 5 | القوائم والصفوف | فهم الفروقات |

### Phase 2: Local Experiments (Weeks 6-9)
### المرحلة 2: التجارب المحلية (الأسابيع 6-9)

Focus: More complex Python, safe local modifications

التركيز: Python أكثر تعقيدًا، تعديلات محلية آمنة

| Week | Python Topic | Git Skills |
|------|-------------|------------|
| 6 | Lab Session | Work in student-playground |
| 6 | جلسة المختبر | العمل في student-playground |
| 7 | Functions | Create local branches (optional) |
| 7 | الدوال | إنشاء فروع محلية (اختياري) |
| 8 | Files & Exceptions | Stash changes |
| 8 | الملفات والاستثناءات | تخزين التغييرات |
| 9 | Lab Session | Compare versions |
| 9 | جلسة المختبر | مقارنة الإصدارات |

### Phase 3: Advanced (Weeks 10-12)
### المرحلة 3: متقدم (الأسابيع 10-12)

Focus: OOP, GUI, potential contributions

التركيز: البرمجة الكائنية، واجهات المستخدم، المساهمات المحتملة

| Week | Python Topic | Git Skills |
|------|-------------|------------|
| 10 | OOP | Create feature branches |
| 10 | البرمجة الكائنية | إنشاء فروع الميزات |
| 11 | GUI Programming | Optional: Fork & PR |
| 11 | برمجة الواجهات | اختياري: Fork و PR |
| 12 | Lab & Review | Portfolio building |
| 12 | المختبر والمراجعة | بناء المحفظة |

---

## The Three Workflows
## سيرات العمل الثلاثة

### Workflow 1: Read-Only (Weeks 1-5)
### سير العمل 1: القراءة فقط (الأسابيع 1-5)

Perfect for beginners. No risk, just learning!

مثالي للمبتدئين. لا مخاطر، فقط التعلم!

```
┌─────────────────────────────────────┐
│         READ-ONLY WORKFLOW          │
│       سير عمل القراءة فقط          │
├─────────────────────────────────────┤
│                                     │
│  [GitHub Repository]                │
│         ↓                           │
│    git clone (once)                 │
│         ↓                           │
│  [Your Computer]                    │
│         ↓                           │
│    git pull (weekly)                │
│         ↓                           │
│  [Updated Materials]                │
│         ↓                           │
│     Read & Learn                    │
│                                     │
└─────────────────────────────────────┘
```

**Commands you need:**
```bash
git clone [URL]    # Once at start
git pull           # Every Sun & Thu
git status         # Check state
git log            # See history
```

**الأوامر التي تحتاجها:**
```bash
git clone [URL]    # مرة في البداية
git pull           # كل أحد وخميس
git status         # تحقق من الحالة
git log            # رؤية التاريخ
```

### Workflow 2: Safe Experimentation (Weeks 6-9)
### سير العمل 2: التجربة الآمنة (الأسابيع 6-9)

Make changes without affecting course materials!

قم بالتغييرات دون التأثير على مواد المقرر!

```
┌─────────────────────────────────────┐
│     SAFE EXPERIMENTATION WORKFLOW   │
│      سير عمل التجربة الآمنة        │
├─────────────────────────────────────┤
│                                     │
│  Course Files → Copy → Playground   │
│                                     │
│  exercises/week-07/functions.py     │
│         ↓ (copy)                    │
│  student-playground/my_functions.py │
│         ↓ (edit freely)             │
│     Your experiments!               │
│                                     │
│  git pull still works perfectly!    │
│                                     │
└─────────────────────────────────────┘
```

**Your safe workflow:**
```bash
# Copy exercise to playground
cp exercises/week-07/functions.py student-playground/my_solution.py

# Work on your copy
code student-playground/my_solution.py

# Pull updates without worry
git pull  # Never conflicts!
```

**سير عملك الآمن:**
```bash
# انسخ التمرين إلى الملعب
cp exercises/week-07/functions.py student-playground/my_solution.py

# اعمل على نسختك
code student-playground/my_solution.py

# اسحب التحديثات دون قلق
git pull  # لا تعارضات أبدًا!
```

### Workflow 3: Advanced Contribution (Optional, Weeks 10+)
### سير العمل 3: المساهمة المتقدمة (اختياري، الأسابيع 10+)

For students who want to contribute improvements!

للطلاب الذين يريدون المساهمة بالتحسينات!

```
┌─────────────────────────────────────┐
│      CONTRIBUTION WORKFLOW          │
│       سير عمل المساهمة             │
├─────────────────────────────────────┤
│                                     │
│  1. Fork on GitHub                  │
│  2. Clone your fork                 │
│  3. Create branch                   │
│  4. Make improvements               │
│  5. Push to your fork               │
│  6. Create Pull Request             │
│                                     │
└─────────────────────────────────────┘
```

---

## Directory Structure & Permissions
## بنية الدليل والصلاحيات

Understanding what you can and cannot modify:

فهم ما يمكنك وما لا يمكنك تعديله:

```
python-m110/
│
├── 📚 lectures/          ❌ Don't modify (instructor updates)
├── 💻 code-examples/     ❌ Don't modify (reference code)
├── ✏️ exercises/         ⚠️ Can modify locally (but pull overwrites)
├── 🧪 labs/             ⚠️ Can modify locally (but pull overwrites)
├── 🎯 projects/         ✅ Your project work
├── 📖 resources/        ❌ Don't modify (course resources)
├── 📝 assessments/      ❌ Don't modify (exam prep)
├── 🌟 student-contributions/ ✅ Can contribute via PR
└── 🎮 student-playground/    ✅ YOUR SPACE! (Git ignores this)
```

**Legend:**
- ❌ = Never modify
- ⚠️ = Can modify but be careful
- ✅ = Safe to modify

**المفتاح:**
- ❌ = لا تعدّل أبدًا
- ⚠️ = يمكن التعديل لكن احذر
- ✅ = آمن للتعديل

---

## The Student-Playground Strategy
## استراتيجية Student-Playground

### What is student-playground/?
### ما هو student-playground/?

Your personal workspace that Git completely ignores!

مساحة عملك الشخصية التي يتجاهلها Git تمامًا!

```
student-playground/
├── my_solutions/        # Your exercise solutions
│   ├── week01_practice.py
│   ├── week02_loops.py
│   └── week03_functions.py
├── experiments/         # Try new things
│   ├── test_gui.py
│   └── database_test.py
├── notes/              # Your notes
│   ├── lecture_notes.md
│   └── tips.txt
└── projects/           # Personal projects
    └── calculator.py
```

### Why Use It?
### لماذا تستخدمه؟

1. **No Git conflicts ever** - Git ignores this folder
2. **Freedom to experiment** - Break things, it's OK!
3. **Organize your way** - Create any structure
4. **Keep your work** - Survives all pulls

1. **لا تعارضات Git أبدًا** - Git يتجاهل هذا المجلد
2. **حرية التجربة** - اكسر الأشياء، لا بأس!
3. **نظّم بطريقتك** - أنشئ أي بنية
4. **احتفظ بعملك** - ينجو من جميع السحبات

### Setting Up Your Playground
### إعداد ملعبك

```bash
# Create your structure
cd python-m110/student-playground

mkdir my_solutions
mkdir experiments
mkdir notes
mkdir projects

# Create a README for yourself
echo "# My M110 Work" > README.md
echo "This is my personal workspace" >> README.md
```

---

## Weekly Student Routine
## روتين الطالب الأسبوعي

### Complete Week Schedule
### جدول الأسبوع الكامل

```
┌────────────────────────────────────────┐
│        WEEKLY GIT ROUTINE              │
│        روتين Git الأسبوعي             │
├────────────────────────────────────────┤
│                                        │
│ SUNDAY (Lecture Day)                  │
│ الأحد (يوم المحاضرة)                  │
│ ├─ 8:00 AM: git pull                  │
│ ├─ 8:15 AM: Review new materials      │
│ ├─ 9:00 AM: Attend lecture            │
│ └─ After: Copy exercises to playground│
│                                        │
│ MONDAY-WEDNESDAY (Practice)            │
│ الإثنين-الأربعاء (الممارسة)          │
│ ├─ Work on exercises in playground    │
│ ├─ Experiment with code examples      │
│ └─ Review lecture materials           │
│                                        │
│ THURSDAY (Lab Day)                    │
│ الخميس (يوم المختبر)                  │
│ ├─ 8:00 AM: git pull                  │
│ ├─ 8:15 AM: Read lab instructions     │
│ ├─ 9:00 AM: Attend lab               │
│ └─ After: Complete lab in playground  │
│                                        │
│ FRIDAY-SATURDAY (Review & Catch-up)   │
│ الجمعة-السبت (المراجعة واللحاق)      │
│ ├─ Review week's materials            │
│ ├─ Complete any pending exercises     │
│ └─ Prepare questions for next week    │
│                                        │
└────────────────────────────────────────┘
```

### Daily Commands Cheatsheet
### ورقة غش الأوامر اليومية

**Sunday & Thursday:**
```bash
cd ~/Documents/AOU/python-m110
git pull
git status
code .
```

**Working Days:**
```bash
cd ~/Documents/AOU/python-m110
code .
# Work in student-playground/
```

---

## Understanding .gitignore
## فهم .gitignore

### What is .gitignore?
### ما هو .gitignore؟

A file that tells Git what to ignore. Like a "Do Not Track" list!

ملف يخبر Git بما يتجاهله. مثل قائمة "عدم التتبع"!

**Course .gitignore contains:**
```gitignore
# Student workspace - your safe zone!
student-playground/

# Operating system files
.DS_Store      # Mac
Thumbs.db      # Windows
*.swp          # Vim

# Python cache
__pycache__/
*.pyc
.pytest_cache/

# IDE settings
.vscode/
.idea/
```

This means Git ignores:
- ✅ Everything in student-playground/
- ✅ System files
- ✅ Python temporary files
- ✅ IDE configurations

هذا يعني أن Git يتجاهل:
- ✅ كل شيء في student-playground/
- ✅ ملفات النظام
- ✅ ملفات Python المؤقتة
- ✅ تكوينات IDE

---

## Optional: Creating Branches
## اختياري: إنشاء الفروع

### What is a Branch?
### ما هو الفرع؟

A separate timeline for your experiments. Like a parallel universe for your code!

خط زمني منفصل لتجاربك. مثل كون موازٍ لكودك!

### When to Use Branches (Week 7+)
### متى تستخدم الفروع (الأسبوع 7+)

```bash
# Create and switch to new branch
git checkout -b my-experiments

# Work freely on this branch
# Edit, add, commit as you like

# Switch back to main
git checkout main

# Pull updates (only affects main)
git pull

# Switch back to your branch
git checkout my-experiments
```

### Visual Branch Concept
### مفهوم الفرع المرئي

```
main:     A → B → C → D → E (instructor updates)
              ↓
my-branch:    B → X → Y → Z (your experiments)
```

---

## Optional: Contributing via Pull Requests
## اختياري: المساهمة عبر طلبات السحب

### When You Can Contribute
### متى يمكنك المساهمة

Found a typo? Solved an exercise brilliantly? Want to share?

وجدت خطأ مطبعي؟ حللت تمرينًا ببراعة؟ تريد المشاركة؟

### Contribution Process (Advanced)
### عملية المساهمة (متقدم)

1. **Fork the repository** on GitHub
2. **Clone your fork** to your computer
3. **Create a branch** for your contribution
4. **Make your changes** (fix typo, add solution, etc.)
5. **Push to your fork** on GitHub
6. **Create Pull Request** to main repository

Example contribution:
```bash
# After forking on GitHub
git clone https://github.com/YOUR_USERNAME/python-m110-fork.git
cd python-m110-fork
git checkout -b fix-typo
# Make your fix
git add .
git commit -m "Fix typo in week-3 README"
git push origin fix-typo
# Create PR on GitHub
```

---

## Building Your Portfolio
## بناء محفظتك

### Why GitHub Portfolio Matters
### لماذا محفظة GitHub مهمة

Employers look at GitHub profiles! Show your learning journey.

أصحاب العمل ينظرون إلى ملفات GitHub! أظهر رحلة تعلمك.

### Creating Your Own Projects Repository
### إنشاء مستودع مشاريعك الخاص

```bash
# Create new repo on GitHub (via website)
# Then locally:
cd ~/Documents/AOU
git clone https://github.com/YOUR_USERNAME/m110-projects.git
cd m110-projects

# Add your best work
cp ../python-m110/student-playground/projects/* .
git add .
git commit -m "Add M110 projects"
git push
```

### Portfolio Structure
### بنية المحفظة

```
m110-projects/
├── README.md           # Describe your projects
├── calculator/         # Project 1
│   ├── calculator.py
│   └── README.md
├── todo-app/          # Project 2
│   ├── todo.py
│   └── README.md
└── data-analyzer/     # Project 3
    ├── analyzer.py
    └── README.md
```

---

## Troubleshooting Common Scenarios
## استكشاف السيناريوهات الشائعة وإصلاحها

### Scenario 1: "I accidentally edited course files"
### السيناريو 1: "حررت ملفات المقرر بالخطأ"

```bash
# See what you changed
git status
git diff

# Discard all changes (careful!)
git checkout -- .

# Or discard specific file
git checkout -- exercises/week-03/loops.py
```

### Scenario 2: "I want to save my changes but also pull"
### السيناريو 2: "أريد حفظ تغييراتي وأيضًا السحب"

```bash
# Option 1: Copy to playground
cp exercises/week-03/loops.py student-playground/my_loops.py

# Option 2: Stash temporarily
git stash
git pull
git stash pop
```

### Scenario 3: "Pull says I have conflicts"
### السيناريو 3: "السحب يقول لدي تعارضات"

```bash
# Safe reset (loses local changes)
git fetch origin
git reset --hard origin/main

# Or abort merge
git merge --abort
```

### Scenario 4: "I want to start fresh"
### السيناريو 4: "أريد البدء من جديد"

```bash
# Nuclear option: delete and re-clone
cd ~/Documents/AOU
rm -rf python-m110
git clone https://github.com/YOUR_USERNAME/python-m110.git
```

---

## Git Commands Progressive Learning
## تعلم أوامر Git التدريجي

### Level 1: Essential (Weeks 1-3)
### المستوى 1: الأساسي (الأسابيع 1-3)

```bash
git clone [URL]    # Get repository
git pull           # Get updates
git status         # Check state
```

### Level 2: Useful (Weeks 4-6)
### المستوى 2: مفيد (الأسابيع 4-6)

```bash
git log --oneline       # View history
git diff               # See changes
git fetch              # Check for updates
```

### Level 3: Intermediate (Weeks 7-9)
### المستوى 3: متوسط (الأسابيع 7-9)

```bash
git stash              # Save changes temporarily
git stash pop          # Restore changes
git checkout -- [file] # Discard changes
```

### Level 4: Advanced (Weeks 10+)
### المستوى 4: متقدم (الأسابيع 10+)

```bash
git checkout -b [branch]  # Create branch
git add [file]           # Stage changes
git commit -m "message"  # Save changes
git push                 # Upload changes
```

---

## Best Practices Summary
## ملخص أفضل الممارسات

### DO ✅
### افعل ✅

1. **Pull regularly** - Sunday & Thursday minimum
2. **Check status** before any operation
3. **Work in playground** for experiments
4. **Keep organized** folder structure
5. **Ask for help** when confused

1. **اسحب بانتظام** - الأحد والخميس كحد أدنى
2. **تحقق من الحالة** قبل أي عملية
3. **اعمل في الملعب** للتجارب
4. **حافظ على التنظيم** في بنية المجلدات
5. **اطلب المساعدة** عند الارتباك

### DON'T ❌
### لا تفعل ❌

1. **Don't push to main** - You can't anyway
2. **Don't edit course files** directly
3. **Don't clone multiple times** - Pull instead
4. **Don't panic** about Git errors
5. **Don't skip pulls** - You'll miss content

1. **لا تدفع إلى main** - لا يمكنك على أي حال
2. **لا تحرر ملفات المقرر** مباشرة
3. **لا تستنسخ عدة مرات** - اسحب بدلاً من ذلك
4. **لا تذعر** من أخطاء Git
5. **لا تتخطى السحب** - ستفوتك محتويات

---

## Your Git Learning Journey
## رحلة تعلم Git الخاصة بك

```
Week 1-3:  "What is Git?" → "I can clone and pull!"
الأسبوع 1-3: "ما هو Git؟" ← "يمكنني الاستنساخ والسحب!"

Week 4-6:  "I understand status" → "I can work safely"
الأسبوع 4-6: "أفهم الحالة" ← "يمكنني العمل بأمان"

Week 7-9:  "I can handle conflicts" → "I'm comfortable"
الأسبوع 7-9: "يمكنني التعامل مع التعارضات" ← "أنا مرتاح"

Week 10-12: "I can contribute" → "I'm Git confident!"
الأسبوع 10-12: "يمكنني المساهمة" ← "أنا واثق في Git!"
```

---

## Quick Reference Card
## بطاقة مرجعية سريعة

Print and keep this:

اطبع واحتفظ بهذا:

```
┌─────────────────────────────────────┐
│        M110 GIT WORKFLOW            │
│       سير عمل Git في M110          │
├─────────────────────────────────────┤
│                                     │
│ DAILY ESSENTIALS:                   │
│   cd python-m110                    │
│   git status                        │
│   git pull                          │
│                                     │
│ SAFE WORKSPACE:                     │
│   student-playground/               │
│                                     │
│ WHEN STUCK:                         │
│   git status                        │
│   git stash                        │
│   git pull                          │
│   git stash pop                     │
│                                     │
│ EMERGENCY RESET:                    │
│   git fetch origin                  │
│   git reset --hard origin/main     │
│                                     │
└─────────────────────────────────────┘
```

---

## Congratulations!
## تهانينا!

You now understand the complete Git workflow for M110! You have:

أنت الآن تفهم سير عمل Git الكامل لـ M110! لديك:

- ✅ **Clear weekly routine** to follow
- ✅ **Safe workspace** in student-playground/
- ✅ **Progressive path** from beginner to advanced
- ✅ **Troubleshooting guide** for common issues
- ✅ **Optional paths** for going beyond basics

- ✅ **روتين أسبوعي واضح** للمتابعة
- ✅ **مساحة عمل آمنة** في student-playground/
- ✅ **مسار تدريجي** من المبتدئ إلى المتقدم
- ✅ **دليل استكشاف الأخطاء** للمشاكل الشائعة
- ✅ **مسارات اختيارية** للذهاب أبعد من الأساسيات

---

## Final Tips
## نصائح نهائية

1. **Git is a tool, not the goal** - Focus on Python first
2. **Mistakes are OK** - You can always reset
3. **Practice makes perfect** - Use Git daily
4. **Build habits** - Same routine every week
5. **Help others** - Teaching reinforces learning

1. **Git أداة، وليس الهدف** - ركز على Python أولاً
2. **الأخطاء مقبولة** - يمكنك دائمًا إعادة التعيين
3. **الممارسة تصنع الكمال** - استخدم Git يوميًا
4. **ابن العادات** - نفس الروتين كل أسبوع
5. **ساعد الآخرين** - التعليم يعزز التعلم

---

## Resources & Help
## الموارد والمساعدة

- **Course Repository:** Your main resource
- **These Guides:** Keep them bookmarked
- **Instructor Office Hours:** Don't hesitate to ask
- **Classmates:** Learn together
- **Stack Overflow:** For specific Git questions

- **مستودع المقرر:** موردك الرئيسي
- **هذه الأدلة:** احتفظ بها في المفضلة
- **ساعات مكتب المدرس:** لا تتردد في السؤال
- **زملاء الصف:** تعلموا معًا
- **Stack Overflow:** لأسئلة Git المحددة

---

*You're now equipped with everything you need for Git success in M110!*
*Good luck with your Python journey!*

*أنت الآن مجهز بكل ما تحتاجه لنجاح Git في M110!*
*حظًا سعيدًا في رحلة Python الخاصة بك!*