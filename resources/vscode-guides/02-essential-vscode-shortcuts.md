# Essential VS Code Shortcuts
# اختصارات VS Code الأساسية

⏱️ **Estimated Time:** 15 minutes
⏱️ **الوقت المقدر:** 15 دقيقة

## What You'll Learn
## ما ستتعلمه

By the end of this guide, you'll be able to:
- ✅ Understand why keyboard shortcuts matter
- ✅ Use the most important shortcuts for Python programming
- ✅ Navigate VS Code efficiently without touching the mouse
- ✅ Customize shortcuts to match your preferences
- ✅ Work faster and more professionally

بنهاية هذا الدليل، ستكون قادرًا على:
- ✅ فهم أهمية اختصارات لوحة المفاتيح
- ✅ استخدام أهم الاختصارات لبرمجة بايثون
- ✅ التنقل في VS Code بكفاءة دون لمس الماوس
- ✅ تخصيص الاختصارات لتناسب تفضيلاتك
- ✅ العمل بشكل أسرع وأكثر احترافية

## Why This Matters
## لماذا هذا مهم

Professional developers use keyboard shortcuts because they:
- **Save time:** Tasks that take 5 clicks become instant
- **Maintain flow:** Keep your hands on the keyboard while thinking
- **Reduce strain:** Less mouse movement means less wrist strain
- **Look professional:** Efficient coding impresses employers

يستخدم المطورون المحترفون اختصارات لوحة المفاتيح لأنها:
- **توفر الوقت:** المهام التي تتطلب 5 نقرات تصبح فورية
- **تحافظ على التدفق:** أبقِ يديك على لوحة المفاتيح أثناء التفكير
- **تقلل الإجهاد:** حركة أقل للماوس تعني إجهاد أقل للمعصم
- **تبدو احترافية:** البرمجة الفعالة تثير إعجاب أصحاب العمل

## Prerequisites
## المتطلبات الأساسية

- VS Code installed and running
- Basic familiarity with VS Code interface ([see previous guide](./01-vscode-interface-overview.md))

- VS Code مثبت ويعمل
- معرفة أساسية بواجهة VS Code ([انظر الدليل السابق](./01-vscode-interface-overview.md))

---

## Platform Key Differences
## اختلافات المفاتيح حسب النظام

Before we start, understand these key mappings:

قبل أن نبدأ، افهم تعيينات المفاتيح هذه:

| Windows/Linux | Mac | Description |
|---------------|-----|-------------|
| `Ctrl` | `Cmd` (⌘) | Primary modifier key |
| `Alt` | `Option` (⌥) | Secondary modifier key |
| `Shift` | `Shift` (⇧) | Same on both |
| `Enter` | `Return` (⏎) | Same function |
| `Backspace` | `Delete` | Delete to the left |

| ويندوز/لينكس | ماك | الوصف |
|---------------|-----|-------------|
| `Ctrl` | `Cmd` (⌘) | مفتاح التعديل الأساسي |
| `Alt` | `Option` (⌥) | مفتاح التعديل الثانوي |
| `Shift` | `Shift` (⇧) | نفسه في كلا النظامين |
| `Enter` | `Return` (⏎) | نفس الوظيفة |
| `Backspace` | `Delete` | حذف لليسار |

**💡 Note:** This guide shows Windows/Linux first, then Mac in parentheses.

**💡 ملاحظة:** هذا الدليل يظهر ويندوز/لينكس أولاً، ثم ماك بين قوسين.

---

## 🎯 The Essential 10 - Master These First
## 🎯 العشرة الأساسية - أتقن هذه أولاً

These are the shortcuts you'll use every day. Learn these before anything else!

هذه هي الاختصارات التي ستستخدمها كل يوم. تعلم هذه قبل أي شيء آخر!

### 1. Save File
### 1. حفظ الملف

**`Ctrl+S`** (Mac: `Cmd+S`)

The most important shortcut! Save your work frequently.

أهم اختصار! احفظ عملك بشكل متكرر.

💡 **Enable Auto Save:** File → Auto Save (never lose work again!)

💡 **تفعيل الحفظ التلقائي:** File → Auto Save (لن تفقد عملك مرة أخرى!)

### 2. Run Python File
### 2. تشغيل ملف بايثون

**`Ctrl+F5`** (Mac: `Cmd+F5`)

Runs your Python file without debugging. This is what you'll use most often.

يشغل ملف بايثون بدون تصحيح. هذا ما ستستخدمه غالبًا.

**Alternative:** Click the ▶️ button in top-right of editor

**البديل:** انقر على زر ▶️ في أعلى يمين المحرر

### 3. Open/Close Terminal
### 3. فتح/إغلاق الطرفية

**`` Ctrl+` ``** (Mac: `` Cmd+` ``)

Toggle the terminal panel. Use this to run Python scripts manually.

إظهار/إخفاء لوحة الطرفية. استخدم هذا لتشغيل سكريبتات بايثون يدويًا.

### 4. Comment/Uncomment Lines
### 4. تعليق/إلغاء تعليق الأسطر

**`Ctrl+/`** (Mac: `Cmd+/`)

Quickly disable code without deleting it. Works on multiple lines!

عطّل الكود بسرعة دون حذفه. يعمل على عدة أسطر!

```python
# This line is commented / هذا السطر معلّق
print("This line runs")  # Partial comment / تعليق جزئي
```

### 5. Find in File
### 5. البحث في الملف

**`Ctrl+F`** (Mac: `Cmd+F`)

Search for text in the current file. Press `Enter` to go to next match.

ابحث عن نص في الملف الحالي. اضغط `Enter` للذهاب للتطابق التالي.

**Extra powers:**
- `F3` or `Enter`: Next match / التطابق التالي
- `Shift+F3` or `Shift+Enter`: Previous match / التطابق السابق
- `Alt+Enter`: Select all matches / حدد جميع التطابقات
- `Esc`: Close search / أغلق البحث

### 6. Quick Open File
### 6. فتح سريع للملف

**`Ctrl+P`** (Mac: `Cmd+P`)

Type part of any filename to open it instantly. No more clicking through folders!

اكتب جزء من أي اسم ملف لفتحه فورًا. لا مزيد من النقر عبر المجلدات!

**Example:** Type "hello" → Opens `01_hello_world.py`

**مثال:** اكتب "hello" → يفتح `01_hello_world.py`

### 7. Command Palette (Your Magic Wand)
### 7. لوحة الأوامر (عصاك السحرية)

**`Ctrl+Shift+P`** (Mac: `Cmd+Shift+P`)

Access EVERY VS Code command. When in doubt, use this!

الوصول لكل أمر في VS Code. عند الشك، استخدم هذا!

**Try these commands:**
- "theme" - Change color theme / تغيير مظهر الألوان
- "settings" - Open settings / فتح الإعدادات
- "python select" - Choose Python interpreter / اختيار مفسر بايثون
- "format" - Format your code / تنسيق كودك

### 8. Show/Hide Sidebar
### 8. إظهار/إخفاء الشريط الجانبي

**`Ctrl+B`** (Mac: `Cmd+B`)

Toggle the sidebar for more coding space.

إظهار/إخفاء الشريط الجانبي لمساحة برمجة أكبر.

### 9. Go to Line
### 9. الذهاب لسطر

**`Ctrl+G`** (Mac: `Cmd+G`)

Jump to any line number. Useful when Python shows an error on "line 42".

القفز لأي رقم سطر. مفيد عندما يظهر بايثون خطأ في "السطر 42".

### 10. Undo/Redo
### 10. تراجع/إعادة

**Undo: `Ctrl+Z`** (Mac: `Cmd+Z`)
**Redo: `Ctrl+Y` or `Ctrl+Shift+Z`** (Mac: `Cmd+Shift+Z`)

Made a mistake? These are your time machines!

أخطأت؟ هذه آلات الزمن الخاصة بك!

---

## 📝 Editing Shortcuts
## 📝 اختصارات التحرير

Make editing code faster and more efficient.

اجعل تحرير الكود أسرع وأكثر كفاءة.

### Select Text Efficiently
### تحديد النص بكفاءة

| Action | Windows/Linux | Mac | Description |
|--------|---------------|-----|-------------|
| Select word | `Ctrl+D` | `Cmd+D` | Select current word |
| Select line | `Ctrl+L` | `Cmd+L` | Select entire line |
| Select all same words | `Ctrl+Shift+L` | `Cmd+Shift+L` | Select all occurrences |
| Expand selection | `Shift+Alt+→` | `Shift+Option+→` | Expand selection smartly |

| الإجراء | ويندوز/لينكس | ماك | الوصف |
|--------|---------------|-----|-------------|
| تحديد كلمة | `Ctrl+D` | `Cmd+D` | حدد الكلمة الحالية |
| تحديد سطر | `Ctrl+L` | `Cmd+L` | حدد السطر بأكمله |
| تحديد كل الكلمات المماثلة | `Ctrl+Shift+L` | `Cmd+Shift+L` | حدد كل التطابقات |
| توسيع التحديد | `Shift+Alt+←` | `Shift+Option+←` | وسّع التحديد بذكاء |

### Move Lines
### تحريك الأسطر

**Move line up:** `Alt+↑` (Mac: `Option+↑`)
**Move line down:** `Alt+↓` (Mac: `Option+↓`)

**تحريك السطر لأعلى:** `Alt+↑` (Mac: `Option+↑`)
**تحريك السطر لأسفل:** `Alt+↓` (Mac: `Option+↓`)

No more cut and paste to reorganize code!

لا مزيد من القص واللصق لإعادة تنظيم الكود!

### Copy Line
### نسخ السطر

**Copy line down:** `Shift+Alt+↓` (Mac: `Shift+Option+↓`)
**Copy line up:** `Shift+Alt+↑` (Mac: `Shift+Option+↑`)

**نسخ السطر لأسفل:** `Shift+Alt+↓` (Mac: `Shift+Option+↓`)
**نسخ السطر لأعلى:** `Shift+Alt+↑` (Mac: `Shift+Option+↑`)

Duplicate lines instantly!

كرر الأسطر فورًا!

### Delete Line
### حذف السطر

**`Ctrl+Shift+K`** (Mac: `Cmd+Shift+K`)

Delete entire line without selecting it first.

احذف السطر بأكمله دون تحديده أولاً.

### Format Document
### تنسيق المستند

**`Shift+Alt+F`** (Mac: `Shift+Option+F`)

Automatically format your Python code to follow PEP 8 style guide.

نسّق كود بايثون تلقائيًا لاتباع دليل أسلوب PEP 8.

---

## 🔍 Navigation Shortcuts
## 🔍 اختصارات التنقل

Move around your code like a ninja!

تحرك في كودك مثل النينجا!

### Jump Between Files
### القفز بين الملفات

| Action | Windows/Linux | Mac | Description |
|--------|---------------|-----|-------------|
| Previous file | `Ctrl+Tab` | `Cmd+Tab` | Cycle through open files |
| Go to definition | `F12` | `F12` | Jump to function/variable definition |
| Peek definition | `Alt+F12` | `Option+F12` | See definition without leaving |
| Go back | `Alt+←` | `Ctrl+-` | Return to previous location |
| Go forward | `Alt+→` | `Ctrl+Shift+-` | Go forward in history |

| الإجراء | ويندوز/لينكس | ماك | الوصف |
|--------|---------------|-----|-------------|
| الملف السابق | `Ctrl+Tab` | `Cmd+Tab` | التنقل بين الملفات المفتوحة |
| الذهاب للتعريف | `F12` | `F12` | القفز لتعريف الدالة/المتغير |
| نظرة خاطفة للتعريف | `Alt+F12` | `Option+F12` | رؤية التعريف دون المغادرة |
| العودة | `Alt+←` | `Ctrl+-` | العودة للموقع السابق |
| التقدم | `Alt+→` | `Ctrl+Shift+-` | التقدم في السجل |

### Search Across Files
### البحث عبر الملفات

**`Ctrl+Shift+F`** (Mac: `Cmd+Shift+F`)

Search in all files in your project. Great for finding where a function is used!

ابحث في جميع ملفات مشروعك. رائع لإيجاد أين تُستخدم الدالة!

---

## 🎨 Multiple Cursors (Advanced Magic)
## 🎨 مؤشرات متعددة (سحر متقدم)

Edit multiple places at once - this will amaze your classmates!

حرر أماكن متعددة مرة واحدة - سيذهل هذا زملاءك!

### Add Cursors
### إضافة مؤشرات

**Click method:** `Alt+Click` (Mac: `Option+Click`)
Place cursors wherever you click.

**طريقة النقر:** `Alt+Click` (Mac: `Option+Click`)
ضع المؤشرات حيثما تنقر.

**Keyboard method:** `Ctrl+Alt+↑/↓` (Mac: `Cmd+Option+↑/↓`)
Add cursor above/below current line.

**طريقة لوحة المفاتيح:** `Ctrl+Alt+↑/↓` (Mac: `Cmd+Option+↑/↓`)
أضف مؤشر فوق/تحت السطر الحالي.

### Example Use Case
### مثال على الاستخدام

Change all variable names at once:
```python
# Before / قبل
score = 85
print(score)
if score > 80:
    return score

# Select all "score", press Ctrl+Shift+L
# حدد كل "score"، اضغط Ctrl+Shift+L
# Type "grade" / اكتب "grade"

# After / بعد
grade = 85
print(grade)
if grade > 80:
    return grade
```

---

## ⚡ Python-Specific Shortcuts
## ⚡ اختصارات خاصة ببايثون

Shortcuts that work especially well with Python code.

اختصارات تعمل بشكل خاص مع كود بايثون.

### Run Python File in Terminal
### تشغيل ملف بايثون في الطرفية

**Right-click in editor → "Run Python File in Terminal"**

No shortcut by default, but you can create one (see Customization section).

**انقر بزر الماوس الأيمن في المحرر → "Run Python File in Terminal"**

لا يوجد اختصار افتراضي، لكن يمكنك إنشاء واحد (انظر قسم التخصيص).

### Select Python Interpreter
### اختيار مفسر بايثون

**`Ctrl+Shift+P`** then type "Python: Select Interpreter"

Choose which Python version to use (important for virtual environments).

**`Ctrl+Shift+P`** ثم اكتب "Python: Select Interpreter"

اختر أي إصدار بايثون تستخدم (مهم للبيئات الافتراضية).

### Run Selection in Terminal
### تشغيل التحديد في الطرفية

**`Shift+Enter`**

Run only the selected Python code. Great for testing small pieces!

شغّل فقط كود بايثون المحدد. رائع لاختبار أجزاء صغيرة!

---

## 🛠️ Customizing Shortcuts
## 🛠️ تخصيص الاختصارات

Make VS Code work the way YOU want!

اجعل VS Code يعمل بالطريقة التي تريدها أنت!

### View Current Shortcuts
### عرض الاختصارات الحالية

1. **`Ctrl+K` then `Ctrl+S`** (Mac: `Cmd+K` then `Cmd+S`)
2. Or: File → Preferences → Keyboard Shortcuts

<!-- -->

1. **`Ctrl+K` ثم `Ctrl+S`** (Mac: `Cmd+K` ثم `Cmd+S`)
2. أو: File → Preferences → Keyboard Shortcuts

### Change a Shortcut
### تغيير اختصار

1. Search for the command
2. Click the pencil icon ✏️
3. Press your new key combination
4. Press `Enter` to save

<!-- -->

1. ابحث عن الأمر
2. انقر على أيقونة القلم ✏️
3. اضغط مجموعة المفاتيح الجديدة
4. اضغط `Enter` للحفظ

### Recommended Custom Shortcuts for Python
### اختصارات مخصصة موصى بها لبايثون

Consider adding these:

| Command | Suggested Shortcut | Why |
|---------|-------------------|-----|
| Run Python File | `F5` | Easier than `Ctrl+F5` |
| Clear Terminal | `Ctrl+K` | Clean output before running |
| Toggle Word Wrap | `Alt+Z` | Long lines easier to read |

فكر في إضافة هذه:

| الأمر | الاختصار المقترح | لماذا |
|---------|-------------------|-----|
| تشغيل ملف بايثون | `F5` | أسهل من `Ctrl+F5` |
| مسح الطرفية | `Ctrl+K` | مخرجات نظيفة قبل التشغيل |
| تبديل التفاف الكلمات | `Alt+Z` | الأسطر الطويلة أسهل للقراءة |

---

## 📋 Printable Cheat Sheet
## 📋 ورقة غش قابلة للطباعة

### Most Used Daily
### الأكثر استخدامًا يوميًا

```
ESSENTIAL SHORTCUTS - WINDOWS/LINUX
====================================
Save File:              Ctrl+S
Run Python:             Ctrl+F5
Open/Close Terminal:    Ctrl+`
Comment Lines:          Ctrl+/
Find:                   Ctrl+F
Quick Open:             Ctrl+P
Command Palette:        Ctrl+Shift+P
Toggle Sidebar:         Ctrl+B
Go to Line:             Ctrl+G
Undo/Redo:              Ctrl+Z / Ctrl+Y

EDITING
=======
Select Word:            Ctrl+D
Move Line Up/Down:      Alt+↑ / Alt+↓
Copy Line Up/Down:      Shift+Alt+↑ / Shift+Alt+↓
Delete Line:            Ctrl+Shift+K
Format Document:        Shift+Alt+F

NAVIGATION
==========
Switch Files:           Ctrl+Tab
Go to Definition:       F12
Go Back:                Alt+←
Search All Files:       Ctrl+Shift+F
```

```
ESSENTIAL SHORTCUTS - MAC
=========================
Save File:              Cmd+S
Run Python:             Cmd+F5
Open/Close Terminal:    Cmd+`
Comment Lines:          Cmd+/
Find:                   Cmd+F
Quick Open:             Cmd+P
Command Palette:        Cmd+Shift+P
Toggle Sidebar:         Cmd+B
Go to Line:             Cmd+G
Undo/Redo:              Cmd+Z / Cmd+Shift+Z

EDITING
=======
Select Word:            Cmd+D
Move Line Up/Down:      Option+↑ / Option+↓
Copy Line Up/Down:      Shift+Option+↑ / Shift+Option+↓
Delete Line:            Cmd+Shift+K
Format Document:        Shift+Option+F

NAVIGATION
==========
Switch Files:           Cmd+Tab
Go to Definition:       F12
Go Back:                Ctrl+-
Search All Files:       Cmd+Shift+F
```

---

## Hands-On Practice
## ممارسة عملية

Let's practice these shortcuts with real code!

لنمارس هذه الاختصارات مع كود حقيقي!

### Exercise 1: Basic Navigation
### التمرين 1: التنقل الأساسي

1. Open `code-examples/chapter-02-fundamentals/01_hello_world.py`
2. Use `Ctrl+P` to quickly open `02_variables.py`
3. Press `Ctrl+Tab` to switch back
4. Use `Ctrl+G` to go to line 5
5. Press `Ctrl+B` to hide/show the sidebar

<!-- -->

1. افتح `code-examples/chapter-02-fundamentals/01_hello_world.py`
2. استخدم `Ctrl+P` لفتح `02_variables.py` بسرعة
3. اضغط `Ctrl+Tab` للعودة
4. استخدم `Ctrl+G` للذهاب للسطر 5
5. اضغط `Ctrl+B` لإخفاء/إظهار الشريط الجانبي

### Exercise 2: Editing Practice
### التمرين 2: ممارسة التحرير

Create a new Python file and type:
```python
print("Hello")
print("Hello")
print("Hello")
```

Now try:
1. Place cursor on "Hello" and press `Ctrl+D` three times
2. Type "Hi" - all three change at once!
3. Press `Ctrl+Z` to undo
4. Select one line with `Ctrl+L`
5. Copy it down with `Shift+Alt+↓`

أنشئ ملف بايثون جديد واكتب:
```python
print("Hello")
print("Hello")
print("Hello")
```

الآن جرب:
1. ضع المؤشر على "Hello" واضغط `Ctrl+D` ثلاث مرات
2. اكتب "Hi" - الثلاثة يتغيرون مرة واحدة!
3. اضغط `Ctrl+Z` للتراجع
4. حدد سطرًا واحدًا باستخدام `Ctrl+L`
5. انسخه لأسفل باستخدام `Shift+Alt+↓`

### Exercise 3: Multiple Cursors
### التمرين 3: مؤشرات متعددة

Type this code:
```python
name1 = "Alice"
name2 = "Bob"
name3 = "Charlie"
```

Challenge: Change all "name" to "student" using multiple cursors:
1. Double-click "name" in first line
2. Press `Ctrl+D` twice more to select other instances
3. Type "student"
4. All three change simultaneously!

اكتب هذا الكود:
```python
name1 = "Alice"
name2 = "Bob"
name3 = "Charlie"
```

التحدي: غيّر كل "name" إلى "student" باستخدام مؤشرات متعددة:
1. انقر مرتين على "name" في السطر الأول
2. اضغط `Ctrl+D` مرتين أخريين لتحديد الحالات الأخرى
3. اكتب "student"
4. الثلاثة يتغيرون في وقت واحد!

---

## Common Issues
## المشاكل الشائعة

### "Shortcut doesn't work!"
### "الاختصار لا يعمل!"

**Possible causes:**
- Different keyboard layout (non-US keyboards may vary)
- Extension overriding the shortcut
- Wrong operating system shortcuts

**الأسباب المحتملة:**
- تخطيط لوحة مفاتيح مختلف (لوحات المفاتيح غير الأمريكية قد تختلف)
- إضافة تتجاوز الاختصار
- اختصارات نظام تشغيل خاطئة

**Solution:** Check and customize in Keyboard Shortcuts settings

**الحل:** تحقق وخصص في إعدادات اختصارات لوحة المفاتيح

### "I forgot the shortcut!"
### "نسيت الاختصار!"

**Solution:** Use Command Palette (`Ctrl+Shift+P`) and type what you want to do. The shortcut appears next to the command!

**الحل:** استخدم لوحة الأوامر (`Ctrl+Shift+P`) واكتب ما تريد فعله. يظهر الاختصار بجانب الأمر!

### "Multiple cursors confuse me"
### "المؤشرات المتعددة تربكني"

**Solution:** Press `Esc` to return to single cursor mode.

**الحل:** اضغط `Esc` للعودة لوضع المؤشر الواحد.

---

## Tips & Tricks
## نصائح وحيل

### Learn Gradually
### تعلم تدريجيًا

Don't try to memorize all shortcuts at once. Start with the Essential 10, then add one new shortcut each week.

لا تحاول حفظ كل الاختصارات مرة واحدة. ابدأ بالعشرة الأساسية، ثم أضف اختصارًا جديدًا كل أسبوع.

### Practice Makes Perfect
### الممارسة تصنع الكمال

Force yourself to use shortcuts even if it's slower at first. Within a week, they'll become natural.

أجبر نفسك على استخدام الاختصارات حتى لو كانت أبطأ في البداية. خلال أسبوع، ستصبح طبيعية.

### Watch the Status Bar
### راقب شريط الحالة

Many menu items show their shortcuts. Look for them as you use menus!

العديد من عناصر القائمة تظهر اختصاراتها. ابحث عنها أثناء استخدام القوائم!

### Create a Sticky Note
### أنشئ ملاحظة لاصقة

Write your 5 most-used shortcuts on a sticky note and put it on your monitor. Remove it once you've memorized them!

اكتب أكثر 5 اختصارات استخدامًا على ملاحظة لاصقة وضعها على شاشتك. أزلها بمجرد حفظها!

---

## Next Steps
## الخطوات التالية

Now that you know the shortcuts, let's set up Python properly:

1. [Python Development in VS Code](./03-python-development-in-vscode.md) - Configure Python for the best experience
2. [Terminal in VS Code](./04-terminal-in-vscode.md) - Master the command line

الآن بعد أن عرفت الاختصارات، لنقم بإعداد بايثون بشكل صحيح:

1. [تطوير بايثون في VS Code](./03-python-development-in-vscode.md) - اضبط بايثون لأفضل تجربة
2. [الطرفية في VS Code](./04-terminal-in-vscode.md) - أتقن سطر الأوامر

---

## Additional Resources
## موارد إضافية

- [Official VS Code Keyboard Shortcuts PDF](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf) (Windows)
- [Official VS Code Keyboard Shortcuts PDF](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf) (Mac)
- [Interactive Keyboard Shortcuts](https://code.visualstudio.com/docs/getstarted/keybindings)
- [VS Code Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

- [اختصارات لوحة المفاتيح الرسمية لـ VS Code PDF](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf) (ويندوز)
- [اختصارات لوحة المفاتيح الرسمية لـ VS Code PDF](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf) (ماك)
- [اختصارات لوحة المفاتيح التفاعلية](https://code.visualstudio.com/docs/getstarted/keybindings)
- [نصائح وحيل VS Code](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

---

**Remember:** Every professional developer was once a beginner who didn't know any shortcuts. Start with a few, practice daily, and soon you'll be coding like a pro!

**تذكر:** كل مطور محترف كان مبتدئًا لا يعرف أي اختصارات. ابدأ ببعض منها، تمرن يوميًا، وقريبًا ستبرمج مثل المحترفين!

⚡ **Speed up your coding journey!** | **سرّع رحلة برمجتك!** ⚡