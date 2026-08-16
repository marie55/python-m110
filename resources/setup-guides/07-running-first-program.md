# Running Your First Python Program
# تشغيل أول برنامج بايثون لك

⏱️ **Estimated Time:** 10-15 minutes
⏱️ **الوقت المقدر:** 10-15 دقيقة

---

## Overview
## نظرة عامة

Congratulations! You've set up Python, VS Code, Git, and cloned the course repository. Now it's time for the exciting part - running your very first Python program!

تهانينا! لقد أعددت Python و VS Code و Git ونسخت مستودع المقرر. الآن حان الوقت للجزء المثير - تشغيل أول برنامج بايثون لك!

This guide will walk you through:
سيرشدك هذا الدليل خلال:

- Finding and opening example code
- إيجاد وفتح كود المثال

- Running Python files from VS Code
- تشغيل ملفات بايثون من VS Code

- Running Python files from the terminal
- تشغيل ملفات بايثون من الطرفية

- Understanding program output
- فهم مخرجات البرنامج

- Troubleshooting common errors
- استكشاف الأخطاء الشائعة

---

## Prerequisites
## المتطلبات الأساسية

Before running your first program:
قبل تشغيل برنامجك الأول:

- ✅ Course repository cloned (see [06-github-repo-cloning.md](06-github-repo-cloning.md))
- ✅ مستودع المقرر منسوخ (انظر [06-github-repo-cloning.md](06-github-repo-cloning.md))

- ✅ Virtual environment set up (see [04-venv-setup.md](04-venv-setup.md))
- ✅ البيئة الافتراضية معدة (انظر [04-venv-setup.md](04-venv-setup.md))

- ✅ Python extension installed (see [05-python-extension-vscode.md](05-python-extension-vscode.md))
- ✅ إضافة Python مثبتة (انظر [05-python-extension-vscode.md](05-python-extension-vscode.md))

---

## Part 1: Opening the Repository in VS Code
## الجزء 1: فتح المستودع في VS Code

### Step 1: Open VS Code
### الخطوة 1: فتح VS Code

1. Launch Visual Studio Code
   شغّل Visual Studio Code

2. Open the repository:
   افتح المستودع:

   **Option 1 - Using Menu:**
   **الخيار 1 - استخدام القائمة:**

   - **File** → **Open Folder**
   - **File** → **Open Folder**

   - Navigate to `python-m110` folder
   - انتقل إلى مجلد `python-m110`

   - Click **Select Folder** (Windows) or **Open** (Mac)
   - انقر **Select Folder** (ويندوز) أو **Open** (ماك)

   **Option 2 - Using Recent:**
   **الخيار 2 - استخدام الأخيرة:**

   - **File** → **Open Recent**
   - **File** → **Open Recent**

   - Select `python-m110` from the list
   - اختر `python-m110` من القائمة

### Step 2: Verify Virtual Environment
### الخطوة 2: التحقق من البيئة الافتراضية

1. Look at the **bottom-left** corner of VS Code
   انظر إلى **الزاوية السفلية اليسرى** من VS Code

2. You should see:
   يجب أن ترى:

   ```
   Python 3.12.0 ('venv': venv)
   ```

3. If you don't see this, select the venv interpreter:
   إذا لم ترَ هذا، اختر مفسر venv:

   - Press **Ctrl/⌘ + Shift + P**
   - اضغط **Ctrl/⌘ + Shift + P**

   - Type: **"Python: Select Interpreter"**
   - اكتب: **"Python: Select Interpreter"**

   - Choose the one with `venv`
   - اختر الذي يحتوي على `venv`

📸 **Screenshot location:** VS Code status bar showing Python interpreter

---

## Part 2: Navigating to Chapter 2 Examples
## الجزء 2: الانتقال إلى أمثلة الفصل الثاني

### Step 1: Open the Explorer
### الخطوة 1: فتح المستكشف

1. Click the **Explorer** icon (📁) in the Activity Bar (left side)
   انقر أيقونة **Explorer** (📁) في شريط النشاط (الجانب الأيسر)

   Or press **Ctrl/⌘ + Shift + E**
   أو اضغط **Ctrl/⌘ + Shift + E**

2. You'll see the folder structure
   سترى بنية المجلدات

### Step 2: Navigate to Chapter 2
### الخطوة 2: الانتقال إلى الفصل الثاني

1. Expand the `code-examples` folder (click the arrow ▶)
   وسّع مجلد `code-examples` (انقر السهم ▶)

2. Expand `chapter-02-fundamentals`
   وسّع `chapter-02-fundamentals`

3. You'll see Python files (.py) inside
   سترى ملفات بايثون (.py) بالداخل

### Step 3: Open Your First Python File
### الخطوة 3: فتح أول ملف بايثون لك

1. Click on `01_hello_world.py`
   انقر على `01_hello_world.py`

2. The file will open in the editor area
   سيفتح الملف في منطقة المحرر

3. You should see colorful syntax highlighting!
   يجب أن ترى تلوين كود ملون!

📸 **Screenshot location:** VS Code Explorer with chapter-02-fundamentals folder expanded

---

## Part 3: Understanding the Code
## الجزء 3: فهم الكود

Let's look at the `01_hello_world.py` file:
دعنا ننظر إلى ملف `01_hello_world.py`:

```python
"""
M110 - Python Programming
Chapter 2: Fundamentals of Python Programming
Topic: Your First Program
الفصل 2: أساسيات برمجة بايثون
الموضوع: برنامجك الأول

This is the traditional first program every programmer writes.
هذا هو البرنامج الأول التقليدي الذي يكتبه كل مبرمج.

It demonstrates the print() function, which displays text on the screen.
يوضح دالة print() التي تعرض النص على الشاشة.
"""

# Display a greeting / عرض تحية
print("Hello, World!")
print("مرحباً بالعالم!")

# Display a message about the course / عرض رسالة عن المقرر
print("Welcome to M110 - Python Programming")
print("أهلاً بك في M110 - برمجة بايثون")
```

### Code Breakdown
### تفصيل الكود

**Triple quotes ("""):** Documentation string (docstring)
**علامات اقتباس ثلاثية ("""):** سطر توثيق (docstring)

- Explains what the program does
- يشرح ما يفعله البرنامج

**Hash symbol (#):** Comments
**رمز الهاش (#):** تعليقات

- Notes for humans, ignored by Python
- ملاحظات للبشر، تتجاهلها بايثون

**print():** Built-in function
**print():** دالة مدمجة

- Displays text to the console
- تعرض النص إلى وحدة التحكم

- Text inside quotes is called a "string"
- النص داخل علامات الاقتباس يُسمى "string"

---

## Part 4: Running the Program from VS Code
## الجزء 4: تشغيل البرنامج من VS Code

Now let's run this program! There are several ways.
الآن دعنا نشغّل هذا البرنامج! هناك عدة طرق.

### Method 1: Run Button (Easiest)
### الطريقة 1: زر التشغيل (الأسهل)

1. Make sure `01_hello_world.py` is open in the editor
   تأكد من أن `01_hello_world.py` مفتوح في المحرر

2. Look at the **top-right corner** of the editor
   انظر إلى **الزاوية العلوية اليمنى** من المحرر

3. Click the **▶️ Run Python File** button
   انقر زر **▶️ Run Python File**

4. The integrated terminal will open at the bottom
   ستفتح الطرفية المدمجة في الأسفل

5. You'll see the output:
   سترى المخرجات:

   ```
   Hello, World!
   مرحباً بالعالم!
   Welcome to M110 - Python Programming
   أهلاً بك في M110 - برمجة بايثون
   ```

🎉 **Congratulations! You just ran your first Python program!**
🎉 **تهانينا! لقد شغّلت أول برنامج بايثون لك للتو!**

📸 **Screenshot location:** VS Code with Run button highlighted and terminal showing output

### Method 2: Right-Click Menu
### الطريقة 2: قائمة النقر بالزر الأيمن

1. **Right-click** anywhere in the Python file
   **انقر بالزر الأيمن** في أي مكان في ملف بايثون

2. Select **"Run Python File in Terminal"**
   اختر **"Run Python File in Terminal"**

3. The program runs and shows output in the terminal
   يعمل البرنامج ويعرض المخرجات في الطرفية

### Method 3: Command Palette
### الطريقة 3: لوحة الأوامر

1. Press **Ctrl + Shift + P** (Windows/Linux) or **⌘ + Shift + P** (Mac)
   اضغط **Ctrl + Shift + P** (ويندوز/لينكس) أو **⌘ + Shift + P** (ماك)

2. Type: **"Python: Run Python File in Terminal"**
   اكتب: **"Python: Run Python File in Terminal"**

3. Press **Enter**
   اضغط **Enter**

4. The program runs in the terminal
   يعمل البرنامج في الطرفية

### Method 4: Keyboard Shortcut (Optional)
### الطريقة 4: اختصار لوحة المفاتيح (اختياري)

If you have the Code Runner extension installed:
إذا كانت إضافة Code Runner مثبتة:

- Press **Ctrl + Alt + N** (Windows/Linux)
- اضغط **Ctrl + Alt + N** (ويندوز/لينكس)

- Press **⌃ + ⌥ + N** (Mac)
- اضغط **⌃ + ⌥ + N** (ماك)

---

## Part 5: Running from the Terminal
## الجزء 5: التشغيل من الطرفية

Understanding how to run Python from the terminal is important for professional development!
فهم كيفية تشغيل Python من الطرفية مهم للتطوير الاحترافي!

### Step 1: Open the Terminal
### الخطوة 1: فتح الطرفية

1. In VS Code, open the integrated terminal:
   في VS Code، افتح الطرفية المدمجة:

   - **View** → **Terminal**
   - **View** → **Terminal**

   OR / أو

   - Press **Ctrl/⌘ + `** (backtick key)
   - اضغط **Ctrl/⌘ + `** (مفتاح backtick)

2. The terminal opens at the bottom
   تفتح الطرفية في الأسفل

### Step 2: Check Your Location
### الخطوة 2: التحقق من موقعك

1. In the terminal, type:
   في الطرفية، اكتب:

   **Windows:**
   ```bash
   cd
   ```

   **Mac/Linux:**
   ```bash
   pwd
   ```

2. You should see a path ending with `python-m110`
   يجب أن ترى مساراً ينتهي بـ `python-m110`

3. If not in the repository root, navigate there:
   إذا لم تكن في جذر المستودع، انتقل إليه:

   **Windows:**
   ```bash
   cd C:\Users\YourName\Dev\python-m110
   ```

   **Mac/Linux:**
   ```bash
   cd ~/Dev/python-m110
   ```

### Step 3: Navigate to the Code Examples Folder
### الخطوة 3: الانتقال إلى مجلد أمثلة الكود

1. Type:
   اكتب:

   ```bash
   cd code-examples/chapter-02-fundamentals
   ```

2. Press **Enter**
   اضغط **Enter**

3. Verify you're in the right place:
   تحقق من أنك في المكان الصحيح:

   **Windows:**
   ```bash
   dir
   ```

   **Mac/Linux:**
   ```bash
   ls
   ```

4. You should see a list of `.py` files
   يجب أن ترى قائمة ملفات `.py`

### Step 4: Run the Python File
### الخطوة 4: تشغيل ملف بايثون

1. Type the run command:
   اكتب أمر التشغيل:

   **Windows:**
   ```bash
   python 01_hello_world.py
   ```

   **Mac/Linux:**
   ```bash
   python3 01_hello_world.py
   ```

2. Press **Enter**
   اضغط **Enter**

3. You'll see the output immediately:
   سترى المخرجات فوراً:

   ```
   Hello, World!
   مرحباً بالعالم!
   Welcome to M110 - Python Programming
   أهلاً بك في M110 - برمجة بايثون
   ```

📸 **Screenshot location:** Terminal showing the python command and output

---

## Part 6: Understanding the Output
## الجزء 6: فهم المخرجات

Let's analyze what happened when you ran the program:
دعنا نحلل ما حدث عندما شغّلت البرنامج:

### Terminal Output Explained
### شرح مخرجات الطرفية

You might see something like this in the terminal:
قد ترى شيئاً مثل هذا في الطرفية:

```
(venv) PS C:\Users\YourName\python-m110\code-examples\chapter-02-fundamentals> python 01_hello_world.py
Hello, World!
مرحباً بالعالم!
Welcome to M110 - Python Programming
أهلاً بك في M110 - برمجة بايثون
(venv) PS C:\Users\YourName\python-m110\code-examples\chapter-02-fundamentals>
```

**Breakdown:**
**التفصيل:**

1. **(venv)** - Virtual environment is active
   **(venv)** - البيئة الافتراضية نشطة

2. **PS C:\...\chapter-02-fundamentals>** - Current directory (prompt)
   **PS C:\...\chapter-02-fundamentals>** - المجلد الحالي (موجه الأوامر)

3. **python 01_hello_world.py** - The command you typed
   **python 01_hello_world.py** - الأمر الذي كتبته

4. **Hello, World!** etc. - Program output
   **Hello, World!** إلخ - مخرجات البرنامج

5. **(venv) PS C:\...\>** - Prompt returns, ready for next command
   **(venv) PS C:\...\>** - موجه الأوامر يعود، جاهز للأمر التالي

### What Happened Behind the Scenes?
### ما الذي حدث خلف الكواليس؟

1. Python interpreter loaded the file
   مفسر Python حمّل الملف

2. Read the code line by line
   قرأ الكود سطراً بسطر

3. Executed each `print()` statement
   نفّذ كل جملة `print()`

4. Displayed text to the terminal
   عرض النص إلى الطرفية

5. Finished and returned control to the terminal
   انتهى وأعاد التحكم إلى الطرفية

---

## Part 7: Experimenting with the Code
## الجزء 7: التجربة مع الكود

Now let's modify the program to make it your own!
الآن دعنا نعدل البرنامج لجعله خاصاً بك!

### Exercise 1: Change the Message
### التمرين 1: تغيير الرسالة

1. In the editor, find this line:
   في المحرر، ابحث عن هذا السطر:

   ```python
   print("Welcome to M110 - Python Programming")
   ```

2. Change it to print your name:
   غيّره ليطبع اسمك:

   ```python
   print("Welcome, Ahmed!")  # Replace Ahmed with your name
   ```

3. Save the file: **Ctrl/⌘ + S**
   احفظ الملف: **Ctrl/⌘ + S**

4. Run the program again (▶️ button or `python 01_hello_world.py`)
   شغّل البرنامج مرة أخرى (زر ▶️ أو `python 01_hello_world.py`)

5. See your personalized message!
   شاهد رسالتك الشخصية!

### Exercise 2: Add More Print Statements
### التمرين 2: إضافة جمل print أكثر

1. Add new lines at the end of the file:
   أضف أسطراً جديدة في نهاية الملف:

   ```python
   print("I am learning Python!")
   print("أنا أتعلم بايثون!")
   print("This is exciting!")
   ```

2. Save and run again
   احفظ وشغّل مرة أخرى

3. See all your messages appear!
   شاهد جميع رسائلك تظهر!

### Exercise 3: Print Numbers and Math
### التمرين 3: طباعة الأرقام والرياضيات

1. Try these examples:
   جرب هذه الأمثلة:

   ```python
   # Numbers / الأرقام
   print(42)
   print(3.14)

   # Math operations / العمليات الحسابية
   print(5 + 3)
   print(10 - 2)
   print(4 * 2)
   print(16 / 2)
   ```

2. Run and see the results!
   شغّل وشاهد النتائج!

📸 **Screenshot location:** Modified code with personalized messages

---

## Part 8: Exploring Other Examples
## الجزء 8: استكشاف أمثلة أخرى

Ready for more? The `code-examples/chapter-01-algorithms` folder has more examples to try - covering the algorithm building blocks (sequence, decision, and repetition) from Chapter 1.
مستعد للمزيد؟ يحتوي مجلد `code-examples/chapter-01-algorithms` على أمثلة أكثر لتجربتها - تغطي لبنات الخوارزميات الأساسية (التسلسل والقرار والتكرار) من الفصل الأول.

### Available Examples
### الأمثلة المتاحة

1. **01_sequence_average.py** - Calculate an average (sequence structure)
   **01_sequence_average.py** - احسب متوسطاً (بنية التسلسل)

2. **02_decision_even_odd.py** - Check even or odd numbers (decision structure)
   **02_decision_even_odd.py** - افحص الأرقام الزوجية والفردية (بنية القرار)

3. **05_grade_calculator_complete.py** - A complete grade calculator (all three structures)
   **05_grade_calculator_complete.py** - حاسبة درجات كاملة (التراكيب الثلاثة كلها)

### Try Each One!
### جرب كل واحد!

1. Open any `.py` file from the folder
   افتح أي ملف `.py` من المجلد

2. Read the code and comments
   اقرأ الكود والتعليقات

3. Run it using the ▶️ button
   شغّله باستخدام زر ▶️

4. Experiment by modifying the code
   جرب بتعديل الكود

5. Learn by doing!
   تعلّم بالممارسة!

---

## Troubleshooting Common Errors
## استكشاف الأخطاء الشائعة

### ❌ "python is not recognized" (Windows)
### ❌ "python is not recognized" (ويندوز)

**Problem:** Python not in PATH or venv not activated
**المشكلة:** Python ليس في PATH أو venv غير مفعّل

**Solution:**
**الحل:**

1. Activate the virtual environment:
   فعّل البيئة الافتراضية:

   ```bash
   venv\Scripts\activate
   ```

2. You should see `(venv)` appear
   يجب أن ترى `(venv)` يظهر

3. Try running again
   حاول التشغيل مرة أخرى

### ❌ "No such file or directory"
### ❌ "No such file or directory"

**Problem:** Wrong directory or file name
**المشكلة:** مجلد خاطئ أو اسم ملف

**Solution:**
**الحل:**

1. Check your current directory:
   تحقق من مجلدك الحالي:

   ```bash
   pwd  # Mac/Linux
   cd   # Windows
   ```

2. Make sure you're in `code-examples/chapter-02-fundamentals/`
   تأكد من أنك في `code-examples/chapter-02-fundamentals/`

3. Check the exact file name (case-sensitive on Mac/Linux!)
   تحقق من اسم الملف الدقيق (حساس لحالة الأحرف على ماك/لينكس!)

4. Use tab completion: type `python 01_` then press Tab
   استخدم الإكمال التلقائي: اكتب `python 01_` ثم اضغط Tab

### ❌ SyntaxError: invalid syntax
### ❌ SyntaxError: invalid syntax

**Problem:** Typo in the code
**المشكلة:** خطأ إملائي في الكود

**Common causes:**
**الأسباب الشائعة:**

- Missing quotes: `print(Hello)` should be `print("Hello")`
- علامات اقتباس مفقودة: `print(Hello)` يجب أن يكون `print("Hello")`

- Mismatched quotes: `print("Hello')` should be `print("Hello")`
- علامات اقتباس غير متطابقة: `print("Hello')` يجب أن يكون `print("Hello")`

- Missing parentheses: `print "Hello"` should be `print("Hello")`
- أقواس مفقودة: `print "Hello"` يجب أن يكون `print("Hello")`

**Solution:**
**الحل:**

1. Read the error message carefully
   اقرأ رسالة الخطأ بعناية

2. Check the line number mentioned
   تحقق من رقم السطر المذكور

3. Look for typos
   ابحث عن أخطاء إملائية

4. VS Code will underline errors in red
   VS Code سيضع خطاً أحمر تحت الأخطاء

### ❌ IndentationError
### ❌ IndentationError

**Problem:** Incorrect spacing at the beginning of lines
**المشكلة:** مسافات غير صحيحة في بداية الأسطر

**Solution:**
**الحل:**

1. Make sure all your code starts at the left margin
   تأكد من أن كل كودك يبدأ عند الهامش الأيسر

2. Don't add extra spaces or tabs before code
   لا تضف مسافات أو تبويبات إضافية قبل الكود

3. Example of correct indentation:
   مثال على المسافة البادئة الصحيحة:

   ```python
   # Correct / صحيح
   print("Hello")
   print("World")

   # Wrong - unexpected indent / خطأ - مسافة بادئة غير متوقعة
       print("Hello")
   ```

### ❌ ModuleNotFoundError
### ❌ ModuleNotFoundError

**Problem:** Missing package or wrong Python interpreter
**المشكلة:** حزمة مفقودة أو مفسر بايثون خاطئ

**Solution:**
**الحل:**

1. Make sure venv is activated (look for `(venv)`)
   تأكد من تفعيل venv (ابحث عن `(venv)`)

2. Install required packages:
   ثبت الحزم المطلوبة:

   ```bash
   pip install -r requirements.txt
   ```

3. Select the correct Python interpreter in VS Code
   اختر مفسر Python الصحيح في VS Code

### ❌ Program Runs But No Output
### ❌ البرنامج يعمل لكن لا مخرجات

**Problem:** Output might be somewhere else
**المشكلة:** المخرجات قد تكون في مكان آخر

**Solution:**
**الحل:**

1. Check if the terminal panel is visible at the bottom
   تحقق من ظهور لوحة الطرفية في الأسفل

2. Look for the "TERMINAL" tab (not "PROBLEMS" or "OUTPUT")
   ابحث عن تبويب "TERMINAL" (وليس "PROBLEMS" أو "OUTPUT")

3. Scroll up in the terminal to see output
   مرر لأعلى في الطرفية لرؤية المخرجات

---

## Understanding VS Code Panels
## فهم لوحات VS Code

When you run Python code, VS Code has several panels that show different information:
عندما تشغّل كود بايثون، VS Code لديه عدة لوحات تعرض معلومات مختلفة:

### Terminal Panel
### لوحة الطرفية

- Shows program output
- تعرض مخرجات البرنامج

- Where you type commands
- حيث تكتب الأوامر

- Interactive - can run multiple programs
- تفاعلية - يمكن تشغيل برامج متعددة

### Output Panel
### لوحة المخرجات

- Shows extension and language server messages
- تعرض رسائل الإضافة وخادم اللغة

- Not for program output (usually)
- ليست لمخرجات البرنامج (عادة)

### Problems Panel
### لوحة المشاكل

- Shows syntax errors
- تعرض أخطاء البنية

- Linting warnings
- تحذيرات فحص الكود

- Check here if code won't run
- تحقق هنا إذا لم يعمل الكود

📸 **Screenshot location:** VS Code bottom panel with TERMINAL, PROBLEMS, OUTPUT tabs labeled

---

## Quick Reference
## مرجع سريع

### Running Python Files
### تشغيل ملفات Python

**From VS Code:**
**من VS Code:**

- Click ▶️ Run button (top-right)
- انقر زر ▶️ Run (أعلى اليمين)

- Right-click → "Run Python File in Terminal"
- النقر بالزر الأيمن → "Run Python File in Terminal"

- Ctrl/⌘ + Shift + P → "Python: Run Python File in Terminal"
- Ctrl/⌘ + Shift + P → "Python: Run Python File in Terminal"

**From Terminal:**
**من الطرفية:**

```bash
# Windows
python filename.py

# Mac/Linux
python3 filename.py
```

### Useful Terminal Commands
### أوامر طرفية مفيدة

```bash
# Check current directory / التحقق من المجلد الحالي
pwd     # Mac/Linux
cd      # Windows

# List files / سرد الملفات
ls      # Mac/Linux
dir     # Windows

# Change directory / تغيير المجلد
cd folder-name

# Go up one level / الصعود مستوى واحد
cd ..

# Clear terminal / مسح الطرفية
clear   # Mac/Linux
cls     # Windows
```

---

## Next Steps
## الخطوات التالية

Excellent work! You've successfully run your first Python program! 🎉
عمل ممتاز! لقد شغّلت أول برنامج بايثون لك بنجاح! 🎉

Now you can:
الآن يمكنك:

1. **Explore more examples** in `code-examples/chapter-01-algorithms/`
   **استكشف أمثلة أكثر** في `code-examples/chapter-01-algorithms/`

2. **Read the Chapter 1 notes** - Check `lectures/chapter-01-algorithms/`
   **اقرأ ملاحظات الفصل الأول** - راجع `lectures/chapter-01-algorithms/`

3. **Try the exercises** - Go to `exercises/chapter-01-algorithms/`
   **جرب التمارين** - اذهب إلى `exercises/chapter-01-algorithms/`

4. **Optional: Set up AI assistants** - [08-claude-code-extension-setup.md](08-claude-code-extension-setup.md)
   **اختياري: إعداد مساعدي الذكاء الاصطناعي** - [08-claude-code-extension-setup.md](08-claude-code-extension-setup.md)

---

## Tips for Success
## نصائح للنجاح

- 🔄 **Run code frequently** - Test as you learn
- 🔄 **شغّل الكود بشكل متكرر** - اختبر أثناء التعلم

- 📝 **Experiment** - Change code and see what happens
- 📝 **جرب** - غيّر الكود وشاهد ما يحدث

- 🐛 **Embrace errors** - They're learning opportunities
- 🐛 **احتضن الأخطاء** - إنها فرص تعلم

- 💬 **Read error messages** - They usually tell you what's wrong
- 💬 **اقرأ رسائل الأخطاء** - عادة ما تخبرك بما هو خاطئ

- 🙋 **Ask for help** - Dr. Laila is there for you, or open a GitHub issue
- 🙋 **اطلب المساعدة** - الدكتورة ليلى موجودة من أجلك، أو افتح GitHub issue

- 🎯 **Practice daily** - Even 15 minutes makes a difference
- 🎯 **تدرب يومياً** - حتى 15 دقيقة تحدث فرقاً

---

*Last Updated: October 2025*
*آخر تحديث: أكتوبر 2025*
