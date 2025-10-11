# Python Extension for VS Code Setup Guide
# دليل إعداد إضافة Python لـ VS Code

⏱️ **Estimated Time:** 10-15 minutes
⏱️ **الوقت المقدر:** 10-15 دقيقة

---

## What is the Python Extension?
## ما هي إضافة Python؟

The Python extension for VS Code, created by Microsoft, adds powerful features specifically for Python development. It transforms VS Code from a simple text editor into a full-featured Python IDE (Integrated Development Environment).

إضافة Python لـ VS Code، التي أنشأتها مايكروسوفت، تضيف ميزات قوية خاصة بتطوير بايثون. تحول VS Code من محرر نصوص بسيط إلى بيئة تطوير متكاملة (IDE) كاملة الميزات لبايثون.

### What Does It Provide?
### ماذا توفر؟

- 💡 **IntelliSense** - Smart code completion and suggestions
- 💡 **IntelliSense** - إكمال ذكي للكود واقتراحات

- 🐛 **Debugging** - Step through code and find bugs
- 🐛 **التصحيح** - المرور عبر الكود وإيجاد الأخطاء

- 🎨 **Syntax Highlighting** - Colorful code that's easier to read
- 🎨 **تلوين الكود** - كود ملون أسهل للقراءة

- 📏 **Linting** - Catch errors and style issues
- 📏 **فحص الكود** - اكتشاف الأخطاء ومشاكل الأسلوب

- 🔧 **Formatting** - Automatically format code to PEP 8 standards
- 🔧 **التنسيق** - تنسيق الكود تلقائياً وفقاً لمعايير PEP 8

- ▶️ **Run Code** - Execute Python files with one click
- ▶️ **تشغيل الكود** - تنفيذ ملفات بايثون بنقرة واحدة

- 🧪 **Testing** - Run and manage unit tests
- 🧪 **الاختبار** - تشغيل وإدارة اختبارات الوحدة

---

## Prerequisites
## المتطلبات الأساسية

Before installing the Python extension:
قبل تثبيت إضافة Python:

- ✅ Python installed (see [01-python-installation.md](01-python-installation.md))
- ✅ بايثون مثبت (انظر [01-python-installation.md](01-python-installation.md))

- ✅ VS Code installed (see [02-vscode-installation.md](02-vscode-installation.md))
- ✅ VS Code مثبت (انظر [02-vscode-installation.md](02-vscode-installation.md))

- ✅ Virtual environment set up (see [04-venv-setup.md](04-venv-setup.md))
- ✅ البيئة الافتراضية معدة (انظر [04-venv-setup.md](04-venv-setup.md))

---

## Part 1: Installing the Python Extension
## الجزء 1: تثبيت إضافة Python

### Step 1: Open Extensions View
### الخطوة 1: فتح عرض الإضافات

1. Open VS Code
   افتح VS Code

2. Open the Extensions view:
   افتح عرض الإضافات:

   - Click the **Extensions** icon 🧩 in the Activity Bar (left side)
   - انقر أيقونة **Extensions** 🧩 في شريط النشاط (الجانب الأيسر)

   OR / أو

   - Press **Ctrl + Shift + X** (Windows/Linux)
   - اضغط **Ctrl + Shift + X** (ويندوز/لينكس)

   - Press **⌘ + Shift + X** (Mac)
   - اضغط **⌘ + Shift + X** (ماك)

📸 **Screenshot location:** VS Code with Extensions panel open

### Step 2: Search for Python Extension
### الخطوة 2: البحث عن إضافة Python

1. In the search box at the top, type:
   في مربع البحث في الأعلى، اكتب:

   ```
   Python
   ```

2. Look for the extension with:
   ابحث عن الإضافة ذات:

   - **Name:** Python
   - **الاسم:** Python

   - **Publisher:** Microsoft
   - **الناشر:** Microsoft

   - **Icon:** Blue and yellow Python logo
   - **الأيقونة:** شعار بايثون الأزرق والأصفر

   - **Millions of downloads**
   - **الملايين من التنزيلات**

3. **Important:** Make sure it's the one by **Microsoft**, not other Python extensions!
   **مهم:** تأكد من أنها من **Microsoft**، وليس إضافات بايثون أخرى!

📸 **Screenshot location:** Python extension by Microsoft in search results

### Step 3: Install the Extension
### الخطوة 3: تثبيت الإضافة

1. Click the **Install** button
   انقر زر **Install**

2. Wait for installation (30-60 seconds)
   انتظر التثبيت (30-60 ثانية)

3. The button will change to a gear icon ⚙️ when installation is complete
   سيتغير الزر إلى أيقونة ترس ⚙️ عند اكتمال التثبيت

4. You may see a notification: "Python extension installed successfully"
   قد ترى إشعاراً: "Python extension installed successfully"

✅ **Python extension is now installed!**
✅ **تم تثبيت إضافة Python الآن!**

### Recommended: Install Pylance
### موصى به: تثبيت Pylance

Pylance is a companion extension that provides faster IntelliSense and type checking.
Pylance هو إضافة مرافقة توفر IntelliSense أسرع وفحص الأنواع.

**Note:** Pylance is usually installed automatically with the Python extension. If not:
**ملاحظة:** Pylance عادة ما يثبت تلقائياً مع إضافة Python. إن لم يحدث:

1. In Extensions view, search for:
   في عرض الإضافات، ابحث عن:

   ```
   Pylance
   ```

2. Find **Pylance** by Microsoft
   ابحث عن **Pylance** من Microsoft

3. Click **Install**
   انقر **Install**

---

## Part 2: Configuring the Python Interpreter
## الجزء 2: تكوين مفسر Python

The Python interpreter is the program that runs your Python code. We need to tell VS Code which one to use.
مفسر Python هو البرنامج الذي يشغّل كود بايثون. نحتاج إلى إخبار VS Code أيهما يستخدم.

### Step 1: Open Your Project
### الخطوة 1: فتح مشروعك

1. Open VS Code
   افتح VS Code

2. Open your course repository:
   افتح مستودع المقرر:

   - **File** → **Open Folder**
   - **File** → **Open Folder**

   - Navigate to `python-m110`
   - انتقل إلى `python-m110`

   - Click **Select Folder** (Windows) or **Open** (Mac)
   - انقر **Select Folder** (ويندوز) أو **Open** (ماك)

### Step 2: Select Python Interpreter
### الخطوة 2: اختيار مفسر Python

1. Press **Ctrl + Shift + P** (Windows/Linux) or **⌘ + Shift + P** (Mac)
   اضغط **Ctrl + Shift + P** (ويندوز/لينكس) أو **⌘ + Shift + P** (ماك)

2. Type:
   اكتب:

   ```
   Python: Select Interpreter
   ```

3. Press **Enter**
   اضغط **Enter**

4. You'll see a list of available Python interpreters. Choose the one with **venv**:
   سترى قائمة بمفسرات Python المتاحة. اختر الذي يحتوي على **venv**:

   ```
   Python 3.12.0 ('venv': venv) ./venv/bin/python
   ```

   or similar / أو مشابه

5. Click on it to select
   انقر عليه للاختيار

### Step 3: Verify Selection
### الخطوة 3: التحقق من الاختيار

Look at the **bottom-left** of the VS Code window. You should see:
انظر إلى **أسفل اليسار** في نافذة VS Code. يجب أن ترى:

```
Python 3.12.0 ('venv': venv)
```

This confirms VS Code is using your virtual environment's Python!
هذا يؤكد أن VS Code يستخدم بايثون من بيئتك الافتراضية!

📸 **Screenshot location:** VS Code status bar showing Python interpreter

💡 **Tip:** If you don't see any interpreter, make sure you've created the virtual environment (see [04-venv-setup.md](04-venv-setup.md))
💡 **نصيحة:** إذا لم ترَ أي مفسر، تأكد من أنك أنشأت البيئة الافتراضية (انظر [04-venv-setup.md](04-venv-setup.md))

---

## Part 3: Running Python Files
## الجزء 3: تشغيل ملفات Python

Now let's learn different ways to run Python code in VS Code!
الآن دعنا نتعلم طرق مختلفة لتشغيل كود بايثون في VS Code!

### Method 1: Run Button (Easiest)
### الطريقة 1: زر التشغيل (الأسهل)

1. Create or open a Python file (e.g., `test.py`)
   أنشئ أو افتح ملف بايثون (مثل `test.py`)

2. Write some Python code:
   اكتب بعض كود بايثون:

   ```python
   # Test file / ملف اختبار
   print("Hello from VS Code!")
   print("مرحباً من VS Code!")
   ```

3. Look at the **top-right** corner - you'll see a **▶️ Run** button
   انظر إلى **الزاوية العلوية اليمنى** - سترى زر **▶️ Run**

4. Click the **▶️ Run** button
   انقر زر **▶️ Run**

5. The integrated terminal will open at the bottom and run your code!
   ستفتح الطرفية المدمجة في الأسفل وتشغل كودك!

📸 **Screenshot location:** Python file with Run button highlighted

### Method 2: Right-Click Menu
### الطريقة 2: قائمة النقر بالزر الأيمن

1. Open a Python file
   افتح ملف بايثون

2. **Right-click** anywhere in the editor
   **انقر بالزر الأيمن** في أي مكان في المحرر

3. Select **"Run Python File in Terminal"**
   اختر **"Run Python File in Terminal"**

4. The code runs in the terminal below
   يعمل الكود في الطرفية أدناه

### Method 3: Keyboard Shortcut
### الطريقة 3: اختصار لوحة المفاتيح

1. Open a Python file
   افتح ملف بايثون

2. Press **Ctrl + Alt + N** (Windows/Linux) or **⌃ + ⌥ + N** (Mac)
   اضغط **Ctrl + Alt + N** (ويندوز/لينكس) أو **⌃ + ⌥ + N** (ماك)

   **Note:** This shortcut requires the "Code Runner" extension (optional)
   **ملاحظة:** هذا الاختصار يتطلب إضافة "Code Runner" (اختياري)

### Method 4: Command Palette
### الطريقة 4: لوحة الأوامر

1. Open a Python file
   افتح ملف بايثون

2. Press **Ctrl/⌘ + Shift + P**
   اضغط **Ctrl/⌘ + Shift + P**

3. Type: **"Python: Run Python File in Terminal"**
   اكتب: **"Python: Run Python File in Terminal"**

4. Press **Enter**
   اضغط **Enter**

---

## Part 4: Using the Integrated Terminal
## الجزء 4: استخدام الطرفية المدمجة

The integrated terminal is built into VS Code - no need to switch to a separate window!
الطرفية المدمجة مدمجة في VS Code - لا حاجة للتبديل إلى نافذة منفصلة!

### Opening the Terminal
### فتح الطرفية

**Option 1:** Menu
**الخيار 1:** القائمة

- **View** → **Terminal**
- **View** → **Terminal**

**Option 2:** Keyboard Shortcut
**الخيار 2:** اختصار لوحة المفاتيح

- Press **Ctrl + `** (Windows/Linux)
- اضغط **Ctrl + `** (ويندوز/لينكس)

- Press **⌘ + `** (Mac)
- اضغط **⌘ + `** (ماك)

### Running Commands in the Terminal
### تشغيل الأوامر في الطرفية

Once the terminal is open:
بمجرد فتح الطرفية:

1. You should see `(venv)` if your virtual environment is active
   يجب أن ترى `(venv)` إذا كانت بيئتك الافتراضية نشطة

2. You can run any Python command:
   يمكنك تشغيل أي أمر بايثون:

   ```bash
   python --version
   pip list
   python myfile.py
   ```

### Terminal Tips
### نصائح الطرفية

- **Multiple terminals:** Click the **+** button to open more terminals
- **طرفيات متعددة:** انقر زر **+** لفتح طرفيات أكثر

- **Switch terminals:** Use the dropdown menu
- **تبديل الطرفيات:** استخدم القائمة المنسدلة

- **Kill terminal:** Click the 🗑️ trash icon
- **إنهاء الطرفية:** انقر أيقونة 🗑️ القمامة

- **Clear terminal:** Type `clear` (Mac/Linux) or `cls` (Windows)
- **مسح الطرفية:** اكتب `clear` (ماك/لينكس) أو `cls` (ويندوز)

📸 **Screenshot location:** VS Code with terminal panel showing multiple terminals

---

## Part 5: IntelliSense and Code Completion
## الجزء 5: IntelliSense وإكمال الكود

IntelliSense provides smart code suggestions as you type!
IntelliSense يوفر اقتراحات كود ذكية أثناء الكتابة!

### How to Use IntelliSense
### كيفية استخدام IntelliSense

1. Create a new Python file
   أنشئ ملف بايثون جديد

2. Start typing:
   ابدأ الكتابة:

   ```python
   import mat
   ```

3. As you type, you'll see a suggestion menu appear
   أثناء الكتابة، سترى قائمة اقتراحات تظهر

4. Use **arrow keys** to navigate
   استخدم **مفاتيح الأسهم** للتنقل

5. Press **Tab** or **Enter** to accept a suggestion
   اضغط **Tab** أو **Enter** لقبول اقتراح

### Triggering IntelliSense Manually
### تحفيز IntelliSense يدوياً

If the suggestion menu doesn't appear:
إذا لم تظهر قائمة الاقتراحات:

- Press **Ctrl + Space** (Windows/Linux)
- اضغط **Ctrl + Space** (ويندوز/لينكس)

- Press **⌃ + Space** (Mac)
- اضغط **⌃ + Space** (ماك)

### Example: Exploring Methods
### مثال: استكشاف الطرق

```python
# Create a list / إنشاء قائمة
my_list = [1, 2, 3, 4, 5]

# Type the variable name followed by a dot / اكتب اسم المتغير متبوعاً بنقطة
my_list.
```

When you type the dot (`.`), IntelliSense will show all available methods:
عندما تكتب النقطة (`.`)، سيعرض IntelliSense جميع الطرق المتاحة:

- `append()`
- `remove()`
- `sort()`
- etc.

### Hover Information
### معلومات التمرير

Hover your mouse over any function or variable to see:
مرر الماوس فوق أي دالة أو متغير لرؤية:

- Type information
- معلومات النوع

- Documentation
- التوثيق

- Parameter details
- تفاصيل المعاملات

📸 **Screenshot location:** IntelliSense popup showing method suggestions

---

## Part 6: Linting and Code Quality
## الجزء 6: فحص الكود وجودة الكود

Linting helps catch errors and enforce coding standards (PEP 8 for Python).
فحص الكود يساعد في اكتشاف الأخطاء وفرض معايير البرمجة (PEP 8 لبايثون).

### What is Linting?
### ما هو فحص الكود؟

A linter analyzes your code and highlights:
فاحص الكود يحلل كودك ويسلط الضوء على:

- ❌ Syntax errors
- ❌ أخطاء البنية

- ⚠️ Potential bugs
- ⚠️ أخطاء محتملة

- 💡 Style violations (PEP 8)
- 💡 انتهاكات الأسلوب (PEP 8)

- 📝 Unused variables
- 📝 متغيرات غير مستخدمة

### Installing a Linter
### تثبيت فاحص كود

The most popular Python linter is **Pylint**. Let's install it:
أكثر فاحص كود بايثون شعبية هو **Pylint**. دعنا نثبته:

1. Make sure your virtual environment is active (look for `(venv)`)
   تأكد من أن بيئتك الافتراضية نشطة (ابحث عن `(venv)`)

2. Open the terminal in VS Code
   افتح الطرفية في VS Code

3. Install Pylint:
   ثبت Pylint:

   ```bash
   pip install pylint
   ```

4. Wait for installation to complete
   انتظر اكتمال التثبيت

### Enabling Linting
### تمكين فحص الكود

1. Press **Ctrl/⌘ + Shift + P**
   اضغط **Ctrl/⌘ + Shift + P**

2. Type: **"Python: Select Linter"**
   اكتب: **"Python: Select Linter"**

3. Choose **pylint** from the list
   اختر **pylint** من القائمة

4. Open Settings: **File** → **Preferences** → **Settings** (or Ctrl/⌘ + ,)
   افتح الإعدادات: **File** → **Preferences** → **Settings** (أو Ctrl/⌘ + ,)

5. Search for: **"python.linting.enabled"**
   ابحث عن: **"python.linting.enabled"**

6. Make sure it's checked ✅
   تأكد من أنه محدد ✅

### Seeing Lint Errors
### رؤية أخطاء فحص الكود

Now when you write code with issues, you'll see:
الآن عندما تكتب كوداً به مشاكل، سترى:

- **Red squiggly lines** - Errors
- **خطوط متموجة حمراء** - أخطاء

- **Yellow squiggly lines** - Warnings
- **خطوط متموجة صفراء** - تحذيرات

- **Green squiggly lines** - Style suggestions
- **خطوط متموجة خضراء** - اقتراحات الأسلوب

Hover over the squiggly line to see the problem!
مرر الماوس فوق الخط المتموج لرؤية المشكلة!

### Example: Finding Issues
### مثال: إيجاد المشاكل

```python
# Bad code / كود سيء
x=5    # No spaces around = (PEP 8 violation)
y = 10
# Unused variable
```

Pylint will highlight:
Pylint سيسلط الضوء على:

- Missing spaces around `=`
- عدم وجود مسافات حول `=`

- Unused variable `y`
- متغير غير مستخدم `y`

📸 **Screenshot location:** Code with lint warnings highlighted

---

## Part 7: Code Formatting (PEP 8)
## الجزء 7: تنسيق الكود (PEP 8)

PEP 8 is Python's official style guide. The Python extension can automatically format your code!
PEP 8 هو دليل الأسلوب الرسمي لبايثون. إضافة Python يمكنها تنسيق كودك تلقائياً!

### Installing a Formatter
### تثبيت منسق

We'll use **Black**, the most popular Python formatter:
سنستخدم **Black**، أشهر منسق بايثون:

1. Make sure venv is active
   تأكد من أن venv نشط

2. Install Black:
   ثبت Black:

   ```bash
   pip install black
   ```

### Setting Black as Default Formatter
### تعيين Black كمنسق افتراضي

1. Press **Ctrl/⌘ + Shift + P**
   اضغط **Ctrl/⌘ + Shift + P**

2. Type: **"Preferences: Open Settings (JSON)"**
   اكتب: **"Preferences: Open Settings (JSON)"**

3. Add these lines inside the curly braces:
   أضف هذه الأسطر داخل الأقواس المعقوفة:

   ```json
   {
     "[python]": {
       "editor.defaultFormatter": "ms-python.black-formatter",
       "editor.formatOnSave": true
     }
   }
   ```

4. Save the file (Ctrl/⌘ + S)
   احفظ الملف (Ctrl/⌘ + S)

### Using the Formatter
### استخدام المنسق

**Automatic:** Now your code will format automatically when you save!
**تلقائي:** الآن سينسق كودك تلقائياً عند الحفظ!

**Manual:** Format code on demand:
**يدوي:** نسق الكود عند الطلب:

1. Right-click in the editor
   انقر بالزر الأيمن في المحرر

2. Select **"Format Document"**
   اختر **"Format Document"**

OR / أو

- Press **Shift + Alt + F** (Windows/Linux)
- اضغط **Shift + Alt + F** (ويندوز/لينكس)

- Press **⇧ + ⌥ + F** (Mac)
- اضغط **⇧ + ⌥ + F** (ماك)

### Example: Before and After
### مثال: قبل وبعد

**Before formatting / قبل التنسيق:**

```python
def calculate_total(a,b,c):
    result=a+b+c
    return result
```

**After formatting / بعد التنسيق:**

```python
def calculate_total(a, b, c):
    result = a + b + c
    return result
```

Black adds proper spacing automatically!
Black يضيف المسافات الصحيحة تلقائياً!

---

## Troubleshooting
## استكشاف الأخطاء وإصلاحها

### ❌ Python extension not working
### ❌ إضافة Python لا تعمل

**Solution:**
**الحل:**

1. Reload VS Code: **Ctrl/⌘ + Shift + P** → **"Developer: Reload Window"**
   أعد تحميل VS Code: **Ctrl/⌘ + Shift + P** → **"Developer: Reload Window"**

2. Restart VS Code completely
   أعد تشغيل VS Code بالكامل

### ❌ No interpreter found
### ❌ لم يتم العثور على مفسر

**Problem:** VS Code can't find Python
**المشكلة:** VS Code لا يمكنه إيجاد Python

**Solution:**
**الحل:**

1. Make sure Python is installed (run `python --version` in terminal)
   تأكد من تثبيت Python (نفّذ `python --version` في الطرفية)

2. Restart VS Code after installing Python
   أعد تشغيل VS Code بعد تثبيت Python

3. Manually select interpreter: **Ctrl/⌘ + Shift + P** → **"Python: Select Interpreter"**
   اختر المفسر يدوياً: **Ctrl/⌘ + Shift + P** → **"Python: Select Interpreter"**

### ❌ IntelliSense not working
### ❌ IntelliSense لا يعمل

**Solution:**
**الحل:**

1. Check Pylance is installed (Extensions → search "Pylance")
   تحقق من تثبيت Pylance (Extensions → ابحث عن "Pylance")

2. Select the correct interpreter (must include venv)
   اختر المفسر الصحيح (يجب أن يتضمن venv)

3. Wait 10-20 seconds after opening a file for IntelliSense to initialize
   انتظر 10-20 ثانية بعد فتح ملف لتهيئة IntelliSense

### ❌ Linter not showing errors
### ❌ فاحص الكود لا يعرض الأخطاء

**Solution:**
**الحل:**

1. Make sure pylint is installed: `pip list | grep pylint`
   تأكد من تثبيت pylint: `pip list | grep pylint`

2. Enable linting in settings
   مكّن فحص الكود في الإعدادات

3. Check the "Problems" tab (bottom panel) for lint messages
   تحقق من علامة تبويب "Problems" (اللوحة السفلية) لرسائل فحص الكود

### ❌ Code not formatting
### ❌ الكود لا ينسق

**Solution:**
**الحل:**

1. Install Black: `pip install black`
   ثبت Black: `pip install black`

2. Check settings.json has the formatting configuration
   تحقق من أن settings.json يحتوي على إعدادات التنسيق

3. Try manual format: **Shift + Alt/⌥ + F**
   جرب التنسيق اليدوي: **Shift + Alt/⌥ + F**

### ❌ "python not found" when running code
### ❌ "python not found" عند تشغيل الكود

**Solution:**
**الحل:**

1. Select the correct interpreter (with venv)
   اختر المفسر الصحيح (مع venv)

2. Activate the virtual environment in terminal
   فعّل البيئة الافتراضية في الطرفية

3. Restart the terminal
   أعد تشغيل الطرفية

---

## Quick Reference
## مرجع سريع

### Essential Shortcuts
### الاختصارات الأساسية

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Run Python file<br>تشغيل ملف Python | Ctrl + Alt + N | ⌃ + ⌥ + N |
| Open terminal<br>فتح الطرفية | Ctrl + ` | ⌘ + ` |
| Command palette<br>لوحة الأوامر | Ctrl + Shift + P | ⌘ + Shift + P |
| IntelliSense<br>IntelliSense | Ctrl + Space | ⌃ + Space |
| Format document<br>تنسيق المستند | Shift + Alt + F | ⇧ + ⌥ + F |
| Go to definition<br>الذهاب إلى التعريف | F12 | F12 |
| Find all references<br>البحث عن جميع المراجع | Shift + F12 | ⇧ + F12 |

### Common Commands
### الأوامر الشائعة

```bash
# Install linter / تثبيت فاحص الكود
pip install pylint

# Install formatter / تثبيت المنسق
pip install black

# Run Python file / تشغيل ملف Python
python filename.py

# Check Python version / التحقق من إصدار Python
python --version
```

---

## Next Steps
## الخطوات التالية

Excellent! Your Python development environment is fully set up! Now:
ممتاز! بيئة تطوير Python الخاصة بك معدة بالكامل! الآن:

1. **Clone the Course Repository** - [06-github-repo-cloning.md](06-github-repo-cloning.md)
   **نسخ مستودع المقرر** - [06-github-repo-cloning.md](06-github-repo-cloning.md)

2. **Run Your First Program** - [07-running-first-program.md](07-running-first-program.md)
   **تشغيل برنامجك الأول** - [07-running-first-program.md](07-running-first-program.md)

3. **Optional: Set up Claude Code** - [08-claude-code-extension-setup.md](08-claude-code-extension-setup.md)
   **اختياري: إعداد Claude Code** - [08-claude-code-extension-setup.md](08-claude-code-extension-setup.md)

---

## Additional Resources
## موارد إضافية

- 📖 [VS Code Python Documentation](https://code.visualstudio.com/docs/python/python-tutorial)
- 📖 [وثائق VS Code Python](https://code.visualstudio.com/docs/python/python-tutorial)

- 📖 [PEP 8 Style Guide](https://pep8.org/)
- 📖 [دليل أسلوب PEP 8](https://pep8.org/)

- 🎥 [Python in VS Code Tutorial](https://www.youtube.com/watch?v=7EXd4_ttIuw)
- 🎥 [درس Python في VS Code](https://www.youtube.com/watch?v=7EXd4_ttIuw)

---

*Last Updated: October 2025*
*آخر تحديث: أكتوبر 2025*
