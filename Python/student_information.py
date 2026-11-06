
# Student Information System
# Project 01 - Python Basics

print("=" * 40)
print("       STUDENT INFORMATION SYSTEM")
print("=" * 40)

# Getting information from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
major = input("Enter your major: ")
university = input("Enter your university: ")
gpa = float(input("Enter your GPA: "))

# Displaying student information
print("\n" + "=" * 40)
print("          STUDENT PROFILE")
print("=" * 40)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Major: {major}")
print(f"University: {university}")
print(f"GPA: {gpa}")

print("=" * 40)
print(f"Welcome, {name}!")
print("Your information was saved successfully.")
print("=" * 40)
