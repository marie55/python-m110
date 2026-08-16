# Exercise 01: Rectangle Area Calculator
# تمرين 01: حاسبة مساحة المستطيل

**Difficulty**: Easy / سهل  
**Topic**: Sequence Structure / هيكل التسلسل  
**Estimated Time**: 15 minutes / 15 دقيقة

---

## Problem Description
## وصف المشكلة

Write a program that calculates the area and perimeter of a rectangle. The program should:
1. Ask the user for the length of the rectangle
2. Ask the user for the width of the rectangle
3. Calculate the area (length × width)
4. Calculate the perimeter (2 × (length + width))
5. Display both results

اكتب برنامجًا يحسب مساحة ومحيط المستطيل. يجب على البرنامج:
1. أن يطلب من المستخدم طول المستطيل
2. أن يطلب من المستخدم عرض المستطيل
3. أن يحسب المساحة (الطول × العرض)
4. أن يحسب المحيط (2 × (الطول + العرض))
5. أن يعرض كلا النتيجتين

---

## Step 1: Write Pseudocode
## الخطوة 1: اكتب الشفرة الزائفة

Before writing Python code, plan your algorithm using pseudocode:

قبل كتابة كود بايثون، خطط لخوارزميتك باستخدام الشفرة الزائفة:

```
START
    [Your pseudocode here]
    [شفرتك الزائفة هنا]
END
```

<details>
<summary>💡 Hint for Pseudocode / تلميح للشفرة الزائفة</summary>

```
START
    INPUT length
    INPUT width
    area = length * width
    perimeter = 2 * (length + width)
    OUTPUT area
    OUTPUT perimeter
END
```
</details>

---

## Step 2: Draw Flowchart (Optional)
## الخطوة 2: ارسم مخططًا انسيابيًا (اختياري)

On paper or using a tool, draw a flowchart for this algorithm.

على الورق أو باستخدام أداة، ارسم مخططًا انسيابيًا لهذه الخوارزمية.

**Flowchart shapes to use:**
- Start/End: Oval / بيضاوي
- Process: Rectangle / مستطيل
- Input/Output: Parallelogram / متوازي أضلاع

---

## Step 3: Implement in Python
## الخطوة 3: نفّذ ببايثون

Now write the Python code. Create a file called `rectangle_area.py`:

الآن اكتب كود بايثون. أنشئ ملفًا باسم `rectangle_area.py`:

```python
# Rectangle Area and Perimeter Calculator
# حاسبة مساحة ومحيط المستطيل

# Step 1: Input
# الخطوة 1: الإدخال
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Step 2: Process
# الخطوة 2: المعالجة
# [Write your calculation code here]
# [اكتب كود الحساب هنا]

# Step 3: Output
# الخطوة 3: الإخراج
# [Write your output code here]
# [اكتب كود الإخراج هنا]
```

---

## Step 4: Test Your Program
## الخطوة 4: اختبر برنامجك

Run your program with these test cases:

شغّل برنامجك بحالات الاختبار هذه:

### Test Case 1:
- **Input**: length = 5, width = 3
- **Expected Output**: 
  - Area = 15
  - Perimeter = 16

### Test Case 2:
- **Input**: length = 10, width = 2.5
- **Expected Output**: 
  - Area = 25
  - Perimeter = 25

### Test Case 3:
- **Input**: length = 7.5, width = 4
- **Expected Output**: 
  - Area = 30
  - Perimeter = 23

---

## Sample Output
## مخرجات نموذجية

```
Enter length: 5
Enter width: 3
Area of rectangle: 15.0
Perimeter of rectangle: 16.0
```

---

## Bonus Challenge
## تحدي إضافي

Enhance your program to also calculate:
1. The diagonal of the rectangle using the formula: √(length² + width²)
   - You'll need: `import math` and `math.sqrt()`
2. Display all results with proper labels in both English and Arabic

حسّن برنامجك ليحسب أيضًا:
1. قطر المستطيل باستخدام الصيغة: √(الطول² + العرض²)
   - ستحتاج: `import math` و `math.sqrt()`
2. اعرض جميع النتائج بتسميات مناسبة بالإنجليزية والعربية

---

## Learning Objectives
## أهداف التعلم

After completing this exercise, you should be able to:
- ✅ Write pseudocode for a simple algorithm
- ✅ Use `input()` to get user data
- ✅ Perform arithmetic operations
- ✅ Use `print()` to display results
- ✅ Understand the SEQUENCE structure

بعد إكمال هذا التمرين، يجب أن تكون قادرًا على:
- ✅ كتابة الشفرة الزائفة لخوارزمية بسيطة
- ✅ استخدام `input()` للحصول على بيانات المستخدم
- ✅ إجراء العمليات الحسابية
- ✅ استخدام `print()` لعرض النتائج
- ✅ فهم هيكل التسلسل

---

## Common Mistakes to Avoid
## أخطاء شائعة يجب تجنبها

❌ **Mistake 1**: Forgetting to convert `input()` to `float`
```python
length = input("Enter length: ")  # This is a STRING, not a number!
```
✅ **Correct**:
```python
length = float(input("Enter length: "))
```

❌ **خطأ 1**: نسيان تحويل `input()` إلى `float`
```python
length = input("Enter length: ")  # هذا نص، ليس رقمًا!
```
✅ **صحيح**:
```python
length = float(input("Enter length: "))
```

---

❌ **Mistake 2**: Wrong perimeter formula
```python
perimeter = 2 * length + width  # Missing parentheses!
```
✅ **Correct**:
```python
perimeter = 2 * (length + width)
```

❌ **خطأ 2**: صيغة خاطئة للمحيط
```python
perimeter = 2 * length + width  # أقواس مفقودة!
```
✅ **صحيح**:
```python
perimeter = 2 * (length + width)
```

---

## Solution
## الحل

<details>
<summary>Click to see solution / انقر لرؤية الحل</summary>

```python
"""
Rectangle Area and Perimeter Calculator
حاسبة مساحة ومحيط المستطيل
"""

# Step 1: Input
# الخطوة 1: الإدخال
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

# Step 2: Process (Calculate)
# الخطوة 2: المعالجة (الحساب)
area = length * width
perimeter = 2 * (length + width)

# Step 3: Output
# الخطوة 3: الإخراج
print(f"\n--- Results / النتائج ---")
print(f"Length: {length}")
print(f"Width: {width}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
print(f"الطول: {length}")
print(f"العرض: {width}")
print(f"المساحة: {area}")
print(f"المحيط: {perimeter}")

# Example output:
# --- Results / النتائج ---
# Length: 5.0
# Width: 3.0
# Area: 15.0
# Perimeter: 16.0
```

### Bonus Solution (with diagonal):
### حل الإضافة (مع القطر):

```python
import math

# Input
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Process
area = length * width
perimeter = 2 * (length + width)
diagonal = math.sqrt(length**2 + width**2)

# Output
print(f"\n📐 Rectangle Calculations / حسابات المستطيل")
print(f"Length / الطول: {length}")
print(f"Width / العرض: {width}")
print(f"Area / المساحة: {area:.2f}")
print(f"Perimeter / المحيط: {perimeter:.2f}")
print(f"Diagonal / القطر: {diagonal:.2f}")
```
</details>

---

## Next Exercise
## التمرين التالي

Once you complete this exercise, move on to:
- [Exercise 02: Temperature Converter](exercise-02.md)

بمجرد إكمال هذا التمرين، انتقل إلى:
- [تمرين 02: محول درجة الحرارة](exercise-02.md)

---

**Good luck! / حظًا موفقًا!** 🚀
