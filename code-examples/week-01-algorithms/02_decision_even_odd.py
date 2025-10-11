"""
M110 - Python Programming
Week 1: Algorithms - Decision Structure
Topic: Even or Odd Checker
الأسبوع 1: الخوارزميات - بنية القرار
الموضوع: فاحص الزوجي والفردي

This program demonstrates the DECISION (IF-ELSE) structure.
يوضح هذا البرنامج بنية القرار (إذا-وإلا).

Algorithm (Pseudocode):
    Start
    Use variable: number
    Input number
    IF number mod 2 = 0
        Print "The number is even"
    ELSE
        Print "The number is odd"
    Stop
"""

# Decision Structure Example: Check if number is even or odd
# مثال على بنية القرار: التحقق إذا كان الرقم زوجي أو فردي

print("="*50)
print("Even or Odd Checker")
print("فاحص الزوجي والفردي")
print("="*50)

# Step 1: Input - Get number from user / المدخلات - الحصول على الرقم من المستخدم
number = int(input("\nEnter an integer number: "))

# Step 2: Decision - Check if even or odd / القرار - التحقق إذا كان زوجي أو فردي
if number % 2 == 0:  # The % operator gives the remainder / العامل % يعطي الباقي
    # If remainder is 0, number is even / إذا كان الباقي 0، الرقم زوجي
    print(f"\n✓ {number} is EVEN")
    print(f"✓ {number} زوجي")
else:
    # Otherwise, number is odd / وإلا، الرقم فردي
    print(f"\n✓ {number} is ODD")
    print(f"✓ {number} فردي")

print("\n" + "="*50)

"""
Example Runs / أمثلة على التشغيل:

Run 1:
==================================================
Even or Odd Checker
فاحص الزوجي والفردي
==================================================

Enter an integer number: 10

✓ 10 is EVEN
✓ 10 زوجي

==================================================

Run 2:
==================================================
Even or Odd Checker
فاحص الزوجي والفردي
==================================================

Enter an integer number: 7

✓ 7 is ODD
✓ 7 فردي

==================================================

Explanation / الشرح:
- This uses DECISION structure / يستخدم بنية القرار
- Program chooses ONE path based on condition / البرنامج يختار مسار واحد بناءً على الشرط
- Modulo operator (%) gives remainder / عامل القسمة (%) يعطي الباقي
  - 10 % 2 = 0 (even) / زوجي
  - 7 % 2 = 1 (odd) / فردي
"""
