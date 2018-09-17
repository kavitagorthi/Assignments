import sqlite3
sqlite_file = '7assignement.sqlite'
table_name1 = 'person6'  # name of the table to be created
col1 = 'Pid' # name of the column
col2 = 'Name' # name of the column
col3 = 'City'
col4 = 'Nick_name'
field_type = 'INTEGER'
lt_person = []
#..........................................................................................
table_name2 = 'Job3'  # name of the table to be created
col1 = 'JOBID' # name of the column
col2 = 'JobName' # name of the column
col3 = 'start_date'
col4 = 'End_date'
col5 = 'Salary'# column data type
field_type = 'INTEGER'
col6 = 'PID'
lt_job =[]
#.....................................................................................

table_name3 = 'Dept1'  # name of the table to be created
col1 = 'Did' # name of the column
col2 = 'DName' # name of the column
col3 = 'Pid'
lt_dept =[]
# Connecting to the database file
'''
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
........................................................Create person table data.................................
# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('CREATE TABLE {tn} ({n1} {ft} PRIMARY KEY)'\
        .format(tn=table_name1, n1=col1, ft=field_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name1, cn=col2))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name1, cn=col3))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name1, cn=col4))

c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (14, 'Vedha','Seattle','Happy')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (13, 'Lora stev','Canada','Lo')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (15, 'Tim stev','Seattle','Tim')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (16, 'Sreeni Rao','China','Sre')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (17, 'Ramesh','India','Lo')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (11, 'George','Seattle','Hap')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (12, 'Larry uv','California','Lo')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (18, 'Ray','China','Lo')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (19, 'Srilatha','India','Hap')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (20, 'Cherry','California','Cherry')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute('COMMIT')
'''
'''
c.execute('SELECT * FROM {tn}'.format(tn = table_name1))
all_rows = c.fetchall()
for i in all_rows:
    lt_person.append(i)
for i in lt_person:
     print("{: >20} {: >20} {: >20}{: >20}".format(i[0], i[1],i[2],i[3]))
'''
'''
........................................................................Create Job Table Data.......................................
table_name2 = 'Job3'  # name of the table to be created
col1 = 'JOBID' # name of the column
col2 = 'JobName' # name of the column
col3 = 'start_date'
col4 = 'End_date'
col5 = 'Salary'# column data type
field_type = 'INTEGER'
col6 = 'PID'
# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({fn}) '\
        .format(tn=table_name2, fn=col1))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name2, cn=col2))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name2, cn=col3))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name2, cn=col4))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name2, cn=col5))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name2, cn=col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (1, 'SR.MANAGER','03-10-2016','06-10-2017','15000','11')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (2, 'MANAGER','02-10-2016','06-12-2017','10000','12')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (3, 'Engineer','01-08-2016','06-10-2017','8000','13')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (4, 'Assit.Engineer','06-03-2016','01-08-2016','7000','13')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (5, 'SR.MANAGER','03-10-2015','06-10-2016','15000','11')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (6, 'Technician','03-10-2016','06-10-2017','8000','14')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (7, 'MANAGER','03-10-2015','06-10-2016','10000','12')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (8, 'Assit.Engineer','03-10-2015','06-10-2016','8000','14')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (1, 'SR.MANAGER','03-10-2016','06-10-2017','15000','11')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (2, 'MANAGER','02-10-2015','06-12-2016','10000','15')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (3, 'Engineer','01-08-2013','06-10-2015','8000','15')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (4, 'Assit.Engineer','06-03-2015','01-08-2015','7000','16')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (5, 'SR.MANAGER','03-10-2015','06-10-2016','15000','16')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (6, 'Technician','03-10-2014','06-10-2015','8000','17')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (7, 'MANAGER','03-10-2015','06-10-2016','10000','17')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4},{n5},{n6}) VALUES (8, 'Assit.Engineer','03-10-2015','06-10-2016','8000','14')". \
          format(tn=table_name2, n1=col1, n2=col2,n3 = col3,n4 = col4,n5=col5,n6 =col6))
c.execute('COMMIT')
.........................................................................Create Dept Table Data............................................................

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('CREATE TABLE {tn} ({n1}) '\
        .format(tn=table_name3, n1=col1))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name3, cn=col2))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name3, cn=col3))

c.execute("INSERT INTO {tn} ({n1}, {n2},{n3}) VALUES (1, 'Civil_Dept','11')". \
          format(tn=table_name3, n1=col1, n2=col2,n3 = col3))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3}) VALUES (1, 'Civil_Dept','13')". \
          format(tn=table_name3, n1=col1, n2=col2,n3 = col3))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3}) VALUES (1, 'Civil_Dept','15')". \
          format(tn=table_name3, n1=col1, n2=col2,n3 = col3))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3}) VALUES (1, 'Civil_Dept','17')". \
          format(tn=table_name3, n1=col1, n2=col2,n3 = col3))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3}) VALUES (2, 'Finance_Dept','12')". \
          format(tn=table_name3, n1=col1, n2=col2,n3 = col3))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3}) VALUES (2, 'Finance_Dept','14')". \
          format(tn=table_name3, n1=col1, n2=col2,n3 = col3))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3}) VALUES (2, 'Finance_Dept','16')". \
          format(tn=table_name3, n1=col1, n2=col2,n3 = col3))
c.execute('COMMIT')


'''
'''
# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT * FROM {tn}'.format(tn = table_name1))
all_rows = c.fetchall()
print("             Person_id        Person_name         Person_city          Person_nickname\n")
for i in all_rows:
    lt_person.append(i)


    print("{: >20} {: >20} {: >20}{: >20}".format(i[0], i[1],i[2],i[3]))
print(".........................................Job table data.......................................................")
c.execute('SELECT * FROM {tn}'.format(tn = table_name2))
all_rows = c.fetchall()
print("                Job_id        Job_title            Start_date          End_date                 Salary          Person_id \n")
for i in all_rows:
    lt_job.append(i)
for i in lt_job:
     print("{: >20} {: >20} {: >20}{: >20}{: >20}{: >20}".format(i[0], i[1],i[2],i[3],i[4],i[5]))

print(".............................................Department table data...................................................")
c.execute('SELECT * FROM {tn}'.format(tn = table_name3))
all_rows = c.fetchall()
print("                Dept_no        Dept_name               Person_id \n")
for i in all_rows:
    lt_dept.append(i)
for i in lt_dept:
     print("{: >20} {: >20} {: >20}".format(i[0], i[1],i[2]))

print("...........................print Dept number,Dept name,Person name...................................")
print("                Dept_no        Dept_name               Person_Name \n")

for i in lt_dept:
    for j in lt_person:
        if(int(i[2])==int(j[0])):
            print("{: >20} {: >20} {: >20}".format(i[0], i[1],j[1]))

print("...........................print Dept number,Dept name,Person name...................................")
print("                Dept_no        Dept_name               Person_Name          Job_title\n")
for i in lt_dept:
    for j in lt_person:
        for k in lt_job:
            if(int(i[2])==int(k[5]) and (k[1]== 'MANAGER') and (int(i[2])==int(j[0]))):
                print("{: >20} {: >20} {: >20}{: >20}".format(i[0], i[1],j[1],k[1]))

print("...........................print Dept number,Dept name,Person name and no.of days worked...................................")
print("                Dept_no        Dept_name            Job_title        Person_name         No.of days worked \n")
from datetime import datetime
date_format = "%m-%d-%Y"
for i in lt_dept:
    for j in lt_job:
        for k in lt_person:
           if(int(i[2])==int(j[5]) and (int(k[0])==int(i[2]))):
            a = datetime.strptime(j[2], date_format)
            b = datetime.strptime(j[3], date_format)
            delta = b - a
            c = delta.days
            if(c > 0):
                print("{: >20} {: >20} {: >20}{: >20}{: >20}".format(i[0], i[1],j[1],k[1],c))

 '''

class print_data:

    def __init__(self):
        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        c.execute('SELECT * FROM {tn}'.format(tn=table_name1))
        all_rows = c.fetchall()
        print("             Person_id        Person_name         Person_city          Person_nickname\n")
        for i in all_rows:
            lt_person.append(i)

            print("{: >20} {: >20} {: >20}{: >20}".format(i[0], i[1], i[2], i[3]))
        print(
            ".........................................Job table data.......................................................")
        c.execute('SELECT * FROM {tn}'.format(tn=table_name2))
        all_rows = c.fetchall()
        print(
            "                Job_id        Job_title            Start_date          End_date                 Salary          Person_id \n")
        for i in all_rows:
            lt_job.append(i)
        for i in lt_job:
            print("{: >20} {: >20} {: >20}{: >20}{: >20}{: >20}".format(i[0], i[1], i[2], i[3], i[4], i[5]))

        print(
            ".............................................Department table data...................................................")
        c.execute('SELECT * FROM {tn}'.format(tn=table_name3))
        all_rows = c.fetchall()
        print("                Dept_no        Dept_name               Person_id \n")
        for i in all_rows:
            lt_dept.append(i)
        for i in lt_dept:
            print("{: >20} {: >20} {: >20}".format(i[0], i[1], i[2]))

        print("...........................print Dept number,Dept name,Person name...................................")
        print("                Dept_no        Dept_name               Person_Name \n")

        for i in lt_dept:
            for j in lt_person:
                if (int(i[2]) == int(j[0])):
                    print("{: >20} {: >20} {: >20}".format(i[0], i[1], j[1]))

        print("...........................print Dept number,Dept name,Person name...................................")
        print("                Dept_no        Dept_name               Person_Name          Job_title\n")
        for i in lt_dept:
            for j in lt_person:
                for k in lt_job:
                    if (int(i[2]) == int(k[5]) and (k[1] == 'MANAGER') and (int(i[2]) == int(j[0]))):
                        print("{: >20} {: >20} {: >20}{: >20}".format(i[0], i[1], j[1], k[1]))

        print(
            "...........................print Dept number,Dept name,Person name and no.of days worked...................................")
        print(
            "                Dept_no        Dept_name            Job_title        Person_name         No.of days worked \n")
        from datetime import datetime
        date_format = "%m-%d-%Y"
        for i in lt_dept:
            for j in lt_job:
                for k in lt_person:
                    if (int(i[2]) == int(j[5]) and (int(k[0]) == int(i[2]))):
                        a = datetime.strptime(j[2], date_format)
                        b = datetime.strptime(j[3], date_format)
                        delta = b - a
                        c = delta.days
                        if (c > 0):
                            print("{: >20} {: >20} {: >20}{: >20}{: >20}".format(i[0], i[1], j[1], k[1], c))


p = print_data()
