'''
Rebeca Llontop
IS 303 - A04

Recipe Scaler: This program scales recipe ingredients up or down based on desired servings. 

Inputs:
- recipe_name (str)
- original_servings (float)
- target_servings (float)
- num_ingredients (int)
- ingredient_name (str)
- ingredient_amount (float)
- ingredient_unit (str)

Processes:
- import math 
- get_valid_int(prompt): ensures user enters a number for amounts and servings
- get_valid_str(prompt): ensures user enters a string for ingrdients and recipe names 
- calculate_scale_factor(original, target): simple division to find the multiplier
- scale_ingredient(amount, factor): multiplies original amount by the factor
- display_scaled_recipe(original_servings, target_servings, scaled_amount): prints the final list clearly

Outputs:
- A formatted list of ingredients with their new, scaled amounts. 
'''
import math 

#--- FUNCTION ----

def get_valid_int(prompt):
    """Keeps telling the user to enter an integer number""" 
    while True:
        try: 
            value = int(input(prompt))
            return value 
        except ValueError:
            print("Invalid input. Please enter a number: ")

def get_valid_strg(prompt):
    """Keeps telling the user to enter a string""" 
    while True:
            value = input(prompt).strip()
            if value != "":
                 return value 
            print("Invalid input. Please enter words: ")

def calculate_scale_factor(original, target):
     """Divides original and target to find the multilplier"""
     factor = target / original
     return factor 

def scale_ingredient (original, factor):
     """Multiplies the original amount by the factor"""
     scaled_amount = original * factor 
     return scaled_amount

def display_scaled_recipe(recipe_name, original_servings, target_servings, ingredients):
     """Prints scaled recipe with a list of ingredients and their scaled amount"""
     print(f"\nRecipe: {recipe_name}")
     print(f"Original Servings: {original_servings}")
     print(f"Target Servings: {target_servings}")
     print(f"\nScaled ingredients for {recipe_name}: ")
     for ingredient in ingredients: 
          print(f"- {ingredient['amount']:.2f} {ingredient['unit']} of {ingredient['name']}")

def main(): 
     recipe_name = get_valid_strg("What is the name of your recipe? ").title()
     original_servings = get_valid_int("What are the original servings? ")
     target_servings = get_valid_int("What is the target servings? ")
     num_ingredients = get_valid_int("How namy numbers of ingredients? ")

     ingredients = [] 
     for i in range(num_ingredients): 
          ingredient_name = get_valid_strg("Enter ingredient name: ").lower()
          ingredient_amount = get_valid_int("Enter ingredient amount: ")
          ingredient_unit = get_valid_strg("Enter ingredient unit: ").lower()
          factor = calculate_scale_factor(original_servings, target_servings) 
          scaled_amount = math.ceil(scale_ingredient (ingredient_amount, factor))
          
          ingredients.append({
          "name": ingredient_name, "amount": scaled_amount, "unit": ingredient_unit     
          })

     display_scaled_recipe(recipe_name, original_servings, target_servings, ingredients)

if __name__ == "__main__":
     main()
    

