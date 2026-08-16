"""
M110 - Python Programming
Week 1: Algorithms - Repetition Structure
Topic: Sum of Test Scores
الأسبوع 1: الخوارزميات - بنية التكرار
الموضوع: مجموع درجات الاختبار

This program demonstrates the REPETITION (WHILE loop) structure.
يوضح هذا البرنامج بنية التكرار (حلقة بينما).

Algorithm (Pseudocode):
    Start
    Use variable: testScore, sum, i
    sum = 0
    i = 1
    WHILE i <= 6
        Input testScore
        sum = sum + testScore
        i = i + 1
    ENDWHILE
    Output sum
    Stop
"""

# Repetition Structure Example: Sum of 6 test scores
# مثال على بنية التكرار: مجموع 6 درجات اختبار

print("="*50)
print("Sum of 6 Test Scores")
print("مجموع 6 درجات اختبار")
print("="*50)

# Step 1: Initialize variables / تهيئة المتغيرات
sum_scores = 0  # Accumulator for total / مُجمّع المجموع الكلي
i = 1  # Counter variable / متغير العداد

# Step 2: Repetition - Loop 6 times / التكرار - كرر 6 مرات
while i <= 6:  # Loop condition / شرط الحلقة
    # Input score / إدخال الدرجة
    score = float(input(f"\nEnter test score #{i}: "))

    # Add to sum / أضف إلى المجموع
    sum_scores += score  # Same as: sum_scores = sum_scores + score

    # Increment counter (IMPORTANT!) / زيادة العداد (مهم!)
    i += 1  # Same as: i = i + 1

# Step 3: Output - Display total / المخرجات - عرض المجموع
print("\n" + "="*50)
print(f"Total sum of scores: {sum_scores}")
print(f"مجموع الدرجات الكلي: {sum_scores}")
print(f"Average: {sum_scores / 6:.2f}")
print(f"المتوسط: {sum_scores / 6:.2f}")
print("="*50)

"""
Example Run / مثال على التشغيل:
==================================================
Sum of 6 Test Scores
مجموع 6 درجات اختبار
==================================================

Enter test score #1: 85

Enter test score #2: 90

Enter test score #3: 78

Enter test score #4: 92

Enter test score #5: 88

Enter test score #6: 95

==================================================
Total sum of scores: 528.0
مجموع الدرجات الكلي: 528.0
Average: 88.00
المتوسط: 88.00
==================================================

Explanation / الشرح:
- This uses REPETITION (WHILE loop) structure / يستخدم بنية التكرار (حلقة بينما)
- Loop repeats EXACTLY 6 times / الحلقة تتكرر بالضبط 6 مرات
- Counter (i) controls how many times / العداد (i) يتحكم في عدد المرات
- Accumulator (sum_scores) keeps running total / المُجمّع (sum_scores) يحتفظ بالمجموع الجاري

Common Mistakes to Avoid / أخطاء شائعة يجب تجنبها:
1. Forgetting to initialize sum to 0 / نسيان تهيئة المجموع إلى 0
2. Forgetting to increment i (infinite loop!) / نسيان زيادة i (حلقة لا نهائية!)
3. Wrong loop condition (e.g., i < 6 instead of i <= 6) / شرط حلقة خاطئ
"""
