# Introduction Function: Greets the user and explains the application
def introduction():
    print("Welcome to GrowThyme: Crop Plantation Season!")
    print("This app provides farmers with guidance on the best planting times to maximize crop yields.")
    print("You can select from different options in the menu, including crop selection, viewing seasonal calendars, and more.\n")

# Crop Selection Function: Allows users to select from a list of crops
def select_crop():
    crops = ["Maize", "Beans", "Tomatoes", "Potatoes", "Carrots", "Onions"]
    print("Available Crops:")
    for idx, crop in enumerate(crops, 1):
        print(f"{idx}. {crop}")
    try:
        choice = int(input("Please enter the number of the crop you want to select: ")) - 1
        if 0 <= choice < len(crops):
            return crops[choice]
        else:
            print("Invalid selection. Please select a valid crop number.\n")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return None

# Seasonal Calendar Function: Displays planting and harvesting months for the selected crop
def seasonal_calendar(crop):
    calendar = {
        "Maize": ("March-April", "August-September"),
        "Beans": ("April-May", "July-August"),
        "Tomatoes": ("May-June", "September-October"),
        "Potatoes": ("February-March", "July-August"),
        "Carrots": ("February-March", "June-July"),
        "Onions": ("March-April", "August-September")
    }
    if crop in calendar:
        planting, harvesting = calendar[crop]
        print(f"Optimal Planting Months for {crop}: {planting}")
        print(f"Optimal Harvesting Months for {crop}: {harvesting}\n")
    else:
        print(f"Sorry, we don't have seasonal information for {crop}.\n")

# Soil Condition Guide Function: Provides soil preparation tips
def soil_condition_guide(crop):
    soil_conditions = {
        "Maize": "Well-drained loamy soil with a pH of 6.0 to 7.0. Prepare by tilling and adding organic matter.",
        "Beans": "Loamy soil with good drainage and a pH of 6.0 to 7.5. Add compost for better yield.",
        "Tomatoes": "Rich, well-drained soil with a pH of 6.2 to 6.8. Use organic fertilizers.",
        "Potatoes": "Light, well-drained sandy loam soil with a pH of 5.5 to 7.0. Avoid waterlogged areas.",
        "Carrots": "Deep, loose sandy loam soil with a pH of 6.0 to 6.8. Remove rocks for straight growth.",
        "Onions": "Loamy soil with good drainage and a pH of 6.0 to 7.0. Add compost or well-rotted manure."
    }
    if crop in soil_conditions:
        print(f"Soil Condition Guide for {crop}: {soil_conditions[crop]}\n")
    else:
        print(f"Sorry, we don't have soil condition information for {crop}.\n")

# Yield Estimation Function: Estimates yield based on planting date
def yield_estimation(crop):
    try:
        planting_date = input("Enter your planned planting date (e.g., 2024-03-15): ")
        # Dummy yield logic for demonstration
        yield_estimates = {
            "Maize": "3,500 kg/ha",
            "Beans": "1,500 kg/ha",
            "Tomatoes": "25,000 kg/ha",
            "Potatoes": "20,000 kg/ha",
            "Carrots": "30,000 kg/ha",
            "Onions": "20,000 kg/ha"
        }
        if crop in yield_estimates:
            print(f"Estimated Yield for {crop}: {yield_estimates[crop]} based on the planting date {planting_date}.\n")
        else:
            print(f"Sorry, we don't have yield estimation data for {crop}.\n")
    except Exception as e:
        print(f"Error in yield estimation: {e}")

# Main Menu Function: Displays menu and handles user navigation
def main_menu():
    while True:
        print("Main Menu:")
        print("1. Select Crop")
        print("2. View Seasonal Calendar")
        print("3. Check Soil Conditions")
        print("4. Estimate Yield")
        print("5. Exit")
        try:
            choice = int(input("Please choose an option: "))
            if choice == 1:
                crop = None
                while not crop:
                    crop = select_crop()
            elif choice == 2:
                if 'crop' in locals() and crop:
                    seasonal_calendar(crop)
                else:
                    print("Please select a crop first.\n")
            elif choice == 3:
                if 'crop' in locals() and crop:
                    soil_condition_guide(crop)
                else:
                    print("Please select a crop first.\n")
            elif choice == 4:
                if 'crop' in locals() and crop:
                    yield_estimation(crop)
                else:
                    print("Please select a crop first.\n")
            elif choice == 5:
                print("Thank you for using GrowThyme. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

# Run the application
if __name__ == "__main__":
    introduction()
    main_menu()
