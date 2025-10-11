# Control Structures Cheatsheet
# ورقة مرجع البُنى التحكمية

**For**: M110 Python Programming | **لـ**: برمجة بايثون M110
**Covers**: Decision & Repetition Structures | **يغطي**: بُنى القرار والتكرار

---

## 🔀 Decision Structures
## 🔀 بُنى القرار

### ✔️ Simple if
### ✔️ if بسيطة

```python
if condition:
    # Code if true / كود إذا صح
```

**Example / مثال**:
```python
age = 18
if age >= 18:
    print("Adult")  # Output: Adult
```

### ✔️ if-else
### ✔️ if-else

```python
if condition:
    # Code if true / كود إذا صح
else:
    # Code if false / كود إذا خطأ
```

**Example / مثال**:
```python
score = 75
if score >= 60:
    print("Pass")    # Output: Pass
else:
    print("Fail")
```

### ✔️ if-elif-else
### ✔️ if-elif-else

```python
if condition1:
    # Code for condition1 / كود للشرط 1
elif condition2:
    # Code for condition2 / كود للشرط 2
else:
    # Code if all false / كود إذا كل الشروط خطأ
```

**Example / مثال**:
```python
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")      # Output: B
elif grade >= 70:
    print("C")
else:
    print("F")
```

### ✔️ Nested if
### ✔️ if متداخلة

```python
if outer_condition:
    if inner_condition:
        # Code / كود
```

**Example / مثال**:
```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")  # Output: Can drive
    else:
        print("Need license")
else:
    print("Too young")
```

---

## 🔁 Repetition Structures (Loops)
## 🔁 بُنى التكرار (الحلقات)

### 🔄 while Loop
### 🔄 حلقة while

```python
while condition:
    # Code to repeat / كود للتكرار
    # Update condition / تحديث الشرط
```

**Example / مثال**:
```python
count = 1
while count <= 3:
    print(count)   # Output: 1 2 3
    count += 1
```

### 🔄 for Loop with range()
### 🔄 حلقة for مع range()

| Syntax | Description | Example | Output |
|--------|-------------|---------|--------|
| `range(stop)` | 0 to stop-1 / من 0 إلى stop-1 | `range(3)` | `0, 1, 2` |
| `range(start, stop)` | start to stop-1 / من start إلى stop-1 | `range(2, 5)` | `2, 3, 4` |
| `range(start, stop, step)` | With step / مع خطوة | `range(0, 10, 2)` | `0, 2, 4, 6, 8` |

**Examples / أمثلة**:
```python
# Simple for loop / حلقة for بسيطة
for i in range(3):
    print(i)        # Output: 0 1 2

# With start and stop / مع بداية ونهاية
for i in range(1, 4):
    print(i)        # Output: 1 2 3

# With step / مع خطوة
for i in range(0, 10, 2):
    print(i)        # Output: 0 2 4 6 8

# Reverse / عكسي
for i in range(5, 0, -1):
    print(i)        # Output: 5 4 3 2 1
```

### 🔄 for Loop with Lists
### 🔄 حلقة for مع القوائم

```python
# Loop through list / التكرار عبر قائمة
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)    # Output: apple banana orange

# With index / مع الفهرس
for i in range(len(fruits)):
    print(i, fruits[i])  # Output: 0 apple, 1 banana, 2 orange
```

---

## 🛑 Loop Control
## 🛑 التحكم بالحلقات

| Keyword | Description | Example |
|---------|-------------|---------|
| **break** | Exit loop immediately / الخروج من الحلقة فوراً | See below |
| **continue** | Skip to next iteration / التخطي للتكرار التالي | See below |

### break Example / مثال break:
```python
for i in range(5):
    if i == 3:
        break       # Exit loop at 3
    print(i)        # Output: 0 1 2
```

### continue Example / مثال continue:
```python
for i in range(5):
    if i == 2:
        continue    # Skip 2
    print(i)        # Output: 0 1 3 4
```

---

## 🔄 Nested Loops
## 🔄 الحلقات المتداخلة

```python
for i in range(3):          # Outer loop / الحلقة الخارجية
    for j in range(2):      # Inner loop / الحلقة الداخلية
        print(i, j)
```

**Output**:
```
0 0
0 1
1 0
1 1
2 0
2 1
```

**Pattern Example / مثال نمط**:
```python
# Print triangle / طباعة مثلث
for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
```

---

## 📊 Common Patterns
## 📊 أنماط شائعة

### Counter Pattern / نمط العداد
```python
count = 0
while count < 5:
    print(count)
    count += 1      # Don't forget! / لا تنسَ!
```

### Accumulator Pattern / نمط المُجمِّع
```python
total = 0
for i in range(1, 6):
    total += i      # Add to total / أضف للمجموع
print(total)        # Output: 15 (1+2+3+4+5)
```

### Sentinel Pattern / نمط الحارس
```python
while True:
    value = input("Enter (q to quit): ")
    if value == 'q':
        break
    print(f"You entered: {value}")
```

### Input Validation / التحقق من الإدخال
```python
age = int(input("Age (0-120): "))
while age < 0 or age > 120:
    print("Invalid!")
    age = int(input("Age (0-120): "))
```

---

## 🔍 Decision Flowchart Symbols
## 🔍 رموز مخططات القرار

| Symbol | Shape | Purpose |
|--------|-------|---------|
| **Start/End** | Oval ⭕ | Program start/end / بداية/نهاية البرنامج |
| **Process** | Rectangle ▭ | Action/calculation / عملية/حساب |
| **Decision** | Diamond ◇ | if/while condition / شرط if/while |
| **Input/Output** | Parallelogram ▱ | Input/print / إدخال/طباعة |
| **Arrow** | → | Flow direction / اتجاه التدفق |

---

## ⚠️ Common Mistakes
## ⚠️ أخطاء شائعة

| Mistake | Wrong ❌ | Correct ✅ |
|---------|----------|-----------|
| **Forgot colon** / **نسيان النقطتين** | `if x > 5` | `if x > 5:` |
| **Wrong indentation** / **مسافة بادئة خاطئة** | No indent after if | 4 spaces indent |
| **Infinite loop** / **حلقة لا نهائية** | `while True:` (no break) | Add break condition |
| **Off-by-one** / **خطأ بواحد** | `range(1, 10)` for 10 items | `range(10)` or `range(1, 11)` |
| **= vs ==** | `if x = 5:` | `if x == 5:` |

---

## ✅ Quick Tips
## ✅ نصائح سريعة

- 🔑 **Indentation**: Always use 4 spaces (not tabs)
  **المسافة البادئة**: استخدم دائماً 4 مسافات

- 📝 **Test edge cases**: Empty, single item, maximum values
  **اختبر الحالات الحدية**: فارغ، عنصر واحد، القيم القصوى

- ⚡ **Simplify conditions**: `if x == True:` → `if x:`
  **بسط الشروط**

- 🎯 **Clear variable names**: `for student in students:` not `for s in st:`
  **أسماء واضحة للمتغيرات**

---

**📌 Keep this handy while writing conditions and loops!**
**📌 احتفظ بهذا بجانبك عند كتابة الشروط والحلقات!**

---

*M110 Python Programming - Arab Open University, Amman*
*برمجة بايثون M110 - الجامعة العربية المفتوحة، عمان*