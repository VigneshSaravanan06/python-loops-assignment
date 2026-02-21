# Name: Saravanan T
# Roll Number: [Your Roll Number]
# Assignment: Python Loops & Automation - Subjective Question

# Task 1:Find Maximum and Minimum
print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
highest = temperatures[0]
lowest = temperatures[0]

for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

print(f"Highest Temperature: {highest}")
print(f"Lowest Temperature: {lowest}")

# Task 2: Count Hot Days
print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
Hot_Days = 0
for T in temperatures:
    if T<=30:
        continue

    Hot_Days=Hot_Days+1

print(f"Hot Days (>30°C):{Hot_Days}")

# Task 3: Alert System
print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0
day = 0   

for temp in temperatures:
    day = day + 1  

    if temp >= 40:
        print("Alert! Extreme temperature", temp, "°C detected on Day", day)
        break

    if temp >= 30:
        hot_days = hot_days + 1

print("Hot Days before alert:", hot_days)
