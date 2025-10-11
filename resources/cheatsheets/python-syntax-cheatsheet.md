# Python Syntax Cheatsheet
# ورقة مرجع صياغة بايثون

**For**: M110 Python Programming | **لـ**: برمجة بايثون M110
**Covers**: Weeks 1-4 (Basics) | **يغطي**: الأسابيع 1-4 (الأساسيات)

---

## 📝 Variables & Data Types
## 📝 المتغيرات وأنواع البيانات

| Type | Description | Example | Value |
|------|-------------|---------|-------|
| **int** | Integer / عدد صحيح | `age = 20` | `20` |
| **float** | Decimal / عدد عشري | `price = 19.99` | `19.99` |
| **str** | Text / نص | `name = "Ali"` | `"Ali"` |
| **bool** | True/False / صح/خطأ | `is_student = True` | `True` |

---

## ⌨️ Input & Output
## ⌨️ الإدخال والإخراج

| Action | Syntax | Example | Output |
|--------|--------|---------|--------|
| **Input** / **إدخال** | `input("prompt")` | `name = input("Name: ")` | User types: `Ali` |
| **Output** / **إخراج** | `print(value)` | `print("Hello")` | `Hello` |
| **Formatted** / **منسق** | `print(f"text {var}")` | `print(f"Age: {age}")` | `Age: 20` |
| **Multiple values** / **قيم متعددة** | `print(x, y)` | `print("Hi", name)` | `Hi Ali` |

---

## 🔢 Arithmetic Operators
## 🔢 المعاملات الحسابية

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition / جمع | `5 + 3` | `8` |
| `-` | Subtraction / طرح | `5 - 3` | `2` |
| `*` | Multiplication / ضرب | `5 * 3` | `15` |
| `/` | Division / قسمة | `10 / 3` | `3.333...` |
| `//` | Integer division / قسمة صحيحة | `10 // 3` | `3` |
| `%` | Modulus (remainder) / الباقي | `10 % 3` | `1` |
| `**` | Exponent / أس | `2 ** 3` | `8` |

---

## 🔍 Comparison Operators
## 🔍 معاملات المقارنة

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to / يساوي | `5 == 5` | `True` |
| `!=` | Not equal / لا يساوي | `5 != 3` | `True` |
| `>` | Greater than / أكبر من | `5 > 3` | `True` |
| `<` | Less than / أصغر من | `5 < 3` | `False` |
| `>=` | Greater or equal / أكبر أو يساوي | `5 >= 5` | `True` |
| `<=` | Less or equal / أصغر أو يساوي | `3 <= 5` | `True` |

---

## 🧠 Logical Operators
## 🧠 المعاملات المنطقية

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both true / كلاهما صحيح | `True and False` | `False` |
| `or` | At least one true / واحد على الأقل صحيح | `True or False` | `True` |
| `not` | Opposite / العكس | `not True` | `False` |

**Priority / الأولوية**: `not` → `and` → `or`

---

## 🔄 Type Conversion
## 🔄 تحويل الأنواع

| From → To | Function | Example | Result |
|-----------|----------|---------|--------|
| str → int | `int()` | `int("42")` | `42` |
| str → float | `float()` | `float("3.14")` | `3.14` |
| int/float → str | `str()` | `str(42)` | `"42"` |
| float → int | `int()` | `int(3.14)` | `3` |
| any → bool | `bool()` | `bool(0)` | `False` |

⚠️ **Common Errors / أخطاء شائعة**:
- `int("3.14")` → ❌ ValueError
- `int("hello")` → ❌ ValueError

---

## 📊 String Operations
## 📊 عمليات النصوص

| Operation | Syntax | Example | Result |
|-----------|--------|---------|--------|
| **Concatenation** / **دمج** | `+` | `"Hello" + " " + "World"` | `"Hello World"` |
| **Repetition** / **تكرار** | `*` | `"Hi" * 3` | `"HiHiHi"` |
| **Length** / **الطول** | `len()` | `len("Hello")` | `5` |
| **Indexing** / **فهرسة** | `[n]` | `"Python"[0]` | `"P"` |
| **Slicing** / **تقطيع** | `[start:end]` | `"Python"[0:3]` | `"Pyt"` |

### String Methods / طرق النصوص

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `.upper()` | Uppercase / أحرف كبيرة | `"hello".upper()` | `"HELLO"` |
| `.lower()` | Lowercase / أحرف صغيرة | `"HELLO".lower()` | `"hello"` |
| `.strip()` | Remove spaces / إزالة الفراغات | `"  hi  ".strip()` | `"hi"` |
| `.replace(old, new)` | Replace / استبدال | `"hello".replace("h", "H")` | `"Hello"` |
| `.split(sep)` | Split to list / تقسيم لقائمة | `"a,b,c".split(",")` | `["a", "b", "c"]` |

---

## 💬 Comments
## 💬 التعليقات

```python
# Single-line comment / تعليق سطر واحد

"""
Multi-line comment
تعليق متعدد الأسطر
"""
```

---

## 🎯 Operator Precedence (Highest → Lowest)
## 🎯 أولوية المعاملات (الأعلى → الأدنى)

1. `()` Parentheses / الأقواس
2. `**` Exponent / الأس
3. `*, /, //, %` Multiplication & Division / الضرب والقسمة
4. `+, -` Addition & Subtraction / الجمع والطرح
5. `<, <=, >, >=, !=, ==` Comparison / المقارنة
6. `not` Logical NOT / النفي المنطقي
7. `and` Logical AND / و المنطقية
8. `or` Logical OR / أو المنطقية

---

## ✅ Quick Tips
## ✅ نصائح سريعة

- 🔑 **Variable names**: lowercase with underscores (`student_name`)
  **أسماء المتغيرات**: أحرف صغيرة مع شرطات سفلية

- ⚠️ **Case-sensitive**: `age` ≠ `Age` ≠ `AGE`
  **حساسة لحالة الأحرف**

- 📝 **Meaningful names**: `total_price` not `x`
  **أسماء ذات معنى**: `total_price` وليس `x`

- 🚫 **Reserved words**: Can't use `if`, `for`, `while`, etc. as variables
  **كلمات محجوزة**: لا يمكن استخدام `if`, `for`, `while`, إلخ كمتغيرات

---

**📌 Print this and keep it beside you while coding!**
**📌 اطبع هذا واحتفظ به بجانبك أثناء البرمجة!**

---

*M110 Python Programming - Arab Open University, Amman*
*برمجة بايثون M110 - الجامعة العربية المفتوحة، عمان*