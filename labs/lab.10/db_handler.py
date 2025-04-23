import psycopg2
from config import load_config

def connect_db():
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print("Database connection error:", error)
        return None

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
    
    try:
        conn = connect_db()
        with conn.cursor() as cur:
            for command in commands:
                cur.execute(command)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error creating tables:", error)
    finally:
        if conn:
            conn.close()

def get_or_create_user(username):
    conn = connect_db()
    try:
        with conn.cursor() as cur:
            # Check if user exists
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            user_id = cur.fetchone()
            
            if user_id:
                return user_id[0]
            else:
                # Create new user
                cur.execute("INSERT INTO users(username) VALUES(%s) RETURNING id", (username,))
                user_id = cur.fetchone()[0]
                conn.commit()
                return user_id
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error in get_or_create_user:", error)
        return None
    finally:
        if conn:
            conn.close()

def get_last_score(user_id):
    conn = connect_db()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT score, level FROM user_scores 
                WHERE user_id = %s 
                ORDER BY saved_at DESC 
                LIMIT 1
            """, (user_id,))
            result = cur.fetchone()
            return result if result else (0, 1)
    except (psycopg2.DatabaseError, Exception) as error:
        print("error", error)
        return (0, 1)
    finally:
        if conn:
            conn.close()

def save_score(user_id, score, level):
    conn = connect_db()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_scores(user_id, score, level)
                VALUES(%s, %s, %s)
            """, (user_id, score, level))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("error", error)
    finally:
        if conn:
            conn.close()