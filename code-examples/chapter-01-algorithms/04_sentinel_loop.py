"""
M110 - Python Programming
Week 1: Algorithms - Sentinel-Controlled Repetition
Topic: Character Printer
الأسبوع 1: الخوارزميات - التكرار المتحكم به بقيمة حارسة
الموضوع: طابعة الحروف

This program demonstrates SENTINEL-CONTROLLED repetition.
يوضح هذا البرنامج التكرار المتحكم به بقيمة حارسة.

Sentinel Value: A special value that signals "stop"
قيمة حارسة: قيمة خاصة تشير إلى "توقف"

Algorithm (Pseudocode):
    Start
    Use variable: letter
    Print "Type in a character or 'q' to stop"
    Input letter
    WHILE letter <> 'q'
        Print letter
        Print "Type in a character or 'q' to stop"
        Input letter
    ENDWHILE
    Stop
"""

# Sentinel-Controlled Loop Example: Print characters until 'q'
# مثال على الحلقة المتحكم بها بقيمة حارسة: اطبع الحروف حتى 'q'

print("="*50)
print("Character Printer (Sentinel-Controlled Loop)")
print("طابعة الحروف (حلقة متحكم بها بقيمة حارسة)")
print("="*50)
print("Type any character and press Enter")
print("Enter 'q' to stop the program")
print("\nاكتب أي حرف واضغط Enter")
print("اكتب 'q' للتوقف")
print("="*50)

# Step 1: Get first input (priming read) / الحصول على أول إدخال (قراءة تحضيرية)
letter = input("\nEnter a character (q to quit): ")

# Step 2: Loop until sentinel value 'q' is entered / حلقة حتى يتم إدخال القيمة الحارسة 'q'
while letter != 'q':  # Loop while NOT 'q' / حلقة بينما ليس 'q'
    # Process the letter / معالجة الحرف
    print(f"You entered: '{letter}' ✓")
    print(f"لقد أدخلت: '{letter}' ✓")

    # Get next input / الحصول على الإدخال التالي
    letter = input("\nEnter a character (q to quit): ")

# Step 3: Loop ended / انتهت الحلقة
print("\n" + "="*50)
print("Program ended. You pressed 'q'")
print("انتهى البرنامج. لقد ضغطت 'q'")
print("="*50)

"""
Example Run / مثال على التشغيل:
==================================================
Character Printer (Sentinel-Controlled Loop)
طابعة الحروف (حلقة متحكم بها بقيمة حارسة)
==================================================
Type any character and press Enter
Enter 'q' to stop the program

اكتب أي حرف واضغط Enter
اكتب 'q' للتوقف
==================================================

Enter a character (q to quit): a
You entered: 'a' ✓
لقد أدخلت: 'a' ✓

Enter a character (q to quit): b
You entered: 'b' ✓
لقد أدخلت: 'b' ✓

Enter a character (q to quit): c
You entered: 'c' ✓
لقد أدخلت: 'c' ✓

Enter a character (q to quit): q

==================================================
Program ended. You pressed 'q'
انتهى البرنامج. لقد ضغطت 'q'
==================================================

Explanation / الشرح:
- This is INDEFINITE REPETITION / هذا تكرار غير محدد
- We don't know HOW MANY times loop will run / لا نعرف كم مرة ستعمل الحلقة
- Loop continues UNTIL sentinel value ('q') is entered / الحلقة تستمر حتى يتم إدخال القيمة الحارسة ('q')
- Need "priming read" before loop / نحتاج "قراءة تحضيرية" قبل الحلقة

Common Sentinel Values / قيم حارسة شائعة:
- -1 for numbers / للأرقام
- 'q', 'quit', 'exit' for text / للنص
- 0 to stop / للتوقف
- Empty string "" / سلسلة فارغة

Key Differences from Counter-Controlled:
الفروقات الرئيسية عن الحلقة المتحكم بها بعداد:

Counter-Controlled:
- Know exact number of repetitions / نعرف العدد الدقيق للتكرارات
- Use counter variable (i) / نستخدم متغير عداد (i)
- Example: "Loop 10 times" / مثال: "كرر 10 مرات"

Sentinel-Controlled:
- Don't know how many repetitions / لا نعرف كم تكراراً
- Use special "stop" value / نستخدم قيمة "توقف" خاصة
- Example: "Loop until user says stop" / مثال: "كرر حتى يقول المستخدم توقف"
"""
