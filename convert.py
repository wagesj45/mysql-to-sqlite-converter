import mysql.connector
import sqlite3

# MySQL connection details
mysql_config = {
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'host': 'your_mysql_host',
    'database': 'your_mysql_database',
    'port': 3306
}

# Connect to MySQL
mysql_conn = mysql.connector.connect(**mysql_config)
mysql_cursor = mysql_conn.cursor()

# Connect to SQLite
sqlite_conn = sqlite3.connect('output_database.sqlite')
sqlite_cursor = sqlite_conn.cursor()

# Get all tables from MySQL
mysql_cursor.execute("SHOW TABLES")
tables = mysql_cursor.fetchall()

for (table_name,) in tables:
    # Get table schema from MySQL
    mysql_cursor.execute(f"DESCRIBE {table_name}")
    schema = mysql_cursor.fetchall()

    # Create table in SQLite
    columns = []
    for column in schema:
        col_name = column[0]
        col_type = column[1]

        # Convert MySQL data types to SQLite
        if "int" in col_type:
            sqlite_type = "INTEGER"
        elif "char" in col_type or "text" in col_type:
            sqlite_type = "TEXT"
        elif "blob" in col_type:
            sqlite_type = "BLOB"
        elif "float" in col_type or "double" in col_type or "decimal" in col_type:
            sqlite_type = "REAL"
        elif "date" in col_type or "time" in col_type or "year" in col_type:
            sqlite_type = "TEXT"
        else:
            sqlite_type = "TEXT"

        columns.append(f"{col_name} {sqlite_type}")

    columns_str = ", ".join(columns)
    sqlite_cursor.execute(f"CREATE TABLE {table_name} ({columns_str})")

    # Fetch data from MySQL table
    mysql_cursor.execute(f"SELECT * FROM {table_name}")
    rows = mysql_cursor.fetchall()

    # Insert data into SQLite table
    placeholders = ", ".join(["?" for _ in columns])
    sqlite_cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", rows)
    sqlite_conn.commit()

# Close connections
mysql_cursor.close()
mysql_conn.close()
sqlite_cursor.close()
sqlite_conn.close()

print("Data has been successfully exported to SQLite.")
