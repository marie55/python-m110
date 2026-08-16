# GitHub Copilot Setup Guide (Optional)
# دليل إعداد GitHub Copilot (اختياري)

⏱️ **Estimated Time:** 15-20 minutes
⏱️ **الوقت المقدر:** 15-20 دقيقة

---

## Important Notice
## إشعار مهم

⚠️ **This setup is OPTIONAL for M110 students.**
⚠️ **هذا الإعداد اختياري لطلاب M110.**

GitHub Copilot is an AI coding assistant, but it's not required for the course. You can complete all assignments without it.
GitHub Copilot هو مساعد برمجة بالذكاء الاصطناعي، لكنه ليس مطلوباً للمقرر. يمكنك إكمال جميع الواجبات بدونه.

---

## What is GitHub Copilot?
## ما هو GitHub Copilot؟

GitHub Copilot is an AI-powered code completion tool developed by GitHub and OpenAI. It suggests code as you type, helping you write code faster and learn programming patterns.

GitHub Copilot هو أداة إكمال كود مدعومة بالذكاء الاصطناعي طورتها GitHub و OpenAI. يقترح الكود أثناء الكتابة، مما يساعدك على كتابة الكود بشكل أسرع وتعلم أنماط البرمجة.

### What Can Copilot Do?
### ماذا يمكن لـ Copilot أن يفعل؟

- 💡 **Auto-complete code** - Suggests complete functions and lines
- 💡 **إكمال الكود تلقائياً** - يقترح دوال وأسطر كاملة

- 📝 **Generate from comments** - Write a comment, get code
- 📝 **توليد من التعليقات** - اكتب تعليقاً، احصل على كود

- 🔄 **Provide alternatives** - Multiple suggestions for same task
- 🔄 **توفير بدائل** - اقتراحات متعددة لنفس المهمة

- 📚 **Learn patterns** - See professional coding styles
- 📚 **تعلم الأنماط** - شاهد أنماط برمجة احترافية

- 🐛 **Quick fixes** - Suggest solutions for errors
- 🐛 **إصلاحات سريعة** - اقترح حلولاً للأخطاء

### Special Feature: Copilot Chat (@learning-assistant)
### ميزة خاصة: Copilot Chat (@learning-assistant)

GitHub Copilot includes a chat feature with a special **@learning-assistant** mode designed for students:
GitHub Copilot يتضمن ميزة دردشة مع وضع **@learning-assistant** خاص مصمم للطلاب:

- Explains concepts in simple terms
- يشرح المفاهيم بمصطلحات بسيطة

- Breaks down code step by step
- يفكك الكود خطوة بخطوة

- Provides learning resources
- يوفر موارد تعليمية

- Guides without giving direct answers
- يرشد دون إعطاء إجابات مباشرة

---

## Prerequisites
## المتطلبات الأساسية

Before setting up GitHub Copilot:
قبل إعداد GitHub Copilot:

- ✅ VS Code installed (see [02-vscode-installation.md](02-vscode-installation.md))
- ✅ VS Code مثبت (انظر [02-vscode-installation.md](02-vscode-installation.md))

- ✅ GitHub account (see [03-git-installation.md](03-git-installation.md))
- ✅ حساب GitHub (انظر [03-git-installation.md](03-git-installation.md))

- ✅ Student email address or student ID
- ✅ عنوان بريد إلكتروني طلابي أو هوية طالب

- ✅ Internet connection
- ✅ اتصال بالإنترنت

---

## Part 1: Getting Free Access (GitHub Education)
## الجزء 1: الحصول على وصول مجاني (GitHub Education)

### Why is it Free?
### لماذا هو مجاني؟

GitHub offers Copilot **FREE** to verified students through the GitHub Student Developer Pack!
GitHub تقدم Copilot **مجاناً** للطلاب المتحققين عبر حزمة مطور الطلاب من GitHub!

- **Regular price:** $10/month
- **السعر العادي:** $10/شهر

- **Student price:** FREE while you're a student
- **سعر الطالب:** مجاني أثناء كونك طالباً

### Step 1: Visit GitHub Education
### الخطوة 1: زيارة GitHub Education

1. Open your web browser
   افتح متصفح الإنترنت

2. Go to:
   اذهب إلى:

   🔗 [https://education.github.com](https://education.github.com)

3. Click **"Get the Pack"** or **"Sign up for Student Developer Pack"**
   انقر **"Get the Pack"** أو **"Sign up for Student Developer Pack"**

📸 **Screenshot location:** GitHub Education homepage

### Step 2: Sign In to GitHub
### الخطوة 2: تسجيل الدخول إلى GitHub

1. Sign in with your GitHub account
   سجل دخول بحساب GitHub الخاص بك

2. If you don't have an account, create one first (see [03-git-installation.md](03-git-installation.md))
   إذا لم يكن لديك حساب، أنشئ واحداً أولاً (انظر [03-git-installation.md](03-git-installation.md))

### Step 3: Verify Student Status
### الخطوة 3: التحقق من حالة الطالب

You'll need to prove you're a student. GitHub accepts:
ستحتاج لإثبات أنك طالب. GitHub تقبل:

**Option 1: School-Issued Email**
**الخيار 1: بريد إلكتروني صادر عن المدرسة**

1. Click **"Verify your student status"**
   انقر **"Verify your student status"**

2. Enter your student email (e.g., `student.id@aou.edu.jo`)
   أدخل بريدك الطلابي (مثل `student.id@aou.edu.jo`)

3. GitHub will send a verification email
   سيرسل GitHub بريد تحقق إلكترونياً

4. Check your email and click the verification link
   تحقق من بريدك وانقر رابط التحقق

**Option 2: Upload Student ID**
**الخيار 2: رفع هوية الطالب**

If you don't have a student email:
إذا لم يكن لديك بريد طلابي:

1. Click **"Upload proof of student status"**
   انقر **"Upload proof of student status"**

2. Take a photo of:
   التقط صورة لـ:

   - Student ID card
   - بطاقة هوية طالب

   - Enrollment letter
   - خطاب قبول

   - Official transcript
   - كشف درجات رسمي

3. Make sure the document shows:
   تأكد من أن المستند يظهر:

   - Your name
   - اسمك

   - School name (Arab Open University)
   - اسم المدرسة (الجامعة العربية المفتوحة)

   - Current date or enrollment period
   - التاريخ الحالي أو فترة التسجيل

4. Upload the image
   ارفع الصورة

### Step 4: Complete Application
### الخطوة 4: إكمال الطلب

1. Fill in the form:
   املأ النموذج:

   - **School name:** Arab Open University
   - **اسم المدرسة:** الجامعة العربية المفتوحة

   - **Graduation year:** (Your expected graduation year)
   - **سنة التخرج:** (سنة تخرجك المتوقعة)

   - **How do you plan to use GitHub?**
     "For M110 Python Programming course and learning software development"
   - **كيف تخطط لاستخدام GitHub؟**
     "لمقرر برمجة بايثون M110 وتعلم تطوير البرمجيات"

2. Click **"Submit your information"**
   انقر **"Submit your information"**

### Step 5: Wait for Approval
### الخطوة 5: انتظار الموافقة

- **Email verification:** Usually instant
- **التحقق من البريد الإلكتروني:** عادة فوري

- **ID verification:** 1-7 days
- **التحقق من الهوية:** 1-7 أيام

You'll receive an email when approved!
ستتلقى بريداً إلكترونياً عند الموافقة!

📸 **Screenshot location:** GitHub Education application confirmation

---

## Part 2: Enabling GitHub Copilot
## الجزء 2: تمكين GitHub Copilot

Once your student status is verified:
بمجرد التحقق من حالتك كطالب:

### Step 1: Navigate to Copilot Settings
### الخطوة 1: الانتقال إلى إعدادات Copilot

1. Go to GitHub and sign in
   اذهب إلى GitHub وسجل دخول

2. Click your **profile picture** (top right)
   انقر **صورة ملفك الشخصي** (أعلى اليمين)

3. Select **"Settings"**
   اختر **"Settings"**

4. In the left sidebar, click **"Copilot"**
   في الشريط الجانبي الأيسر، انقر **"Copilot"**

### Step 2: Enable Copilot
### الخطوة 2: تمكين Copilot

1. You should see a message: **"GitHub Copilot is free for verified students"**
   يجب أن ترى رسالة: **"GitHub Copilot is free for verified students"**

2. Click **"Get access to GitHub Copilot"** or **"Enable GitHub Copilot"**
   انقر **"Get access to GitHub Copilot"** أو **"Enable GitHub Copilot"**

3. Review the terms
   راجع الشروط

4. Click **"Save"** or **"Enable"**
   انقر **"Save"** أو **"Enable"**

✅ **GitHub Copilot is now enabled for your account!**
✅ **تم تمكين GitHub Copilot لحسابك الآن!**

📸 **Screenshot location:** GitHub Copilot settings page

---

## Part 3: Installing Copilot in VS Code
## الجزء 3: تثبيت Copilot في VS Code

### Step 1: Open Extensions
### الخطوة 1: فتح الإضافات

1. Open VS Code
   افتح VS Code

2. Click **Extensions** icon (🧩) in the Activity Bar
   انقر أيقونة **Extensions** (🧩) في شريط النشاط

   OR / أو

   Press **Ctrl/⌘ + Shift + X**
   اضغط **Ctrl/⌘ + Shift + X**

### Step 2: Search for GitHub Copilot
### الخطوة 2: البحث عن GitHub Copilot

1. In the search box, type:
   في مربع البحث، اكتب:

   ```
   GitHub Copilot
   ```

2. Look for **two** extensions:
   ابحث عن **إضافتين**:

   **a) GitHub Copilot**
   - Publisher: GitHub
   - الناشر: GitHub

   - Main extension for code suggestions
   - الإضافة الرئيسية لاقتراحات الكود

   **b) GitHub Copilot Chat**
   - Publisher: GitHub
   - الناشر: GitHub

   - Chat interface for asking questions
   - واجهة دردشة لطرح الأسئلة

📸 **Screenshot location:** Extensions panel with both Copilot extensions

### Step 3: Install Both Extensions
### الخطوة 3: تثبيت كلا الإضافتين

1. Click **"Install"** on **GitHub Copilot**
   انقر **"Install"** على **GitHub Copilot**

2. Wait for installation (20-30 seconds)
   انتظر التثبيت (20-30 ثانية)

3. Click **"Install"** on **GitHub Copilot Chat**
   انقر **"Install"** على **GitHub Copilot Chat**

4. Wait for installation
   انتظر التثبيت

✅ **Both extensions are now installed!**
✅ **تم تثبيت كلا الإضافتين الآن!**

---

## Part 4: Signing In to Copilot
## الجزء 4: تسجيل الدخول إلى Copilot

### Step 1: Authenticate
### الخطوة 1: المصادقة

After installing, VS Code will prompt you to sign in:
بعد التثبيت، سيطالبك VS Code بتسجيل الدخول:

1. A notification will appear: **"Sign in to use GitHub Copilot"**
   سيظهر إشعار: **"Sign in to use GitHub Copilot"**

2. Click **"Sign In to GitHub"**
   انقر **"Sign In to GitHub"**

3. VS Code will open your web browser
   سيفتح VS Code متصفح الويب الخاص بك

4. GitHub will ask: **"Authorize Visual Studio Code"**
   سيسأل GitHub: **"Authorize Visual Studio Code"**

5. Click **"Authorize"**
   انقر **"Authorize"**

6. Enter your GitHub password if prompted
   أدخل كلمة مرور GitHub إذا طُلب

7. You may see a device code - copy and paste it
   قد ترى كود جهاز - انسخه والصقه

8. Return to VS Code
   ارجع إلى VS Code

### Step 2: Verify Sign-In
### الخطوة 2: التحقق من تسجيل الدخول

1. Look at the **bottom-right** of VS Code
   انظر إلى **أسفل اليمين** في VS Code

2. You should see a **Copilot icon** (✨ or GitHub logo)
   يجب أن ترى **أيقونة Copilot** (✨ أو شعار GitHub)

3. If it shows **"Copilot: Ready"**, you're signed in!
   إذا أظهرت **"Copilot: Ready"**، فأنت مسجل دخول!

📸 **Screenshot location:** VS Code status bar with Copilot icon

---

## Part 5: Using GitHub Copilot
## الجزء 5: استخدام GitHub Copilot

### Code Suggestions
### اقتراحات الكود

Copilot suggests code as you type!
Copilot يقترح الكود أثناء الكتابة!

1. Create a new Python file: `test_copilot.py`
   أنشئ ملف بايثون جديد: `test_copilot.py`

2. Type a comment describing what you want:
   اكتب تعليقاً يصف ما تريد:

   ```python
   # Function to calculate the area of a rectangle
   ```

3. Press **Enter** and start typing:
   اضغط **Enter** وابدأ الكتابة:

   ```python
   def calculate_rectangle_area
   ```

4. Copilot will suggest the rest! You'll see **gray text**:
   سيقترح Copilot الباقي! سترى **نصاً رمادياً**:

   ```python
   def calculate_rectangle_area(length, width):
       return length * width
   ```

5. Press **Tab** to accept the suggestion
   اضغط **Tab** لقبول الاقتراح

6. Press **Esc** to reject
   اضغط **Esc** للرفض

### Multiple Suggestions
### اقتراحات متعددة

1. When you see a Copilot suggestion (gray text)
   عندما ترى اقتراح Copilot (نص رمادي)

2. Press **Alt + ]** (Windows/Linux) or **⌥ + ]** (Mac) to see next suggestion
   اضغط **Alt + ]** (ويندوز/لينكس) أو **⌥ + ]** (ماك) لرؤية الاقتراح التالي

3. Press **Alt + [** or **⌥ + [** to see previous suggestion
   اضغط **Alt + [** أو **⌥ + [** لرؤية الاقتراح السابق

4. Press **Tab** to accept, **Esc** to dismiss
   اضغط **Tab** لقبول، **Esc** للرفض

### Inline Suggestions
### الاقتراحات المضمنة

Copilot can suggest:
Copilot يمكنه اقتراح:

- **Complete functions** from comments
- **دوال كاملة** من التعليقات

- **Next lines of code** based on context
- **أسطر الكود التالية** بناءً على السياق

- **Variable names** that make sense
- **أسماء متغيرات** منطقية

- **Common patterns** (loops, conditions, etc.)
- **أنماط شائعة** (حلقات، شروط، إلخ)

📸 **Screenshot location:** VS Code showing Copilot suggestion in gray text

---

## Part 6: Using Copilot Chat
## الجزء 6: استخدام Copilot Chat

Copilot Chat is like having a programming tutor!
Copilot Chat مثل وجود مدرس برمجة!

### Opening Copilot Chat
### فتح Copilot Chat

**Method 1: Activity Bar**
**الطريقة 1: شريط النشاط**

1. Click the **Chat** icon in the Activity Bar (looks like a speech bubble)
   انقر أيقونة **Chat** في شريط النشاط (تبدو مثل فقاعة كلام)

2. A chat panel opens on the left
   تفتح لوحة دردشة على اليسار

**Method 2: Keyboard Shortcut**
**الطريقة 2: اختصار لوحة المفاتيح**

- Press **Ctrl + I** (Windows/Linux)
- اضغط **Ctrl + I** (ويندوز/لينكس)

- Press **⌘ + I** (Mac)
- اضغط **⌘ + I** (ماك)

**Method 3: Right-Click**
**الطريقة 3: النقر بالزر الأيمن**

1. Select code in the editor
   حدد كوداً في المحرر

2. Right-click
   انقر بالزر الأيمن

3. Choose **"Copilot"** → **"Explain This"** or **"Fix This"**
   اختر **"Copilot"** → **"Explain This"** أو **"Fix This"**

### Asking Questions
### طرح الأسئلة

Type questions in the chat:
اكتب أسئلة في الدردشة:

```
How do I create a list in Python?
```

```
كيف أنشئ قائمة في Python؟
```

```
What's the difference between a for loop and a while loop?
```

```
ما الفرق بين حلقة for وحلقة while؟
```

### Using @learning-assistant
### استخدام @learning-assistant

For educational help, use the special learning assistant:
للمساعدة التعليمية، استخدم مساعد التعلم الخاص:

1. In Copilot Chat, type:
   في Copilot Chat، اكتب:

   ```
   @learning-assistant
   ```

2. Then ask your question:
   ثم اسأل سؤالك:

   ```
   @learning-assistant Explain what a function is
   ```

   ```
   @learning-assistant اشرح ما هي الدالة
   ```

The @learning-assistant will:
@learning-assistant سـ:

- Explain concepts step by step
- يشرح المفاهيم خطوة بخطوة

- Use beginner-friendly language
- يستخدم لغة مناسبة للمبتدئين

- Provide examples
- يوفر أمثلة

- Guide you to discover answers
- يرشدك لاكتشاف الإجابات

📸 **Screenshot location:** Copilot Chat with @learning-assistant conversation

---

## Part 7: Copilot Features in VS Code
## الجزء 7: ميزات Copilot في VS Code

### Slash Commands
### أوامر الشرطة المائلة

In Copilot Chat, use slash commands for specific tasks:
في Copilot Chat، استخدم أوامر الشرطة المائلة لمهام محددة:

- **/explain** - Explain selected code
- **/explain** - شرح الكود المحدد

- **/fix** - Suggest fix for errors
- **/fix** - اقترح إصلاحاً للأخطاء

- **/tests** - Generate unit tests
- **/tests** - ولّد اختبارات وحدة

- **/docs** - Add documentation
- **/docs** - أضف توثيقاً

**Example:**
**مثال:**

1. Select a function in your code
   حدد دالة في كودك

2. In chat, type:
   في الدردشة، اكتب:

   ```
   /explain
   ```

3. Copilot explains the selected code!
   Copilot يشرح الكود المحدد!

### Inline Chat
### الدردشة المضمنة

Edit code with AI assistance directly in the editor:
عدّل الكود بمساعدة الذكاء الاصطناعي مباشرة في المحرر:

1. Press **Ctrl/⌘ + I** in the editor
   اضغط **Ctrl/⌘ + I** في المحرر

2. A chat box appears inline
   تظهر مربع دردشة مضمن

3. Type what you want to change:
   اكتب ما تريد تغييره:

   ```
   Add error handling to this function
   ```

   ```
   أضف معالجة أخطاء لهذه الدالة
   ```

4. Copilot suggests changes
   Copilot يقترح تغييرات

5. Accept or reject
   اقبل أو ارفض

### Voice Input (Optional)
### إدخال صوتي (اختياري)

Some versions support voice:
بعض الإصدارات تدعم الصوت:

1. Click the **microphone icon** in chat
   انقر **أيقونة الميكروفون** في الدردشة

2. Speak your question
   تحدث بسؤالك

3. Copilot transcribes and answers
   Copilot ينسخ ويجيب

---

## Part 8: Best Practices
## الجزء 8: أفضل الممارسات

### Do's ✅
### افعل ✅

- **Review all suggestions** - Don't blindly accept
- **راجع جميع الاقتراحات** - لا تقبل بشكل أعمى

- **Learn from code** - Understand what Copilot suggests
- **تعلم من الكود** - افهم ما يقترحه Copilot

- **Use for boilerplate** - Let it handle repetitive code
- **استخدم للكود النمطي** - دعه يتعامل مع الكود المتكرر

- **Ask questions** - Use chat to clarify concepts
- **اسأل أسئلة** - استخدم الدردشة لتوضيح المفاهيم

- **Experiment** - Try different prompts
- **جرب** - جرب موجهات مختلفة

### Don'ts ❌
### لا تفعل ❌

- **Copy without understanding** - Always know what the code does
- **النسخ بدون فهم** - اعرف دائماً ما يفعله الكود

- **Trust blindly** - Copilot can make mistakes
- **الثقة العمياء** - Copilot يمكنه ارتكاب أخطاء

- **Skip learning fundamentals** - Use as helper, not replacement
- **تخطي تعلم الأساسيات** - استخدم كمساعد، وليس بديلاً

- **Rely on it for exams** - Exams test YOUR knowledge
- **الاعتماد عليه في الامتحانات** - الامتحانات تختبر معرفتك أنت

- **Ignore PEP 8** - Still follow course coding standards
- **تجاهل PEP 8** - اتبع معايير البرمجة للمقرر

### Effective Prompts
### الموجهات الفعالة

**Bad:**
**سيئ:**
```python
# function
```

**Good:**
**جيد:**
```python
# Function to calculate the factorial of a number using recursion
```

**Better:**
**أفضل:**
```python
# Function to calculate factorial of n using recursion
# Parameters: n (int) - non-negative integer
# Returns: int - factorial of n
# Example: factorial(5) returns 120
```

More specific comments = better suggestions!
تعليقات أكثر تحديداً = اقتراحات أفضل!

---

## Troubleshooting
## استكشاف الأخطاء وإصلاحها

### ❌ "Not authorized" or "Not signed in"
### ❌ "Not authorized" أو "Not signed in"

**Solution:**
**الحل:**

1. Check the Copilot icon in status bar
   تحقق من أيقونة Copilot في شريط الحالة

2. Click it and select **"Sign in to GitHub"**
   انقر عليها واختر **"Sign in to GitHub"**

3. Complete the authentication flow
   أكمل تدفق المصادقة

### ❌ "Copilot subscription required"
### ❌ "Copilot subscription required"

**Problem:** Student verification not complete
**المشكلة:** التحقق من الطالب غير مكتمل

**Solution:**
**الحل:**

1. Check your GitHub Education application status
   تحقق من حالة طلب GitHub Education الخاص بك

2. Visit: https://education.github.com/benefits
   زر: https://education.github.com/benefits

3. Complete verification if pending
   أكمل التحقق إذا كان قيد الانتظار

4. Wait for approval email
   انتظر بريد الموافقة الإلكتروني

### ❌ Copilot not showing suggestions
### ❌ Copilot لا يعرض اقتراحات

**Solution:**
**الحل:**

1. Check Copilot is enabled:
   تحقق من تمكين Copilot:

   - Look for icon in status bar
   - ابحث عن أيقونة في شريط الحالة

   - Click it to toggle on/off
   - انقر عليها للتبديل تشغيل/إيقاف

2. Check file type:
   تحقق من نوع الملف:

   - Copilot works best with `.py` files
   - Copilot يعمل بشكل أفضل مع ملفات `.py`

   - Save your file first
   - احفظ ملفك أولاً

3. Reload VS Code:
   أعد تحميل VS Code:

   - Ctrl/⌘ + Shift + P → "Developer: Reload Window"
   - Ctrl/⌘ + Shift + P → "Developer: Reload Window"

### ❌ Suggestions are low quality
### ❌ الاقتراحات ذات جودة منخفضة

**Solution:**
**الحل:**

1. Write better comments
   اكتب تعليقات أفضل

2. Provide more context
   وفّر سياقاً أكثر

3. Use descriptive variable/function names
   استخدم أسماء متغيرات/دوال وصفية

4. Try alternative suggestions (Alt + ])
   جرب اقتراحات بديلة (Alt + ])

### ❌ Chat not responding
### ❌ الدردشة لا تستجيب

**Solution:**
**الحل:**

1. Check internet connection
   تحقق من اتصال الإنترنت

2. Restart the chat:
   أعد تشغيل الدردشة:

   - Close chat panel
   - أغلق لوحة الدردشة

   - Reopen (Ctrl/⌘ + I)
   - أعد الفتح (Ctrl/⌘ + I)

3. Sign out and sign in again
   سجل خروج وسجل دخول مرة أخرى

---

## Comparing Copilot and Claude Code
## مقارنة Copilot و Claude Code

### GitHub Copilot
### GitHub Copilot

**Strengths:**
**نقاط القوة:**
- Free for students
- مجاني للطلاب
- Real-time code completion
- إكمال كود في الوقت الفعلي
- Integrated tightly with VS Code
- مدمج بإحكام مع VS Code
- Great for learning patterns
- رائع لتعلم الأنماط

**Best for:**
**الأفضل لـ:**
- Writing code faster
- كتابة الكود بشكل أسرع
- Learning syntax
- تعلم البنية
- Quick questions via chat
- أسئلة سريعة عبر الدردشة

### Claude Code
### Claude Code

**Strengths:**
**نقاط القوة:**
- Deep explanations
- شروحات عميقة
- M110-specific (Dr. Laila)
- خاص بـ M110 (الدكتورة ليلى)
- Better for debugging
- أفضل لتصحيح الأخطاء
- More conversational
- أكثر محادثة

**Best for:**
**الأفضل لـ:**
- Understanding concepts
- فهم المفاهيم
- Debugging complex issues
- تصحيح مشاكل معقدة
- Code reviews
- مراجعات الكود

**You can use BOTH!** They complement each other.
**يمكنك استخدام كليهما!** يكمل أحدهما الآخر.

---

## Quick Reference
## مرجع سريع

### Keyboard Shortcuts
### اختصارات لوحة المفاتيح

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Accept suggestion<br>قبول الاقتراح | Tab | Tab |
| Reject suggestion<br>رفض الاقتراح | Esc | Esc |
| Next suggestion<br>الاقتراح التالي | Alt + ] | ⌥ + ] |
| Previous suggestion<br>الاقتراح السابق | Alt + [ | ⌥ + [ |
| Open chat<br>فتح الدردشة | Ctrl + I | ⌘ + I |
| Inline chat<br>دردشة مضمنة | Ctrl + I | ⌘ + I |

### Chat Commands
### أوامر الدردشة

```
@learning-assistant [question]    # Educational help
/explain                          # Explain selected code
/fix                              # Fix errors
/tests                            # Generate tests
/docs                             # Add documentation
```

---

## Next Steps
## الخطوات التالية

You're all set with GitHub Copilot!
أنت جاهز تماماً مع GitHub Copilot!

Now:
الآن:

1. **Practice with examples** - Try it on Chapter 1 code
   **تدرب مع الأمثلة** - جربه على كود الفصل الأول

2. **Use @learning-assistant** - Ask about Python concepts
   **استخدم @learning-assistant** - اسأل عن مفاهيم Python

3. **Combine with Claude Code** - Use both tools together
   **ادمج مع Claude Code** - استخدم كلا الأداتين معاً

4. **Check troubleshooting guide** - [10-troubleshooting-common-issues.md](10-troubleshooting-common-issues.md)
   **راجع دليل استكشاف الأخطاء** - [10-troubleshooting-common-issues.md](10-troubleshooting-common-issues.md)

---

## Additional Resources
## موارد إضافية

- 📖 [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- 📖 [وثائق GitHub Copilot](https://docs.github.com/en/copilot)

- 🎓 [GitHub Education](https://education.github.com/)
- 🎓 [GitHub Education](https://education.github.com/)

- 💡 [Copilot Best Practices](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- 💡 [أفضل ممارسات Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)

---

*Last Updated: October 2025*
*آخر تحديث: أكتوبر 2025*
