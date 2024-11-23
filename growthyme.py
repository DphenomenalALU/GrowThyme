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

# Introduction Function
def introduction():
    print("Welcome to GrowThyme: Crop Plantation Season!")
    print("This app provides farmers with guidance on the best planting times to maximize crop yields.")
    print("You can select from different options in the menu, including entering crop details, viewing seasonal calendars, and more.\n")

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
    if planting and harvesting:
        print(f"Optimal Planting Months for {crop}: {planting}")
        print(f"Optimal Harvesting Months for {crop}: {harvesting}\n")
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
        print(f"Soil Condition Guide for {crop}: {soil_conditions}\n")
    else:
        print(f"Sorry, we don't have soil condition information for {crop}.\n")

