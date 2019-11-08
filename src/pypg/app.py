import psycopg2 as pg

#docker inside
db_connector = {
    'host': "postgres",
    'user': "dbuser",
    'dbname': "dbapp",
    'password': "1234"
}

connect_string = "host={host} user={user} dbname={dbname} password={password}".format(
    **db_connector)


# with pg.connect(connect_string) as conn:
#     with conn.cursor() as cur:
#         cur.execute(
#             "CREATE TABLE guser (      id integer primary key,      name varchar(20),      email varchar(20)    );")

def read_tables():
    with pg.connect(connect_string) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")
            for table in cur.fetchall():
                print(table)

def read_dbs():
    sql = '''SELECT datname FROM pg_database;'''
    with pg.connect(connect_string) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            for db in cur.fetchall():
                print(db)

def create_table(table_name):
    sql = f'''CREATE TABLE {table_name} (
        id integer primary key,
        name varchar(20),
        email varchar(20)
    );
    '''
    print(sql)
    try:
        conn = pg.connect(connect_string) #db 연결(로그인)
        cur = conn.cursor() #db 작업할 지시자 설정
        cur.execute(sql) #sql문 실행

        #db 저장 및 종료
        conn.commit()
        conn.close()
    except pg.OperationalError as e:
        print(e)

def main():
    print("pg!")
    read_dbs()
    #create_table("student")
    print("---tables---")
    read_tables()




if __name__ == ("__main__"):
    main()