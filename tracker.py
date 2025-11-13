# -----------------------------------------------------------
# Name: Nikhil Sehrawat
# Course: B.Tech CSE (AIML) - Section G
# Date: 12-Nov-2025
# Project: Daily Calorie Tracker (Assignment – 01)
# -----------------------------------------------------------

print("\nWelcome to the Daily Calorie Tracker!")
print("This tool helps you log meals, calculate calories, and compare with your daily limit.\n")

# -------------------------------
# Task 2: Input & Data Collection
# -------------------------------
meal_names = []
calorie_values = []

meal_count = int(input("How many meals do you want to enter? "))

for i in range(meal_count):
    name = input(f"Enter meal {i+1} name: ")
    calories = float(input(f"Enter calories for {name}: "))

    meal_names.append(name)
    calorie_values.append(calories)

print("\n--- Data Recorded Successfully ---\n")

# -------------------------
# Task 3: Calculations
# -------------------------
total_calories = sum(calorie_values)
average_calories = total_calories / meal_count

daily_limit = float(input("Enter your daily calorie limit: "))

# -------------------------
# Task 4: Warning System
# -------------------------
print("\nCalorie Limit Check:")

if total_calories > daily_limit:
    status = "⚠️ You have exceeded your daily calorie limit!"
else:
    status = "✔ You are within your daily limit. Good job!"

print(status)

# -------------------------
# Task 5: Formatted Output
# -------------------------
print("\n-------------------------------------------")
print("Meal Name\t\tCalories")
print("-------------------------------------------")

for i in range(meal_count):
    print(f"{meal_names[i]}\t\t{calorie_values[i]}")

print("-------------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t\t{average_calories:.2f}")
print("-------------------------------------------\n")

# -------------------------
# Task 6: Save Session Log
# -------------------------
save = input("Do you want to save this session to a file? (yes/no): ").lower()

if save == "yes":
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("calorie_log.txt", "w") as file:
        file.write("------ Daily Calorie Tracker Log ------\n")
        file.write(f"Timestamp: {timestamp}\n\n")

        file.write("Meal Name\tCalories\n")
        file.write("-----------------------------------\n")

        for i in range(meal_count):
            file.write(f"{meal_names[i]}\t{calorie_values[i]}\n")

        file.write("-----------------------------------\n")
        file.write(f"Total Calories: {total_calories}\n")
        file.write(f"Average Calories: {average_calories:.2f}\n")
        file.write(f"Status: {status}\n")

    print("\n📁 Log saved as calorie_log.txt")
else:
    print("\nLog not saved.")

print("\nThank you for using the Daily Calorie Tracker!")
