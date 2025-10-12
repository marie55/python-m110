# Week 1: Algorithms, Flowcharts & Pseudocodes
# الأسبوع الأول: الخوارزميات، المخططات الانسيابية والشفرة الزائفة

**Week**: October 12-16, 2025
**Chapter**: Chapter 1
**Official Slides**: [Meeting1-Algorithms-s.pdf](../../slides-official/chapter-01-algorithms/Meeting1-Algorithms-s.pdf)

---

## Learning Objectives
## أهداف التعلم

By the end of this week, you should be able to:

في نهاية هذا الأسبوع، يجب أن تكون قادراً على:

1. **Understand what an algorithm is** and why it's important in programming
   **فهم ما هي الخوارزمية** ولماذا هي مهمة في البرمجة

2. **Design algorithms** using flowcharts and pseudocode
   **تصميم الخوارزميات** باستخدام المخططات الانسيابية والشفرة الزائفة

3. **Recognize the three basic structures**: Sequence, Decision, and Repetition
   **التعرف على التراكيب الأساسية الثلاثة**: التسلسل، القرار، والتكرار

4. **Translate pseudocode and flowcharts to Python code**
   **ترجمة الشفرة الزائفة والمخططات الانسيابية إلى كود بايثون**

---

## Why This Week Matters
## لماذا هذا الأسبوع مهم

**Think before you code!**
**فكر قبل أن تكتب الكود!**

Before a building is constructed, architects create blueprints. Before writing code, programmers design algorithms. This week teaches you to **think algorithmically** – a skill that separates good programmers from great ones.

قبل بناء المبنى، ينشئ المهندسون المخططات. قبل كتابة الكود، يصمم المبرمجون الخوارزميات. يعلمك هذا الأسبوع **التفكير الخوارزمي** – وهي مهارة تفصل المبرمجين الجيدين عن العظماء.

---

## Core Concepts
## المفاهيم الأساسية

### 1. What is an Algorithm?
### ما هي الخوارزمية؟

**Definition:**
An **algorithm** is an **ordered set of unambiguous steps** that describes a process to solve a problem.

**التعريف:**
الخوارزمية هي **مجموعة مرتبة من الخطوات الواضحة** التي تصف عملية لحل مشكلة.

**Key characteristics:**
**الخصائص الرئيسية:**

- ✅ **Unambiguous** (واضحة): Each step has only one meaning
  - كل خطوة لها معنى واحد فقط

- ✅ **Input** (مدخلات): 0 or more well-defined inputs
  - صفر أو أكثر من المدخلات المحددة جيداً

- ✅ **Output** (مخرجات): At least 1 output that matches desired result
  - على الأقل مخرج واحد يطابق النتيجة المرغوبة

- ✅ **Finiteness** (محدودة): Must terminate after finite steps
  - يجب أن تنتهي بعد عدد محدود من الخطوات

- ✅ **Feasibility** (قابلة للتنفيذ): Can be done with available resources
  - يمكن تنفيذها بالموارد المتاحة

- ✅ **Independent** (مستقلة): Not tied to specific programming language
  - غير مرتبطة بلغة برمجة محددة

**Real-life examples:**
**أمثلة من الحياة الواقعية:**

- 🍰 Recipe for baking / وصفة للخبز
- 📱 Steps to unlock phone / خطوات لفتح الهاتف
- 🧪 Lab procedure / إجراء المختبر

---

### 2. The Three Basic Structures
### التراكيب الأساسية الثلاثة

Every algorithm can be built using these three structures:

يمكن بناء كل خوارزمية باستخدام هذه التراكيب الثلاثة:

#### A. Sequence (التسلسل)

Execute steps one after another in order.

تنفيذ الخطوات واحدة تلو الأخرى بالترتيب.

**Example: Calculate average**
**مثال: حساب المتوسط**

```
Input sum
average = sum / 6
Output average
```

**Python code:**
```python
# Sequence example - Calculate average
# مثال التسلسل - حساب المتوسط
total = float(input("Enter sum: "))
average = total / 6
print(f"Average: {average}")
```

---

#### B. Decision (القرار)

Choose between alternatives based on a condition.

الاختيار بين البدائل بناءً على شرط.

**Example: Even or Odd**
**مثال: زوجي أو فردي**

```
IF number mod 2 = 0
    Print "Even"
ELSE
    Print "Odd"
END IF
```

**Python code:**
```python
# Decision example - Even or Odd
# مثال القرار - زوجي أو فردي
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even / زوجي")
else:
    print("Odd / فردي")
```

---

#### C. Repetition (التكرار)

Repeat steps while condition is true.

تكرار الخطوات بينما الشرط صحيح.

**Example: Sum of scores**
**مثال: مجموع الدرجات**

```
i = 1
sum = 0
WHILE i <= 6
    Input score
    Add score to sum
    i = i + 1
END WHILE
Output sum
```

**Python code:**
```python
# Repetition example - Sum of scores
# مثال التكرار - مجموع الدرجات
i = 1
total = 0
while i <= 6:
    score = float(input(f"Enter score {i}: "))
    total += score
    i += 1
print(f"Total: {total}")
```

---

## Flowcharts
## المخططات الانسيابية

Flowcharts are **visual representations** of algorithms using standard symbols:

المخططات الانسيابية هي **تمثيلات مرئية** للخوارزميات باستخدام رموز قياسية:

### Standard Flowchart Symbols
### رموز المخططات الانسيابية القياسية

| Symbol | Name | الاسم | Purpose | الغرض |
|--------|------|-------|---------|--------|
| Oval | Terminal | بداية/نهاية | Start/End | بداية/نهاية |
| Rectangle | Process | معالجة | Actions/Calculations | إجراءات/حسابات |
| Diamond | Decision | قرار | Conditional branching | تفرع شرطي |
| Parallelogram | Input/Output | إدخال/إخراج | Read/Print data | قراءة/طباعة البيانات |
| Arrow | Flow line | خط التدفق | Direction of flow | اتجاه التدفق |

### Example: Calculate Average Flowchart
### مثال: مخطط انسيابي لحساب المتوسط

```
[Start]
   ↓
[Input: sum]
   ↓
[Process: average = sum / 6]
   ↓
[Output: average]
   ↓
[End]
```

---

## Pseudocode
## الشفرة الزائفة

Pseudocode is a **simplified, language-independent** way to describe an algorithm using English-like statements.

الشفرة الزائفة هي طريقة **مبسطة ومستقلة عن اللغة** لوصف الخوارزمية باستخدام عبارات تشبه اللغة الإنجليزية.

### Pseudocode Keywords
### كلمات الشفرة الزائفة المفتاحية

| Keyword | الكلمة المفتاحية | Purpose | الغرض |
|---------|------------------|---------|-------|
| START | بداية | Begin algorithm | بداية الخوارزمية |
| END | نهاية | End algorithm | نهاية الخوارزمية |
| INPUT | إدخال | Read data | قراءة البيانات |
| OUTPUT | إخراج | Display data | عرض البيانات |
| IF...THEN...ELSE | إذا...فإن...وإلا | Decision | قرار |
| WHILE...ENDWHILE | بينما...نهاية بينما | Loop | حلقة تكرار |
| FOR...ENDFOR | لكل...نهاية لكل | Loop | حلقة تكرار |
| SET | تعيين | Assign value | تعيين قيمة |

### Example: Grade Checker Pseudocode
### مثال: شفرة زائفة لفاحص الدرجات

```
START
    INPUT grade
    IF grade >= 50 THEN
        OUTPUT "Pass"
    ELSE
        OUTPUT "Fail"
    END IF
END
```

**Translation to Python:**
**الترجمة إلى بايثون:**

```python
# Grade checker
# فاحص الدرجات
grade = float(input("Enter grade: "))
if grade >= 50:
    print("Pass / نجاح")
else:
    print("Fail / رسوب")
```

---

## From Algorithm to Code: Complete Example
## من الخوارزمية إلى الكود: مثال كامل

### Problem: Calculate class average and determine Pass/Fail
### المشكلة: حساب متوسط الصف وتحديد نجاح/رسوب

**Step 1: Pseudocode**
**الخطوة 1: الشفرة الزائفة**

```
START
    counter = 0
    sum = 0
    INPUT grade
    WHILE grade != -1
        sum = sum + grade
        counter = counter + 1
        INPUT grade
    END WHILE

    IF counter > 0 THEN
        average = sum / counter
        OUTPUT average
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

**Step 2: Flowchart**
**الخطوة 2: المخطط الانسيابي**

```
[Start]
   ↓
[counter = 0, sum = 0]
   ↓
[Input grade]
   ↓
   ◇ grade != -1?
   ↓ Yes           ↓ No
[sum += grade]     ◇ counter > 0?
[counter += 1]     ↓ Yes         ↓ No
[Input grade]   [average =    [Output "No
   ↓            sum/counter]   grades"]
   ↑← Back      [Output avg]      ↓
                   ↓            [End]
                ◇ average >= 50?
                ↓ Yes    ↓ No
            ["Pass"]  ["Fail"]
                ↓         ↓
              [End]     [End]
```

**Step 3: Python Code**
**الخطوة 3: كود بايثون**

See [../../code-examples/week-01-algorithms/05_grade_calculator_complete.py](../../code-examples/week-01-algorithms/05_grade_calculator_complete.py)

---

## Code Examples
## أمثلة البرمجة

All code examples are available in:
جميع أمثلة الأكواد متوفرة في:

[../../code-examples/week-01-algorithms/](../../code-examples/week-01-algorithms/)

1. `01_sequence_average.py` - Sequence structure example
2. `02_decision_even_odd.py` - Decision structure example
3. `03_repetition_sum_scores.py` - Repetition structure example
4. `04_sentinel_loop.py` - Sentinel-controlled loop
5. `05_grade_calculator_complete.py` - Complete example with all structures
6. `flowchart_to_code.py` - Converting flowcharts to code
7. `pseudocode_examples.py` - Various pseudocode translations

---

## Practice Exercises
## تمارين عملية

Complete exercises are in:
التمارين الكاملة في:

[../../exercises/week-01/](../../exercises/week-01/)

### Recommended practice order:
### الترتيب الموصى به للتمرين:

1. **Easy Level** / **المستوى السهل**
   - Rectangle area calculator
   - Temperature converter
   - Simple calculator

2. **Medium Level** / **المستوى المتوسط**
   - Grade checker
   - Positive/negative checker
   - Triangle area with validation

3. **Advanced Level** / **المستوى المتقدم**
   - Print numbers 1-10
   - Sum of N numbers
   - Find maximum
   - Count positives (Sentinel)

4. **Challenge** / **التحدي**
   - Multiplication table
   - Grade letter calculator
   - Password validator

---

## Common Mistakes to Avoid
## الأخطاء الشائعة التي يجب تجنبها

### ❌ Don't:
- Skip the planning phase and jump directly to coding
- Use ambiguous language in pseudocode
- Forget to terminate loops (infinite loops)
- Mix up the assignment operator (=) with equality (==)

### ✅ Do:
- Always plan your algorithm first (pseudocode or flowchart)
- Use clear, descriptive variable names
- Test your algorithm with sample data before coding
- Add comments explaining your logic

### ❌ لا تفعل:
- تخطى مرحلة التخطيط والقفز مباشرة إلى البرمجة
- استخدام لغة غامضة في الشفرة الزائفة
- نسيان إنهاء الحلقات (حلقات لا نهائية)
- الخلط بين عامل التعيين (=) والمساواة (==)

### ✅ افعل:
- خطط دائماً للخوارزمية أولاً (شفرة زائفة أو مخطط انسيابي)
- استخدم أسماء متغيرات واضحة ووصفية
- اختبر الخوارزمية بعينات بيانات قبل البرمجة
- أضف تعليقات تشرح منطقك

---

## Key Takeaways
## النقاط الرئيسية

✅ **Algorithms are step-by-step solutions** to problems

✅ **Flowcharts visualize** algorithm flow using standard symbols

✅ **Pseudocode describes** algorithms in English-like statements

✅ **Three basic structures**: Sequence, Decision, Repetition

✅ **Think first, code later** - planning saves debugging time!

**بالعربية:**

✅ **الخوارزميات هي حلول خطوة بخطوة** للمشاكل

✅ **المخططات الانسيابية تصور** تدفق الخوارزمية باستخدام رموز قياسية

✅ **الشفرة الزائفة تصف** الخوارزميات بعبارات تشبه الإنجليزية

✅ **ثلاثة تراكيب أساسية**: التسلسل، القرار، التكرار

✅ **فكر أولاً، اكتب الكود لاحقاً** - التخطيط يوفر وقت تصحيح الأخطاء!

---

## Additional Resources
## موارد إضافية

### Video Tutorials
- [Week 1 Video Guide](../../resources/video-tutorials/video-tutorials-guide.md#week-1)

### Cheatsheets
- [Control Structures Cheatsheet](../../resources/cheatsheets/control-structures-cheatsheet.md)
- [Python Syntax Cheatsheet](../../resources/cheatsheets/python-syntax-cheatsheet.md)

### Practice Platforms
- Use Dr. Laila: `/laila` - Ask for custom practice problems
- Check the FAQ: [../../resources/faq.md](../../resources/faq.md)

---

## Week 1 Checklist
## قائمة التحقق للأسبوع الأول

Before moving to Week 2, make sure you can:

قبل الانتقال إلى الأسبوع 2، تأكد من أنك تستطيع:

- [ ] Define what an algorithm is / تعريف ما هي الخوارزمية
- [ ] Identify the characteristics of a good algorithm / تحديد خصائص الخوارزمية الجيدة
- [ ] Draw flowcharts using standard symbols / رسم المخططات الانسيابية باستخدام الرموز القياسية
- [ ] Write pseudocode for simple problems / كتابة شفرة زائفة لمشاكل بسيطة
- [ ] Recognize sequence, decision, and repetition structures / التعرف على تراكيب التسلسل والقرار والتكرار
- [ ] Convert pseudocode to Python code / تحويل الشفرة الزائفة إلى كود بايثون
- [ ] Convert flowcharts to Python code / تحويل المخططات الانسيابية إلى كود بايثون
- [ ] Debug simple algorithm errors / تصحيح أخطاء الخوارزمية البسيطة

---

**Next Week**: Week 2 - Fundamentals of Python Programming

**الأسبوع القادم**: الأسبوع 2 - أساسيات برمجة بايثون

---

*Happy Algorithm Designing! / تصميم خوارزميات سعيد!* 🎯