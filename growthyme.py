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
    # Data for planting and harvesting times for demonstration
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

# Main Function to run the first three features
def main():
    introduction()
    crop = None

    while not crop:
        crop = select_crop()
    
    seasonal_calendar(crop)

# Run the application
if __name__ == "__main__":
    main()

