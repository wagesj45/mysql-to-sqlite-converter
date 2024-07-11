# MySQL to SQLite Export Script

## Overview

This script exports data from a MySQL database to an SQLite database. It handles the conversion of MySQL data types to their closest SQLite equivalents, allowing the data to be browsed in SQLite even if some data types are not directly compatible. The script is useful for transferring data from MySQL to SQLite for offline access, backup, or analysis purposes.

## How It Works

1. **Connect to MySQL**: The script connects to a specified MySQL database using the provided credentials and configuration.
2. **Retrieve Tables and Schema**: It fetches all table names and their schemas from the MySQL database.
3. **Create SQLite Tables**: For each table, it converts the MySQL data types to SQLite-compatible types and creates the corresponding tables in the SQLite database.
4. **Transfer Data**: The script fetches all rows from each MySQL table and inserts them into the newly created SQLite tables.
5. **Close Connections**: Finally, the script ensures that all database connections are properly closed.

## Prerequisites

- Python 3.x
- `mysql-connector-python` library
- `sqlite3` library (comes with the standard Python library)

## Installation

1. **Clone the Repository** (if applicable)
   ```sh
   git clone https://git.jordanwages.com/wagesj45/mysql-to-sqlite-converter.git
   cd mysql-to-sqlite-converter
   ```

## Install Required Libraries

```sh
pip install mysql-connector-python
```

## Configuration

Update the `mysql_config` dictionary in the script with your MySQL database details:

```python
mysql_config = {
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'host': 'your_mysql_host',
    'database': 'your_mysql_database',
    'port': 3306
}
```

## Usage

Run the script to export data from MySQL to SQLite:

```sh
python export_mysql_to_sqlite.py
```

## Important Notes

- Data Types Conversion: The script converts MySQL data types to SQLite data types as closely as possible. For example:
   - `INT` in MySQL becomes `INTEGER` in SQLite.
   - `VARCHAR` and `TEXT` in MySQL become `TEXT` in SQLite.
   - `FLOAT`, `DOUBLE`, and `DECIMAL` in MySQL become `REAL` in SQLite.
   - `DATE`, `TIME`, and `YEAR` in MySQL become `TEXT` in SQLite.

- SQLite Database File: The SQLite database file (`output_database.sqlite`) will be created in the same directory as the script. You can change the file name and path as needed.

- Non-Standard MySQL Port: If your MySQL database runs on a non-standard port, ensure to update the port field in the `mysql_config` dictionary.

## Troubleshooting

- Connection Issues: Ensure that the MySQL server is running and accessible, and that the credentials and host information are correct.

-Data Type Compatibility: Some complex MySQL data types may not convert perfectly to SQLite. The script uses the closest compatible types, but you may need to handle specific cases manually if needed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

This script uses the `mysql-connector-python` library for MySQL connectivity and the built-in sqlite3 library for SQLite operations.