"""
M110 - Python Programming
Week 1: Algorithms - Pseudocode to Python
Topic: Translating Pseudocode to Executable Python
الأسبوع 1: الخوارزميات - من الشفرة الزائفة إلى بايثون

This file demonstrates how to translate pseudocode into Python code.
Pseudocode is a way to describe algorithms using English-like statements.
يوضح هذا الملف كيفية ترجمة الشفرة الزائفة إلى كود بايثون.
الشفرة الزائفة هي طريقة لوصف الخوارزميات باستخدام جمل شبيهة بالإنجليزية.
"""

print("=" * 70)
print("PSEUDOCODE TO PYTHON TRANSLATION EXAMPLES")
print("أمثلة ترجمة الشفرة الزائفة إلى بايثون")
print("=" * 70)

# =============================================================================
# EXAMPLE 1: SIMPLE SEQUENCE - Calculate Rectangle Area
# مثال 1: تسلسل بسيط - حساب مساحة المستطيل
# =============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 1: Rectangle Area Calculator")
print("مثال 1: حاسبة مساحة المستطيل")
print("=" * 70)

print("\n📝 PSEUDOCODE / الشفرة الزائفة:")
print("""
START
    INPUT length
    INPUT width
    area = length * width
    OUTPUT area
END
""")

print("💻 PYTHON CODE / كود بايثون:")
print("-" * 70)

# Translation / الترجمة
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print(f"Rectangle area = {area}")
print(f"مساحة المستطيل = {area}")

# =============================================================================
# EXAMPLE 2: DECISION - Determine Grade Letter
# مثال 2: القرار - تحديد حرف الدرجة
# =============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 2: Grade Letter Determiner")
print("مثال 2: محدد حرف الدرجة")
print("=" * 70)

print("\n📝 PSEUDOCODE / الشفرة الزائفة:")
print("""
START
    INPUT grade
    IF grade >= 90 THEN
        OUTPUT "A"
    ELSE IF grade >= 80 THEN
        OUTPUT "B"
    ELSE IF grade >= 70 THEN
        OUTPUT "C"
    ELSE IF grade >= 60 THEN
        OUTPUT "D"
    ELSE
        OUTPUT "F"
    END IF
END
""")

print("💻 PYTHON CODE / كود بايثون:")
print("-" * 70)

# Translation / الترجمة
grade = float(input("Enter grade (0-100): "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Grade letter: {letter}")
print(f"حرف الدرجة: {letter}")

# =============================================================================
# EXAMPLE 3: WHILE LOOP - Countdown Timer
# مثال 3: حلقة بينما - عداد تنازلي
# =============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 3: Countdown Timer")
print("مثال 3: عداد تنازلي")
print("=" * 70)

print("\n📝 PSEUDOCODE / الشفرة الزائفة:")
print("""
START
    INPUT start_number
    counter = start_number
    WHILE counter > 0 DO
        OUTPUT counter
        counter = counter - 1
    END WHILE
    OUTPUT "Blast off!"
END
""")

print("💻 PYTHON CODE / كود بايثون:")
print("-" * 70)

# Translation / الترجمة
start_number = int(input("Enter countdown start: "))
counter = start_number

while counter > 0:
    print(counter)
    counter = counter - 1

print("🚀 Blast off!")
print("🚀 انطلق!")

# =============================================================================
# EXAMPLE 4: NESTED DECISION - Eligibility Checker
# مثال 4: قرار متداخل - فاحص الأهلية
# =============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 4: Voting Eligibility Checker")
print("مثال 4: فاحص أهلية التصويت")
print("=" * 70)

print("\n📝 PSEUDOCODE / الشفرة الزائفة:")
print("""
START
    INPUT age
    INPUT is_citizen
    
    IF age >= 18 THEN
        IF is_citizen = "yes" THEN
            OUTPUT "Eligible to vote"
        ELSE
            OUTPUT "Not eligible: Must be a citizen"
        END IF
    ELSE
        OUTPUT "Not eligible: Must be 18 or older"
    END IF
END
""")

print("💻 PYTHON CODE / كود بايثون:")
print("-" * 70)

# Translation / الترجمة
age = int(input("Enter age: "))
is_citizen = input("Are you a citizen? (yes/no): ").lower()

if age >= 18:
    if is_citizen == "yes":
        print("✅ Eligible to vote")
        print("✅ مؤهل للتصويت")
    else:
        print("❌ Not eligible: Must be a citizen")
        print("❌ غير مؤهل: يجب أن تكون مواطناً")
else:
    print("❌ Not eligible: Must be 18 or older")
    print("❌ غير مؤهل: يجب أن تكون 18 سنة أو أكبر")

# =============================================================================
# EXAMPLE 5: SENTINEL-CONTROLLED LOOP - Average Calculator
# مثال 5: حلقة يتحكم فيها حارس - حاسبة المتوسط
# =============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 5: Average Calculator (Sentinel-Controlled)")
print("مثال 5: حاسبة المتوسط (يتحكم فيها حارس)")
print("=" * 70)

print("\n📝 PSEUDOCODE / الشفرة الزائفة:")
print("""
START
    sum = 0
    count = 0
    
    INPUT number
    WHILE number != -1 DO
        sum = sum + number
        count = count + 1
        INPUT number
    END WHILE
    
    IF count > 0 THEN
        average = sum / count
        OUTPUT average
    ELSE
        OUTPUT "No numbers entered"
    END IF
END
""")

print("💻 PYTHON CODE / كود بايثون:")
print("-" * 70)
print("Enter numbers (enter -1 to stop):")
print("أدخل الأرقام (أدخل -1 للتوقف):")

# Translation / الترجمة
sum_total = 0
count = 0

number = float(input("Enter number: "))
while number != -1:
    sum_total = sum_total + number
    count = count + 1
    number = float(input("Enter number: "))

if count > 0:
    average = sum_total / count
    print(f"Average: {average:.2f}")
    print(f"المتوسط: {average:.2f}")
else:
    print("No numbers entered")
    print("لم يتم إدخال أرقام")

# =============================================================================
# EXAMPLE 6: FOR LOOP (COUNT-CONTROLLED) - Multiplication Table
# مثال 6: حلقة لـ (يتحكم فيها العداد) - جدول الضرب
# =============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 6: Multiplication Table")
print("مثال 6: جدول الضرب")
print("=" * 70)

print("\n📝 PSEUDOCODE / الشفرة الزائفة:")
print("""
START
    INPUT number
    FOR i FROM 1 TO 10 DO
        result = number * i
        OUTPUT number, "x", i, "=", result
    END FOR
END
""")

print("💻 PYTHON CODE / كود بايثون:")
print("-" * 70)

# Translation / الترجمة
number = int(input("Enter number for multiplication table: "))

for i in range(1, 11):  # range(1, 11) gives 1,2,3...10
    result = number * i
    print(f"{number} x {i} = {result}")

# =============================================================================
# EXAMPLE 7: COMPLEX ALGORITHM - Find Maximum and Minimum
# مثال 7: خوارزمية معقدة - إيجاد الأكبر والأصغر
# =============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 7: Find Maximum and Minimum")
print("مثال 7: إيجاد الأكبر والأصغر")
print("=" * 70)

print("\n📝 PSEUDOCODE / الشفرة الزائفة:")
print("""
START
    INPUT how_many
    INPUT first_number
    max = first_number
    min = first_number
    
    FOR i FROM 2 TO how_many DO
        INPUT number
        IF number > max THEN
            max = number
        END IF
        IF number < min THEN
            min = number
        END IF
    END FOR
    
    OUTPUT "Maximum:", max
    OUTPUT "Minimum:", min
END
""")

print("💻 PYTHON CODE / كود بايثون:")
print("-" * 70)

# Translation / الترجمة
how_many = int(input("How many numbers? "))

if how_many > 0:
    first_number = float(input("Enter number 1: "))
    max_value = first_number
    min_value = first_number
    
    for i in range(2, how_many + 1):
        number = float(input(f"Enter number {i}: "))
        
        if number > max_value:
            max_value = number
        
        if number < min_value:
            min_value = number
    
    print(f"Maximum: {max_value}")
    print(f"Minimum: {min_value}")
    print(f"الأكبر: {max_value}")
    print(f"الأصغر: {min_value}")
else:
    print("Please enter at least 1 number")
    print("الرجاء إدخال رقم واحد على الأقل")

# =============================================================================
# EXAMPLE 8: VALIDATION LOOP - Get Valid Input
# مثال 8: حلقة التحقق - الحصول على إدخال صحيح
# =============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 8: Input Validation")
print("مثال 8: التحقق من الإدخال")
print("=" * 70)

print("\n📝 PSEUDOCODE / الشفرة الزائفة:")
print("""
START
    valid = false
    WHILE valid = false DO
        INPUT age
        IF age >= 0 AND age <= 120 THEN
            valid = true
        ELSE
            OUTPUT "Invalid age. Try again."
        END IF
    END WHILE
    OUTPUT "Valid age entered:", age
END
""")

print("💻 PYTHON CODE / كود بايثون:")
print("-" * 70)

# Translation / الترجمة
valid = False

while not valid:
    age = int(input("Enter age (0-120): "))
    
    if 0 <= age <= 120:
        valid = True
    else:
        print("❌ Invalid age. Try again.")
        print("❌ عمر غير صحيح. حاول مرة أخرى.")

print(f"✅ Valid age entered: {age}")
print(f"✅ عمر صحيح: {age}")

# =============================================================================
# PSEUDOCODE NOTATION GUIDE
# دليل رموز الشفرة الزائفة
# =============================================================================
print("\n" + "=" * 70)
print("PSEUDOCODE NOTATION GUIDE")
print("دليل رموز الشفرة الزائفة")
print("=" * 70)
print("""
┌────────────────────────────────────────────────────────────────┐
│ PSEUDOCODE              │ PYTHON                              │
├────────────────────────────────────────────────────────────────┤
│ INPUT variable          │ variable = input()                  │
│ OUTPUT message          │ print(message)                      │
│ SET variable = value    │ variable = value                    │
│ IF condition THEN       │ if condition:                       │
│ ELSE                    │ else:                               │
│ WHILE condition DO      │ while condition:                    │
│ FOR i FROM 1 TO 10 DO   │ for i in range(1, 11):              │
│ variable MOD 2          │ variable % 2                        │
│ variable = variable + 1 │ variable = variable + 1             │
│ AND                     │ and                                 │
│ OR                      │ or                                  │
│ NOT                     │ not                                 │
└────────────────────────────────────────────────────────────────┘

KEY DIFFERENCES / الاختلافات الرئيسية:
────────────────────────────────────────
1. Pseudocode uses natural language, Python uses exact syntax
   الشفرة الزائفة تستخدم لغة طبيعية، بايثون تستخدم صياغة دقيقة

2. Pseudocode doesn't care about indentation, Python requires it
   الشفرة الزائفة لا تهتم بالمسافات البادئة، بايثون تتطلبها

3. Pseudocode is for planning, Python is for executing
   الشفرة الزائفة للتخطيط، بايثون للتنفيذ
""")

# =============================================================================
# PRACTICE EXERCISE
# تمرين الممارسة
# =============================================================================
print("\n" + "=" * 70)
print("PRACTICE EXERCISE / تمرين الممارسة")
print("=" * 70)
print("""
Try converting this pseudocode to Python:
حاول تحويل هذه الشفرة الزائفة إلى بايثون:

START
    sum_even = 0
    sum_odd = 0
    FOR i FROM 1 TO 10 DO
        IF i MOD 2 = 0 THEN
            sum_even = sum_even + i
        ELSE
            sum_odd = sum_odd + i
        END IF
    END FOR
    OUTPUT "Sum of even numbers:", sum_even
    OUTPUT "Sum of odd numbers:", sum_odd
END

📝 Write your solution and run it!
📝 اكتب حلك وشغله!
""")

print("\n" + "=" * 70)
print("END OF PSEUDOCODE EXAMPLES")
print("نهاية أمثلة الشفرة الزائفة")
print("=" * 70)

# Solution to practice exercise (uncomment to see)
# حل تمرين الممارسة (احذف التعليق لرؤيته)
"""
sum_even = 0
sum_odd = 0

for i in range(1, 11):
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i

print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}")
"""
