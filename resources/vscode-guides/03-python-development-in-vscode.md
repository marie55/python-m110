# Python Development in VS Code
# تطوير بايثون في VS Code

⏱️ **Estimated Time:** 25 minutes
⏱️ **الوقت المقدر:** 25 دقيقة

## What You'll Learn
## ما ستتعلمه

By the end of this guide, you'll be able to:
- ✅ Install and configure the Python extension
- ✅ Select the correct Python interpreter (from your virtual environment)
- ✅ Use IntelliSense for auto-completion
- ✅ Understand and fix linting errors
- ✅ Format your code automatically to follow PEP 8
- ✅ Run Python code in multiple ways
- ✅ Debug your code (optional advanced skill)
- ✅ Read and understand error messages

بنهاية هذا الدليل، ستكون قادرًا على:
- ✅ تثبيت وإعداد إضافة بايثون
- ✅ اختيار مفسر بايثون الصحيح (من بيئتك الافتراضية)
- ✅ استخدام IntelliSense للإكمال التلقائي
- ✅ فهم وإصلاح أخطاء التحليل (linting)
- ✅ تنسيق كودك تلقائيًا لاتباع PEP 8
- ✅ تشغيل كود بايثون بطرق متعددة
- ✅ تصحيح كودك (مهارة متقدمة اختيارية)
- ✅ قراءة وفهم رسائل الخطأ

## Why This Matters
## لماذا هذا مهم

VS Code with proper Python setup gives you superpowers:
- **IntelliSense**: Auto-completes your code and shows function documentation
- **Error detection**: Finds mistakes before you run your code
- **Auto-formatting**: Makes your code beautiful and consistent
- **Debugging**: Step through code line by line to find bugs
- **Professional workflow**: Same tools used by professional developers

VS Code مع إعداد بايثون الصحيح يمنحك قوى خارقة:
- **IntelliSense**: يكمل كودك تلقائيًا ويظهر وثائق الدوال
- **اكتشاف الأخطاء**: يجد الأخطاء قبل تشغيل كودك
- **التنسيق التلقائي**: يجعل كودك جميلاً ومتسقًا
- **التصحيح**: تتبع الكود سطرًا بسطر لإيجاد الأخطاء
- **سير العمل الاحترافي**: نفس الأدوات التي يستخدمها المطورون المحترفون

## Prerequisites
## المتطلبات الأساسية

- VS Code installed and familiar with interface ([see guide 1](./01-vscode-interface-overview.md))
- Python installed on your computer ([see installation guide](../setup-guides/01-python-installation.md))
- Virtual environment created in `/python-m110/venv/`

- VS Code مثبت ومألوف مع الواجهة ([انظر الدليل 1](./01-vscode-interface-overview.md))
- بايثون مثبت على جهازك ([انظر دليل التثبيت](../setup-guides/01-python-installation.md))
- بيئة افتراضية منشأة في `/python-m110/venv/`

---

## Installing the Python Extension
## تثبيت إضافة بايثون

The Python extension transforms VS Code into a powerful Python IDE.

إضافة بايثون تحول VS Code إلى IDE قوي لبايثون.

### Step 1: Open Extensions View
### الخطوة 1: افتح عرض الإضافات

1. Click the Extensions icon in Activity Bar (🧩)
2. Or press `Ctrl+Shift+X` (Mac: `Cmd+Shift+X`)

<!-- -->

1. انقر على أيقونة الإضافات في شريط الأنشطة (🧩)
2. أو اضغط `Ctrl+Shift+X` (Mac: `Cmd+Shift+X`)

### Step 2: Search and Install
### الخطوة 2: ابحث وثبّت

1. Type "Python" in the search box
2. Look for **"Python"** by Microsoft (has millions of downloads)
3. Click the blue **"Install"** button
4. Wait for installation to complete (about 30 seconds)

<!-- -->

1. اكتب "Python" في صندوق البحث
2. ابحث عن **"Python"** من Microsoft (لديها ملايين التحميلات)
3. انقر على زر **"Install"** الأزرق
4. انتظر اكتمال التثبيت (حوالي 30 ثانية)

### Step 3: Verify Installation
### الخطوة 3: تحقق من التثبيت

Open any `.py` file. You should see:
- Colored syntax highlighting
- "Python" in the bottom-right status bar
- A play button (▶️) in the top-right

افتح أي ملف `.py`. يجب أن ترى:
- تمييز الصياغة الملون
- "Python" في شريط الحالة السفلي الأيمن
- زر التشغيل (▶️) في الأعلى الأيمن

🎉 **Success!** The Python extension is installed!

🎉 **نجاح!** تم تثبيت إضافة بايثون!

---

## Selecting Python Interpreter
## اختيار مفسر بايثون

This is CRUCIAL! You must select the Python interpreter from your virtual environment.

هذا مهم جداً! يجب عليك اختيار مفسر بايثون من بيئتك الافتراضية.

### Why This Matters
### لماذا هذا مهم

Your computer might have multiple Python versions:
- System Python (came with your OS)
- Python you installed
- Virtual environment Python (what we want!)

جهازك قد يحتوي على إصدارات بايثون متعددة:
- بايثون النظام (جاء مع نظام التشغيل)
- بايثون الذي ثبّته
- بايثون البيئة الافتراضية (ما نريده!)

### How to Select the Right Interpreter
### كيفية اختيار المفسر الصحيح

#### Method 1: Status Bar (Easiest)
#### الطريقة 1: شريط الحالة (الأسهل)

1. Look at the bottom-right status bar
2. Click on the Python version shown (e.g., "Python 3.11.2")
3. A list appears at the top
4. Select: **`./venv/bin/python`** (Mac/Linux) or **`.\venv\Scripts\python.exe`** (Windows)

<!-- -->

1. انظر إلى شريط الحالة السفلي الأيمن
2. انقر على إصدار بايثون المعروض (مثل "Python 3.11.2")
3. تظهر قائمة في الأعلى
4. اختر: **`./venv/bin/python`** (Mac/Linux) أو **`.\venv\Scripts\python.exe`** (Windows)

#### Method 2: Command Palette
#### الطريقة 2: لوحة الأوامر

1. Press `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
2. Type "Python: Select Interpreter"
3. Press `Enter`
4. Choose the one with **`venv`** in the path

<!-- -->

1. اضغط `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
2. اكتب "Python: Select Interpreter"
3. اضغط `Enter`
4. اختر الذي يحتوي على **`venv`** في المسار

### How to Verify
### كيفية التحقق

The status bar should show:
- **Good**: `3.11.2 ('venv': venv)` ✅
- **Bad**: `3.11.2 64-bit` ❌ (not using virtual environment)

شريط الحالة يجب أن يظهر:
- **جيد**: `3.11.2 ('venv': venv)` ✅
- **سيئ**: `3.11.2 64-bit` ❌ (لا يستخدم البيئة الافتراضية)

---

## IntelliSense (Auto-Completion)
## IntelliSense (الإكمال التلقائي)

IntelliSense is like having a Python expert sitting next to you!

IntelliSense مثل وجود خبير بايثون يجلس بجانبك!

### What IntelliSense Does
### ما يفعله IntelliSense

- **Auto-completes** as you type
- **Shows function signatures** (what parameters a function needs)
- **Displays documentation** when you hover
- **Suggests imports** for modules you need

- **يكمل تلقائيًا** أثناء الكتابة
- **يظهر توقيعات الدوال** (ما المعاملات التي تحتاجها الدالة)
- **يعرض الوثائق** عند التمرير
- **يقترح الاستيرادات** للوحدات التي تحتاجها

### How to Use IntelliSense
### كيفية استخدام IntelliSense

#### Auto-Completion
#### الإكمال التلقائي

1. Start typing: `prin`
2. IntelliSense shows suggestions
3. Use arrow keys to select
4. Press `Tab` or `Enter` to accept

<!-- -->

1. ابدأ بالكتابة: `prin`
2. يظهر IntelliSense الاقتراحات
3. استخدم مفاتيح الأسهم للاختيار
4. اضغط `Tab` أو `Enter` للقبول

#### Function Help
#### مساعدة الدوال

Type a function name and opening parenthesis:
```python
print(  # IntelliSense shows: print(value, ..., sep=' ', end='\n', ...)
```

اكتب اسم دالة وقوس الفتح:
```python
print(  # IntelliSense يظهر: print(value, ..., sep=' ', end='\n', ...)
```

#### Quick Info
#### معلومات سريعة

Hover over any variable or function to see its documentation:
```python
import math
math.sqrt  # Hover to see: "Return the square root of x"
```

مرر فوق أي متغير أو دالة لرؤية وثائقها:
```python
import math
math.sqrt  # مرر لترى: "Return the square root of x"
```

### IntelliSense Shortcuts
### اختصارات IntelliSense

| Action | Shortcut | Description |
|--------|----------|-------------|
| Trigger suggestions | `Ctrl+Space` | Manually show suggestions |
| Parameter hints | `Ctrl+Shift+Space` | Show function parameters |
| Quick info | Hover mouse | Show documentation |

| الإجراء | الاختصار | الوصف |
|--------|----------|-------------|
| إظهار الاقتراحات | `Ctrl+Space` | إظهار الاقتراحات يدويًا |
| تلميحات المعاملات | `Ctrl+Shift+Space` | إظهار معاملات الدالة |
| معلومات سريعة | تمرير الماوس | إظهار الوثائق |

---

## Linting (Error Detection)
## التحليل (اكتشاف الأخطاء)

Linting finds errors and style issues in your code before you run it.

التحليل يجد الأخطاء ومشاكل الأسلوب في كودك قبل تشغيله.

### Understanding Linting Indicators
### فهم مؤشرات التحليل

VS Code shows problems with colored squiggly lines:

VS Code يظهر المشاكل بخطوط متعرجة ملونة:

- 🔴 **Red squiggles**: Errors (code won't run)
- 🟡 **Yellow squiggles**: Warnings (code runs but has issues)
- 🟢 **Green squiggles**: Info (style suggestions)

- 🔴 **خطوط حمراء متعرجة**: أخطاء (الكود لن يعمل)
- 🟡 **خطوط صفراء متعرجة**: تحذيرات (الكود يعمل لكن به مشاكل)
- 🟢 **خطوط خضراء متعرجة**: معلومات (اقتراحات للأسلوب)

### Common Linting Messages
### رسائل التحليل الشائعة

#### Error Examples (Red)
#### أمثلة على الأخطاء (أحمر)

```python
print(Hello)  # ❌ NameError: name 'Hello' is not defined
prin("test")  # ❌ NameError: name 'prin' is not defined
if x = 5:     # ❌ SyntaxError: invalid syntax (should be ==)
```

#### Warning Examples (Yellow)
#### أمثلة على التحذيرات (أصفر)

```python
import math  # ⚠️ 'math' imported but unused
x = 5
x = 10       # ⚠️ Redefinition of unused 'x'
```

#### Style Examples (Green)
#### أمثلة على الأسلوب (أخضر)

```python
def myFunction():  # 💚 Function name should be lowercase with underscores
x=5+3             # 💚 Missing whitespace around operator
```

### Viewing All Problems
### عرض جميع المشاكل

1. Press `Ctrl+Shift+M` (Mac: `Cmd+Shift+M`)
2. Or click "Problems" tab in the panel
3. Click any problem to jump to that line

<!-- -->

1. اضغط `Ctrl+Shift+M` (Mac: `Cmd+Shift+M`)
2. أو انقر على تبويب "Problems" في اللوحة
3. انقر على أي مشكلة للقفز لذلك السطر

### Configuring Linting
### إعداد التحليل

VS Code uses Pylint by default. You can also use:
- **flake8**: Faster, focuses on errors
- **mypy**: Type checking
- **bandit**: Security issues

VS Code يستخدم Pylint افتراضيًا. يمكنك أيضًا استخدام:
- **flake8**: أسرع، يركز على الأخطاء
- **mypy**: فحص الأنواع
- **bandit**: مشاكل الأمان

To change linter:
1. `Ctrl+Shift+P` → "Python: Select Linter"
2. Choose your preferred linter
3. VS Code will offer to install it

لتغيير المحلل:
1. `Ctrl+Shift+P` → "Python: Select Linter"
2. اختر المحلل المفضل
3. VS Code سيعرض تثبيته

---

## Code Formatting (PEP 8)
## تنسيق الكود (PEP 8)

PEP 8 is Python's style guide. Formatting makes your code beautiful and consistent!

PEP 8 هو دليل أسلوب بايثون. التنسيق يجعل كودك جميلاً ومتسقًا!

### What is PEP 8?
### ما هو PEP 8؟

Python Enhancement Proposal 8 - the official Python style guide:
- Indentation: 4 spaces
- Line length: 79 characters max
- Spaces around operators: `x = 5`, not `x=5`
- Function names: `lowercase_with_underscores`
- Class names: `CapitalizedWords`

Python Enhancement Proposal 8 - دليل أسلوب بايثون الرسمي:
- المسافة البادئة: 4 مسافات
- طول السطر: 79 حرف كحد أقصى
- مسافات حول العوامل: `x = 5`، ليس `x=5`
- أسماء الدوال: `lowercase_with_underscores`
- أسماء الفئات: `CapitalizedWords`

### Auto-Format Your Code
### التنسيق التلقائي لكودك

#### Format on Save (Recommended)
#### التنسيق عند الحفظ (موصى به)

1. Open Settings: `Ctrl+,` (Mac: `Cmd+,`)
2. Search for "format on save"
3. Check the box for "Editor: Format On Save"
4. Now your code formats automatically when you save!

<!-- -->

1. افتح الإعدادات: `Ctrl+,` (Mac: `Cmd+,`)
2. ابحث عن "format on save"
3. ضع علامة على "Editor: Format On Save"
4. الآن كودك ينسق تلقائيًا عند الحفظ!

#### Manual Formatting
#### التنسيق اليدوي

Press `Shift+Alt+F` (Mac: `Shift+Option+F`) to format current file.

اضغط `Shift+Alt+F` (Mac: `Shift+Option+F`) لتنسيق الملف الحالي.

### Before and After Formatting
### قبل وبعد التنسيق

**Before (messy):**
```python
def calculate_area(length,width):
x=length*width
if x>100:
 print("Large area")
else:
  print("Small area")
return x
```

**After (beautiful):**
```python
def calculate_area(length, width):
    x = length * width
    if x > 100:
        print("Large area")
    else:
        print("Small area")
    return x
```

### Choosing a Formatter
### اختيار منسق

Popular Python formatters:
- **autopep8**: Follows PEP 8 strictly
- **black**: Opinionated, no configuration needed
- **yapf**: Highly configurable

منسقات بايثون الشائعة:
- **autopep8**: يتبع PEP 8 بدقة
- **black**: رأي قوي، لا يحتاج إعداد
- **yapf**: قابل للتخصيص بشكل كبير

To set formatter:
1. `Ctrl+Shift+P` → "Python: Select Formatter"
2. Choose your preferred formatter
3. VS Code will install it if needed

لتعيين المنسق:
1. `Ctrl+Shift+P` → "Python: Select Formatter"
2. اختر المنسق المفضل
3. VS Code سيثبته إذا لزم الأمر

---

## Running Python Code
## تشغيل كود بايثون

VS Code offers multiple ways to run Python code. Choose what works best for you!

VS Code يوفر طرق متعددة لتشغيل كود بايثون. اختر ما يناسبك!

### Method 1: Run Button (Easiest)
### الطريقة 1: زر التشغيل (الأسهل)

1. Open a `.py` file
2. Click the ▶️ button in top-right
3. Output appears in terminal

<!-- -->

1. افتح ملف `.py`
2. انقر على زر ▶️ في الأعلى الأيمن
3. يظهر الإخراج في الطرفية

### Method 2: Keyboard Shortcut
### الطريقة 2: اختصار لوحة المفاتيح

Press `Ctrl+F5` (Mac: `Cmd+F5`) to run without debugging.

اضغط `Ctrl+F5` (Mac: `Cmd+F5`) للتشغيل بدون تصحيح.

### Method 3: Right-Click Menu
### الطريقة 3: قائمة النقر الأيمن

1. Right-click in the editor
2. Select "Run Python File in Terminal"

<!-- -->

1. انقر بزر الماوس الأيمن في المحرر
2. اختر "Run Python File in Terminal"

### Method 4: Terminal Commands
### الطريقة 4: أوامر الطرفية

Open terminal (`` Ctrl+` ``) and type:
```bash
python your_file.py  # Windows
python3 your_file.py  # Mac/Linux
```

افتح الطرفية (`` Ctrl+` ``) واكتب:
```bash
python your_file.py  # ويندوز
python3 your_file.py  # ماك/لينكس
```

### Method 5: Interactive Mode
### الطريقة 5: الوضع التفاعلي

1. Select code you want to run
2. Press `Shift+Enter`
3. Code runs in Python interactive window

<!-- -->

1. حدد الكود الذي تريد تشغيله
2. اضغط `Shift+Enter`
3. يعمل الكود في نافذة بايثون التفاعلية

### Understanding the Output
### فهم الإخراج

When you run code, the terminal shows:
```
(venv) PS C:\python-m110> python code-examples/chapter-02-fundamentals/01_hello_world.py
Hello, World!
(venv) PS C:\python-m110>
```

عندما تشغل الكود، تظهر الطرفية:
```
(venv) PS C:\python-m110> python code-examples/chapter-02-fundamentals/01_hello_world.py
Hello, World!
(venv) PS C:\python-m110>
```

- `(venv)`: Virtual environment is active ✅
- `PS C:\python-m110>`: Current directory
- `python ...`: Command that ran
- `Hello, World!`: Your program's output

- `(venv)`: البيئة الافتراضية نشطة ✅
- `PS C:\python-m110>`: المجلد الحالي
- `python ...`: الأمر الذي تم تشغيله
- `Hello, World!`: إخراج برنامجك

---

## Reading Error Messages
## قراءة رسائل الخطأ

Don't panic when you see errors! They're trying to help you.

لا تذعر عند رؤية الأخطاء! إنها تحاول مساعدتك.

### Anatomy of an Error Message
### تشريح رسالة خطأ

```
Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print(message)
NameError: name 'message' is not defined
```

Let's decode this:
1. **Traceback**: Python is showing you where the error happened
2. **File "test.py", line 5**: Error is in test.py at line 5
3. **print(message)**: The exact line with the error
4. **NameError**: Type of error
5. **name 'message' is not defined**: What went wrong

لنفك هذا:
1. **Traceback**: بايثون يريك أين حدث الخطأ
2. **File "test.py", line 5**: الخطأ في test.py في السطر 5
3. **print(message)**: السطر الدقيق مع الخطأ
4. **NameError**: نوع الخطأ
5. **name 'message' is not defined**: ما الذي حدث خطأ

### Common Python Errors
### أخطاء بايثون الشائعة

#### SyntaxError
```python
if x = 5:  # ❌ Should be == not =
    print("Five")

# SyntaxError: invalid syntax
```

**Fix:** Check for typos, missing colons, wrong operators

**الإصلاح:** تحقق من الأخطاء الإملائية، النقطتين المفقودتين، العوامل الخاطئة

#### NameError
```python
print(mesage)  # ❌ Typo: should be 'message'

# NameError: name 'mesage' is not defined
```

**Fix:** Check spelling, make sure variable is defined

**الإصلاح:** تحقق من التهجئة، تأكد من تعريف المتغير

#### IndentationError
```python
if True:
print("Hello")  # ❌ Needs indentation

# IndentationError: expected an indented block
```

**Fix:** Add proper indentation (4 spaces)

**الإصلاح:** أضف المسافة البادئة الصحيحة (4 مسافات)

#### TypeError
```python
"5" + 5  # ❌ Can't add string and number

# TypeError: can only concatenate str (not "int") to str
```

**Fix:** Convert types: `int("5") + 5` or `"5" + str(5)`

**الإصلاح:** حول الأنواع: `int("5") + 5` أو `"5" + str(5)`

### Tips for Debugging Errors
### نصائح لتصحيح الأخطاء

1. **Read the error type first** (NameError, SyntaxError, etc.)
2. **Look at the line number** - Click to jump there
3. **Read the error message** - It usually tells you exactly what's wrong
4. **Check the line above** - Sometimes the error is there
5. **Google the error** - Someone else had this problem too!

<!-- -->

1. **اقرأ نوع الخطأ أولاً** (NameError، SyntaxError، إلخ.)
2. **انظر إلى رقم السطر** - انقر للقفز إليه
3. **اقرأ رسالة الخطأ** - عادة تخبرك بالضبط ما الخطأ
4. **تحقق من السطر أعلاه** - أحيانًا يكون الخطأ هناك
5. **ابحث في Google عن الخطأ** - شخص آخر واجه هذه المشكلة أيضًا!

---

## Debugging (Optional Advanced)
## التصحيح (متقدم اختياري)

Debugging lets you run code line by line to find bugs. It's like slow-motion for code!

التصحيح يتيح لك تشغيل الكود سطرًا بسطر لإيجاد الأخطاء. إنه مثل الحركة البطيئة للكود!

### Setting Breakpoints
### تعيين نقاط التوقف

1. Click to the left of a line number
2. A red dot appears (breakpoint)
3. Code will pause here when debugging

<!-- -->

1. انقر على يسار رقم السطر
2. تظهر نقطة حمراء (نقطة توقف)
3. سيتوقف الكود هنا عند التصحيح

### Start Debugging
### بدء التصحيح

Press `F5` (not `Ctrl+F5`) to start debugging.

اضغط `F5` (ليس `Ctrl+F5`) لبدء التصحيح.

### Debug Controls
### عناصر تحكم التصحيح

When paused at a breakpoint:
- **Continue (F5)**: Run until next breakpoint
- **Step Over (F10)**: Execute current line
- **Step Into (F11)**: Go into function calls
- **Step Out (Shift+F11)**: Exit current function
- **Stop (Shift+F5)**: Stop debugging

عند التوقف عند نقطة توقف:
- **المتابعة (F5)**: التشغيل حتى نقطة التوقف التالية
- **الخطوة فوق (F10)**: تنفيذ السطر الحالي
- **الخطوة داخل (F11)**: الدخول في استدعاءات الدوال
- **الخطوة خارج (Shift+F11)**: الخروج من الدالة الحالية
- **الإيقاف (Shift+F5)**: إيقاف التصحيح

### Watch Variables
### مراقبة المتغيرات

While debugging, you can see all variable values in the "Variables" panel. Watch them change as you step through code!

أثناء التصحيح، يمكنك رؤية جميع قيم المتغيرات في لوحة "Variables". شاهدها تتغير أثناء التنقل عبر الكود!

---

## Hands-On Practice
## ممارسة عملية

Let's practice everything we learned!

لنمارس كل ما تعلمناه!

### Exercise 1: Setup Check
### التمرين 1: فحص الإعداد

1. Create a new file: `test_setup.py`
2. Type this code:
```python
import sys
print(f"Python version: {sys.version}")
print(f"Executable: {sys.executable}")

# Check if we're using venv
if "venv" in sys.executable:
    print("✅ Using virtual environment!")
else:
    print("❌ Not using virtual environment")
```
3. Run it with the ▶️ button
4. Verify you see "✅ Using virtual environment!"

<!-- -->

1. أنشئ ملفًا جديدًا: `test_setup.py`
2. اكتب هذا الكود:
```python
import sys
print(f"Python version: {sys.version}")
print(f"Executable: {sys.executable}")

# تحقق إذا كنا نستخدم venv
if "venv" in sys.executable:
    print("✅ Using virtual environment!")
else:
    print("❌ Not using virtual environment")
```
3. شغّله بزر ▶️
4. تحقق من رؤية "✅ Using virtual environment!"

### Exercise 2: IntelliSense Practice
### التمرين 2: ممارسة IntelliSense

Type this slowly and watch IntelliSense help:
```python
import math

# Type 'math.' and see all available functions
radius = 5
area = math.  # IntelliSense shows options!

# Try typing 'pr' and see print appear
pr  # Complete to 'print'
```

اكتب هذا ببطء وشاهد IntelliSense يساعد:
```python
import math

# اكتب 'math.' وشاهد كل الدوال المتاحة
radius = 5
area = math.  # IntelliSense يظهر الخيارات!

# جرب كتابة 'pr' وشاهد print تظهر
pr  # أكمل إلى 'print'
```

### Exercise 3: Fix the Errors
### التمرين 3: أصلح الأخطاء

This code has errors. Use linting to find and fix them:
```python
# This code has 5 errors - find them all!
import time

def greet(name)  # Error 1: Missing colon
print("Hello, " + Name)  # Error 2 & 3: Indentation and variable name

x == 10  # Error 4: Should be = not ==

if x > 5
    print("Big number")  # Error 5: Missing colon above
```

هذا الكود به أخطاء. استخدم التحليل لإيجادها وإصلاحها:
```python
# هذا الكود به 5 أخطاء - اعثر عليها جميعًا!
import time

def greet(name)  # خطأ 1: نقطتان مفقودتان
print("Hello, " + Name)  # خطأ 2 و 3: المسافة البادئة واسم المتغير

x == 10  # خطأ 4: يجب أن يكون = ليس ==

if x > 5
    print("Big number")  # خطأ 5: نقطتان مفقودتان أعلاه
```

### Exercise 4: Format Ugly Code
### التمرين 4: تنسيق كود قبيح

Save this ugly code and watch it auto-format:
```python
def calculate(x,y,z):
 result=x+y*z
 if result>100:
   print("Big")
 else:
     print("Small")
 return    result
```

احفظ هذا الكود القبيح وشاهده ينسق تلقائيًا:
```python
def calculate(x,y,z):
 result=x+y*z
 if result>100:
   print("Big")
 else:
     print("Small")
 return    result
```

---

## Common Issues
## المشاكل الشائعة

### "Python extension not working"
### "إضافة بايثون لا تعمل"

**Solution:**
1. Restart VS Code
2. Make sure you have a `.py` file open
3. Check that Python is installed: Run `python --version` in terminal

**الحل:**
1. أعد تشغيل VS Code
2. تأكد من فتح ملف `.py`
3. تحقق من تثبيت بايثون: شغّل `python --version` في الطرفية

### "Wrong Python version selected"
### "إصدار بايثون خاطئ محدد"

**Solution:** Click Python version in status bar and select the one with `venv`

**الحل:** انقر على إصدار بايثون في شريط الحالة واختر الذي مع `venv`

### "IntelliSense not showing suggestions"
### "IntelliSense لا يظهر الاقتراحات"

**Solution:**
1. Check Python interpreter is selected
2. Save your file with `.py` extension
3. Press `Ctrl+Space` to manually trigger

**الحل:**
1. تحقق من تحديد مفسر بايثون
2. احفظ ملفك بامتداد `.py`
3. اضغط `Ctrl+Space` للتشغيل اليدوي

### "Linting errors won't go away"
### "أخطاء التحليل لا تختفي"

**Solution:** Save the file - linting updates on save

**الحل:** احفظ الملف - التحليل يُحدث عند الحفظ

---

## Tips & Tricks
## نصائح وحيل

### Use Docstrings
### استخدم Docstrings

Write documentation for your functions:
```python
def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle

    Returns:
        float: The area of the circle
    """
    return 3.14159 * radius ** 2
```

اكتب وثائق لدوالك:
```python
def calculate_area(radius):
    """
    حساب مساحة الدائرة.

    المعاملات:
        radius (float): نصف قطر الدائرة

    الإرجاع:
        float: مساحة الدائرة
    """
    return 3.14159 * radius ** 2
```

### Use Type Hints (Advanced)
### استخدم تلميحات الأنواع (متقدم)

Help IntelliSense understand your code better:
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

# IntelliSense now knows 'name' is a string!
```

ساعد IntelliSense على فهم كودك بشكل أفضل:
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

# IntelliSense الآن يعرف أن 'name' نص!
```

### Install Helpful Extensions
### ثبّت إضافات مفيدة

- **Python Docstring Generator**: Auto-generate docstrings
- **Python Test Explorer**: Run tests easily
- **Python Preview**: Visualize data structures

- **Python Docstring Generator**: توليد docstrings تلقائيًا
- **Python Test Explorer**: تشغيل الاختبارات بسهولة
- **Python Preview**: تصور هياكل البيانات

---

## Next Steps
## الخطوات التالية

You've mastered Python in VS Code! Now learn about the terminal:

[Terminal in VS Code](./04-terminal-in-vscode.md) - Master the command line

لقد أتقنت بايثون في VS Code! الآن تعلم عن الطرفية:

[الطرفية في VS Code](./04-terminal-in-vscode.md) - أتقن سطر الأوامر

---

## Additional Resources
## موارد إضافية

- [Python in VS Code Documentation](https://code.visualstudio.com/docs/languages/python)
- [Python Extension Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Python Debugging in VS Code](https://code.visualstudio.com/docs/python/debugging)

- [وثائق بايثون في VS Code](https://code.visualstudio.com/docs/languages/python)
- [دروس إضافة بايثون](https://code.visualstudio.com/docs/python/python-tutorial)
- [دليل أسلوب PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [تصحيح بايثون في VS Code](https://code.visualstudio.com/docs/python/debugging)

---

**Remember:** Every error is a learning opportunity. Don't be afraid to experiment and break things - that's how you learn!

**تذكر:** كل خطأ هو فرصة للتعلم. لا تخف من التجربة وكسر الأشياء - هكذا تتعلم!

🐍 **Happy Python Coding!** | **برمجة بايثون سعيدة!** 🐍