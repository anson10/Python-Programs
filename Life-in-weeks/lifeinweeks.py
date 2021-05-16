total_days = 90 * 365
total_weeks = 90 * 52
total_months = 90 * 12

user_age = int(input("Enter your age :"))
remaining_days = total_days - (user_age * 365)
remaining_weeks = total_weeks - (user_age * 52)
remaining_months = total_months - (user_age *12)

print(f"You have {remaining_days} days , {remaining_weeks} weeks, and {remaining_months} months left.")