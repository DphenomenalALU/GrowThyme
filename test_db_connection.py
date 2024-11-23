import psycopg2
from psycopg2.extras import DictCursor

def get_db_connection():
    return psycopg2.connect(
        "postgres://neondb_owner:6kiP4JQEtVgm@ep-red-bar-a5wncap9-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require&options=endpoint%3Dep-red-bar-a5wncap9"
    )

try:
    conn = get_db_connection()
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("SELECT 1;")
        print("Database connected successfully!")
except Exception as e:
    print(f"Database connection failed: {e}")
finally:
    if conn:
        conn.close()