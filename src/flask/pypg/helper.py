import psycopg2 as pg
import psycopg2.extras #field명을 알 때 활용

#docker inside
db_connector = {
    'host': "postgres",
    'user': "dbuser",
    'dbname': "dbapp",
    'password': "1234"
}

connect_string = "host={host} user={user} dbname={dbname} password={password}".format(
    **db_connector)


def read_tables():
    tables = []
    with pg.connect(connect_string) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")
            for table in cur.fetchall():
                tables.append(table)
        
        return tables

def read_dbs():
    sql = '''SELECT datname FROM pg_database;'''
    with pg.connect(connect_string) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            for db in cur.fetchall():
                print(db)

def create_table(table_name):
    sql = f'''CREATE TABLE {table_name} (
        name varchar(100),
        phone varchar(100)
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


def insert(table_name, name, phone):
    sql = f'''INSERT INTO {table_name} 
        VALUES('{name}', '{phone}');
        '''
    print(sql)
    try:
        conn = pg.connect(connect_string) 
        cur = conn.cursor() 
        cur.execute(sql) 

        conn.commit()
        conn.close()
    except pg.OperationalError as e:
        print(e)
        return -1
    
    return 0


def select(table_name, name):
    sql = f'''SELECT name, phone FROM {table_name} WHERE name LIKE '%{name}%';
    '''
    print(sql)
    try:
        conn=pg.connect(connect_string) 
        cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(sql)
        result=cur.fetchall()  
       
        conn.close()
        return result
    except Exception as e:
        print(e)
        return[]


def count(table_name, name):
    sql = f'''SELECT COUNT(*) FROM {table_name} WHERE name LIKE '%{name}%';
    '''
    print(sql)
    try:
        conn=pg.connect(connect_string) 
        cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(sql)
        result=cur.fetchall()  
       
        conn.close()
        return result
    except Exception as e:
        print(e)
        return[]


def delete(table_name, name):
    sql = f'''DELETE FROM {table_name} WHERE name='{name}';
    '''
    print(sql)
    try:
        conn = pg.connect(connect_string) 
        cur = conn.cursor() 
        cur.execute(sql) 

        conn.commit()
        conn.close()
    except pg.OperationalError as e:
        print(e)
        return -1
    
    return 0


def update(table_name, name, phone):
    sql = f'''UPDATE {table_name} SET phone='{phone}' WHERE name='{name}';
    '''
    print(sql)
    try:
        conn = pg.connect(connect_string) 
        cur = conn.cursor() 
        cur.execute(sql) 

        conn.commit()
        conn.close()
    except pg.OperationalError as e:
        print(e)
        return -1
    
    return 0


def students_list():
    sql = f'''SELECT name, phone FROM student
    '''
    try:
        conn=pg.connect(connect_string) 
        cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(sql)
        result=cur.fetchall() 
      
        conn.close()
        return result
    except Exception as e:
        print(e)
        return[]

