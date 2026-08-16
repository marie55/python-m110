# Chapter 1 Lecture Notes: Algorithms, Flowcharts & Pseudocodes
# ملاحظات محاضرة الفصل 1: الخوارزميات، المخططات الانسيابية والشفرة الزائفة

**Topic**: Introduction to Algorithms and Algorithm Design
**Official Slides**: [Meeting1-Algorithms-s.pdf](../../slides-official/chapter-01-algorithms/Meeting1-Algorithms-s.pdf)

**الموضوع**: مقدمة في الخوارزميات وتصميم الخوارزميات
**الشرائح الرسمية**: [Meeting1-Algorithms-s.pdf](../../slides-official/chapter-01-algorithms/Meeting1-Algorithms-s.pdf)

---

## 📋 Table of Contents
## 📋 جدول المحتويات

1. [What is an Algorithm?](#1-what-is-an-algorithm)
2. [Characteristics of Good Algorithms](#2-characteristics-of-good-algorithms)
3. [Algorithm Design Tools](#3-algorithm-design-tools)
4. [The Three Basic Structures](#4-the-three-basic-structures)
5. [Flowchart Symbols](#5-flowchart-symbols)
6. [Pseudocode Conventions](#6-pseudocode-conventions)
7. [From Algorithm to Python Code](#7-from-algorithm-to-python-code)
8. [Real-World Examples](#8-real-world-examples)
9. [Common Mistakes](#9-common-mistakes)
10. [Practice Problems](#10-practice-problems)

---

## 1. What is an Algorithm?
## 1. ما هي الخوارزمية؟

### Definition / التعريف

An **algorithm** is an **ordered set of unambiguous steps** that describes a process to solve a problem.

**الخوارزمية** هي **مجموعة مرتبة من الخطوات الواضحة** التي تصف عملية لحل مشكلة.

### Etymology / أصل الكلمة

The word "algorithm" comes from the name of the Persian mathematician **Al-Khwarizmi** (محمد بن موسى الخوارزمي), who lived in the 9th century. He is considered the father of algebra!

كلمة "algorithm" تأتي من اسم العالم الرياضي الفارسي **الخوارزمي** (محمد بن موسى الخوارزمي)، الذي عاش في القرن التاسع. يُعتبر أبو الجبر!

### Real-Life Algorithms / خوارزميات من الحياة الواقعية

Before we dive into programming, let's recognize that we use algorithms every day:

قبل أن نتعمق في البرمجة، لنتعرف على أننا نستخدم الخوارزميات كل يوم:

#### Example 1: Making Coffee ☕
#### مثال 1: صنع القهوة ☕

```
1. Boil water
2. Put coffee grounds in filter
3. Pour hot water over coffee
4. Wait for brewing
5. Pour coffee into cup
6. Add sugar/milk (optional)
7. Drink and enjoy!
```

**This is an algorithm!** It's a clear, step-by-step process to solve a problem (making coffee).

**هذه خوارزمية!** إنها عملية واضحة خطوة بخطوة لحل مشكلة (صنع القهوة).

#### Example 2: Getting to University 🚗
#### مثال 2: الوصول إلى الجامعة 🚗

```
1. Wake up
2. Get dressed
3. Eat breakfast
4. Check traffic app
5. IF traffic is heavy THEN
      Take alternative route
   ELSE
      Take regular route
6. Drive to university
7. Park car
8. Enter building
```

**Notice the IF-ELSE?** This is a **decision structure** in our algorithm!

**لاحظت IF-ELSE؟** هذا **هيكل قرار** في خوارزميتنا!

#### Example 3: Studying for Exam 📚
#### مثال 3: الدراسة للامتحان 📚

```
1. Open textbook to chapter 1
2. Read section
3. Take notes
4. Do practice problems
5. IF understand topic THEN
      Move to next section
   ELSE
      Review section again
6. REPEAT steps 2-5 UNTIL all chapters covered
7. Take practice exam
```

**This has both decision (IF-ELSE) and repetition (REPEAT UNTIL)!**

**هذا يحتوي على كل من القرار (IF-ELSE) والتكرار (REPEAT UNTIL)!**

---

## 2. Characteristics of Good Algorithms
## 2. خصائص الخوارزميات الجيدة

A good algorithm must have these six characteristics:

يجب أن تحتوي الخوارزمية الجيدة على هذه الخصائص الست:

### 1. Unambiguous (واضحة)
**Each step has exactly ONE meaning**

Every instruction must be crystal clear, with no room for interpretation.

كل تعليمة يجب أن تكون واضحة تمامًا، بدون مجال للتفسير.

❌ **Bad**: "Add some sugar"  (How much is "some"?)
✅ **Good**: "Add 2 teaspoons of sugar"

❌ **سيئ**: "أضف بعض السكر"  (كم هو "بعض"؟)
✅ **جيد**: "أضف ملعقتين صغيرتين من السكر"

### 2. Well-Defined Input (إدخال محدد جيدًا)
**0 or more inputs, all clearly specified**

The algorithm must specify what inputs it needs and in what format.

يجب أن تحدد الخوارزمية ما تحتاجه من مدخلات وبأي صيغة.

Example: "Input: Two numbers (length and width) as positive real numbers"

مثال: "الإدخال: رقمان (الطول والعرض) كأرقام حقيقية موجبة"

### 3. Well-Defined Output (إخراج محدد جيدًا)
**At least 1 output that matches the desired result**

The algorithm must produce a result that solves the problem.

يجب أن تنتج الخوارزمية نتيجة تحل المشكلة.

Example: "Output: The area of the rectangle"

مثال: "الإخراج: مساحة المستطيل"

### 4. Finiteness (محدودة)
**Must terminate after a finite number of steps**

An algorithm cannot run forever. It must eventually end.

لا يمكن أن تعمل الخوارزمية إلى الأبد. يجب أن تنتهي في النهاية.

❌ **Bad**: 
```
WHILE True DO
    Print "Hello"
END WHILE
```
This runs forever! / هذا يعمل إلى الأبد!

✅ **Good**:
```
FOR i FROM 1 TO 10 DO
    Print "Hello"
END FOR
```
This stops after 10 times. / هذا يتوقف بعد 10 مرات.

### 5. Feasibility (قابلة للتنفيذ)
**Can be executed with available resources**

The steps must be practical and doable.

يجب أن تكون الخطوات عملية وقابلة للتنفيذ.

❌ **Bad**: "Calculate the exact value of π to infinite decimal places"
✅ **Good**: "Calculate π to 5 decimal places"

❌ **سيئ**: "احسب القيمة الدقيقة لـ π إلى أماكن عشرية لا نهائية"
✅ **جيد**: "احسب π إلى 5 أماكن عشرية"

### 6. Language Independent (مستقلة عن اللغة)
**Not tied to any specific programming language**

An algorithm should work regardless of which programming language you use.

يجب أن تعمل الخوارزمية بغض النظر عن لغة البرمجة التي تستخدمها.

The algorithm "add two numbers" works in Python, Java, C++, JavaScript, etc.

الخوارزمية "اجمع رقمين" تعمل في بايثون، جافا، C++، جافا سكريبت، إلخ.

---

## 3. Algorithm Design Tools
## 3. أدوات تصميم الخوارزميات

We use two main tools to design algorithms **before writing code**:

نستخدم أداتين رئيسيتين لتصميم الخوارزميات **قبل كتابة الكود**:

### 3.1 Flowcharts (المخططات الانسيابية)

**Visual representation** of an algorithm using standard shapes and arrows.

**تمثيل مرئي** للخوارزمية باستخدام أشكال وأسهم معيارية.

**Advantages:**
- ✅ Easy to understand (visual)
- ✅ Shows flow of control clearly
- ✅ Good for presentations
- ✅ Language-independent

**المزايا:**
- ✅ سهل الفهم (مرئي)
- ✅ يظهر تدفق التحكم بوضوح
- ✅ جيد للعروض التقديمية
- ✅ مستقل عن اللغة

**Disadvantages:**
- ❌ Takes time to draw
- ❌ Hard to modify
- ❌ Not suitable for complex algorithms

**العيوب:**
- ❌ يستغرق وقتًا للرسم
- ❌ صعب التعديل
- ❌ غير مناسب للخوارزميات المعقدة

### 3.2 Pseudocode (الشفرة الزائفة)

**Text-based description** of an algorithm using English-like statements.

**وصف نصي** للخوارزمية باستخدام جمل شبيهة بالإنجليزية.

**Advantages:**
- ✅ Quick to write
- ✅ Easy to modify
- ✅ Good for complex algorithms
- ✅ Closer to actual code

**المزايا:**
- ✅ سريع الكتابة
- ✅ سهل التعديل
- ✅ جيد للخوارزميات المعقدة
- ✅ أقرب إلى الكود الفعلي

**Disadvantages:**
- ❌ Less visual
- ❌ May not be clear to non-programmers

**العيوب:**
- ❌ أقل بصرية
- ❌ قد لا يكون واضحًا لغير المبرمجين

### Which to Use?
### أيهما تستخدم؟

**Use flowcharts when:**
- Teaching beginners
- Showing overall structure
- Presenting to non-technical audience

**استخدم المخططات الانسيابية عندما:**
- تعلم المبتدئين
- إظهار الهيكل العام
- تقديم لجمهور غير تقني

**Use pseudocode when:**
- Planning actual code
- Working on complex algorithms
- Collaborating with programmers

**استخدم الشفرة الزائفة عندما:**
- تخطط للكود الفعلي
- تعمل على خوارزميات معقدة
- تتعاون مع المبرمجين

---

## 4. The Three Basic Structures
## 4. الهياكل الأساسية الثلاثة

**Every algorithm can be built using these three structures!**

**يمكن بناء كل خوارزمية باستخدام هذه الهياكل الثلاثة!**

### Structure 1: SEQUENCE (التسلسل)

**Execute steps one after another in order**

**تنفيذ الخطوات واحدة تلو الأخرى بالترتيب**

```
Step 1
Step 2
Step 3
...
```

**Example: Calculate Average of 3 Numbers**
```
INPUT num1
INPUT num2
INPUT num3
sum = num1 + num2 + num3
average = sum / 3
OUTPUT average
```

**Python Code:**
```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
sum_total = num1 + num2 + num3
average = sum_total / 3
print(f"Average: {average}")
```

---

### Structure 2: DECISION (القرار)

**Choose between alternatives based on a condition**

**الاختيار بين البدائل بناءً على شرط**

```
IF condition THEN
    Action A
ELSE
    Action B
END IF
```

**Example: Check if Number is Even or Odd**
```
INPUT number
IF number MOD 2 = 0 THEN
    OUTPUT "Even"
ELSE
    OUTPUT "Odd"
END IF
```

**Python Code:**
```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Multiple Conditions (IF-ELIF-ELSE):**
```
IF grade >= 90 THEN
    OUTPUT "A"
ELSE IF grade >= 80 THEN
    OUTPUT "B"
ELSE IF grade >= 70 THEN
    OUTPUT "C"
ELSE
    OUTPUT "F"
END IF
```

---

### Structure 3: REPETITION (التكرار)

**Repeat steps while a condition is true**

**تكرار الخطوات طالما الشرط صحيح**

**Two types:**
1. **Count-controlled** (عدد محدد من المرات)
2. **Condition-controlled** (حتى يتحقق شرط)

#### Type A: Count-Controlled (FOR loop)

**Repeat a specific number of times**

**تكرار عدد محدد من المرات**

```
FOR i FROM 1 TO 10 DO
    Print i
END FOR
```

**Python Code:**
```python
for i in range(1, 11):  # 1 to 10 inclusive
    print(i)
```

#### Type B: Condition-Controlled (WHILE loop)

**Repeat as long as condition is true**

**تكرار طالما الشرط صحيح**

```
i = 1
WHILE i <= 10 DO
    Print i
    i = i + 1
END WHILE
```

**Python Code:**
```python
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

---

## 5. Flowchart Symbols
## 5. رموز المخطط الانسيابي

### Standard Flowchart Shapes
### الأشكال المعيارية للمخطط الانسيابي

```
┌────────────────────────────────────────────────────────┐
│ Symbol     │ Name               │ Purpose             │
├────────────────────────────────────────────────────────┤
│  ( )       │ Oval / بيضاوي      │ Start/End           │
│  [ ]       │ Rectangle/مستطيل   │ Process/معالجة      │
│  < >       │ Diamond / معين     │ Decision /قرار      │
│  / /       │ Parallelogram      │ Input/Output        │
│  ────>     │ Arrow / سهم        │ Flow direction      │
│  ⭘         │ Circle / دائرة     │ Connector           │
└────────────────────────────────────────────────────────┘
```

### Example Flowchart: Check if Number is Positive

```
    ┌──────────────┐
    │    START     │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ INPUT number │  ← Parallelogram (Input)
    └──────┬───────┘
           │
           ▼
        ╱     ╲
      ╱ number ╲       ← Diamond (Decision)
     ╱    > 0?  ╲
    ╱___________╲
    │           │
  YES│           │NO
    │           │
    ▼           ▼
┌────────┐  ┌────────┐
│"Positive"  │"Not    │  ← Rectangles (Process/Output)
│        │  │Positive"
└───┬────┘  └───┬────┘
    │           │
    └─────┬─────┘
          │
          ▼
    ┌──────────┐
    │   END    │
    └──────────┘
```

---

## 6. Pseudocode Conventions
## 6. اصطلاحات الشفرة الزائفة

### Common Keywords / الكلمات المفتاحية الشائعة

```
┌─────────────────────────────────────────────────────┐
│ Pseudocode         │ Meaning / المعنى              │
├─────────────────────────────────────────────────────┤
│ START / END        │ Beginning / End of algorithm  │
│ INPUT              │ Get data from user            │
│ OUTPUT             │ Display result                │
│ SET / =            │ Assign value                  │
│ IF / THEN / ELSE   │ Conditional                   │
│ WHILE / DO         │ Loop with condition           │
│ FOR / TO / DO      │ Loop with counter             │
│ REPEAT / UNTIL     │ Loop (condition at end)       │
│ AND / OR / NOT     │ Logical operators             │
│ MOD                │ Modulus (remainder)           │
└─────────────────────────────────────────────────────┘
```

### Pseudocode Example: Sum of N Numbers

```
START
    INPUT n
    sum = 0
    i = 1
    WHILE i <= n DO
        INPUT number
        sum = sum + number
        i = i + 1
    END WHILE
    OUTPUT sum
END
```

**Corresponding Python Code:**
```python
n = int(input("How many numbers? "))
sum_total = 0
i = 1

while i <= n:
    number = float(input(f"Enter number {i}: "))
    sum_total = sum_total + number
    i = i + 1

print(f"Sum: {sum_total}")
```

---

## 7. From Algorithm to Python Code
## 7. من الخوارزمية إلى كود بايثون

### Translation Guide / دليل الترجمة

```
┌────────────────────────────────────────────────────────┐
│ Algorithm Notation │ Python Code                      │
├────────────────────────────────────────────────────────┤
│ INPUT x            │ x = input() or float(input())    │
│ OUTPUT x           │ print(x)                         │
│ x = 5              │ x = 5                            │
│ x = x + 1          │ x = x + 1                        │
│ IF x > 0 THEN      │ if x > 0:                        │
│ ELSE               │ else:                            │
│ WHILE x < 10 DO    │ while x < 10:                    │
│ FOR i FROM 1 TO 10 │ for i in range(1, 11):           │
│ x MOD 2            │ x % 2                            │
│ x^2                │ x ** 2                           │
│ AND                │ and                              │
│ OR                 │ or                               │
│ NOT                │ not                              │
└────────────────────────────────────────────────────────┘
```

### Complete Example: Grade Calculator

**Pseudocode:**
```
START
    sum = 0
    count = 0
    INPUT grade
    WHILE grade != -1 DO
        sum = sum + grade
        count = count + 1
        INPUT grade
    END WHILE
    
    IF count > 0 THEN
        average = sum / count
        IF average >= 50 THEN
            OUTPUT "Pass"
        ELSE
            OUTPUT "Fail"
        END IF
    ELSE
        OUTPUT "No grades entered"
    END IF
END
```

**Python Code:**
```python
# Grade Calculator with Sentinel Loop
# حاسبة الدرجات مع حلقة حارس

sum_grades = 0
count = 0

grade = float(input("Enter grade (-1 to stop): "))

while grade != -1:
    sum_grades = sum_grades + grade
    count = count + 1
    grade = float(input("Enter grade (-1 to stop): "))

if count > 0:
    average = sum_grades / count
    print(f"Average: {average:.2f}")
    
    if average >= 50:
        print("Result: PASS ✓")
    else:
        print("Result: FAIL ✗")
else:
    print("No grades entered")
```

---

## 8. Real-World Examples
## 8. أمثلة من العالم الواقعي

### Example 1: Login System

**Algorithm:**
```
START
    attempts = 0
    WHILE attempts < 3 DO
        INPUT username
        INPUT password
        IF username = "admin" AND password = "1234" THEN
            OUTPUT "Login successful"
            EXIT
        ELSE
            OUTPUT "Invalid credentials"
            attempts = attempts + 1
        END IF
    END WHILE
    OUTPUT "Account locked"
END
```

### Example 2: Shopping Cart Total

**Algorithm:**
```
START
    total = 0
    INPUT "More items? (yes/no)"
    WHILE answer = "yes" DO
        INPUT item_price
        total = total + item_price
        INPUT "More items? (yes/no)"
    END WHILE
    
    tax = total * 0.16  # 16% tax in Jordan
    final_total = total + tax
    OUTPUT "Subtotal:", total
    OUTPUT "Tax:", tax
    OUTPUT "Total:", final_total
END
```

### Example 3: Find Largest Number

**Algorithm:**
```
START
    INPUT first_number
    largest = first_number
    
    FOR i FROM 2 TO 10 DO
        INPUT number
        IF number > largest THEN
            largest = number
        END IF
    END FOR
    
    OUTPUT "Largest number:", largest
END
```

---

## 9. Common Mistakes
## 9. الأخطاء الشائعة

### Mistake 1: Infinite Loop (حلقة لا نهائية)

❌ **Bad:**
```python
i = 1
while i <= 10:
    print(i)
    # Forgot to increment i!
```
This runs forever because `i` never changes!

✅ **Correct:**
```python
i = 1
while i <= 10:
    print(i)
    i = i + 1  # Don't forget this!
```

### Mistake 2: Off-by-One Error

❌ **Bad:**
```python
for i in range(1, 10):  # This goes from 1 to 9, NOT 1 to 10!
    print(i)
```

✅ **Correct:**
```python
for i in range(1, 11):  # This goes from 1 to 10
    print(i)
```

### Mistake 3: Wrong Order of Operations

❌ **Bad:**
```python
average = sum / count
count = count + 1  # Too late! Already calculated wrong average
```

✅ **Correct:**
```python
count = count + 1
average = sum / count  # Now count is correct
```

### Mistake 4: Forgetting Sentinel Check

❌ **Bad:**
```python
while grade != -1:
    sum_grades = sum_grades + grade  # Adds -1 to sum!
    grade = float(input("Enter grade: "))
```

✅ **Correct:**
```python
grade = float(input("Enter grade: "))  # Get first grade BEFORE loop
while grade != -1:
    sum_grades = sum_grades + grade
    grade = float(input("Enter grade: "))
```

---

## 10. Practice Problems
## 10. مسائل للممارسة

### Problem 1: Factorial Calculator
Write pseudocode and Python code to calculate the factorial of a number.
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

### Problem 2: Password Validator
Write an algorithm that checks if a password is valid:
- At least 8 characters
- Contains at least one digit
- Contains at least one uppercase letter

### Problem 3: Number Guessing Game
Create an algorithm where:
1. Computer picks a random number (1-100)
2. User guesses
3. Computer says "higher" or "lower"
4. Continue until user guesses correctly
5. Display number of attempts

---

## Key Takeaways
## النقاط الرئيسية

✅ **Algorithms** are step-by-step solutions to problems
✅ Good algorithms are **unambiguous**, **finite**, and **feasible**
✅ **Flowcharts** visualize algorithms (good for beginners)
✅ **Pseudocode** describes algorithms in text (faster to write)
✅ **Three structures**: Sequence, Decision, Repetition
✅ **Think first, code later** - design before implementing
✅ Every algorithm can be translated to Python (or any language)

✅ **الخوارزميات** هي حلول خطوة بخطوة للمشاكل
✅ الخوارزميات الجيدة **واضحة**، **محدودة**، و**قابلة للتنفيذ**
✅ **المخططات الانسيابية** تصور الخوارزميات (جيدة للمبتدئين)
✅ **الشفرة الزائفة** تصف الخوارزميات نصياً (أسرع في الكتابة)
✅ **ثلاثة هياكل**: التسلسل، القرار، التكرار
✅ **فكر أولاً، ابرمج لاحقاً** - صمم قبل التنفيذ
✅ يمكن ترجمة كل خوارزمية إلى بايثون (أو أي لغة)

---

## Resources for Further Learning
## موارد للتعلم الإضافي

- **Code Examples**: [../../code-examples/chapter-01-algorithms/](../../code-examples/chapter-01-algorithms/)
- **Practice Exercises**: [../../exercises/chapter-01-algorithms/](../../exercises/chapter-01-algorithms/)
- **Additional Resources**: [../../lectures/chapter-01-algorithms/additional-resources.md](additional-resources.md)

---

## Next Chapter Preview
## معاينة الفصل القادم

**Chapter 2: Fundamentals of Python Programming**
- Variables and data types
- Input and output
- Operators
- String manipulation
- Type conversion

Get ready to start coding! 🚀

---

**Remember**: 
- Complete exercises in [exercises/chapter-01-algorithms/](../../exercises/chapter-01-algorithms/)
- Use Dr. Laila (`/laila`) if you need help!

**تذكر**:
- أكمل التمارين في [exercises/chapter-01-algorithms/](../../exercises/chapter-01-algorithms/)
- استخدم د. ليلى (`/laila`) إذا كنت بحاجة للمساعدة!

---

**End of Lecture Notes**
**نهاية ملاحظات المحاضرة**
