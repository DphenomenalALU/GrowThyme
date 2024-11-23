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

