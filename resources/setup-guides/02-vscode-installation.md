# Visual Studio Code Installation Guide
# دليل تثبيت Visual Studio Code

⏱️ **Estimated Time:** 10-15 minutes
⏱️ **الوقت المقدر:** 10-15 دقيقة

---

## Overview
## نظرة عامة

Visual Studio Code (VS Code) is a free, powerful text editor that we'll use to write Python code. It has many features that make programming easier, like syntax highlighting, auto-completion, and debugging tools. Think of it as Microsoft Word, but for code!

Visual Studio Code (VS Code) هو محرر نصوص مجاني وقوي سنستخدمه لكتابة كود بايثون. لديه العديد من الميزات التي تجعل البرمجة أسهل، مثل تلوين الكود، والإكمال التلقائي، وأدوات تصحيح الأخطاء. فكر فيه كـ Microsoft Word، ولكن للكود!

---

## Prerequisites
## المتطلبات الأساسية

Before installing VS Code, ensure you have:
قبل تثبيت VS Code، تأكد من أن لديك:

- ✅ Python already installed (see [01-python-installation.md](01-python-installation.md))
- ✅ بايثون مثبت بالفعل (انظر [01-python-installation.md](01-python-installation.md))

- ✅ Internet connection (download is about 90MB)
- ✅ اتصال بالإنترنت (التحميل حوالي 90 ميجابايت)

- ✅ About 500MB free disk space
- ✅ حوالي 500 ميجابايت مساحة فارغة على القرص

---

## Installation Steps
## خطوات التثبيت

### 🪟 For Windows Users
### 🪟 لمستخدمي ويندوز

#### Step 1: Download VS Code
#### الخطوة 1: تحميل VS Code

1. Open your web browser and visit:
   افتح متصفح الإنترنت وقم بزيارة:

   🔗 [https://code.visualstudio.com/](https://code.visualstudio.com/)

2. Click the big blue **"Download for Windows"** button
   انقر على الزر الأزرق الكبير **"Download for Windows"**

3. The installer (`VSCodeUserSetup-x64-x.xx.x.exe`) will download to your **Downloads** folder
   سيتم تحميل المثبت (`VSCodeUserSetup-x64-x.xx.x.exe`) إلى مجلد **التنزيلات**

📸 **Screenshot location:** VS Code homepage with Download button highlighted

#### Step 2: Run the Installer
#### الخطوة 2: تشغيل برنامج التثبيت

1. Navigate to your **Downloads** folder
   انتقل إلى مجلد **التنزيلات**

2. Double-click `VSCodeUserSetup-x64-x.xx.x.exe`
   انقر مرتين على `VSCodeUserSetup-x64-x.xx.x.exe`

3. If Windows asks "Do you want to allow this app...", click **"Yes"**
   إذا سأل ويندوز "Do you want to allow this app..."، انقر **"Yes"**

4. **License Agreement**: Click **"I accept the agreement"** then **"Next"**
   **اتفاقية الترخيص**: انقر **"I accept the agreement"** ثم **"Next"**

5. **Select Destination**: Keep the default location, click **"Next"**
   **اختر الوجهة**: احتفظ بالموقع الافتراضي، انقر **"Next"**

6. **Select Start Menu Folder**: Keep default, click **"Next"**
   **اختر مجلد قائمة البدء**: احتفظ بالافتراضي، انقر **"Next"**

7. **Select Additional Tasks** - CHECK these important boxes:
   **اختر المهام الإضافية** - حدد هذه المربعات المهمة:

   ✅ Create a desktop icon
   ✅ إنشاء أيقونة على سطح المكتب

   ✅ Add "Open with Code" action to Windows Explorer file context menu
   ✅ إضافة "Open with Code" إلى قائمة النقر بالزر الأيمن

   ✅ Add "Open with Code" action to Windows Explorer directory context menu
   ✅ إضافة "Open with Code" إلى قائمة المجلدات

   ✅ Register Code as an editor for supported file types
   ✅ تسجيل Code كمحرر للملفات المدعومة

   ✅ Add to PATH (this should be checked by default)
   ✅ إضافة إلى PATH (يجب أن يكون محدداً بشكل افتراضي)

8. Click **"Next"** then **"Install"**
   انقر **"Next"** ثم **"Install"**

9. Wait for installation (1-3 minutes)
   انتظر التثبيت (1-3 دقائق)

10. When complete, keep **"Launch Visual Studio Code"** checked and click **"Finish"**
    عند الانتهاء، اترك **"Launch Visual Studio Code"** محدداً وانقر **"Finish"**

📸 **Screenshot locations:**
- Additional Tasks screen with all checkboxes
- VS Code launching for the first time

---

### 🍎 For macOS Users
### 🍎 لمستخدمي ماك

#### Step 1: Download VS Code
#### الخطوة 1: تحميل VS Code

1. Visit the VS Code website:
   قم بزيارة موقع VS Code:

   🔗 [https://code.visualstudio.com/](https://code.visualstudio.com/)

2. Click **"Download for Mac"** button
   انقر على زر **"Download for Mac"**

3. Choose the right version:
   اختر الإصدار الصحيح:

   - **Apple Silicon** (M1/M2/M3 Macs) - Download the "Apple Silicon" version
   - **Apple Silicon** (M1/M2/M3 Macs) - حمل إصدار "Apple Silicon"

   - **Intel Macs** - Download the "Intel Chip" version
   - **Intel Macs** - حمل إصدار "Intel Chip"

   Not sure? Click Apple menu  → **About This Mac** to check your processor
   غير متأكد؟ انقر قائمة Apple  → **About This Mac** للتحقق من المعالج

4. The `.zip` file will download to **Downloads**
   سيتم تحميل ملف `.zip` إلى **التنزيلات**

#### Step 2: Install VS Code
#### الخطوة 2: تثبيت VS Code

1. Open **Finder** and go to **Downloads**
   افتح **Finder** واذهب إلى **التنزيلات**

2. Double-click the `VSCode-darwin-*.zip` file to extract it
   انقر مرتين على ملف `VSCode-darwin-*.zip` لفك الضغط

3. Drag **Visual Studio Code.app** to the **Applications** folder
   اسحب **Visual Studio Code.app** إلى مجلد **Applications**

4. Open VS Code:
   افتح VS Code:

   - Press **Command ⌘ + Space** to open Spotlight
     اضغط **Command ⌘ + Space** لفتح Spotlight

   - Type **"Visual Studio Code"** and press **Enter**
     اكتب **"Visual Studio Code"** واضغط **Enter**

5. If macOS says "Visual Studio Code is from an unidentified developer":
   إذا قال macOS "Visual Studio Code is from an unidentified developer":

   - Go to **System Preferences** → **Security & Privacy**
     اذهب إلى **System Preferences** → **Security & Privacy**

   - Click **"Open Anyway"**
     انقر **"Open Anyway"**

#### Step 3: Add VS Code to PATH (Mac)
#### الخطوة 3: إضافة VS Code إلى PATH (ماك)

1. Open VS Code
   افتح VS Code

2. Press **Command ⌘ + Shift + P** to open Command Palette
   اضغط **Command ⌘ + Shift + P** لفتح Command Palette

3. Type **"shell command"** and select:
   اكتب **"shell command"** واختر:

   **"Shell Command: Install 'code' command in PATH"**

4. Enter your Mac password if prompted
   أدخل كلمة مرور الماك إذا طُلب

5. You'll see "Shell command 'code' successfully installed"
   سترى "Shell command 'code' successfully installed"

---

### 🐧 For Linux Users (Ubuntu/Debian)
### 🐧 لمستخدمي لينكس (Ubuntu/Debian)

#### Option 1: Using Snap (Easiest)
#### الخيار 1: استخدام Snap (الأسهل)

1. Open Terminal (Ctrl + Alt + T)
   افتح Terminal (Ctrl + Alt + T)

2. Install VS Code with one command:
   ثبت VS Code بأمر واحد:

   ```bash
   sudo snap install code --classic
   ```

3. Enter your password when prompted
   أدخل كلمة المرور عند الطلب

4. Wait for installation (2-5 minutes)
   انتظر التثبيت (2-5 دقائق)

#### Option 2: Using .deb Package
#### الخيار 2: استخدام حزمة .deb

1. Download the `.deb` package from:
   حمل حزمة `.deb` من:

   🔗 [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)

2. Open Terminal in Downloads folder:
   افتح Terminal في مجلد التنزيلات:

   ```bash
   cd ~/Downloads
   ```

3. Install the package:
   ثبت الحزمة:

   ```bash
   sudo dpkg -i code_*.deb
   ```

4. If there are dependency issues:
   إذا كانت هناك مشاكل في التبعيات:

   ```bash
   sudo apt-get install -f
   ```

---

## First Launch and Initial Setup
## التشغيل الأول والإعداد الأولي

### Welcome Screen
### شاشة الترحيب

When you first open VS Code, you'll see the Welcome tab:
عندما تفتح VS Code لأول مرة، سترى علامة تبويب الترحيب:

1. **Choose Your Theme**: Select a color theme you like
   **اختر السمة**: اختر سمة الألوان التي تعجبك

   - **Dark themes** are easier on the eyes for long coding sessions
   - **السمات الداكنة** أسهل على العينين لجلسات البرمجة الطويلة

   - **Light themes** are good for bright environments
   - **السمات الفاتحة** جيدة للبيئات المضيئة

2. You can skip other welcome options for now
   يمكنك تخطي خيارات الترحيب الأخرى الآن

### Understanding the Interface
### فهم الواجهة

Let's explore VS Code's main areas:
دعنا نستكشف المناطق الرئيسية في VS Code:

📸 **Screenshot location:** VS Code interface with labeled areas

1. **Activity Bar** (Left side icons)
   **شريط النشاط** (الأيقونات على اليسار)

   - 📁 **Explorer**: View and manage files
   - 📁 **المستكشف**: عرض وإدارة الملفات

   - 🔍 **Search**: Find text across files
   - 🔍 **البحث**: البحث عن نص عبر الملفات

   - 🌿 **Source Control**: Git integration (we'll use later)
   - 🌿 **التحكم بالمصدر**: تكامل Git (سنستخدمه لاحقاً)

   - 🐛 **Run and Debug**: Debug your code
   - 🐛 **التشغيل والتصحيح**: تصحيح أخطاء الكود

   - 🧩 **Extensions**: Add new features
   - 🧩 **الإضافات**: إضافة ميزات جديدة

2. **Side Bar**: Shows content based on Activity Bar selection
   **الشريط الجانبي**: يعرض المحتوى بناءً على اختيار شريط النشاط

3. **Editor Area**: Where you write code
   **منطقة المحرر**: حيث تكتب الكود

4. **Panel** (Bottom): Terminal, output, problems, debug console
   **اللوحة** (الأسفل): الطرفية، المخرجات، المشاكل، وحدة التصحيح

5. **Status Bar** (Very bottom): Shows information about your file
   **شريط الحالة** (الأسفل جداً): يعرض معلومات عن ملفك

### Basic Settings
### الإعدادات الأساسية

Let's configure some helpful settings:
دعنا نضبط بعض الإعدادات المفيدة:

1. Open Settings:
   افتح الإعدادات:

   - **Windows/Linux**: File → Preferences → Settings (or Ctrl + ,)
   - **Windows/Linux**: File → Preferences → Settings (أو Ctrl + ,)

   - **Mac**: Code → Preferences → Settings (or Command ⌘ + ,)
   - **Mac**: Code → Preferences → Settings (أو Command ⌘ + ,)

2. Search and enable these settings:
   ابحث وفعّل هذه الإعدادات:

   - **"Auto Save"**: Set to "afterDelay" to save files automatically
   - **"Auto Save"**: اضبط على "afterDelay" لحفظ الملفات تلقائياً

   - **"Font Size"**: Increase to 14 or 16 for better readability
   - **"Font Size"**: زد إلى 14 أو 16 لسهولة القراءة

   - **"Word Wrap"**: Turn on to wrap long lines
   - **"Word Wrap"**: شغّل للف الأسطر الطويلة

   - **"Minimap"**: Turn off if you find it distracting
   - **"Minimap"**: أطفئ إذا وجدته مشتتاً

### Essential Keyboard Shortcuts
### اختصارات لوحة المفاتيح الأساسية

Learn these shortcuts to work faster:
تعلم هذه الاختصارات للعمل بشكل أسرع:

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Save file<br>حفظ الملف | Ctrl + S | ⌘ + S |
| Open file<br>فتح ملف | Ctrl + O | ⌘ + O |
| Find text<br>البحث عن نص | Ctrl + F | ⌘ + F |
| Replace text<br>استبدال نص | Ctrl + H | ⌘ + H |
| Open terminal<br>فتح الطرفية | Ctrl + ` | ⌘ + ` |
| Command palette<br>لوحة الأوامر | Ctrl + Shift + P | ⌘ + Shift + P |
| New file<br>ملف جديد | Ctrl + N | ⌘ + N |
| Close file<br>إغلاق ملف | Ctrl + W | ⌘ + W |

---

## Testing VS Code
## اختبار VS Code

Let's create your first file in VS Code:
دعنا ننشئ ملفك الأول في VS Code:

1. Open VS Code
   افتح VS Code

2. Create a new file: **File** → **New File** (or Ctrl/⌘ + N)
   أنشئ ملفاً جديداً: **File** → **New File** (أو Ctrl/⌘ + N)

3. Type this simple Python code:
   اكتب كود بايثون البسيط هذا:

   ```python
   # My first Python program in VS Code
   # أول برنامج بايثون لي في VS Code

   print("Hello, VS Code!")
   print("مرحباً VS Code!")
   ```

4. Save the file: **File** → **Save** (or Ctrl/⌘ + S)
   احفظ الملف: **File** → **Save** (أو Ctrl/⌘ + S)

5. Name it `hello.py` and save to your Desktop
   سمّه `hello.py` واحفظه على سطح المكتب

6. Notice how the text becomes colorful! This is **syntax highlighting**
   لاحظ كيف أصبح النص ملوناً! هذا هو **تلوين الكود**

---

## Opening the Terminal in VS Code
## فتح الطرفية في VS Code

The terminal lets you run Python code directly from VS Code:
الطرفية تسمح لك بتشغيل كود بايثون مباشرة من VS Code:

1. Open terminal:
   افتح الطرفية:

   - **Menu**: View → Terminal
   - **القائمة**: View → Terminal

   - **Keyboard**: Ctrl + ` (backtick key, usually above Tab)
   - **لوحة المفاتيح**: Ctrl + ` (مفتاح backtick، عادة فوق Tab)

2. The terminal appears at the bottom
   تظهر الطرفية في الأسفل

3. You can now run Python commands here!
   يمكنك الآن تشغيل أوامر بايثون هنا!

📸 **Screenshot location:** VS Code with terminal open at bottom

---

## Troubleshooting
## استكشاف الأخطاء وإصلاحها

### ❌ VS Code won't open (Windows)
### ❌ VS Code لا يفتح (ويندوز)

- Right-click VS Code icon → **"Run as administrator"**
  انقر بالزر الأيمن على أيقونة VS Code → **"Run as administrator"**

- Check Windows Defender isn't blocking it
  تحقق من أن Windows Defender لا يحجبه

### ❌ "code" command not found (Mac/Linux)
### ❌ أمر "code" غير موجود (ماك/لينكس)

- In VS Code: Command/Ctrl + Shift + P
  في VS Code: Command/Ctrl + Shift + P

- Type "shell command" and install it
  اكتب "shell command" وثبته

### ❌ VS Code is in wrong language
### ❌ VS Code بلغة خاطئة

1. Press Ctrl/⌘ + Shift + P
   اضغط Ctrl/⌘ + Shift + P

2. Type "Configure Display Language"
   اكتب "Configure Display Language"

3. Select your preferred language
   اختر لغتك المفضلة

### ❌ Text is too small/large
### ❌ النص صغير/كبير جداً

- **Zoom in**: Ctrl/⌘ + Plus (+)
  **تكبير**: Ctrl/⌘ + Plus (+)

- **Zoom out**: Ctrl/⌘ + Minus (-)
  **تصغير**: Ctrl/⌘ + Minus (-)

- **Reset zoom**: Ctrl/⌘ + 0
  **إعادة تعيين**: Ctrl/⌘ + 0

---

## Next Steps
## الخطوات التالية

Great job! VS Code is now installed. Continue with:
عمل رائع! تم تثبيت VS Code. تابع مع:

1. **Install Git** - [03-git-installation.md](03-git-installation.md)
   **تثبيت Git** - [03-git-installation.md](03-git-installation.md)

2. **Set up Python Extension** - [05-python-extension-vscode.md](05-python-extension-vscode.md)
   **إعداد إضافة بايثون** - [05-python-extension-vscode.md](05-python-extension-vscode.md)

3. **Clone the course repository** - [06-github-repo-cloning.md](06-github-repo-cloning.md)
   **نسخ مستودع المقرر** - [06-github-repo-cloning.md](06-github-repo-cloning.md)

---

## Useful VS Code Resources
## موارد VS Code مفيدة

- 📖 [VS Code Documentation](https://code.visualstudio.com/docs)
- 📖 [وثائق VS Code](https://code.visualstudio.com/docs)

- 🎥 [VS Code Intro Videos](https://code.visualstudio.com/docs/getstarted/introvideos)
- 🎥 [فيديوهات تعريفية لـ VS Code](https://code.visualstudio.com/docs/getstarted/introvideos)

- 🎮 [Interactive Playground](https://code.visualstudio.com/docs/editor/codebasics)
- 🎮 [ساحة تفاعلية](https://code.visualstudio.com/docs/editor/codebasics)

---

## Tips for Success
## نصائح للنجاح

- 💡 **Explore the interface** - Click around and see what each button does
- 💡 **استكشف الواجهة** - انقر حول وشاهد ما يفعله كل زر

- 💡 **Don't memorize everything** - You'll learn as you use it
- 💡 **لا تحفظ كل شيء** - ستتعلم أثناء الاستخدام

- 💡 **Use the Command Palette** - It can do almost everything (Ctrl/⌘ + Shift + P)
- 💡 **استخدم لوحة الأوامر** - يمكنها فعل كل شيء تقريباً (Ctrl/⌘ + Shift + P)

- 💡 **Customize your workspace** - Make it comfortable for you
- 💡 **خصص مساحة عملك** - اجعلها مريحة لك

---

*Last Updated: October 2025*
*آخر تحديث: أكتوبر 2025*