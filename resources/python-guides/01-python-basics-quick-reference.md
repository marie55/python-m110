# Python Basics Quick Reference (Weeks 1-4)
# مرجع سريع لأساسيات بايثون (الأسابيع 1-4)

## Variables & Data Types
## المتغيرات وأنواع البيانات

### Creating Variables | إنشاء المتغيرات
```python
name = "Ahmed"          # String | نص
age = 20               # Integer | عدد صحيح
height = 175.5         # Float | عدد عشري
is_student = True      # Boolean | منطقي
```

### Data Types | أنواع البيانات
```python
# Checking type | فحص النوع
type(name)      # <class 'str'>
type(age)       # <class 'int'>
type(height)    # <class 'float'>
type(is_student) # <class 'bool'>
```

---

## Input/Output
## الإدخال/الإخراج

### Getting Input | الحصول على المدخلات
```python
name = input("Enter your name: ")  # Always returns string
# دائماً يُرجع نص
age = int(input("Enter age: "))    # Convert to integer
# تحويل إلى عدد صحيح
```

### Displaying Output | عرض المخرجات
```python
print("Hello World")                    # Basic print
print("Hello", name)                    # Multiple items
print(f"You are {age} years old")       # f-string (recommended)
print("Score:", 95, "Grade:", "A")      # Multiple values
```

---

## Operators
## العمليات

### Arithmetic | الحسابية
```python
10 + 3    # 13    Addition | الجمع
10 - 3    # 7     Subtraction | الطرح
10 * 3    # 30    Multiplication | الضرب
10 / 3    # 3.333 Division | القسمة
10 // 3   # 3     Floor division | قسمة صحيحة
10 % 3    # 1     Modulo (remainder) | باقي القسمة
10 ** 3   # 1000  Power | الأس
```

### Comparison | المقارنة
```python
x = 10
x == 10   # True   Equal to | يساوي
x != 5    # True   Not equal | لا يساوي
x > 5     # True   Greater than | أكبر من
x < 20    # True   Less than | أصغر من
x >= 10   # True   Greater or equal | أكبر أو يساوي
x <= 10   # True   Less or equal | أصغر أو يساوي
```

### Logical | المنطقية
```python
x = 10
y = 5
(x > 5) and (y < 10)  # True   Both true | كلاهما صحيح
(x > 15) or (y < 10)  # True   One is true | واحد صحيح
not (x > 15)          # True   Opposite | العكس
```

---

## Decision Structures
## هياكل القرار

### if Statement | جملة if
```python
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")    # This executes
elif grade >= 70:
    print("C")
else:
    print("F")
# Output: B
```

### Nested if | if متداخلة
```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Can enter")  # This executes
    else:
        print("Need ID")
else:
    print("Too young")
# Output: Can enter
```

---

## Loops
## الحلقات

### while Loop | حلقة while
```python
count = 1
while count <= 3:
    print(count)
    count += 1
# Output: 1 2 3
```

### for Loop with range | حلقة for مع range
```python
# Simple range
for i in range(3):
    print(i)       # 0 1 2

# Start, stop
for i in range(2, 5):
    print(i)       # 2 3 4

# Start, stop, step
for i in range(0, 10, 2):
    print(i)       # 0 2 4 6 8
```

### for Loop with List | حلقة for مع قائمة
```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
# Output: apple banana orange
```

### Loop Control | التحكم بالحلقات
```python
# break - exit loop completely
for i in range(5):
    if i == 3:
        break
    print(i)    # 0 1 2

# continue - skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)    # 0 1 3 4
```

---

## String Operations
## عمليات النصوص

### Basic Operations | العمليات الأساسية
```python
name = "Python"

# Length | الطول
len(name)           # 6

# Concatenation | الدمج
greeting = "Hello " + name    # "Hello Python"

# Repetition | التكرار
stars = "*" * 5     # "*****"

# Membership | العضوية
"Py" in name        # True
"x" not in name     # True
```

### String Methods | دوال النصوص
```python
text = "  Hello World  "

text.upper()        # "  HELLO WORLD  "
text.lower()        # "  hello world  "
text.strip()        # "Hello World" (removes spaces)
text.replace("World", "Python")  # "  Hello Python  "

# Check methods
"hello".isalpha()   # True (all letters)
"123".isdigit()     # True (all digits)
"Hello".startswith("He")  # True
"World".endswith("ld")    # True
```

### String Indexing | فهرسة النصوص
```python
word = "Python"
#       012345   (positive index)
#      -6-5-4-3-2-1 (negative index)

word[0]     # 'P'    First character
word[-1]    # 'n'    Last character
word[1:4]   # 'yth'  Slice from 1 to 3
word[:2]    # 'Py'   First 2 characters
word[2:]    # 'thon' From index 2 to end
```

---

## Type Conversion
## تحويل الأنواع

### Common Conversions | التحويلات الشائعة
```python
# String to Number | نص إلى رقم
int("123")      # 123
float("3.14")   # 3.14

# Number to String | رقم إلى نص
str(123)        # "123"
str(3.14)       # "3.14"

# Boolean Conversion | تحويل منطقي
bool(0)         # False (0 is false)
bool(1)         # True (non-zero is true)
bool("")        # False (empty string is false)
bool("hello")   # True (non-empty is true)
```

### Input Conversion | تحويل المدخلات
```python
# input() always returns string
age_text = input("Enter age: ")  # "25"
age = int(age_text)              # 25

# Or in one line
score = float(input("Enter score: "))  # Direct conversion
```

---

## Common Patterns
## أنماط شائعة

### Accumulator Pattern | نمط التراكم
```python
# Sum numbers
total = 0
for i in range(1, 6):
    total += i
print(total)  # 15

# Count items
count = 0
for item in ["a", "b", "c"]:
    count += 1
print(count)  # 3
```

### Validation Loop | حلقة التحقق
```python
# Keep asking until valid input
age = -1
while age < 0 or age > 120:
    age = int(input("Enter valid age (0-120): "))
print(f"Your age is {age}")
```

### Finding Maximum/Minimum | إيجاد الأكبر/الأصغر
```python
numbers = [45, 67, 23, 89, 12]

# Find maximum
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)  # 89

# Or use built-in
print(max(numbers))  # 89
print(min(numbers))  # 12
```

---

## Quick Tips
## نصائح سريعة

### Naming Conventions | قواعد التسمية
```python
student_name = "Ali"    # ✅ snake_case for variables
MAXIMUM_AGE = 120      # ✅ UPPER_CASE for constants
StudentName = "Ali"    # ❌ Avoid PascalCase for variables
```

### Common Mistakes | أخطاء شائعة
```python
# Forgetting colon
if x > 5:   # ✅ Don't forget :
    print("big")

# Wrong indentation
if x > 5:
    print("big")    # ✅ 4 spaces
   print("big")     # ❌ 3 spaces

# = vs ==
x = 5      # ✅ Assignment
if x == 5: # ✅ Comparison
if x = 5:  # ❌ Syntax error!
```

### Debugging Tips | نصائح التصحيح
```python
# Use print to see values
x = 10
y = 20
print(f"x={x}, y={y}")  # Debug line
result = x + y
print(f"result={result}")  # Check result
```

---

## Practice Exercises
## تمارين تطبيقية

```python
# 1. Calculate average of 3 numbers
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
num3 = float(input("Third number: "))
average = (num1 + num2 + num3) / 3
print(f"Average: {average}")

# 2. Check if number is even or odd
number = int(input("Enter number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Print multiplication table
num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

---

**Remember:** Practice daily, type code yourself, and don't be afraid of errors!

**تذكر:** تدرب يومياً، اكتب الكود بنفسك، ولا تخف من الأخطاء!