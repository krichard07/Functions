fix_text = "testcase"

def dollarizer(text):
   return f"Dollarizer: {text.replace("s", "$")}"

converted_text = dollarizer(fix_text)
print(converted_text)

def eurizer(text):
   return f"Eurizer: {text.replace("e", "€")}"

converted_text = eurizer(fix_text)
print(converted_text)

def replacer(text):
   return f"Replacer: {text.replace("t", "#")}"

converted_text = replacer(fix_text)
print(converted_text)

def wonky(text):
   return f"Wonky Text: {text.replace( "s", "$",).replace("e", "€").replace("l", "£")}"

converted_text = wonky(fix_text)
print(converted_text)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(f"Celsius to Fahrenheit: {celsius_to_fahrenheit(25.0)}")

current_age = 28

def age_in_days():
    #global current_age
    year = 365
    days = current_age * year
    return days

print(f"Ages in Days: {age_in_days()}")

def simple_interest(p, r, t):
    si = p * r * t
    return si

print(f"Simple Interest: {float(simple_interest(5, 6, 7))}")


def plan_finances(principal_amount,rate_of_interest, time_in_years, desired_final_amount):
    final_amount = principal_amount * (1 + rate_of_interest * time_in_years)
    if final_amount >= desired_final_amount:
        return True
    else:
        return False
    
principal_amount = 1100
rate_of_interest = 0.05
time_in_years = 3
desired_final_amount = 1150

result = plan_finances(principal_amount,rate_of_interest, time_in_years, desired_final_amount)
print(f"Plan Finances: {result}")