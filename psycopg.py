import psycopg2

# Define the colors and their frequencies
colors = {
    "GREEN": 7,
    "YELLOW": 4,
    "BROWN": 4,
    "BLUE": 22,
    "PINK": 4,
    "ORANGE": 8,
    "CREAM": 2,
    "RED": 11,
    "WHITE": 14,
    "ARSH": 1,
    "BLEW": 1,
    "BLACK": 2,
    "WHITE": 6,
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    port="your_port",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create a cursor object to execute database queries
cur = conn.cursor()

# Create a table to store the colors and frequencies
cur.execute("""
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(255) PRIMARY KEY,
        frequency INTEGER
    )
""")

# Insert the colors and frequencies into the database
for color, frequency in colors.items():
    cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()