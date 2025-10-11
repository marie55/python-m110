# VS Code Interface Overview
# نظرة عامة على واجهة VS Code

⏱️ **Estimated Time:** 20 minutes
⏱️ **الوقت المقدر:** 20 دقيقة

## What You'll Learn
## ما ستتعلمه

By the end of this guide, you'll be able to:
- ✅ Understand the difference between an IDE and a text editor
- ✅ Identify the five main areas of the VS Code interface
- ✅ Open and navigate folders in VS Code
- ✅ Customize the appearance to your liking
- ✅ Feel comfortable using VS Code for Python programming

بنهاية هذا الدليل، ستكون قادرًا على:
- ✅ فهم الفرق بين IDE ومحرر النصوص
- ✅ تحديد المناطق الخمس الرئيسية في واجهة VS Code
- ✅ فتح المجلدات والتنقل فيها في VS Code
- ✅ تخصيص المظهر حسب ذوقك
- ✅ الشعور بالراحة في استخدام VS Code لبرمجة بايثون

## Why This Matters
## لماذا هذا مهم

Visual Studio Code (VS Code) is one of the most popular code editors used by professional developers worldwide. It's free, powerful, and packed with features that make coding easier. Learning to use VS Code well will make you more productive and prepare you for real-world development work.

Visual Studio Code (VS Code) هو واحد من أكثر محررات الأكواد شعبية التي يستخدمها المطورون المحترفون في جميع أنحاء العالم. إنه مجاني، قوي، ومليء بالميزات التي تجعل البرمجة أسهل. تعلم استخدام VS Code بشكل جيد سيجعلك أكثر إنتاجية ويعدك لعمل التطوير في العالم الواقعي.

## Prerequisites
## المتطلبات الأساسية

- VS Code installed on your computer ([see installation guide](../setup-guides/02-vscode-installation.md))
- The `python-m110` repository cloned to your computer

- VS Code مثبت على جهازك ([انظر دليل التثبيت](../setup-guides/02-vscode-installation.md))
- مستودع `python-m110` منسوخ على جهازك

---

## What is an IDE?
## ما هو IDE؟

### IDE vs Text Editor
### IDE مقابل محرر النصوص

Before we dive into VS Code, let's understand what makes it special.

قبل أن نغوص في VS Code، دعونا نفهم ما الذي يجعله مميزًا.

**Text Editor** (like Notepad or TextEdit):
- Opens and edits text files
- No special features for coding
- Can't run your code directly
- No error checking
- Basic find and replace

**محرر النصوص** (مثل Notepad أو TextEdit):
- يفتح ويحرر ملفات النصوص
- لا توجد ميزات خاصة للبرمجة
- لا يمكنه تشغيل كودك مباشرة
- لا يوجد فحص للأخطاء
- بحث واستبدال أساسي

**IDE** (Integrated Development Environment) like VS Code:
- Opens and edits code with syntax highlighting (colors!)
- Auto-completes your code (IntelliSense)
- Runs your code with one click
- Shows errors as you type
- Integrates with Git for version control
- Has built-in terminal
- Can install extensions for extra features
- Supports debugging (finding bugs step by step)

**IDE** (بيئة التطوير المتكاملة) مثل VS Code:
- يفتح ويحرر الكود مع تمييز الصياغة (بالألوان!)
- يكمل كودك تلقائيًا (IntelliSense)
- يشغل كودك بنقرة واحدة
- يظهر الأخطاء أثناء الكتابة
- يتكامل مع Git للتحكم في الإصدارات
- يحتوي على طرفية مدمجة
- يمكنه تثبيت الإضافات للحصول على ميزات إضافية
- يدعم التصحيح (إيجاد الأخطاء خطوة بخطوة)

💡 **Think of it this way:** Text editor = basic phone 📱, IDE = smartphone 📱✨

💡 **فكر في الأمر بهذه الطريقة:** محرر النصوص = هاتف أساسي 📱، IDE = هاتف ذكي 📱✨

---

## VS Code Interface Tour
## جولة في واجهة VS Code

When you first open VS Code, it can look overwhelming. Let's break it down into manageable pieces.

عندما تفتح VS Code لأول مرة، قد يبدو مربكًا. لنقسمه إلى أجزاء يمكن إدارتها.

### The Five Main Areas
### المناطق الخمس الرئيسية

```
┌─────┬────────────────────────────────────────────┬─────────┐
│  A  │                    C. Editor                 │         │
│  C  ├────────────────────────────────────────────┤    D    │
│  T  │                                              │         │
│  I  │           Where you write your code          │  Panel  │
│  V  │                                              │         │
│  I  │                                              ├─────────┤
│  T  ├────────────────────────────────────────────┤         │
│  Y  │               E. Terminal/Panel             │         │
│     │                                              │         │
│ BAR │          Command line at bottom             │         │
├─────┴────────────────────────────────────────────┴─────────┤
│                    F. Status Bar                            │
└──────────────────────────────────────────────────────────────┘
       B. Side Bar (changes based on Activity Bar selection)
```

### 1. Activity Bar (Left Edge)
### 1. شريط الأنشطة (الحافة اليسرى)

The vertical bar on the far left with icons. This is your main navigation.

الشريط العمودي على أقصى اليسار بالأيقونات. هذا هو التنقل الرئيسي الخاص بك.

**Icons you'll see:**
| Icon | Name | What it does | Keyboard Shortcut |
|------|------|--------------|-------------------|
| 📁 | Explorer | Browse your files and folders | `Ctrl+Shift+E` (Windows/Linux) <br> `Cmd+Shift+E` (Mac) |
| 🔍 | Search | Find text across all files | `Ctrl+Shift+F` <br> `Cmd+Shift+F` |
| 🔀 | Source Control | Git integration (version control) | `Ctrl+Shift+G` <br> `Cmd+Shift+G` |
| ▶️ | Run & Debug | Run and debug your code | `Ctrl+Shift+D` <br> `Cmd+Shift+D` |
| 🧩 | Extensions | Install add-ons to enhance VS Code | `Ctrl+Shift+X` <br> `Cmd+Shift+X` |

**الأيقونات التي ستراها:**
| أيقونة | الاسم | ماذا يفعل | اختصار لوحة المفاتيح |
|------|------|-------------|-------------------|
| 📁 | المستكشف | تصفح ملفاتك ومجلداتك | `Ctrl+Shift+E` (ويندوز/لينكس) <br> `Cmd+Shift+E` (ماك) |
| 🔍 | البحث | ابحث عن نص في جميع الملفات | `Ctrl+Shift+F` <br> `Cmd+Shift+F` |
| 🔀 | التحكم في المصدر | تكامل Git (التحكم في الإصدارات) | `Ctrl+Shift+G` <br> `Cmd+Shift+G` |
| ▶️ | التشغيل والتصحيح | شغل وصحح كودك | `Ctrl+Shift+D` <br> `Cmd+Shift+D` |
| 🧩 | الإضافات | ثبّت إضافات لتحسين VS Code | `Ctrl+Shift+X` <br> `Cmd+Shift+X` |

**🎯 Try it now:** Click each icon and watch the Side Bar change!

**🎯 جربه الآن:** انقر على كل أيقونة وشاهد الشريط الجانبي يتغير!

### 2. Side Bar (Context Panel)
### 2. الشريط الجانبي (لوحة السياق)

This area changes based on what you select in the Activity Bar. Most of the time, you'll use the Explorer view.

هذه المنطقة تتغير بناءً على ما تختاره في شريط الأنشطة. معظم الوقت، ستستخدم عرض المستكشف.

**Explorer View Shows:**
- Folder structure (tree view)
- Open files (tabs at top of editor)
- Outline of current file
- Timeline (file history)

**عرض المستكشف يظهر:**
- هيكل المجلدات (عرض شجري)
- الملفات المفتوحة (تبويبات في أعلى المحرر)
- مخطط الملف الحالي
- الجدول الزمني (تاريخ الملف)

### 3. Editor (Main Area)
### 3. المحرر (المنطقة الرئيسية)

This is where you write your code! The editor has many features:

هنا حيث تكتب كودك! المحرر له العديد من الميزات:

- **Tabs:** Open multiple files at once
- **Syntax highlighting:** Colors for different code elements
- **Line numbers:** Reference specific lines
- **Code folding:** Hide/show blocks of code
- **Minimap:** Bird's eye view of your file (right side)
- **Split view:** View multiple files side by side

- **التبويبات:** افتح عدة ملفات في وقت واحد
- **تمييز الصياغة:** ألوان لعناصر الكود المختلفة
- **أرقام الأسطر:** مرجع لأسطر محددة
- **طي الكود:** إخفاء/إظهار كتل من الكود
- **الخريطة المصغرة:** نظرة شاملة على ملفك (الجانب الأيمن)
- **العرض المقسم:** عرض عدة ملفات جنبًا إلى جنب

### 4. Panel (Bottom Area)
### 4. اللوحة (المنطقة السفلى)

Usually contains the terminal, but can show:
- Terminal (command line)
- Problems (errors and warnings)
- Output (from running programs)
- Debug Console (for debugging)

عادة تحتوي على الطرفية، لكن يمكن أن تظهر:
- الطرفية (سطر الأوامر)
- المشاكل (أخطاء وتحذيرات)
- الإخراج (من البرامج قيد التشغيل)
- وحدة التصحيح (للتصحيح)

**Toggle Panel:** Press `` Ctrl+` `` (Windows/Linux) or `` Cmd+` `` (Mac)

**إظهار/إخفاء اللوحة:** اضغط `` Ctrl+` `` (ويندوز/لينكس) أو `` Cmd+` `` (ماك)

### 5. Status Bar (Bottom Edge)
### 5. شريط الحالة (الحافة السفلى)

Shows important information:
- Current line and column
- Selected programming language
- Encoding (UTF-8)
- Line endings (LF/CRLF)
- Python interpreter version
- Git branch
- Notifications and errors

يظهر معلومات مهمة:
- السطر والعمود الحالي
- لغة البرمجة المختارة
- الترميز (UTF-8)
- نهايات الأسطر (LF/CRLF)
- إصدار مفسر بايثون
- فرع Git
- الإشعارات والأخطاء

---

## Opening Your Course Repository
## فتح مستودع المقرر الخاص بك

Let's practice opening your course repository in VS Code.

لنتمرن على فتح مستودع المقرر الخاص بك في VS Code.

### Method 1: File Menu
### الطريقة 1: قائمة الملف

1. Click **File → Open Folder** (Windows/Linux) or **File → Open** (Mac)
2. Navigate to where you cloned `python-m110`
3. Select the entire `python-m110` folder
4. Click "Select Folder" or "Open"

1. انقر على **File → Open Folder** (ويندوز/لينكس) أو **File → Open** (ماك)
2. انتقل إلى حيث قمت باستنساخ `python-m110`
3. حدد مجلد `python-m110` بأكمله
4. انقر على "Select Folder" أو "Open"

### Method 2: Drag and Drop
### الطريقة 2: السحب والإفلات

1. Find the `python-m110` folder in your file explorer
2. Drag it onto the VS Code window
3. VS Code will open it automatically

1. ابحث عن مجلد `python-m110` في مستكشف الملفات
2. اسحبه إلى نافذة VS Code
3. سيفتحه VS Code تلقائيًا

### What You Should See
### ما يجب أن تراه

In the Explorer (Side Bar), you should see:
```
python-m110/
├── 📁 code-examples/
├── 📁 exercises/
├── 📁 labs/
├── 📁 lectures/
├── 📁 projects/
├── 📁 resources/
├── 📁 venv/
├── 📄 README.md
└── 📄 requirements.txt
```

في المستكشف (الشريط الجانبي)، يجب أن ترى:
```
python-m110/
├── 📁 code-examples/
├── 📁 exercises/
├── 📁 labs/
├── 📁 lectures/
├── 📁 projects/
├── 📁 resources/
├── 📁 venv/
├── 📄 README.md
└── 📄 requirements.txt
```

🎉 **Success!** You're now viewing your course repository in VS Code!

🎉 **نجاح!** أنت الآن تشاهد مستودع المقرر الخاص بك في VS Code!

---

## Customizing VS Code Appearance
## تخصيص مظهر VS Code

Make VS Code comfortable for your eyes and preferences.

اجعل VS Code مريحًا لعينيك وتفضيلاتك.

### Change the Theme
### تغيير المظهر

1. Press `Ctrl+K` then `Ctrl+T` (Windows/Linux) or `Cmd+K` then `Cmd+T` (Mac)
2. Or go to **File → Preferences → Theme → Color Theme**
3. Use arrow keys to preview themes
4. Press `Enter` to select

1. اضغط `Ctrl+K` ثم `Ctrl+T` (ويندوز/لينكس) أو `Cmd+K` ثم `Cmd+T` (ماك)
2. أو اذهب إلى **File → Preferences → Theme → Color Theme**
3. استخدم مفاتيح الأسهم لمعاينة المظاهر
4. اضغط `Enter` للاختيار

**Popular Themes:**
- **Dark+** (default dark) - Easy on the eyes for long coding sessions
- **Light+** (default light) - Good for bright environments
- **Monokai** - Popular among Python developers
- **One Dark Pro** - Modern and colorful

**المظاهر الشائعة:**
- **Dark+** (الافتراضي الداكن) - مريح للعيون لجلسات البرمجة الطويلة
- **Light+** (الافتراضي الفاتح) - جيد للبيئات المضيئة
- **Monokai** - شائع بين مطوري بايثون
- **One Dark Pro** - حديث وملون

### Adjust Font Size
### تعديل حجم الخط

**Quick adjustment:**
- **Zoom in:** `Ctrl+` (Windows/Linux) or `Cmd+` (Mac)
- **Zoom out:** `Ctrl-` (Windows/Linux) or `Cmd-` (Mac)
- **Reset:** `Ctrl+0` (Windows/Linux) or `Cmd+0` (Mac)

**التعديل السريع:**
- **التكبير:** `Ctrl+` (ويندوز/لينكس) أو `Cmd+` (ماك)
- **التصغير:** `Ctrl-` (ويندوز/لينكس) أو `Cmd-` (ماك)
- **إعادة تعيين:** `Ctrl+0` (ويندوز/لينكس) أو `Cmd+0` (ماك)

**Permanent change:**
1. Go to **File → Preferences → Settings**
2. Search for "font size"
3. Change "Editor: Font Size" to your preference (14-18 is common)

**التغيير الدائم:**
1. اذهب إلى **File → Preferences → Settings**
2. ابحث عن "font size"
3. غير "Editor: Font Size" حسب تفضيلك (14-18 شائع)

---

## Workspace vs Single File
## مساحة العمل مقابل ملف واحد

Understanding this difference is important for organizing your work.

فهم هذا الفرق مهم لتنظيم عملك.

### Single File Mode
### وضع الملف الواحد

When you open just one file:
- No folder structure visible
- Limited features
- Good for quick edits

عندما تفتح ملفًا واحدًا فقط:
- لا يظهر هيكل المجلدات
- ميزات محدودة
- جيد للتعديلات السريعة

### Workspace/Folder Mode (Recommended)
### وضع مساحة العمل/المجلد (موصى به)

When you open a folder:
- See all files and folders
- Full VS Code features
- Can run terminal commands in correct location
- Git integration works
- Extensions work properly

عندما تفتح مجلدًا:
- ترى جميع الملفات والمجلدات
- ميزات VS Code الكاملة
- يمكنك تشغيل أوامر الطرفية في الموقع الصحيح
- يعمل تكامل Git
- تعمل الإضافات بشكل صحيح

**💡 Always open the entire `python-m110` folder, not individual files!**

**💡 دائمًا افتح مجلد `python-m110` بالكامل، ليس ملفات فردية!**

---

## Hands-On Practice
## ممارسة عملية

Let's practice what you've learned!

لنمارس ما تعلمته!

### Exercise 1: Navigate the Interface
### التمرين 1: التنقل في الواجهة

1. Open VS Code
2. Open the `python-m110` folder
3. Click on each Activity Bar icon and observe the Side Bar
4. Open the file `code-examples/week-02-fundamentals/01_hello_world.py`
5. Toggle the terminal panel with `` Ctrl+` ``
6. Look at the Status Bar - what information do you see?

1. افتح VS Code
2. افتح مجلد `python-m110`
3. انقر على كل أيقونة في شريط الأنشطة ولاحظ الشريط الجانبي
4. افتح الملف `code-examples/week-02-fundamentals/01_hello_world.py`
5. أظهر/أخف لوحة الطرفية باستخدام `` Ctrl+` ``
6. انظر إلى شريط الحالة - ما المعلومات التي تراها؟

### Exercise 2: Customize Your Environment
### التمرين 2: خصص بيئتك

1. Try 3 different color themes
2. Adjust the font size to your comfort
3. Open two files side by side (right-click a tab → "Split Right")
4. Close all open files (right-click a tab → "Close All")

1. جرب 3 مظاهر ألوان مختلفة
2. اضبط حجم الخط لراحتك
3. افتح ملفين جنبًا إلى جنب (انقر بزر الماوس الأيمن على تبويب → "Split Right")
4. أغلق جميع الملفات المفتوحة (انقر بزر الماوس الأيمن على تبويب → "Close All")

---

## Common Issues
## المشاكل الشائعة

### "I can't find my file!"
### "لا أستطيع إيجاد ملفي!"

**Solution:** Make sure you opened the entire folder, not just a file. Check the Explorer panel.

**الحل:** تأكد من أنك فتحت المجلد بأكمله، ليس مجرد ملف. تحقق من لوحة المستكشف.

### "VS Code looks different from the screenshots"
### "VS Code يبدو مختلفًا عن لقطات الشاشة"

**Solution:** VS Code updates frequently. The core features remain the same, but icons or colors might change slightly.

**الحل:** يتم تحديث VS Code بشكل متكرر. تبقى الميزات الأساسية كما هي، لكن الأيقونات أو الألوان قد تتغير قليلاً.

### "I accidentally closed a panel"
### "أغلقت لوحة بالخطأ"

**Solution:** Use the View menu to restore any panel, or reset the layout with **View → Appearance → Reset View Locations**.

**الحل:** استخدم قائمة View لاستعادة أي لوحة، أو أعد تعيين التخطيط باستخدام **View → Appearance → Reset View Locations**.

### "The text is too small/large"
### "النص صغير/كبير جدًا"

**Solution:** Use `Ctrl+` / `Ctrl-` (or `Cmd+` / `Cmd-` on Mac) to zoom.

**الحل:** استخدم `Ctrl+` / `Ctrl-` (أو `Cmd+` / `Cmd-` على ماك) للتكبير/التصغير.

---

## Tips & Tricks
## نصائح وحيل

### Quick File Opening
### فتح سريع للملفات

Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac) and start typing a filename. VS Code will search and show matching files!

اضغط `Ctrl+P` (ويندوز/لينكس) أو `Cmd+P` (ماك) وابدأ بكتابة اسم الملف. سيبحث VS Code ويعرض الملفات المطابقة!

### Command Palette
### لوحة الأوامر

Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to access all VS Code commands. This is your magic wand!

اضغط `Ctrl+Shift+P` (ويندوز/لينكس) أو `Cmd+Shift+P` (ماك) للوصول إلى جميع أوامر VS Code. هذه عصاك السحرية!

### Multiple Cursors
### مؤشرات متعددة

Hold `Alt` (Windows/Linux) or `Option` (Mac) and click to place multiple cursors. Type once, edit multiple places!

اضغط مع الاستمرار على `Alt` (ويندوز/لينكس) أو `Option` (ماك) وانقر لوضع مؤشرات متعددة. اكتب مرة واحدة، عدل في أماكن متعددة!

### Zen Mode
### وضع Zen

Press `Ctrl+K` then `Z` to enter Zen Mode - a distraction-free coding environment. Press `Esc` twice to exit.

اضغط `Ctrl+K` ثم `Z` للدخول في وضع Zen - بيئة برمجة خالية من المشتتات. اضغط `Esc` مرتين للخروج.

---

## Next Steps
## الخطوات التالية

Now that you're familiar with the VS Code interface, move on to:

1. [Essential VS Code Shortcuts](./02-essential-vscode-shortcuts.md) - Learn keyboard shortcuts to code faster
2. [Python Development in VS Code](./03-python-development-in-vscode.md) - Set up Python properly
3. [Terminal in VS Code](./04-terminal-in-vscode.md) - Master the integrated terminal

الآن بعد أن أصبحت على دراية بواجهة VS Code، انتقل إلى:

1. [اختصارات VS Code الأساسية](./02-essential-vscode-shortcuts.md) - تعلم اختصارات لوحة المفاتيح للبرمجة بشكل أسرع
2. [تطوير بايثون في VS Code](./03-python-development-in-vscode.md) - إعداد بايثون بشكل صحيح
3. [الطرفية في VS Code](./04-terminal-in-vscode.md) - إتقان الطرفية المدمجة

---

## Additional Resources
## موارد إضافية

- [Official VS Code Documentation](https://code.visualstudio.com/docs)
- [VS Code Intro Videos](https://code.visualstudio.com/docs/getstarted/introvideos)
- [Python in VS Code Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [VS Code Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

- [وثائق VS Code الرسمية](https://code.visualstudio.com/docs)
- [فيديوهات مقدمة VS Code](https://code.visualstudio.com/docs/getstarted/introvideos)
- [دروس بايثون في VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [نصائح وحيل VS Code](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

---

**Remember:** Don't feel overwhelmed! You don't need to master everything at once. Start with the basics, and gradually explore more features as you become comfortable.

**تذكر:** لا تشعر بالإرهاق! لا تحتاج لإتقان كل شيء دفعة واحدة. ابدأ بالأساسيات، واستكشف المزيد من الميزات تدريجيًا عندما تصبح مرتاحًا.

🚀 **Happy Coding!** | **برمجة سعيدة!** 🚀