# Claude Code Extension Setup Guide (Optional)
# دليل إعداد إضافة Claude Code (اختياري)

⏱️ **Estimated Time:** 15-20 minutes
⏱️ **الوقت المقدر:** 15-20 دقيقة

---

## Important Notice
## إشعار مهم

⚠️ **This setup is OPTIONAL for M110 students.**
⚠️ **هذا الإعداد اختياري لطلاب M110.**

Claude Code is an AI coding assistant that can help you learn, but it's not required for the course. You can complete all assignments and exams without it.
Claude Code هو مساعد برمجة بالذكاء الاصطناعي يمكنه مساعدتك في التعلم، لكنه ليس مطلوباً للمقرر. يمكنك إكمال جميع الواجبات والامتحانات بدونه.

---

## What is Claude Code?
## ما هو Claude Code؟

Claude Code is an official VS Code extension from Anthropic that integrates Claude AI directly into your coding environment. Think of it as having an expert programming tutor available 24/7.

Claude Code هو إضافة رسمية لـ VS Code من Anthropic تدمج Claude AI مباشرة في بيئة البرمجة الخاصة بك. فكر فيه كوجود مدرس برمجة خبير متاح على مدار الساعة.

### What Can Claude Code Do?
### ماذا يمكن لـ Claude Code أن يفعل؟

- 💬 **Answer questions** about Python concepts
- 💬 **الإجابة على الأسئلة** حول مفاهيم Python

- 📖 **Explain code** line by line
- 📖 **شرح الكود** سطراً بسطر

- 🐛 **Debug errors** and suggest fixes
- 🐛 **تصحيح الأخطاء** واقتراح الإصلاحات

- 💡 **Suggest improvements** to your code
- 💡 **اقتراح تحسينات** على كودك

- 📝 **Generate code examples** for learning
- 📝 **إنشاء أمثلة كود** للتعلم

- ✅ **Review your solutions** and provide feedback
- ✅ **مراجعة حلولك** وتقديم ملاحظات

### Special Feature: Dr. Laila
### ميزة خاصة: الدكتورة ليلى

Your instructor has configured a special AI assistant called **Dr. Laila** (الدكتورة ليلى) specifically for M110 students. Dr. Laila:
قام مدرسك بتكوين مساعد ذكاء اصطناعي خاص يُسمى **الدكتورة ليلى** خصيصاً لطلاب M110. الدكتورة ليلى:

- Understands the M110 curriculum
- تفهم منهج M110

- Explains concepts at beginner level
- تشرح المفاهيم على مستوى المبتدئين

- Provides bilingual support (English/Arabic)
- توفر دعماً ثنائي اللغة (إنجليزي/عربي)

- Aligns with course materials and PEP 8 standards
- تتماشى مع مواد المقرر ومعايير PEP 8

- Guides you without giving away complete assignment solutions
- ترشدك دون إعطاء حلول الواجبات الكاملة

---

## Prerequisites
## المتطلبات الأساسية

Before setting up Claude Code:
قبل إعداد Claude Code:

- ✅ VS Code installed (see [02-vscode-installation.md](02-vscode-installation.md))
- ✅ VS Code مثبت (انظر [02-vscode-installation.md](02-vscode-installation.md))

- ✅ Internet connection
- ✅ اتصال بالإنترنت

- ✅ Credit card or payment method (for API credits)
- ✅ بطاقة ائتمان أو طريقة دفع (لرصيد API)

- ✅ Basic understanding of API keys (we'll explain)
- ✅ فهم أساسي لمفاتيح API (سنشرح)

---

## Part 1: Understanding API Keys and Costs
## الجزء 1: فهم مفاتيح API والتكاليف

### What is an API Key?
### ما هو مفتاح API؟

An API key is like a password that allows Claude Code to communicate with Anthropic's servers. It's unique to you and should be kept private.

مفتاح API هو مثل كلمة مرور تسمح لـ Claude Code بالتواصل مع خوادم Anthropic. إنه فريد لك ويجب أن يبقى خاصاً.

### How Much Does It Cost?
### كم يكلف؟

Claude operates on a **pay-as-you-go** model:
Claude يعمل على نموذج **الدفع حسب الاستخدام**:

- **Input tokens:** $0.003 per 1,000 tokens (~750 words)
- **رموز الإدخال:** $0.003 لكل 1,000 رمز (~750 كلمة)

- **Output tokens:** $0.015 per 1,000 tokens
- **رموز الإخراج:** $0.015 لكل 1,000 رمز

**Realistic usage for students:**
**الاستخدام الواقعي للطلاب:**

- Light usage (5-10 questions/day): ~$5-10/month
- استخدام خفيف (5-10 أسئلة/يوم): ~$5-10/شهر

- Moderate usage (20-30 questions/day): ~$15-25/month
- استخدام معتدل (20-30 سؤال/يوم): ~$15-25/شهر

- Heavy usage: ~$30-50/month
- استخدام كثيف: ~$30-50/شهر

💡 **Tip:** You can set spending limits in your Anthropic account to control costs!
💡 **نصيحة:** يمكنك تعيين حدود إنفاق في حساب Anthropic للتحكم في التكاليف!

### Free Alternatives
### بدائل مجانية

If cost is a concern, consider:
إذا كانت التكلفة مصدر قلق، فكر في:

- GitHub Copilot (free for students with GitHub Education)
- GitHub Copilot (مجاني للطلاب مع GitHub Education)

- ChatGPT Free (web-based, not integrated with VS Code)
- ChatGPT مجاني (على الويب، غير مدمج مع VS Code)

- Ask your instructor during office hours
- اسأل مدرسك خلال الساعات المكتبية

---

## Part 2: Creating an Anthropic Account
## الجزء 2: إنشاء حساب Anthropic

### Step 1: Visit Anthropic Console
### الخطوة 1: زيارة Anthropic Console

1. Open your web browser
   افتح متصفح الإنترنت

2. Go to:
   اذهب إلى:

   🔗 [https://console.anthropic.com](https://console.anthropic.com)

3. Click **"Sign Up"** or **"Get Started"**
   انقر **"Sign Up"** أو **"Get Started"**

📸 **Screenshot location:** Anthropic Console homepage

### Step 2: Create Your Account
### الخطوة 2: إنشاء حسابك

1. Choose a sign-up method:
   اختر طريقة التسجيل:

   - **Email and password**
   - **البريد الإلكتروني وكلمة المرور**

   - **Google account**
   - **حساب Google**

   - **GitHub account** (recommended if you have one)
   - **حساب GitHub** (موصى به إذا كان لديك واحد)

2. Fill in your information:
   املأ معلوماتك:

   - Full name
   - الاسم الكامل

   - Email address (student email recommended)
   - عنوان البريد الإلكتروني (البريد الطلابي موصى به)

   - Password (strong and unique)
   - كلمة المرور (قوية وفريدة)

3. Agree to Terms of Service and Privacy Policy
   وافق على شروط الخدمة وسياسة الخصوصية

4. Click **"Create Account"**
   انقر **"Create Account"**

### Step 3: Verify Your Email
### الخطوة 3: التحقق من بريدك الإلكتروني

1. Check your email inbox
   تحقق من صندوق بريدك

2. Look for an email from Anthropic
   ابحث عن بريد إلكتروني من Anthropic

3. Click the verification link
   انقر رابط التحقق

4. Your email is now verified!
   تم التحقق من بريدك الإلكتروني الآن!

---

## Part 3: Setting Up Billing
## الجزء 3: إعداد الفوترة

⚠️ **Important:** You need to add a payment method before you can use the API.
⚠️ **مهم:** تحتاج لإضافة طريقة دفع قبل أن تتمكن من استخدام API.

### Step 1: Navigate to Billing
### الخطوة 1: الانتقال إلى الفوترة

1. In the Anthropic Console, click **"Settings"** (gear icon)
   في Anthropic Console، انقر **"Settings"** (أيقونة الترس)

2. Click **"Billing"** in the left sidebar
   انقر **"Billing"** في الشريط الجانبي الأيسر

### Step 2: Add Payment Method
### الخطوة 2: إضافة طريقة دفع

1. Click **"Add Payment Method"**
   انقر **"Add Payment Method"**

2. Enter your credit card information:
   أدخل معلومات بطاقة الائتمان:

   - Card number
   - رقم البطاقة

   - Expiration date
   - تاريخ الانتهاء

   - CVC/CVV code
   - كود CVC/CVV

   - Billing address
   - عنوان الفوترة

3. Click **"Add Card"**
   انقر **"Add Card"**

### Step 3: Set Spending Limits (Recommended)
### الخطوة 3: تعيين حدود الإنفاق (موصى به)

Protect yourself from unexpected charges!
احمِ نفسك من رسوم غير متوقعة!

1. In Billing settings, find **"Usage Limits"**
   في إعدادات الفوترة، ابحث عن **"Usage Limits"**

2. Set a **monthly budget** (e.g., $20)
   عيّن **ميزانية شهرية** (مثلاً، $20)

3. Enable **email notifications** at 50%, 80%, and 100%
   فعّل **إشعارات البريد الإلكتروني** عند 50%، 80%، و 100%

4. Click **"Save"**
   انقر **"Save"**

📸 **Screenshot location:** Billing page with usage limits highlighted

---

## Part 4: Generating an API Key
## الجزء 4: إنشاء مفتاح API

### Step 1: Navigate to API Keys
### الخطوة 1: الانتقال إلى مفاتيح API

1. In the Anthropic Console, click **"API Keys"** in the left sidebar
   في Anthropic Console، انقر **"API Keys"** في الشريط الجانبي الأيسر

2. You'll see a page titled "API Keys"
   سترى صفحة بعنوان "API Keys"

### Step 2: Create a New Key
### الخطوة 2: إنشاء مفتاح جديد

1. Click **"Create Key"** or **"+ New Key"**
   انقر **"Create Key"** أو **"+ New Key"**

2. Give your key a name:
   أعطِ مفتاحك اسماً:

   ```
   M110-VSCode
   ```

   This helps you identify where you're using this key
   هذا يساعدك في تحديد أين تستخدم هذا المفتاح

3. Click **"Create Key"**
   انقر **"Create Key"**

### Step 3: Copy Your API Key
### الخطوة 3: نسخ مفتاح API

⚠️ **CRITICAL:** You can only see this key once!
⚠️ **حرج:** يمكنك رؤية هذا المفتاح مرة واحدة فقط!

1. A key will appear that looks like:
   سيظهر مفتاح يبدو مثل:

   ```
   sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

2. Click the **"Copy"** button
   انقر زر **"Copy"**

3. **Immediately paste it somewhere safe:**
   **الصق فوراً في مكان آمن:**

   - Password manager (best option)
   - مدير كلمات المرور (الخيار الأفضل)

   - Encrypted note
   - ملاحظة مشفرة

   - Secure document
   - مستند آمن

⚠️ **NEVER share your API key or commit it to GitHub!**
⚠️ **لا تشارك مفتاح API أو ترسله إلى GitHub أبداً!**

📸 **Screenshot location:** API Keys page with new key (blurred for security)

---

## Part 5: Installing Claude Code Extension
## الجزء 5: تثبيت إضافة Claude Code

### Step 1: Open Extensions in VS Code
### الخطوة 1: فتح الإضافات في VS Code

1. Open VS Code
   افتح VS Code

2. Click the **Extensions** icon (🧩) in the Activity Bar
   انقر أيقونة **Extensions** (🧩) في شريط النشاط

   OR / أو

   Press **Ctrl/⌘ + Shift + X**
   اضغط **Ctrl/⌘ + Shift + X**

### Step 2: Search for Claude Code
### الخطوة 2: البحث عن Claude Code

1. In the search box, type:
   في مربع البحث، اكتب:

   ```
   Claude Code
   ```

2. Look for the extension:
   ابحث عن الإضافة:

   - **Name:** Claude Code
   - **الاسم:** Claude Code

   - **Publisher:** Anthropic
   - **الناشر:** Anthropic

   - **Official extension** with Anthropic logo
   - **إضافة رسمية** بشعار Anthropic

📸 **Screenshot location:** Extensions panel with Claude Code

### Step 3: Install the Extension
### الخطوة 3: تثبيت الإضافة

1. Click the **"Install"** button
   انقر زر **"Install"**

2. Wait for installation (30-60 seconds)
   انتظر التثبيت (30-60 ثانية)

3. The extension is now installed!
   الإضافة مثبتة الآن!

---

## Part 6: Configuring Claude Code with Your API Key
## الجزء 6: تكوين Claude Code بمفتاح API الخاص بك

### Step 1: Open Claude Code Settings
### الخطوة 1: فتح إعدادات Claude Code

1. Click the **Claude icon** in the Activity Bar (left side)
   انقر **أيقونة Claude** في شريط النشاط (الجانب الأيسر)

2. A panel will open on the left showing "Welcome to Claude Code"
   ستفتح لوحة على اليسار تعرض "Welcome to Claude Code"

3. Click **"Add API Key"** or **"Configure"**
   انقر **"Add API Key"** أو **"Configure"**

### Step 2: Enter Your API Key
### الخطوة 2: إدخال مفتاح API الخاص بك

1. A prompt will appear asking for your API key
   سيظهر موجه يطلب مفتاح API الخاص بك

2. Paste your API key (the one you copied earlier)
   الصق مفتاح API (الذي نسخته سابقاً)

   ```
   sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

3. Press **Enter**
   اضغط **Enter**

4. VS Code will verify the key
   سيتحقق VS Code من المفتاح

✅ **Success! Claude Code is now connected!**
✅ **نجح! Claude Code متصل الآن!**

### Step 3: Test the Connection
### الخطوة 3: اختبار الاتصال

1. In the Claude Code panel, type a simple question:
   في لوحة Claude Code، اكتب سؤالاً بسيطاً:

   ```
   What is Python?
   ```

2. Press **Enter** or click **Send**
   اضغط **Enter** أو انقر **Send**

3. Claude should respond with an explanation!
   يجب أن يستجيب Claude بشرح!

📸 **Screenshot location:** Claude Code panel with test conversation

---

## Part 7: Activating Dr. Laila
## الجزء 7: تفعيل الدكتورة ليلى

Dr. Laila is a custom configuration designed specifically for M110 students.
الدكتورة ليلى هي تكوين مخصص مصمم خصيصاً لطلاب M110.

### What Makes Dr. Laila Special?
### ما الذي يجعل الدكتورة ليلى خاصة؟

- Knows the M110 curriculum and weekly topics
- تعرف منهج M110 والمواضيع الأسبوعية

- Explains at beginner-friendly level
- تشرح على مستوى مناسب للمبتدئين

- Provides bilingual help (English/Arabic)
- توفر مساعدة ثنائية اللغة (إنجليزي/عربي)

- Encourages learning, doesn't just give answers
- تشجع التعلم، لا تعطي الإجابات فقط

- Follows PEP 8 standards
- تتبع معايير PEP 8

### How to Use Dr. Laila
### كيفية استخدام الدكتورة ليلى

The repository includes a file called `HOW-TO-USE-DR-LAILA.md` with detailed instructions.
المستودع يتضمن ملفاً يُسمى `HOW-TO-USE-DR-LAILA.md` مع تعليمات مفصلة.

**Quick method:**
**الطريقة السريعة:**

1. Open Claude Code panel
   افتح لوحة Claude Code

2. Type the slash command:
   اكتب أمر الشرطة المائلة:

   ```
   /laila
   ```

3. Press **Enter**
   اضغط **Enter**

4. Dr. Laila is now activated and ready to help!
   الدكتورة ليلى مفعلة الآن وجاهزة للمساعدة!

5. Try asking:
   حاول السؤال:

   ```
   /laila Explain what a variable is in simple terms
   ```

   OR in Arabic / أو بالعربية:

   ```
   /laila اشرح ما هو المتغير بمصطلحات بسيطة
   ```

📸 **Screenshot location:** Claude Code with /laila command and response

---

## Part 8: Best Practices for Using AI Assistants
## الجزء 8: أفضل الممارسات لاستخدام مساعدي الذكاء الاصطناعي

### Do's ✅
### افعل ✅

- **Ask for explanations** - "Why does this work?"
- **اطلب التوضيحات** - "لماذا يعمل هذا؟"

- **Debug together** - "I'm getting this error, what does it mean?"
- **صحح معاً** - "أحصل على هذا الخطأ، ماذا يعني؟"

- **Learn concepts** - "What's the difference between a list and a tuple?"
- **تعلم المفاهيم** - "ما الفرق بين list و tuple؟"

- **Review your code** - "Can you review my solution and suggest improvements?"
- **راجع كودك** - "هل يمكنك مراجعة حلي واقتراح تحسينات؟"

- **Explore alternatives** - "Is there a better way to do this?"
- **استكشف البدائل** - "هل هناك طريقة أفضل لفعل هذا؟"

### Don'ts ❌
### لا تفعل ❌

- **Copy without understanding** - Don't just paste AI code
- **النسخ بدون فهم** - لا تلصق كود الذكاء الاصطناعي فقط

- **Skip the learning** - AI should help you learn, not do the work
- **تخطي التعلم** - الذكاء الاصطناعي يجب أن يساعدك في التعلم، لا أن يقوم بالعمل

- **Rely completely** - Develop your own problem-solving skills
- **الاعتماد الكامل** - طور مهارات حل المشكلات الخاصة بك

- **Submit AI code as yours** - Always understand and modify
- **إرسال كود الذكاء الاصطناعي على أنه لك** - افهم ودائماً عدّل دائماً

- **Share your API key** - Keep it private!
- **مشاركة مفتاح API** - احتفظ به خاصاً!

### Effective Questioning
### الأسئلة الفعالة

**Bad question:**
**سؤال سيئ:**
```
Write a program for my exercise
```

**Good question:**
**سؤال جيد:**
```
I'm working on Exercise 3 about loops. I wrote this code [paste code],
but I'm getting an IndexError. Can you help me understand why and
guide me to fix it?
```

---

## Part 9: Security and Privacy
## الجزء 9: الأمان والخصوصية

### Protecting Your API Key
### حماية مفتاح API الخاص بك

⚠️ **Never:**
⚠️ **أبداً:**

- Commit API keys to Git/GitHub
- ترسل مفاتيح API إلى Git/GitHub

- Share keys in screenshots or videos
- تشارك المفاتيح في لقطات الشاشة أو الفيديوهات

- Post keys in forums or chat
- تنشر المفاتيح في المنتديات أو الدردشة

- Email keys to others
- ترسل المفاتيح بالبريد الإلكتروني للآخرين

✅ **Always:**
✅ **دائماً:**

- Store keys in password managers
- احفظ المفاتيح في مديري كلمات المرور

- Use environment variables (advanced)
- استخدم متغيرات البيئة (متقدم)

- Delete and regenerate if exposed
- احذف وأعد إنشاء إذا تعرضت للكشف

### If Your Key is Compromised
### إذا تم اختراق مفتاحك

1. Go to Anthropic Console → API Keys
   اذهب إلى Anthropic Console → API Keys

2. Click **"Delete"** next to the compromised key
   انقر **"Delete"** بجوار المفتاح المخترق

3. Create a new key
   أنشئ مفتاحاً جديداً

4. Update VS Code with the new key
   حدّث VS Code بالمفتاح الجديد

---

## Troubleshooting
## استكشاف الأخطاء وإصلاحها

### ❌ "Invalid API Key" error
### ❌ خطأ "Invalid API Key"

**Solution:**
**الحل:**

1. Check you copied the entire key (starts with `sk-ant-api03-`)
   تحقق من نسخ المفتاح بالكامل (يبدأ بـ `sk-ant-api03-`)

2. No extra spaces before or after
   لا مسافات إضافية قبل أو بعد

3. Generate a new key if needed
   أنشئ مفتاحاً جديداً إذا لزم الأمر

### ❌ "Insufficient credits" error
### ❌ خطأ "Insufficient credits"

**Solution:**
**الحل:**

1. Check your Anthropic Console → Billing
   تحقق من Anthropic Console → Billing

2. Add credits or update payment method
   أضف رصيداً أو حدّث طريقة الدفع

3. Verify your card is not declined
   تحقق من عدم رفض بطاقتك

### ❌ Claude Code not responding
### ❌ Claude Code لا يستجيب

**Solution:**
**الحل:**

1. Check your internet connection
   تحقق من اتصال الإنترنت

2. Reload VS Code: Ctrl/⌘ + Shift + P → "Developer: Reload Window"
   أعد تحميل VS Code: Ctrl/⌘ + Shift + P → "Developer: Reload Window"

3. Check Anthropic status page: status.anthropic.com
   تحقق من صفحة حالة Anthropic: status.anthropic.com

### ❌ /laila command not working
### ❌ أمر /laila لا يعمل

**Solution:**
**الحل:**

1. Make sure you're in the course repository folder
   تأكد من أنك في مجلد مستودع المقرر

2. Check that `.claude/commands/laila.md` file exists
   تحقق من وجود ملف `.claude/commands/laila.md`

3. Reload VS Code
   أعد تحميل VS Code

---

## Cost Management Tips
## نصائح إدارة التكلفة

### Save Money
### وفّر المال

- 💬 **Be concise** - Shorter questions cost less
- 💬 **كن موجزاً** - الأسئلة الأقصر تكلف أقل

- 🎯 **Be specific** - Avoid back-and-forth conversations
- 🎯 **كن محدداً** - تجنب المحادثات ذهاباً وإياباً

- 📚 **Read docs first** - Use AI for clarification, not first resource
- 📚 **اقرأ الوثائق أولاً** - استخدم الذكاء الاصطناعي للتوضيح، وليس كمورد أول

- 🔄 **Start new conversations** - Don't keep long threads
- 🔄 **ابدأ محادثات جديدة** - لا تحتفظ بسلاسل طويلة

- ⏰ **Use during focused study** - Don't leave it open all day
- ⏰ **استخدم أثناء الدراسة المركزة** - لا تتركه مفتوحاً طوال اليوم

### Monitor Usage
### راقب الاستخدام

Check your usage regularly:
تحقق من استخدامك بانتظام:

1. Go to Anthropic Console → Usage
   اذهب إلى Anthropic Console → Usage

2. View daily/monthly spending
   اعرض الإنفاق اليومي/الشهري

3. Set alerts for budget thresholds
   عيّن تنبيهات لحدود الميزانية

---

## Alternative Free Options
## خيارات بديلة مجانية

If Claude Code doesn't fit your budget:
إذا لم يناسب Claude Code ميزانيتك:

### 1. GitHub Copilot (Free for Students)
### 1. GitHub Copilot (مجاني للطلاب)

See [09-github-copilot-setup.md](09-github-copilot-setup.md)
انظر [09-github-copilot-setup.md](09-github-copilot-setup.md)

### 2. ChatGPT Free (Web-based)
### 2. ChatGPT مجاني (على الويب)

- Visit chat.openai.com
- زر chat.openai.com

- Not integrated with VS Code
- غير مدمج مع VS Code

- Copy/paste code
- انسخ/الصق الكود

### 3. Office Hours with Instructor
### 3. الساعات المكتبية مع المدرس

- Free and personalized
- مجاني ومخصص

- Best for assignment help
- الأفضل للمساعدة في الواجبات

- Builds relationship with instructor
- يبني علاقة مع المدرس

---

## Next Steps
## الخطوات التالية

Congratulations on setting up Claude Code!
تهانينا على إعداد Claude Code!

Now you can:
الآن يمكنك:

1. **Start learning with Dr. Laila** - Read `HOW-TO-USE-DR-LAILA.md`
   **ابدأ التعلم مع الدكتورة ليلى** - اقرأ `HOW-TO-USE-DR-LAILA.md`

2. **Ask questions** while working on exercises
   **اسأل أسئلة** أثناء العمل على التمارين

3. **Get code reviews** for your solutions
   **احصل على مراجعات كود** لحلولك

4. **Debug faster** when you encounter errors
   **صحح أسرع** عندما تواجه أخطاء

5. **Consider GitHub Copilot too** - [09-github-copilot-setup.md](09-github-copilot-setup.md)
   **فكر في GitHub Copilot أيضاً** - [09-github-copilot-setup.md](09-github-copilot-setup.md)

---

## Additional Resources
## موارد إضافية

- 📖 [Anthropic Documentation](https://docs.anthropic.com/)
- 📖 [وثائق Anthropic](https://docs.anthropic.com/)

- 💰 [Pricing Calculator](https://console.anthropic.com/settings/pricing)
- 💰 [حاسبة التسعير](https://console.anthropic.com/settings/pricing)

- 🔒 [API Security Best Practices](https://docs.anthropic.com/en/api/security)
- 🔒 [أفضل ممارسات أمان API](https://docs.anthropic.com/en/api/security)

---

*Last Updated: October 2025*
*آخر تحديث: أكتوبر 2025*
