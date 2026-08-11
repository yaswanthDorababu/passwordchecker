import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = "passwordchecker.db"


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            result TEXT NOT NULL,
            score INTEGER NOT NULL,
            is_common INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    connection.commit()
    connection.close()


def create_user(name, email, password):
    connection = get_db()
    cursor = connection.cursor()

    password_hash = generate_password_hash(password)

    try:
        cursor.execute(
            """
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
            """,
            (name, email, password_hash)
        )

        connection.commit()
        user_id = cursor.lastrowid
        connection.close()

        print("USER CREATED:", email)
        return user_id

    except sqlite3.IntegrityError:
        connection.close()
        print("EMAIL ALREADY EXISTS:", email)
        return None


def get_user_by_email(email):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()
    connection.close()

    return user


def save_history(user_id, result, score, is_common):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO history
        (user_id, result, score, is_common)
        VALUES (?, ?, ?, ?)
        """,
        (user_id, result, score, int(is_common))
    )

    connection.commit()
    connection.close()


def get_history(user_id):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM history
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    history = cursor.fetchall()
    connection.close()

    return history


if __name__ == "__main__":
    create_tables()
    print("Database created successfully.")
    
def get_dashboard_stats(user_id):
    connection = get_db()
    cursor = connection.cursor()

    # Total password checks
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE user_id = ?
        """,
        (user_id,)
    )
    total_checks = cursor.fetchone()[0]

    # Excellent passwords
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE user_id = ?
        AND result = 'Excellent'
        """,
        (user_id,)
    )
    strong_passwords = cursor.fetchone()[0]

    # Good passwords
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE user_id = ?
        AND result = 'Good'
        """,
        (user_id,)
    )
    good_passwords = cursor.fetchone()[0]

    # Weak passwords
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE user_id = ?
        AND result = 'Weak'
        """,
        (user_id,)
    )
    weak_passwords = cursor.fetchone()[0]

    connection.close()

    return {
        "total_checks": total_checks,
        "strong_passwords": strong_passwords,
        "good_passwords": good_passwords,
        "weak_passwords": weak_passwords
    }
