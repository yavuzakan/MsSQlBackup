import pypyodbc as odbc
from datetime import datetime

simdi = datetime.today().strftime('%Y-%m-%d')
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'localhost'
DATABASE_NAME = ''
username = 'sa'
password = ''
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={{{SERVER_NAME}}};
    DATABASE={{{DATABASE_NAME}}};
    Trust_Connection=yes;
    uid={{{username}}};
    pwd={{{password}}};
"""
conn = odbc.connect(connection_string)
print(conn)
backup = "c:\\backup\\"+simdi+DATABASE_NAME+".bak"
sql = "BACKUP DATABASE ["+DATABASE_NAME+"] TO DISK = N'{0}'".format(backup)
cursor = conn.cursor().execute(sql)
while cursor.nextset():
     pass
conn.close()