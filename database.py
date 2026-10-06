import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    return conn


def create_db_table():
    try:
        conn = connect_to_db()

        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL
            );
        """)

        conn.commit()
        print("User table created successfully")

    except Exception as e:
        print("User table creation failed:", e)

    finally:
        conn.close()


def get_users():
    users = []

    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        for row in rows:
            users.append({
                "user_id": row["user_id"],
                "name": row["name"],
                "email": row["email"],
                "phone": row["phone"],
                "address": row["address"],
                "country": row["country"]
            })

    except Exception as e:
        print("Get users failed:", e)

    finally:
        conn.close()

    return users


def get_user_by_id(user_id):
    user = {}

    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE user_id = ?",
            (user_id,)
        )

        row = cur.fetchone()

        if row:
            user = {
                "user_id": row["user_id"],
                "name": row["name"],
                "email": row["email"],
                "phone": row["phone"],
                "address": row["address"],
                "country": row["country"]
            }

    except Exception as e:
        print("Get user failed:", e)

    finally:
        conn.close()

    return user


def insert_user(user):
    inserted_user = {}

    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO users
            (name, email, phone, address, country)
            VALUES (?, ?, ?, ?, ?)
        """, (
            user["name"],
            user["email"],
            user["phone"],
            user["address"],
            user["country"]
        ))

        conn.commit()

        inserted_user = get_user_by_id(cur.lastrowid)

    except Exception as e:
        conn.rollback()
        print("Insert failed:", e)

    finally:
        conn.close()

    return inserted_user


def update_user(user):
    updated_user = {}

    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute("""
            UPDATE users
            SET name = ?,
                email = ?,
                phone = ?,
                address = ?,
                country = ?
            WHERE user_id = ?
        """, (
            user["name"],
            user["email"],
            user["phone"],
            user["address"],
            user["country"],
            user["user_id"]
        ))

        conn.commit()

        updated_user = get_user_by_id(user["user_id"])

    except Exception as e:
        conn.rollback()
        print("Update failed:", e)

    finally:
        conn.close()

    return updated_user


def patch_user(user_id, data):
    try:
        current_user = get_user_by_id(user_id)

        if not current_user:
            return {}

        for field in ["name", "email", "phone", "address", "country"]:
            if field in data:
                current_user[field] = data[field]

        return update_user(current_user)

    except Exception as e:
        print("Patch failed:", e)
        return {}


def delete_user(user_id):
    message = {}

    try:
        conn = connect_to_db()

        conn.execute(
            "DELETE FROM users WHERE user_id = ?",
            (user_id,)
        )

        conn.commit()

        message["status"] = "User deleted successfully"

    except Exception as e:
        conn.rollback()
        print("Delete failed:", e)
        message["status"] = "Cannot delete user"

    finally:
        conn.close()

    return message