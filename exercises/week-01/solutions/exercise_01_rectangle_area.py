"""
M110 - Week 1 Exercise Solutions
Exercise 1: Rectangle Area Calculator
تمرين 1: حاسبة مساحة المستطيل

Problem:
Write a program that reads length and width, calculates area, and displays result.

المشكلة:
اكتب برنامجاً يقرأ الطول والعرض، يحسب المساحة، ويعرض النتيجة.

Algorithm (Pseudocode):
    Start
    Use variables: length, width, area
    Input length
    Input width
    area = length * width
    Output area
    Stop
"""

# Solution / الحل

print("Rectangle Area Calculator")
print("حاسبة مساحة المستطيل")
print("="*40)

# Input / المدخلات
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Process / المعالجة
area = length * width

# Output / المخرجات
print(f"\nArea of rectangle: {area}")
print(f"مساحة المستطيل: {area}")

"""
Example Run:
Rectangle Area Calculator
حاسبة مساحة المستطيل
========================================
Enter length: 5
Enter width: 3

Area of rectangle: 15.0
مساحة المستطيل: 15.0
"""
