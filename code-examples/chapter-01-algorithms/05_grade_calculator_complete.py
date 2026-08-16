"""
M110 - Python Programming
Chapter 1: Algorithms - Complete Example (All Three Structures)
Topic: Student Grade Calculator
الفصل 1: الخوارزميات - مثال كامل (التراكيب الثلاثة كلها)
الموضوع: حاسبة درجات الطلاب

This program demonstrates ALL THREE structures together:
- SEQUENCE
- DECISION
- REPETITION

يوضح هذا البرنامج التراكيب الثلاثة معاً:
- التسلسل
- القرار
- التكرار

Algorithm (Pseudocode):
    Start
    counter = 0
    sum = 0
    Print "Enter grades (-1 to stop)"
    Input grade
    WHILE grade != -1
        Add grade to sum
        Increment counter
        Input grade
    ENDWHILE
    IF counter > 0
        average = sum / counter
        Print average
        IF average >= 50
            Print "PASS"
        ELSE
            Print "FAIL"
        END IF
    ELSE
        Print "No grades entered"
    END IF
    Stop
"""

# Complete Grade Calculator - Using all three structures
# حاسبة الدرجات الكاملة - باستخدام التراكيب الثلاثة

print("="*60)
print("Student Grade Calculator - Class Average")
print("حاسبة درجات الطلاب - متوسط الصف")
print("="*60)
print("Enter student grades one by one")
print("Enter -1 when finished")
print("\nأدخل درجات الطلاب واحدة تلو الأخرى")
print("أدخل -1 عند الانتهاء")
print("="*60)

# SEQUENCE: Initialize variables / التسلسل: تهيئة المتغيرات
counter = 0  # Count how many grades / عد كم درجة
sum_grades = 0  # Sum of all grades / مجموع كل الدرجات

# Priming read / القراءة التحضيرية
grade = float(input("\nEnter grade (or -1 to stop): "))

# REPETITION: Sentinel-controlled loop / التكرار: حلقة متحكم بها بقيمة حارسة
while grade != -1:  # Sentinel value is -1 / القيمة الحارسة هي -1
    # SEQUENCE inside loop / التسلسل داخل الحلقة
    sum_grades += grade  # Add to sum / أضف إلى المجموع
    counter += 1  # Increment count / زيادة العدد

    # Get next grade / الحصول على الدرجة التالية
    grade = float(input("Enter grade (or -1 to stop): "))

print("\n" + "="*60)

# DECISION: Check if any grades were entered / القرار: تحقق إذا تم إدخال أي درجات
if counter > 0:  # At least one grade entered / على الأقل درجة واحدة
    # SEQUENCE: Calculate average / التسلسل: احسب المتوسط
    average = sum_grades / counter

    # Display results / عرض النتائج
    print(f"Number of students: {counter}")
    print(f"عدد الطلاب: {counter}")
    print(f"\nTotal sum of grades: {sum_grades}")
    print(f"مجموع الدرجات الكلي: {sum_grades}")
    print(f"\nClass Average: {average:.2f}")
    print(f"متوسط الصف: {average:.2f}")

    # DECISION: Determine Pass/Fail / القرار: تحديد نجاح/رسوب
    print("\n" + "-"*60)
    if average >= 50:  # Pass threshold / عتبة النجاح
        print("✓ Class PASSED (Average >= 50)")
        print("✓ الصف نجح (المتوسط >= 50)")
        print("🎉 Congratulations! / مبروك!")
    else:
        print("✗ Class FAILED (Average < 50)")
        print("✗ الصف رسب (المتوسط < 50)")
        print("📚 More study needed / مطلوب المزيد من الدراسة")

else:  # No grades entered / لم يتم إدخال درجات
    print("⚠ No grades were entered!")
    print("⚠ لم يتم إدخال أي درجات!")

print("="*60)

"""
Example Run 1 (Pass): مثال 1 (نجاح)
============================================================
Student Grade Calculator - Class Average
حاسبة درجات الطلاب - متوسط الصف
============================================================
Enter student grades one by one
Enter -1 when finished

أدخل درجات الطلاب واحدة تلو الأخرى
أدخل -1 عند الانتهاء
============================================================

Enter grade (or -1 to stop): 85
Enter grade (or -1 to stop): 90
Enter grade (or -1 to stop): 78
Enter grade (or -1 to stop): 92
Enter grade (or -1 to stop): -1

============================================================
Number of students: 4
عدد الطلاب: 4

Total sum of grades: 345.0
مجموع الدرجات الكلي: 345.0

Class Average: 86.25
متوسط الصف: 86.25

------------------------------------------------------------
✓ Class PASSED (Average >= 50)
✓ الصف نجح (المتوسط >= 50)
🎉 Congratulations! / مبروك!
============================================================

Example Run 2 (Fail): مثال 2 (رسوب)
============================================================
Enter grade (or -1 to stop): 30
Enter grade (or -1 to stop): 45
Enter grade (or -1 to stop): 40
Enter grade (or -1 to stop): -1

============================================================
Number of students: 3
عدد الطلاب: 3

Total sum of grades: 115.0
مجموع الدرجات الكلي: 115.0

Class Average: 38.33
متوسط الصف: 38.33

------------------------------------------------------------
✗ Class FAILED (Average < 50)
✗ الصف رسب (المتوسط < 50)
📚 More study needed / مطلوب المزيد من الدراسة
============================================================

Structure Breakdown / تحليل التراكيب:

1. SEQUENCE (التسلسل):
   - Initialize counter and sum / تهيئة العداد والمجموع
   - Calculate average / حساب المتوسط
   - Display results / عرض النتائج

2. DECISION (القرار):
   - IF counter > 0 / إذا العداد > 0
   - IF average >= 50 / إذا المتوسط >= 50

3. REPETITION (التكرار):
   - WHILE grade != -1 / بينما الدرجة != -1
   - Sentinel-controlled loop / حلقة متحكم بها بقيمة حارسة

This is a REAL-WORLD example combining all concepts!
هذا مثال من العالم الحقيقي يجمع كل المفاهيم!
"""
