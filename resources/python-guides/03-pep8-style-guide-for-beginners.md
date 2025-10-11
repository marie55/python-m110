# PEP 8 Style Guide for Beginners
# دليل أسلوب PEP 8 للمبتدئين

## Overview
## نظرة عامة

PEP 8 is Python's official style guide—think of it as the "grammar rules" for writing clean, professional Python code. Following PEP 8 makes your code easier to read, share, and maintain. It's what separates beginner code from professional code!

PEP 8 هو دليل الأسلوب الرسمي لبايثون—فكر فيه كـ"قواعد نحوية" لكتابة كود بايثون نظيف واحترافي. اتباع PEP 8 يجعل كودك أسهل في القراءة والمشاركة والصيانة. إنه ما يفصل كود المبتدئين عن الكود الاحترافي!

---

## What is PEP 8?
## ما هو PEP 8؟

**PEP** = Python Enhancement Proposal
**PEP** = مقترح تحسين بايثون

**PEP 8** = Style Guide for Python Code (written by Python's creator!)
**PEP 8** = دليل الأسلوب لكود بايثون (كتبه منشئ بايثون!)

Think of it like this: If Python is a language, PEP 8 is the "proper writing" guide.
فكر في الأمر هكذا: إذا كان بايثون لغة، فإن PEP 8 هو دليل "الكتابة الصحيحة".

---

## Why Code Style Matters
## لماذا أسلوب الكود مهم

### 1. Readability
### 1. القابلية للقراءة
"Code is read much more often than it is written." - Guido van Rossum (Python's creator)
"الكود يُقرأ أكثر بكثير مما يُكتب." - جويدو فان روسوم (منشئ بايثون)

### 2. Teamwork
### 2. العمل الجماعي
When everyone follows the same style, working together is easier.
عندما يتبع الجميع نفس الأسلوب، يصبح العمل معاً أسهل.

### 3. Professionalism
### 3. الاحترافية
Clean code shows you care about quality. Employers notice this!
الكود النظيف يُظهر اهتمامك بالجودة. أصحاب العمل يلاحظون هذا!

### 4. Fewer Bugs
### 4. أخطاء أقل
Consistent style helps you spot mistakes faster.
الأسلوب المتسق يساعدك على اكتشاف الأخطاء بشكل أسرع.

---

## Essential PEP 8 Rules for This Course
## قواعد PEP 8 الأساسية لهذا المقرر

### 1. Naming Conventions
### 1. قواعد التسمية

Different types of names have different styles:
أنواع مختلفة من الأسماء لها أساليب مختلفة:

#### Variables and Functions: `snake_case`
#### المتغيرات والدوال: `snake_case`
```python
# ✅ Good
student_name = "Ahmed"
total_score = 95
def calculate_average():
    pass

# ❌ Bad
studentName = "Ahmed"      # This is camelCase (wrong!)
TotalScore = 95            # This is PascalCase (wrong!)
def CalculateAverage():    # Wrong for functions!
    pass
```

#### Constants: `UPPER_SNAKE_CASE`
#### الثوابت: `UPPER_SNAKE_CASE`
```python
# ✅ Good
MAX_STUDENTS = 30
PI_VALUE = 3.14159
TAX_RATE = 0.15

# ❌ Bad
max_students = 30    # Looks like a variable
MaxStudents = 30     # Wrong style
```

#### Class Names: `PascalCase` (Week 10)
#### أسماء الفئات: `PascalCase` (الأسبوع 10)
```python
# ✅ Good
class Student:
    pass

class BankAccount:
    pass

# ❌ Bad
class student:        # Should start with capital
    pass

class bank_account:   # Should be PascalCase
    pass
```

#### Quick Reference Table:
#### جدول مرجعي سريع:

| Type | Style | Example |
|------|-------|---------|
| Variable | snake_case | `user_age` |
| Function | snake_case | `get_input()` |
| Constant | UPPER_SNAKE | `MAX_SIZE` |
| Class | PascalCase | `StudentGrade` |

---

### 2. Indentation
### 2. المسافة البادئة

**Rule:** Use 4 spaces (not tabs!)
**القاعدة:** استخدم 4 مسافات (ليس تبويبات!)

```python
# ✅ Good (4 spaces)
if score >= 90:
    print("Excellent!")
    if has_bonus:
        score += 5

# ❌ Bad (2 spaces)
if score >= 90:
  print("Excellent!")

# ❌ Bad (tabs - looks ok but causes errors!)
if score >= 90:
	print("Excellent!")  # This is a tab
```

**VS Code Tip:** Set VS Code to show whitespace characters:
**نصيحة VS Code:** اضبط VS Code لإظهار أحرف المسافات:
- View → Render Whitespace
- عرض ← إظهار المسافات البيضاء

---

### 3. Whitespace Around Operators
### 3. المسافات حول العمليات

Put spaces around operators for readability:
ضع مسافات حول العمليات للقراءة:

```python
# ✅ Good
x = 10
y = x * 2 + 1
result = (a + b) * (c - d)
is_valid = age >= 18 and has_id

# ❌ Bad (no spaces - hard to read)
x=10
y=x*2+1
result=(a+b)*(c-d)
is_valid=age>=18and has_id
```

**Exception:** No spaces inside parentheses:
**استثناء:** لا مسافات داخل الأقواس:

```python
# ✅ Good
print(x, y)
calculate(2 + 3)

# ❌ Bad
print( x, y )
calculate( 2 + 3 )
```

---

### 4. Whitespace After Commas
### 4. المسافات بعد الفواصل

Always add space after commas, not before:
أضف مسافة دائماً بعد الفواصل، ليس قبلها:

```python
# ✅ Good
numbers = [1, 2, 3, 4, 5]
print(x, y, z)
def greet(name, age, city):
    pass

# ❌ Bad
numbers = [1,2,3,4,5]      # No spaces
numbers = [1 , 2 , 3]      # Space before comma
print(x,y,z)               # No spaces
```

---

### 5. Comments
### 5. التعليقات

Write helpful comments that explain WHY, not WHAT:
اكتب تعليقات مفيدة تشرح لماذا، ليس ماذا:

```python
# ✅ Good comments
# Check if student passed (60% is passing grade at AOU)
if score >= 60:
    status = "Pass"

# Use binary search for efficiency with large datasets
index = binary_search(data, target)

# ❌ Bad comments
# Set x to 10
x = 10  # This is obvious!

# Loop through list
for item in items:  # We can see it's a loop!
    process(item)
```

**Comment Style Rules:**
**قواعد أسلوب التعليقات:**

```python
# ✅ Good
# This is a comment with space after #
# Multiple lines each start with #
# Each sentence starts with capital

# ❌ Bad
#This has no space after hash
# this doesn't start with capital
```

---

### 6. Line Length
### 6. طول السطر

Keep lines under 79 characters (so code fits on screen):
احتفظ بالأسطر تحت 79 حرفاً (ليناسب الكود الشاشة):

```python
# ❌ Bad (too long)
student_information = {"name": "Ahmed", "age": 20, "grades": [85, 90, 88], "address": "123 Main Street, Amman, Jordan"}

# ✅ Good (split into multiple lines)
student_information = {
    "name": "Ahmed",
    "age": 20,
    "grades": [85, 90, 88],
    "address": "123 Main Street, Amman, Jordan"
}

# ✅ Good (break long conditions)
if (temperature > 30 and humidity > 80
    and weather_condition == "sunny"):
    print("It's very hot!")
```

---

### 7. Blank Lines
### 7. الأسطر الفارغة

Use blank lines to organize code into logical sections:
استخدم الأسطر الفارغة لتنظيم الكود في أقسام منطقية:

```python
# ✅ Good (organized with blank lines)
import math
import random


def calculate_circle_area(radius):
    """Calculate area of a circle."""
    return math.pi * radius ** 2


def calculate_square_area(side):
    """Calculate area of a square."""
    return side ** 2


# Main program
radius = 5
area = calculate_circle_area(radius)
print(f"Circle area: {area}")

# ❌ Bad (no organization)
import math
import random
def calculate_circle_area(radius):
    """Calculate area of a circle."""
    return math.pi * radius ** 2
def calculate_square_area(side):
    """Calculate area of a square."""
    return side ** 2
radius = 5
area = calculate_circle_area(radius)
print(f"Circle area: {area}")
```

**Rules:**
**القواعد:**
- 2 blank lines between functions
- سطران فارغان بين الدوال
- 2 blank lines after imports
- سطران فارغان بعد الاستيرادات
- 1 blank line between logical sections
- سطر فارغ واحد بين الأقسام المنطقية

---

## Good vs Bad Examples: Side-by-Side
## أمثلة جيدة مقابل سيئة: جنباً إلى جنب

### Example 1: Complete Program
### مثال 1: برنامج كامل

#### ❌ Bad Style:
```python
#calculate student grades
def calc(g):
  total=sum(g)
  avg=total/len(g)
  if avg>=90:grade='A'
  elif avg>=80:grade='B'
  elif avg>=70:grade='C'
  else:grade='F'
  return grade
StudentGrades=[85,90,78,92,88]
result=calc(StudentGrades)
print("Grade:",result)
```

#### ✅ Good Style:
```python
# Calculate student grades based on average

def calculate_grade(grades):
    """Calculate letter grade based on average score."""
    total = sum(grades)
    average = total / len(grades)

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    else:
        grade = 'F'

    return grade


# Main program
student_grades = [85, 90, 78, 92, 88]
result = calculate_grade(student_grades)
print("Grade:", result)
```

**What's Better?**
**ما الأفضل؟**
- Clear function name / اسم دالة واضح
- Proper spacing / مسافات صحيحة
- Good variable names / أسماء متغيرات جيدة
- Organized with blank lines / منظم بأسطر فارغة
- Helpful comments / تعليقات مفيدة

---

### Example 2: Input Validation
### مثال 2: التحقق من المدخلات

#### ❌ Bad Style:
```python
age=int(input("age:"))
if age<0or age>120:print("invalid")
else:
  if age>=18:print("adult")
  else:print("minor")
```

#### ✅ Good Style:
```python
# Get and validate user age
age = int(input("Enter your age: "))

# Validate age range
if age < 0 or age > 120:
    print("Invalid age")
else:
    # Check if adult or minor
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")
```

---

## Automatic Formatting in VS Code
## التنسيق التلقائي في VS Code

Let VS Code help you follow PEP 8!
دع VS Code يساعدك في اتباع PEP 8!

### Install Python Extension:
### تثبيت إضافة Python:
1. Open VS Code / افتح VS Code
2. Go to Extensions (Ctrl+Shift+X) / اذهب إلى الإضافات
3. Search "Python" / ابحث عن "Python"
4. Install official Python extension / ثبّت إضافة Python الرسمية

### Enable Format on Save:
### تفعيل التنسيق عند الحفظ:
1. File → Preferences → Settings / ملف ← التفضيلات ← الإعدادات
2. Search "format on save" / ابحث عن "format on save"
3. Check the box / ضع علامة في المربع

### Use Formatter:
### استخدام المنسق:
- Right-click → Format Document / انقر بزر الماوس الأيمن ← تنسيق المستند
- Or: Shift+Alt+F / أو: Shift+Alt+F

---

## Common PEP 8 Violations to Avoid
## انتهاكات PEP 8 الشائعة التي يجب تجنبها

### 1. Multiple Statements on One Line
### 1. عبارات متعددة في سطر واحد
```python
# ❌ Bad
x = 1; y = 2; z = 3

# ✅ Good
x = 1
y = 2
z = 3
```

### 2. Unnecessary Parentheses
### 2. أقواس غير ضرورية
```python
# ❌ Bad
if (x > 5):
    pass

# ✅ Good
if x > 5:
    pass
```

### 3. Comparing to True/False
### 3. المقارنة مع True/False
```python
# ❌ Bad
if is_valid == True:
    pass

# ✅ Good
if is_valid:
    pass

# ❌ Bad
if is_valid == False:
    pass

# ✅ Good
if not is_valid:
    pass
```

### 4. Using Semicolons
### 4. استخدام الفاصلة المنقوطة
```python
# ❌ Bad (this is not C or Java!)
x = 5;
print(x);

# ✅ Good
x = 5
print(x)
```

---

## Why We Care (Industry Standards)
## لماذا نهتم (معايير الصناعة)

### Real-World Impact:
### التأثير في العالم الحقيقي:

1. **Job Interviews:** Clean code impresses interviewers
   **مقابلات العمل:** الكود النظيف يثير إعجاب المحاورين

2. **Code Reviews:** Teams review each other's code
   **مراجعات الكود:** الفرق تراجع كود بعضها البعض

3. **Open Source:** Contributing requires following style guides
   **المصدر المفتوح:** المساهمة تتطلب اتباع أدلة الأسلوب

4. **Maintenance:** You'll read your old code months later
   **الصيانة:** ستقرأ كودك القديم بعد شهور

### What Professionals Say:
### ما يقوله المحترفون:
> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." - Martin Fowler

> "أي أحمق يمكنه كتابة كود يفهمه الكمبيوتر. المبرمجون الجيدون يكتبون كوداً يفهمه البشر." - مارتن فاولر

---

## Key Takeaways
## النقاط الرئيسية

✅ **Use snake_case for variables and functions**
✅ **استخدم snake_case للمتغيرات والدوال**

✅ **Always use 4 spaces for indentation**
✅ **استخدم دائماً 4 مسافات للمسافة البادئة**

✅ **Add spaces around operators and after commas**
✅ **أضف مسافات حول العمليات وبعد الفواصل**

✅ **Keep lines under 79 characters**
✅ **احتفظ بالأسطر تحت 79 حرفاً**

✅ **Write meaningful variable names**
✅ **اكتب أسماء متغيرات ذات معنى**

✅ **Organize code with blank lines**
✅ **نظم الكود بأسطر فارغة**

✅ **Comment the WHY, not the WHAT**
✅ **علّق على السبب، ليس على ماذا**

---

## Practice Challenge
## تحدي الممارسة

Fix this code to follow PEP 8:
أصلح هذا الكود ليتبع PEP 8:

```python
# Bad style - fix it!
def calc(x,y,z):
  avg=(x+y+z)/3
  if avg>=90:g='A'
  elif avg>=80:g='B'
  else:g='F'
  return g
score1=85;score2=90;score3=88
FinalGrade=calc(score1,score2,score3)
print("Grade:",FinalGrade)
```

Try fixing it yourself, then check your solution!
حاول إصلاحه بنفسك، ثم تحقق من حلك!

---

## Additional Resources
## موارد إضافية

- [Official PEP 8 Guide](https://www.python.org/dev/peps/pep-0008/)
- [PEP 8 Checker Online](http://pep8online.com/)
- VS Code Extension: "Python" by Microsoft
- VS Code Extension: "Pylint" for automatic style checking

---

**Remember:** Good style is a habit. Start now, and it becomes natural!
**تذكر:** الأسلوب الجيد عادة. ابدأ الآن، وسيصبح طبيعياً!

**Pro Tip:** Write clean code from the start—it's harder to clean up messy code later!
**نصيحة احترافية:** اكتب كوداً نظيفاً من البداية—من الصعب تنظيف الكود الفوضوي لاحقاً!