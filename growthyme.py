import psycopg2
from psycopg2.extras import DictCursor

# Database connection using the full connection string format with the endpoint parameter
def get_db_connection():
    try:
        # Corrected connection string
        conn = psycopg2.connect(
            "postgres://neondb_owner:6kiP4JQEtVgm@ep-red-bar-a5wncap9-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require&options=endpoint%3Dep-red-bar-a5wncap9"
        )
        print("Connection successful!")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to write to the session transcript in the desired format
def write_to_transcript(crop, planting_months=None, harvesting_months=None, soil_conditions=None, estimated_yield=None):
    with open("session_transcript.txt", "a") as file:
        file.write(f"Crop Name: {crop}\n")
        if planting_months:
            file.write(f"Optimal Planting Months: {planting_months}\n")
        if harvesting_months:
            file.write(f"Optimal Harvesting Months: {harvesting_months}\n")
        if soil_conditions:
            file.write(f"Soil Condition Guide for {crop}: {soil_conditions}\n")
        if estimated_yield:
            file.write(f"Estimated Yield for {crop}: {estimated_yield}\n")
        file.write("\n")  # Blank line between different crop details

# Introduction Function
def introduction():
    intro_text = "Welcome to GrowThyme: Crop Plantation Season!\nThis app provides farmers with guidance on the best planting times to maximize crop yields.\nYou can select from different options in the menu, including entering crop details, viewing seasonal calendars, and more.\n"
    print(intro_text)
    write_to_transcript("Welcome to GrowThyme: Crop Plantation Season!")

# Validate user-inputted crop name
def validate_crop(crop_name):
    try:
        conn = get_db_connection()
        if conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT crop_name FROM crops WHERE crop_name ILIKE %s;", (crop_name,))
                result = cur.fetchone()
                return result['crop_name'] if result else None
    except Exception as e:
        print(f"Error validating crop: {e}")
    finally:
        if conn:
            conn.close()

# Crop Selection Function
def select_crop():
    while True:
        crop_name = input("Please enter the name of the crop you want to select: ").strip()
        validated_crop = validate_crop(crop_name)
        if validated_crop:
            print(f"You selected: {validated_crop}\n")
            write_to_transcript(f"Crop Name: {validated_crop}")
            return validated_crop
        else:
            print("Crop not found in our database. Please try again or check the spelling.\n")

# Fetch seasonal calendar for a crop
def fetch_seasonal_calendar(crop):
    try:
        conn = get_db_connection()
        if conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT planting_months, harvesting_months FROM seasonal_calendar WHERE crop_name = %s;", (crop,))
                result = cur.fetchone()
                if result:
                    return result['planting_months'], result['harvesting_months']
                else:
                    return None, None
    except Exception as e:
        print(f"Error fetching seasonal calendar: {e}")
    finally:
        if conn:
            conn.close()

# Seasonal Calendar Function
def seasonal_calendar(crop):
    planting, harvesting = fetch_seasonal_calendar(crop)
    if planting:
        calendar_info = f"Optimal Planting Months: {planting}\n"
        print(calendar_info)
        write_to_transcript(crop, planting_months=planting)

        # Ask the user if they'd like to see the harvesting time
        show_harvesting = input(f"Would you like to see the harvesting months for {crop}? (y/n): ").strip().lower()
        if show_harvesting == 'y' and harvesting:
            harvesting_info = f"Optimal Harvesting Months: {harvesting}\n"
            print(harvesting_info)
            write_to_transcript(crop, harvesting_months=harvesting)
        elif show_harvesting != 'y':
            print("Skipping harvesting months display.\n")
    else:
        print(f"Sorry, we don't have seasonal information for {crop}.\n")

# Fetch soil condition for a crop
def fetch_soil_conditions(crop):
    try:
        conn = get_db_connection()
        if conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT soil_conditions FROM soil_guides WHERE crop_name = %s;", (crop,))
                result = cur.fetchone()
                return result['soil_conditions'] if result else None
    except Exception as e:
        print(f"Error fetching soil conditions: {e}")
    finally:
        if conn:
            conn.close()

# Soil Condition Guide Function
def soil_condition_guide(crop):
    soil_conditions = fetch_soil_conditions(crop)
    if soil_conditions:
        soil_info = f"Soil Condition Guide for {crop}: {soil_conditions}\n"
        print(soil_info)
        write_to_transcript(crop, soil_conditions=soil_conditions)
    else:
        print(f"Sorry, we don't have soil condition information for {crop}.\n")

# Yield Estimation Function
def fetch_yield_estimation(crop, planting_date):
    try:
        conn = get_db_connection()
        if conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT estimated_yield FROM yield_estimations WHERE crop_name = %s;", (crop,))
                result = cur.fetchone()
                return result['estimated_yield'] if result else None
    except Exception as e:
        print(f"Error fetching yield estimation: {e}")
    finally:
        if conn:
            conn.close()

def yield_estimation(crop):
    planting_date = input("Enter your planned planting date (e.g., 2024-03-15): ")
    estimated_yield = fetch_yield_estimation(crop, planting_date)
    if estimated_yield:
        yield_info = f"Estimated Yield for {crop}: {estimated_yield} based on the planting date {planting_date}.\n"
        print(yield_info)
        write_to_transcript(crop, estimated_yield=yield_info)
    else:
        print(f"Sorry, we don't have yield estimation data for {crop}.\n")

# Main Menu Function
def main_menu():
    introduction()
    crop = None
    while True:
        print("\nMain Menu:")
        print("1. Enter Crop Name")
        print("2. View Seasonal Calendar")
        print("3. Check Soil Conditions")
        print("4. Estimate Yield")
        print("5. Exit")
        try:
            choice = int(input("Please choose an option: "))
            if choice == 1:
                crop = select_crop()
            elif choice == 2:
                if crop:
                    seasonal_calendar(crop)
                else:
                    print("Please enter a crop name first.\n")
            elif choice == 3:
                if crop:
                    soil_condition_guide(crop)
                else:
                    print("Please enter a crop name first.\n")
            elif choice == 4:
                if crop:
                    yield_estimation(crop)
                else:
                    print("Please enter a crop name first.\n")
            elif choice == 5:
                print("Thank you for using GrowThyme. Goodbye!")
                write_to_transcript("Session Ended.\n")
                break
            else:
                print("Invalid choice. Please select a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    # After session ends, ask user if they'd like to download and open the transcript
    download_transcript()

# Function to allow user to download and open transcript
def download_transcript():
    try:
        with open("session_transcript.txt", "r") as file:
            transcript_content = file.read()
            print("Your session transcript has been saved!")
            print("Would you like to open it now? (y/n)")
            open_choice = input().strip().lower()
            if open_choice == "y":
                print("\nTranscript content:\n")
                print(transcript_content)
            else:
                print("You can open the transcript later at any time.")
    except FileNotFoundError:
        print("No transcript found!")

# Run the application
if __name__ == "__main__":
    main_menu()
