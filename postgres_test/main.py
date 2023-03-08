import psycopg2

conn = psycopg2.connect(host="localhost", dbname="dvdrental", user="postgres", password="password", port=5432)

cursor = conn.cursor()

cursor.execute(
    """ 
    Create table if not exists table1_test(
    id int primary key,
    name varchar(255),
    age int,
    gender char
    );
    """
)

cursor.execute("truncate table table1_test;")
cursor.execute(
    """ 
    insert into table1_test(id, name, age, gender) values
    (1, 'Mike', 30, 'm'),
    (2, 'Lisa', 54, 'f'),
    (3, 'John', 50, 'm'),
    (4, 'Bob', 40, 'm'),
    (5, 'Julie', 80, 'f');
    """
)

cursor.execute("select * from table1_test where name = 'Bob';")
print(cursor.fetchone())
print("===========================")

cursor.execute(""" select * from table1_test where age < 50""")
for row in cursor.fetchall():
    print(row)


print("===========================")
sql = cursor.mogrify("""select * from table1_test where starts_with(name, %s) and age < %s;""", ("M", 50))
print(f"query: {sql}")

cursor.execute(sql)
print(cursor.fetchall())


# Close cursor and connection
conn.commit()
cursor.close()
conn.close()
