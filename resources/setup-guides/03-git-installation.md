# Git Installation and Setup Guide
# دليل تثبيت وإعداد Git

⏱️ **Estimated Time:** 15-20 minutes
⏱️ **الوقت المقدر:** 15-20 دقيقة

---

## What is Git?
## ما هو Git؟

Git is a version control system that tracks changes to your files over time. Think of it like a time machine for your code - you can save snapshots, go back to previous versions, and collaborate with others. GitHub is a website that hosts Git repositories online.

Git هو نظام للتحكم في الإصدارات يتتبع التغييرات على ملفاتك عبر الزمن. فكر فيه كآلة زمن لكودك - يمكنك حفظ لقطات، والعودة إلى إصدارات سابقة، والتعاون مع الآخرين. GitHub هو موقع ويب يستضيف مستودعات Git على الإنترنت.

### Why do we need Git for this course?
### لماذا نحتاج Git في هذا المقرر؟

- 📥 **Download course materials** - All exercises and examples are on GitHub
- 📥 **تحميل مواد المقرر** - جميع التمارين والأمثلة على GitHub

- 🔄 **Get updates** - Pull new materials as the course progresses
- 🔄 **الحصول على التحديثات** - سحب المواد الجديدة مع تقدم المقرر

- 💾 **Track your progress** - Save your work history
- 💾 **تتبع تقدمك** - حفظ تاريخ عملك

- 🚀 **Industry skill** - Git is used by all professional programmers
- 🚀 **مهارة صناعية** - Git يُستخدم من قبل جميع المبرمجين المحترفين

---

## Prerequisites
## المتطلبات الأساسية

Before installing Git:
قبل تثبيت Git:

- ✅ VS Code installed (see [02-vscode-installation.md](02-vscode-installation.md))
- ✅ VS Code مثبت (انظر [02-vscode-installation.md](02-vscode-installation.md))

- ✅ Internet connection
- ✅ اتصال بالإنترنت

- ✅ An email address (for Git configuration)
- ✅ عنوان بريد إلكتروني (لإعداد Git)

---

## Part 1: Installing Git
## الجزء 1: تثبيت Git

### 🪟 For Windows Users
### 🪟 لمستخدمي ويندوز

#### Step 1: Download Git for Windows
#### الخطوة 1: تحميل Git لويندوز

1. Visit the official Git website:
   قم بزيارة موقع Git الرسمي:

   🔗 [https://git-scm.com/download/windows](https://git-scm.com/download/windows)

2. The download should start automatically. If not, click **"Click here to download"**
   يجب أن يبدأ التحميل تلقائياً. إن لم يحدث، انقر **"Click here to download"**

3. Save the installer (`Git-2.x.x-64-bit.exe`) to **Downloads**
   احفظ المثبت (`Git-2.x.x-64-bit.exe`) في **التنزيلات**

📸 **Screenshot location:** Git download page

#### Step 2: Install Git
#### الخطوة 2: تثبيت Git

⚠️ **Important**: The installer has many screens. We'll use mostly default settings.
⚠️ **مهم**: المثبت له شاشات عديدة. سنستخدم الإعدادات الافتراضية غالباً.

1. Double-click the downloaded installer
   انقر مرتين على المثبت المحمل

2. If Windows asks for permission, click **"Yes"**
   إذا طلب ويندوز الإذن، انقر **"Yes"**

3. **License**: Click **"Next"**
   **الرخصة**: انقر **"Next"**

4. **Installation location**: Keep default, click **"Next"**
   **موقع التثبيت**: احتفظ بالافتراضي، انقر **"Next"**

5. **Components**: Keep defaults checked, click **"Next"**
   **المكونات**: احتفظ بالافتراضيات محددة، انقر **"Next"**

6. **Start Menu folder**: Keep default, click **"Next"**
   **مجلد قائمة البدء**: احتفظ بالافتراضي، انقر **"Next"**

7. **Default editor**:
   **المحرر الافتراضي**:

   - Select **"Use Visual Studio Code as Git's default editor"**
     اختر **"Use Visual Studio Code as Git's default editor"**

   - Click **"Next"**
     انقر **"Next"**

8. **Initial branch name**: Keep **"Let Git decide"**, click **"Next"**
   **اسم الفرع الأولي**: احتفظ بـ **"Let Git decide"**، انقر **"Next"**

9. **PATH environment**: Select **"Git from the command line and also from 3rd-party software"**, click **"Next"**
   **بيئة PATH**: اختر **"Git from the command line and also from 3rd-party software"**، انقر **"Next"**

10. **SSH executable**: Use **"Use bundled OpenSSH"**, click **"Next"**
    **SSH التنفيذي**: استخدم **"Use bundled OpenSSH"**، انقر **"Next"**

11. **HTTPS transport**: Use **"Use the OpenSSL library"**, click **"Next"**
    **نقل HTTPS**: استخدم **"Use the OpenSSL library"**، انقر **"Next"**

12. **Line ending conversions**: Keep **"Checkout Windows-style, commit Unix-style"**, click **"Next"**
    **تحويلات نهاية السطر**: احتفظ بـ **"Checkout Windows-style, commit Unix-style"**، انقر **"Next"**

13. **Terminal emulator**: Choose **"Use Windows' default console window"**, click **"Next"**
    **محاكي الطرفية**: اختر **"Use Windows' default console window"**، انقر **"Next"**

14. **Git pull behavior**: Keep default, click **"Next"**
    **سلوك Git pull**: احتفظ بالافتراضي، انقر **"Next"**

15. **Credential helper**: Keep **"Git Credential Manager"**, click **"Next"**
    **مساعد الاعتماد**: احتفظ بـ **"Git Credential Manager"**، انقر **"Next"**

16. **Extra options**: Keep defaults, click **"Next"**
    **خيارات إضافية**: احتفظ بالافتراضيات، انقر **"Next"**

17. **Experimental options**: Don't check any, click **"Install"**
    **خيارات تجريبية**: لا تحدد أياً، انقر **"Install"**

18. Wait for installation (2-5 minutes)
    انتظر التثبيت (2-5 دقائق)

19. Click **"Finish"**
    انقر **"Finish"**

---

### 🍎 For macOS Users
### 🍎 لمستخدمي ماك

#### Option 1: Install via Xcode Command Line Tools (Recommended)
#### الخيار 1: التثبيت عبر أدوات سطر أوامر Xcode (موصى به)

1. Open Terminal (Command ⌘ + Space, type "Terminal")
   افتح Terminal (Command ⌘ + Space، اكتب "Terminal")

2. Type this command and press Enter:
   اكتب هذا الأمر واضغط Enter:

   ```bash
   git --version
   ```

3. If Git isn't installed, macOS will prompt you to install Xcode Command Line Tools
   إذا لم يكن Git مثبتاً، سيطلب منك macOS تثبيت أدوات سطر أوامر Xcode

4. Click **"Install"** in the popup
   انقر **"Install"** في النافذة المنبثقة

5. Agree to the license
   وافق على الرخصة

6. Wait for installation (5-15 minutes depending on internet speed)
   انتظر التثبيت (5-15 دقيقة حسب سرعة الإنترنت)

#### Option 2: Download from Git website
#### الخيار 2: التحميل من موقع Git

1. Visit:
   قم بزيارة:

   🔗 [https://git-scm.com/download/mac](https://git-scm.com/download/mac)

2. Download the latest macOS Git installer
   حمل أحدث مثبت Git لـ macOS

3. Open the `.dmg` file and run the installer
   افتح ملف `.dmg` وشغل المثبت

4. Follow the installation wizard
   اتبع معالج التثبيت

---

### 🐧 For Linux Users (Ubuntu/Debian)
### 🐧 لمستخدمي لينكس (Ubuntu/Debian)

1. Open Terminal (Ctrl + Alt + T)
   افتح Terminal (Ctrl + Alt + T)

2. Update package index:
   حدث فهرس الحزم:

   ```bash
   sudo apt update
   ```

3. Install Git:
   ثبت Git:

   ```bash
   sudo apt install git
   ```

4. Enter password when prompted
   أدخل كلمة المرور عند الطلب

5. Type **Y** and press Enter to confirm
   اكتب **Y** واضغط Enter للتأكيد

---

## Part 2: Verify Git Installation
## الجزء 2: التحقق من تثبيت Git

Let's make sure Git is properly installed:
دعنا نتأكد من أن Git مثبت بشكل صحيح:

1. Open a new terminal/command prompt:
   افتح terminal/موجه أوامر جديد:

   - **Windows**: Press Windows key, type "cmd", press Enter
   - **Windows**: اضغط مفتاح Windows، اكتب "cmd"، اضغط Enter

   - **Mac**: Command ⌘ + Space, type "Terminal", press Enter
   - **Mac**: Command ⌘ + Space، اكتب "Terminal"، اضغط Enter

   - **Linux**: Ctrl + Alt + T
   - **Linux**: Ctrl + Alt + T

2. Type this command:
   اكتب هذا الأمر:

   ```bash
   git --version
   ```

3. You should see something like:
   يجب أن ترى شيئاً مثل:

   ```
   git version 2.42.0
   ```

✅ If you see a version number, Git is installed successfully!
✅ إذا رأيت رقم إصدار، فقد تم تثبيت Git بنجاح!

❌ If you see "command not found", restart your computer and try again
❌ إذا رأيت "command not found"، أعد تشغيل الكمبيوتر وحاول مرة أخرى

---

## Part 3: Configure Git
## الجزء 3: إعداد Git

Now we need to tell Git who you are. This information is attached to your commits.
الآن نحتاج لإخبار Git من أنت. هذه المعلومات ترفق مع commits الخاصة بك.

### Set Your Name and Email
### ضبط اسمك وبريدك الإلكتروني

1. Open terminal/command prompt
   افتح terminal/موجه الأوامر

2. Set your name (replace "Your Name" with your actual name):
   اضبط اسمك (استبدل "Your Name" باسمك الفعلي):

   ```bash
   git config --global user.name "Your Name"
   ```

   Example / مثال:
   ```bash
   git config --global user.name "Ahmed Hassan"
   ```

3. Set your email (use the email you'll use for GitHub):
   اضبط بريدك الإلكتروني (استخدم البريد الذي ستستخدمه لـ GitHub):

   ```bash
   git config --global user.email "your.email@example.com"
   ```

   Example / مثال:
   ```bash
   git config --global user.email "ahmed.hassan@student.aou.edu.jo"
   ```

### Verify Your Configuration
### التحقق من إعدادك

Check that your configuration is correct:
تحقق من أن إعدادك صحيح:

```bash
git config --global --list
```

You should see:
يجب أن ترى:

```
user.name=Your Name
user.email=your.email@example.com
```

---

## Part 4: Create a GitHub Account
## الجزء 4: إنشاء حساب GitHub

GitHub is where we'll store and share code online. It's free!
GitHub هو المكان الذي سنخزن ونشارك فيه الكود على الإنترنت. إنه مجاني!

1. Visit GitHub:
   قم بزيارة GitHub:

   🔗 [https://github.com](https://github.com)

2. Click **"Sign up"** (top right corner)
   انقر **"Sign up"** (الزاوية العلوية اليمنى)

3. Enter your information:
   أدخل معلوماتك:

   - **Username**: Choose something professional (e.g., ahmed-hassan-2024)
   - **اسم المستخدم**: اختر شيئاً احترافياً (مثل ahmed-hassan-2024)

   - **Email**: Use your student email if possible
   - **البريد الإلكتروني**: استخدم بريدك الطلابي إن أمكن

   - **Password**: Choose a strong password
   - **كلمة المرور**: اختر كلمة مرور قوية

4. Solve the puzzle to verify you're human
   حل اللغز للتحقق من أنك إنسان

5. Click **"Create account"**
   انقر **"Create account"**

6. Verify your email:
   تحقق من بريدك الإلكتروني:

   - Check your email inbox
     تحقق من صندوق بريدك

   - Click the verification link from GitHub
     انقر رابط التحقق من GitHub

7. Complete the setup questions (you can skip most of them)
   أكمل أسئلة الإعداد (يمكنك تخطي معظمها)

📸 **Screenshot locations:**
- GitHub signup page
- Email verification screen

### GitHub Student Developer Pack (Optional)
### حزمة مطور الطلاب من GitHub (اختياري)

As a student, you can get free access to premium tools:
كطالب، يمكنك الحصول على وصول مجاني لأدوات متميزة:

1. Visit:
   قم بزيارة:

   🔗 [https://education.github.com/pack](https://education.github.com/pack)

2. Click **"Sign up for Student Developer Pack"**
   انقر **"Sign up for Student Developer Pack"**

3. Verify your student status with your university email or ID
   تحقق من حالتك كطالب ببريدك الجامعي أو الهوية

---

## Part 5: Test Git in VS Code
## الجزء 5: اختبار Git في VS Code

Let's verify Git works with VS Code:
دعنا نتحقق من أن Git يعمل مع VS Code:

1. Open VS Code
   افتح VS Code

2. Open the integrated terminal:
   افتح الطرفية المدمجة:

   - View → Terminal (or Ctrl/⌘ + `)
   - View → Terminal (أو Ctrl/⌘ + `)

3. Type:
   اكتب:

   ```bash
   git --version
   ```

4. You should see the Git version
   يجب أن ترى إصدار Git

5. Check the Source Control panel:
   تحقق من لوحة التحكم بالمصدر:

   - Click the branch icon 🌿 in the Activity Bar (left side)
     انقر أيقونة الفرع 🌿 في شريط النشاط (الجانب الأيسر)

   - You should see "Source Control" with no errors
     يجب أن ترى "Source Control" بدون أخطاء

---

## Common Git Commands (Reference)
## أوامر Git الشائعة (مرجع)

Here are the Git commands you'll use most in this course:
هنا أوامر Git التي ستستخدمها أكثر في هذا المقرر:

| Command | What it does | Arabic |
|---------|--------------|--------|
| `git clone [url]` | Download a repository | تحميل مستودع |
| `git pull` | Get latest changes | الحصول على آخر التغييرات |
| `git status` | Check what's changed | التحقق من التغييرات |
| `git add .` | Stage all changes | تحضير جميع التغييرات |
| `git commit -m "message"` | Save changes | حفظ التغييرات |
| `git push` | Upload changes | رفع التغييرات |
| `git log` | View history | عرض التاريخ |

Don't worry about memorizing these now - we'll learn them as we use them!
لا تقلق بشأن حفظ هذه الآن - سنتعلمها أثناء استخدامها!

---

## Troubleshooting
## استكشاف الأخطاء وإصلاحها

### ❌ "git is not recognized" (Windows)
### ❌ "git is not recognized" (ويندوز)

1. Restart your computer first
   أعد تشغيل الكمبيوتر أولاً

2. If still not working, reinstall Git and make sure to select "Git from the command line"
   إذا لم يعمل، أعد تثبيت Git وتأكد من اختيار "Git from the command line"

### ❌ "xcrun: error" (Mac)
### ❌ "xcrun: error" (ماك)

Install Xcode Command Line Tools:
ثبت أدوات سطر أوامر Xcode:

```bash
xcode-select --install
```

### ❌ "Permission denied" errors
### ❌ أخطاء "Permission denied"

- Use `sudo` before the command (Mac/Linux)
  استخدم `sudo` قبل الأمر (ماك/لينكس)

- Run terminal as Administrator (Windows)
  شغل الطرفية كمسؤول (ويندوز)

### ❌ Can't remember if Git is configured
### ❌ لا تتذكر إن كان Git مُعداً

Check your configuration:
تحقق من إعدادك:

```bash
git config --global user.name
git config --global user.email
```

---

## Next Steps
## الخطوات التالية

Excellent! Git is now installed and configured. Continue with:
ممتاز! Git مثبت ومُعد الآن. تابع مع:

1. **Set up Virtual Environment** - [04-venv-setup.md](04-venv-setup.md)
   **إعداد البيئة الافتراضية** - [04-venv-setup.md](04-venv-setup.md)

2. **Install Python Extension for VS Code** - [05-python-extension-vscode.md](05-python-extension-vscode.md)
   **تثبيت إضافة Python لـ VS Code** - [05-python-extension-vscode.md](05-python-extension-vscode.md)

3. **Clone the Course Repository** - [06-github-repo-cloning.md](06-github-repo-cloning.md)
   **نسخ مستودع المقرر** - [06-github-repo-cloning.md](06-github-repo-cloning.md)

---

## Tips for Success
## نصائح للنجاح

- 📝 **Practice Git commands** - The more you use them, the easier they become
- 📝 **تدرب على أوامر Git** - كلما استخدمتها أكثر، أصبحت أسهل

- 🔄 **Don't fear mistakes** - Git lets you undo almost anything
- 🔄 **لا تخف من الأخطاء** - Git يسمح لك بالتراجع عن أي شيء تقريباً

- 📚 **Focus on basics first** - You only need 6-7 commands for this course
- 📚 **ركز على الأساسيات أولاً** - تحتاج فقط 6-7 أوامر لهذا المقرر

- 🤝 **Ask for help** - Git can be confusing at first, that's normal!
- 🤝 **اطلب المساعدة** - Git قد يكون محيراً في البداية، هذا طبيعي!

---

*Last Updated: October 2025*
*آخر تحديث: أكتوبر 2025*