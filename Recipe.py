# Task 1 Number of serving
def get_number_of_servings(prompt):
    while True:
        try:
            servings = int(input(prompt))
            if servings <= 0:
                print("Error: Number of servings must be a positive integer.")
            else:
                return servings
        except ValueError:
            print("Error: Please enter a valid number.")

original_servings = get_number_of_servings("Enter the number of servings the recipe is originally for: ")
desired_servings = get_number_of_servings("Enter the number of servings you wish to make: ")

# Task 2 Quantity adjustor
def calculate_adjustment_factor(original_servings, desired_servings):
    try:
        adjustment_factor = desired_servings / original_servings
        return adjustment_factor
    except ZeroDivisionError:
        print("Error: Original servings cannot be zero.")
        return None
    except Exception as e:
        print(f"An error occurred during the calculation: {e}")
        return None

adjustment_factor = calculate_adjustment_factor(original_servings, desired_servings)
if adjustment_factor is not None:
    print("Adjustment factor:", adjustment_factor)

# Task 3 Serving Success
def display_adjusted_quantities(original_quantities, adjustment_factor):
    adjusted_quantities = [quantity * adjustment_factor for quantity in original_quantities]
    print("Adjusted recipe quantities:")
    for quantity in adjusted_quantities:
        print(quantity)

original_quantities = [1, 2, 3]  
display_adjusted_quantities(original_quantities, adjustment_factor)

print("Let's get cooking!")
