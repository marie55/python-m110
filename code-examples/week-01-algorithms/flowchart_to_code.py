"""
M110 - Python Programming
Week 1: Algorithms - Flowchart to Python Code
Topic: Translating Flowcharts to Executable Python
الأسبوع 1: الخوارزميات - من المخطط الانسيابي إلى كود بايثون

This file demonstrates how to translate flowchart logic into Python code.
We'll show three examples covering the three basic structures.
يوضح هذا الملف كيفية ترجمة منطق المخطط الانسيابي إلى كود بايثون.
سنعرض ثلاثة أمثلة تغطي الهياكل الأساسية الثلاثة.
"""

print("=" * 60)
print("FLOWCHART TO PYTHON CODE EXAMPLES")
print("أمثلة تحويل المخطط الانسيابي إلى كود بايثون")
print("=" * 60)

# =============================================================================
# EXAMPLE 1: SEQUENCE STRUCTURE
# مثال 1: هيكل التسلسل
# =============================================================================
print("\n" + "=" * 60)
print("Example 1: Calculate Circle Area (SEQUENCE)")
print("مثال 1: حساب مساحة الدائرة (التسلسل)")
print("=" * 60)

print("\n📊 FLOWCHART LOGIC / منطق المخطط الانسيابي:")
print("""
┌─────────────────┐
│     START       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Input radius   │  ← إدخال نصف القطر
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ area = π × r²   │  ← حساب المساحة
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Output area    │  ← إخراج المساحة
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│      END        │
└─────────────────┘
""")

print("💻 PYTHON CODE / كود بايثون:\n")

# Step 1: Input / الخطوة 1: الإدخال
radius = float(input("Enter radius of circle: "))

# Step 2: Process / الخطوة 2: المعالجة
pi = 3.14159
area = pi * (radius ** 2)

# Step 3: Output / الخطوة 3: الإخراج
print(f"Area of circle: {area:.2f}")
print(f"مساحة الدائرة: {area:.2f}")

# =============================================================================
# EXAMPLE 2: DECISION STRUCTURE (IF-ELSE)
# مثال 2: هيكل القرار (إذا-وإلا)
# =============================================================================
print("\n" + "=" * 60)
print("Example 2: Check Passing Grade (DECISION)")
print("مثال 2: فحص درجة النجاح (القرار)")
print("=" * 60)

print("\n📊 FLOWCHART LOGIC / منطق المخطط الانسيابي:")
print("""
┌─────────────────┐
│     START       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Input grade    │  ← إدخال الدرجة
└────────┬────────┘
         │
         ▼
      ╱     ╲
    ╱ grade ╲         ← هل الدرجة >= 50؟
   ╱  >= 50? ╲
  ╱___________╲
  │           │
YES│           │NO
  │           │
  ▼           ▼
┌──────┐   ┌──────┐
│"Pass"│   │"Fail"│  ← نجح / رسب
└───┬──┘   └──┬───┘
    │         │
    └────┬────┘
         │
         ▼
┌─────────────────┐
│      END        │
└─────────────────┘
""")

print("💻 PYTHON CODE / كود بايثون:\n")

# Input / الإدخال
grade = float(input("Enter your grade: "))

# Decision / القرار
if grade >= 50:
    print("Result: PASS ✓")
    print("النتيجة: نجح ✓")
else:
    print("Result: FAIL ✗")
    print("النتيجة: رسب ✗")

# =============================================================================
# EXAMPLE 3: REPETITION STRUCTURE (WHILE LOOP)
# مثال 3: هيكل التكرار (حلقة بينما)
# =============================================================================
print("\n" + "=" * 60)
print("Example 3: Sum First N Numbers (REPETITION)")
print("مثال 3: جمع أول N أرقام (التكرار)")
print("=" * 60)

print("\n📊 FLOWCHART LOGIC / منطق المخطط الانسيابي:")
print("""
┌─────────────────┐
│     START       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Input N       │  ← إدخال N
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  sum = 0        │  ← المجموع = 0
│  i = 1          │  ← العداد = 1
└────────┬────────┘
         │
    ┌────▼────┐
    │  ╱     ╲│
    │╱  i<=N  ╲│  ← هل العداد <= N؟
    │╲   ?    ╱│
    │ ╲     ╱ │
    └──┬───┬──┘
      YES  NO
       │   │
       │   │
       │   └──────────────┐
       │                  │
       ▼                  │
┌─────────────┐           │
│ sum = sum+i │  ← جمع    │
│ i = i + 1   │  ← زيادة  │
└──────┬──────┘           │
       │                  │
       └──────┐           │
              │           │
         ▲────┘           │
         │ (loop back)    │
                          │
         ┌────────────────┘
         │
         ▼
┌─────────────────┐
│  Output sum     │  ← إخراج المجموع
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│      END        │
└─────────────────┘
""")

print("💻 PYTHON CODE / كود بايثون:\n")

# Input / الإدخال
n = int(input("Enter how many numbers to sum: "))

# Initialize / التهيئة
sum_total = 0
i = 1

# Repetition (loop) / التكرار (الحلقة)
while i <= n:
    sum_total = sum_total + i  # Add current number / إضافة الرقم الحالي
    i = i + 1                  # Increment counter / زيادة العداد

# Output / الإخراج
print(f"Sum of first {n} numbers: {sum_total}")
print(f"مجموع أول {n} أرقام: {sum_total}")

# Mathematical formula check / التحقق بالصيغة الرياضية
formula_result = n * (n + 1) // 2
print(f"Formula verification: {formula_result} (should match)")
print(f"التحقق بالصيغة: {formula_result} (يجب أن يتطابق)")

# =============================================================================
# EXAMPLE 4: COMBINED STRUCTURES (Real-World Example)
# مثال 4: الهياكل المدمجة (مثال من العالم الواقعي)
# =============================================================================
print("\n" + "=" * 60)
print("Example 4: Number Classifier (COMBINED)")
print("مثال 4: مصنف الأرقام (مدمج)")
print("=" * 60)

print("\n📊 FLOWCHART LOGIC / منطق المخطط الانسيابي:")
print("""
This combines SEQUENCE + REPETITION + DECISION
هذا يجمع التسلسل + التكرار + القرار

1. SEQUENCE: Initialize counters
2. REPETITION: Loop to get numbers
3. DECISION: Check if positive/negative/zero
4. SEQUENCE: Output final counts
""")

print("\n💻 PYTHON CODE / كود بايثون:\n")

# SEQUENCE: Initialize / التسلسل: التهيئة
positive_count = 0
negative_count = 0
zero_count = 0

# Get how many numbers / الحصول على عدد الأرقام
how_many = int(input("How many numbers will you enter? "))

# REPETITION: Loop through numbers / التكرار: التكرار عبر الأرقام
counter = 1
while counter <= how_many:
    number = float(input(f"Enter number {counter}: "))
    
    # DECISION: Classify the number / القرار: تصنيف الرقم
    if number > 0:
        positive_count = positive_count + 1
    elif number < 0:
        negative_count = negative_count + 1
    else:
        zero_count = zero_count + 1
    
    counter = counter + 1

# SEQUENCE: Output results / التسلسل: إخراج النتائج
print("\n📊 RESULTS / النتائج:")
print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeros: {zero_count}")
print(f"الأرقام الموجبة: {positive_count}")
print(f"الأرقام السالبة: {negative_count}")
print(f"الأصفار: {zero_count}")

# =============================================================================
# KEY TAKEAWAYS
# النقاط الرئيسية
# =============================================================================
print("\n" + "=" * 60)
print("KEY TAKEAWAYS / النقاط الرئيسية")
print("=" * 60)
print("""
✅ Flowcharts visualize algorithm logic
   المخططات الانسيابية تُصور منطق الخوارزمية

✅ Shapes have meanings:
   - Rectangle = Process (معالجة)
   - Diamond = Decision (قرار)
   - Parallelogram = Input/Output (إدخال/إخراج)

✅ Three structures map to Python:
   - SEQUENCE → Step-by-step code
   - DECISION → if/elif/else
   - REPETITION → while/for loops

✅ Think in flowchart, code in Python!
   فكر بالمخطط الانسيابي، ابرمج ببايثون!
""")

print("\n" + "=" * 60)
print("END OF EXAMPLES / نهاية الأمثلة")
print("=" * 60)
