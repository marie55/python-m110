"""
M110 - Python Programming
Week 1: Algorithms - Sequence Structure
Topic: Calculate Average
الأسبوع 1: الخوارزميات - بنية التسلسل
الموضوع: حساب المتوسط

This program demonstrates the SEQUENCE structure.
يوضح هذا البرنامج بنية التسلسل.

Algorithm (Pseudocode):
خوارزمية (شفرة زائفة):
    Start
    Use variable sum, average
    Input sum
    average = sum / 6
    Output average
    Stop
"""

# Sequence Structure Example: Calculate average of 6 numbers
# مثال على بنية التسلسل: حساب متوسط 6 أرقام

print("="*50)
print("Calculate Average of 6 Numbers")
print("حساب متوسط 6 أرقام")
print("="*50)

# Step 1: Input - Get the sum from user / المدخلات - الحصول على المجموع من المستخدم
sum_of_numbers = float(input("Enter the sum of 6 numbers: "))

# Step 2: Process - Calculate the average / المعالجة - حساب المتوسط
average = sum_of_numbers / 6

# Step 3: Output - Display the result / المخرجات - عرض النتيجة
print(f"\nThe average is: {average}")
print(f"المتوسط هو: {average}")

"""
Example Run / مثال على التشغيل:
==================================================
Calculate Average of 6 Numbers
حساب متوسط 6 أرقام
==================================================
Enter the sum of 6 numbers: 90

The average is: 15.0
المتوسط هو: 15.0

Explanation / الشرح:
- This is a SEQUENCE structure / هذه بنية تسلسل
- Steps execute one after another / الخطوات تنفذ واحدة تلو الأخرى
- No decisions, no loops / لا قرارات، لا حلقات
- Just: Input → Process → Output / فقط: مدخلات ← معالجة ← مخرجات
"""
