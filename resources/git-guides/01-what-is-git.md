# What is Git?
# ما هو Git؟

## What You'll Learn
## ما ستتعلمه

By the end of this guide, you'll understand:
- ✅ What Git is and why developers use it
- ✅ The difference between Git and GitHub
- ✅ Basic Git terminology
- ✅ Why we use Git in this course

بنهاية هذا الدليل، ستفهم:
- ✅ ما هو Git ولماذا يستخدمه المطورون
- ✅ الفرق بين Git و GitHub
- ✅ المصطلحات الأساسية في Git
- ✅ لماذا نستخدم Git في هذا المقرر

---

## Why This Matters
## لماذا هذا مهم

Git is the most widely used version control system in the software industry. Learning Git early in your programming journey gives you a professional skill that employers value. It's not just a tool for this course—it's a tool you'll use throughout your career.

Git هو نظام التحكم في الإصدارات الأكثر استخدامًا في صناعة البرمجيات. تعلم Git مبكرًا في رحلتك البرمجية يمنحك مهارة مهنية يقدرها أصحاب العمل. ليس مجرد أداة لهذا المقرر—بل أداة ستستخدمها طوال حياتك المهنية.

**Did you know?** Over 95% of professional developers use Git!

**هل تعلم؟** أكثر من 95% من المطورين المحترفين يستخدمون Git!

---

## What is Version Control?
## ما هو التحكم في الإصدارات؟

### The Problem
### المشكلة

Imagine you're writing an essay for your literature class. You make changes, but later realize the original version was better. Without version control, your changes are lost forever.

تخيل أنك تكتب مقالاً لصف الأدب. تقوم بإجراء تغييرات، لكن لاحقًا تدرك أن النسخة الأصلية كانت أفضل. بدون التحكم في الإصدارات، تضيع تغييراتك للأبد.

### The Old Way (Without Git)
### الطريقة القديمة (بدون Git)

People used to save multiple versions manually:
- `my_project_final.py`
- `my_project_final_v2.py`
- `my_project_final_FINAL.py`
- `my_project_final_FINAL_for_real.py`

كان الناس يحفظون نسخًا متعددة يدويًا:
- `my_project_final.py`
- `my_project_final_v2.py`
- `my_project_final_FINAL.py`
- `my_project_final_FINAL_for_real.py`

**Sound familiar?** This gets messy quickly!

**يبدو مألوفًا؟** هذا يصبح فوضويًا بسرعة!

### The Git Way
### طريقة Git

Git automatically tracks every change you make. You can:
- ✅ See exactly what changed and when
- ✅ Go back to any previous version
- ✅ Try experiments without fear of breaking things
- ✅ Work with others without overwriting their changes

Git يتتبع تلقائيًا كل تغيير تقوم به. يمكنك:
- ✅ رؤية بالضبط ما تغير ومتى
- ✅ العودة إلى أي نسخة سابقة
- ✅ تجربة التجارب دون خوف من كسر الأشياء
- ✅ العمل مع الآخرين دون الكتابة فوق تغييراتهم

---

## Think of Git Like...
## فكر في Git مثل...

### 🎮 Video Game Save Points
### 🎮 نقاط حفظ ألعاب الفيديو

Git commits are like save points in a video game. If you make a mistake, you can reload an earlier save!

الالتزامات (commits) في Git مثل نقاط الحفظ في ألعاب الفيديو. إذا ارتكبت خطأ، يمكنك إعادة تحميل حفظ سابق!

### 📝 Google Docs Version History
### 📝 سجل الإصدارات في Google Docs

Ever used "Version History" in Google Docs? Git does the same thing, but for code!

هل استخدمت يومًا "Version History" في Google Docs؟ Git يفعل نفس الشيء، ولكن للكود!

### 📸 Photo Snapshots
### 📸 لقطات الصور

Each Git commit is like taking a photo of your code at a specific moment. You can browse through your "photo album" later!

كل التزام (commit) في Git مثل التقاط صورة لكودك في لحظة محددة. يمكنك تصفح "ألبوم الصور" الخاص بك لاحقًا!

---

## Git vs GitHub: What's the Difference?
## Git مقابل GitHub: ما الفرق؟

This confuses many beginners, so let's clarify:

هذا يحير العديد من المبتدئين، لذا دعونا نوضح:

| Git | GitHub |
|-----|--------|
| Software tool on your computer | Website/service on the internet |
| أداة برمجية على حاسوبك | موقع ويب/خدمة على الإنترنت |
| Works offline (local) | Works online (remote) |
| يعمل دون اتصال (محلي) | يعمل عبر الإنترنت (عن بُعد) |
| Version control system | Hosting service for Git repositories |
| نظام التحكم في الإصدارات | خدمة استضافة لمستودعات Git |
| Free and open source | Free for public projects |
| مجاني ومفتوح المصدر | مجاني للمشاريع العامة |

### Analogy
### تشبيه

**Git is like Microsoft Word** (the program on your computer)
**GitHub is like Google Drive** (where you store and share documents online)

**Git مثل Microsoft Word** (البرنامج على حاسوبك)
**GitHub مثل Google Drive** (حيث تخزن وتشارك المستندات عبر الإنترنت)

---

## Basic Git Terminology
## المصطلحات الأساسية في Git

Let's learn the essential vocabulary. Don't worry if these seem confusing at first—they'll become clear with practice!

لنتعلم المفردات الأساسية. لا تقلق إذا بدت هذه محيرة في البداية—ستصبح واضحة مع الممارسة!

### Repository (Repo)
### المستودع (Repo)

**What it is:** A folder that Git tracks. Contains all your project files and their history.

**ما هو:** مجلد يتتبعه Git. يحتوي على جميع ملفات مشروعك وتاريخها.

**Analogy:** Think of it as a magical folder that remembers everything that ever happened inside it.

**تشبيه:** فكر فيه كمجلد سحري يتذكر كل شيء حدث بداخله.

### Commit
### الالتزام (Commit)

**What it is:** A snapshot of your code at a specific point in time. Like a save point.

**ما هو:** لقطة من كودك في نقطة زمنية محددة. مثل نقطة الحفظ.

**Analogy:** Like taking a photo of your room—you can see exactly how it looked at that moment.

**تشبيه:** مثل التقاط صورة لغرفتك—يمكنك رؤية بالضبط كيف بدت في تلك اللحظة.

### Clone
### النسخ (Clone)

**What it is:** Making a copy of a repository from GitHub to your computer.

**ما هو:** عمل نسخة من مستودع من GitHub إلى حاسوبك.

**Analogy:** Like downloading a movie to watch offline—you get your own copy.

**تشبيه:** مثل تحميل فيلم لمشاهدته دون اتصال—تحصل على نسختك الخاصة.

### Pull
### السحب (Pull)

**What it is:** Getting the latest updates from GitHub to your computer.

**ما هو:** الحصول على أحدث التحديثات من GitHub إلى حاسوبك.

**Analogy:** Like refreshing your social media feed to see new posts.

**تشبيه:** مثل تحديث موجز وسائل التواصل الاجتماعي لرؤية المنشورات الجديدة.

### Push
### الدفع (Push)

**What it is:** Sending your changes from your computer to GitHub.

**ما هو:** إرسال تغييراتك من حاسوبك إلى GitHub.

**Analogy:** Like uploading photos to Instagram—sharing your work with others.

**تشبيه:** مثل رفع الصور إلى Instagram—مشاركة عملك مع الآخرين.

### Branch
### الفرع (Branch)

**What it is:** A separate version of your code where you can experiment safely.

**ما هو:** نسخة منفصلة من كودك حيث يمكنك التجربة بأمان.

**Analogy:** Like having a rough draft and a final draft of an essay—you can experiment in the rough draft.

**تشبيه:** مثل وجود مسودة أولية ونسخة نهائية من مقال—يمكنك التجربة في المسودة الأولية.

---

## Visual Guide: How Git Works
## دليل مرئي: كيف يعمل Git

### The Git Workflow Diagram
### مخطط سير عمل Git

```
[Your Computer/Local]          [Internet/GitHub]
[حاسوبك/محلي]                   [الإنترنت/GitHub]
       ↓                              ↑
    CLONE                          PUSH
    (نسخ)                         (دفع)
       ↓                              ↑
 Working Directory    ←→      Remote Repository
 (دليل العمل)                  (المستودع البعيد)
       ↓                              ↑
    PULL                         (Updates)
    (سحب)                       (تحديثات)
       ↓                              ↑
```

### Timeline View
### عرض الخط الزمني

```
Start → Commit 1 → Commit 2 → Commit 3 → Current
بداية → التزام 1 → التزام 2 → التزام 3 → الحالي

Each commit saves:
كل التزام يحفظ:
- What changed / ما تغير
- Who made the change / من قام بالتغيير
- When it happened / متى حدث
- Why (commit message) / لماذا (رسالة الالتزام)
```

---

## Why We Use Git in This Course
## لماذا نستخدم Git في هذا المقرر

### 1. Professional Skill Development
### 1. تطوير المهارات المهنية

Git is used by every professional developer. Learning it now gives you a head start in your career!

Git يستخدمه كل مطور محترف. تعلمه الآن يمنحك بداية قوية في حياتك المهنية!

### 2. Easy Access to Course Materials
### 2. سهولة الوصول لمواد المقرر

- All course materials in one place
- Get updates instantly when instructor adds new content
- Never lose important files

- جميع مواد المقرر في مكان واحد
- احصل على التحديثات فورًا عندما يضيف المدرس محتوى جديدًا
- لا تفقد الملفات المهمة أبدًا

### 3. Learn Industry Practices
### 3. تعلم ممارسات الصناعة

You'll learn how real development teams work together on projects.

ستتعلم كيف تعمل فرق التطوير الحقيقية معًا على المشاريع.

### 4. Build Your Portfolio
### 4. بناء محفظتك

Your GitHub profile can showcase your work to future employers!

يمكن لملفك الشخصي على GitHub عرض أعمالك لأصحاب العمل المستقبليين!

---

## Common Questions
## الأسئلة الشائعة

### Q: Do I need to be good at Git to pass this course?
### س: هل أحتاج أن أكون جيدًا في Git لاجتياز هذا المقرر؟

**A:** No! You only need to know basic commands (clone and pull). We'll teach you everything step by step.

**ج:** لا! تحتاج فقط معرفة الأوامر الأساسية (clone و pull). سنعلمك كل شيء خطوة بخطوة.

### Q: What if I make a mistake?
### س: ماذا لو ارتكبت خطأ؟

**A:** Don't worry! Git is very forgiving. You can't break the course repository, and we'll help you fix any issues.

**ج:** لا تقلق! Git متسامح جدًا. لا يمكنك كسر مستودع المقرر، وسنساعدك في إصلاح أي مشاكل.

### Q: Is Git only for programmers?
### س: هل Git للمبرمجين فقط؟

**A:** While mostly used by programmers, Git can track any files! Writers, designers, and researchers also use it.

**ج:** بينما يستخدمه المبرمجون غالبًا، يمكن لـ Git تتبع أي ملفات! الكُتاب والمصممون والباحثون يستخدمونه أيضًا.

### Q: Do I need to pay for Git or GitHub?
### س: هل أحتاج للدفع مقابل Git أو GitHub؟

**A:** No! Git is completely free, and GitHub is free for students and public projects.

**ج:** لا! Git مجاني تمامًا، و GitHub مجاني للطلاب والمشاريع العامة.

---

## Real-World Examples
## أمثلة من العالم الحقيقي

### Companies Using Git
### الشركات التي تستخدم Git

- **Google** - All their code is version controlled
- **Microsoft** - Windows development uses Git
- **Facebook/Meta** - Manages billions of lines of code with Git
- **Netflix** - Tracks all their service code

- **جوجل** - كل كودهم تحت التحكم في الإصدارات
- **مايكروسوفت** - تطوير Windows يستخدم Git
- **فيسبوك/ميتا** - يدير مليارات الأسطر من الكود باستخدام Git
- **نتفليكس** - يتتبع كل كود خدمتهم

### Why Companies Love Git
### لماذا تحب الشركات Git

1. **Team Collaboration** - Multiple developers can work together
2. **Code History** - Can see who changed what and why
3. **Backup** - Code is never lost
4. **Experimentation** - Can try new features safely

1. **التعاون الجماعي** - يمكن لعدة مطورين العمل معًا
2. **تاريخ الكود** - يمكن رؤية من غيّر ماذا ولماذا
3. **النسخ الاحتياطي** - لا يضيع الكود أبدًا
4. **التجريب** - يمكن تجربة ميزات جديدة بأمان

---

## Practice Exercise
## تمرين الممارسة

### Mental Exercise (No Computer Needed)
### تمرين ذهني (لا حاسوب مطلوب)

Think about a time when you wished you could "undo" changes to a document or project. How would Git have helped in that situation?

فكر في وقت تمنيت فيه أن تتمكن من "التراجع" عن تغييرات في مستند أو مشروع. كيف كان Git سيساعد في تلك الحالة؟

### Reflection Questions
### أسئلة للتأمل

1. What's one thing about Git that excites you?
2. What's one thing that seems challenging?
3. How might Git skills help in your future career?

1. ما الشيء الوحيد حول Git الذي يثير حماسك؟
2. ما الشيء الوحيد الذي يبدو صعبًا؟
3. كيف يمكن أن تساعد مهارات Git في حياتك المهنية المستقبلية؟

---

## Next Steps
## الخطوات التالية

Ready to start using Git? Your next guide will teach you the basic commands you need for this course:

مستعد لبدء استخدام Git؟ دليلك التالي سيعلمك الأوامر الأساسية التي تحتاجها لهذا المقرر:

➡️ **[02-basic-git-commands.md](02-basic-git-commands.md)** - Learn the essential Git commands

➡️ **[02-basic-git-commands.md](02-basic-git-commands.md)** - تعلم أوامر Git الأساسية

---

## Remember
## تذكر

- 🎯 **You don't need to master Git** - Just learn the basics
- 💪 **Git is a professional skill** - It looks great on your resume
- 🤝 **We're here to help** - Ask questions when stuck
- 📈 **It gets easier with practice** - Don't worry if it seems complex at first

- 🎯 **لا تحتاج لإتقان Git** - فقط تعلم الأساسيات
- 💪 **Git مهارة مهنية** - تبدو رائعة في سيرتك الذاتية
- 🤝 **نحن هنا للمساعدة** - اسأل عند التعثر
- 📈 **يصبح أسهل مع الممارسة** - لا تقلق إذا بدا معقدًا في البداية

---

*Keep going! You're learning a skill that every professional developer uses!*

*استمر! أنت تتعلم مهارة يستخدمها كل مطور محترف!*