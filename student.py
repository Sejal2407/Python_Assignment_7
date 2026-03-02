import psycopg2

def manage_student_data():
    conn = None
    try:
        # 1. Connect to PostgreSQL
        
        conn = psycopg2.connect(dbname="college",user="postgres",password="sejal24post",host="localhost",port="5433")
        cur = conn.cursor()

        # 2. Create table if it doesn't exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INTEGER,
                grade VARCHAR(10)
            );
        ''')
        conn.commit()

        # 3. Take User Input
        print("\n--- Enter New Student ---")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")

        # 4. Insert Data
        cur.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
        conn.commit()
        print("Data saved successfully.\n")

        # 5. Fetch Data using fetchone()
        print("--- Current Student List ---")
        cur.execute("SELECT id, name, age, grade FROM students;")

        while True:
            row = cur.fetchone()
            if row is None:  # Break the loop if no more rows are found
                break
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Grade: {row[3]}")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print("\nDatabase connection closed.")

manage_student_data()