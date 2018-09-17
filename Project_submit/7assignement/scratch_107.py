import sqlite3
sqlite_file = '7assignement_2.sqlite'
table_name1 = 'Donar'  # name of the table to be created
col1 = 'Pid' # name of the column
col2 = 'Name' # name of the column
col3 = 'City'
col4 = 'Amount'
field_type = 'INTEGER'
# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
'''
c.execute('CREATE TABLE {tn} ({n1} {ft} PRIMARY KEY)'\
        .format(tn=table_name1, n1=col1, ft=field_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name1, cn=col2))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name1, cn=col3))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name1, cn=col4))

c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (1, 'Vedha','Seattle','100')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (2, 'Lora stev','Canada','10')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (3, 'Tim stev','Seattle','40')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (4, 'Sreeni Rao','China','200')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (5, 'Ramesh','India','50')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (6, 'George','Seattle','60')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (7, 'Larry uv','California','90')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (8, 'Vedha','Seattle','200')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (9, 'Vedha','Seattle','20')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute("INSERT INTO {tn} ({n1}, {n2},{n3},{n4}) VALUES (10, 'Sreeni Rao','China','40')". \
          format(tn=table_name1, n1=col1, n2=col2,n3 = col3,n4 = col4))
c.execute('COMMIT')

'''
c.execute('SELECT * FROM {tn}'.format(tn = table_name1))
all_rows = c.fetchall()
for i in all_rows:
    print(i)
c.execute('SELECT NAME, SUM(AMOUNT),COUNT(NAME)  FROM Donar GROUP BY NAME')
all_rows = c.fetchall()
for i in all_rows:
    print(i)

class  donar:

   def  __init__(self):
        print("Menu:")
        print("1.Send thank you mail to the donars")
        print("2.Create report")
        print("3.Add donars")
        print("4.quit")
        i = int(input("enter your choice 1 or 2 or 3 or 4:       "))
        c.execute('SELECT NAME,CITY, SUM(AMOUNT),COUNT(NAME)  FROM Donar GROUP BY NAME,CITY')
        all_rows = c.fetchall()

        if (i == 2):

            print("...........................This is the  Donars Report..................................")
            print("           Donar_Name        Donar_City           Donated_amount      No.of Times Donated  \n")
            for i in all_rows:
                   k = '$'+str(i[2])
                   print("{: >20} {: >20} {: >20}{: >20}".format(i[0], i[1], k,i[3]))
        elif(i == 1):
            print("...........................The Thankyou mail is send to the list of Donars..................................")
            print("           Donar_List\n")
            for i in all_rows:
                print("{: >20}".format(i[0]))
            for i in all_rows:
              k = '$'+str(i[2])
              file = open("{}"".txt".format(i[0]), 'a+')
              file.write("  Dear  ""{}".format(i[0]))
              file.write("\n")
              file.write(" \n")
              file.write("    Thank you for your very kind donation of ")
              file.write("{}".format(k))
              file.write("\n")
              file.write("\n")
              file.write("    It will be used for very good cause.")
              file.write("\n")
              file.write("           Sincerely, \n")
              file.write("          -The Team  ")
              file.close

        elif(i == 3):
            def add_donar():

                sqlite_file = '7assignement_2.sqlite'
                table_name1 = 'Donar'  # name of the table to be created
                col1 = 'Pid'  # name of the column
                col2 = 'Name'  # name of the column
                col3 = 'City'
                col4 = 'Amount'
                field_type = 'INTEGER'
                # Connecting to the database file
                conn = sqlite3.connect(sqlite_file)
                c = conn.cursor()
                ID = int(input("enter no   "))
                NAME= input("enter name   ")
                CITY = input("enter city  ")
                AMOUNT = int(input("enter amount to donate   "))

                c.execute('INSERT INTO DONAR(PID,NAME,CITY,AMOUNT) VALUES (?,?,?,?)',(ID,NAME,CITY,AMOUNT))
                c.execute('COMMIT')
                print("do you want to add any donars  ")
                k = input("enter y/n  ")
                if (k == 'y' or k == 'Y'):
                    add_donar()
                elif (k == 'n' or k == 'N'):
                    c.execute('SELECT NAME,CITY, SUM(AMOUNT),COUNT(NAME)  FROM Donar GROUP BY NAME,CITY')
                    all_rows = c.fetchall()
                    print("...........................This is the  Donars Report..................................")
                    print("           Donar_Name        Donar_City           Donated_amount      No.of Times Donated  \n")
                    for i in all_rows:
                        k = '$' + str(i[2])
                        print("{: >20} {: >20} {: >20}{: >20}".format(i[0], i[1], k, i[3]))



            add_donar()


donar()

'''..................................output of the code.........................................................
Menu:
1.Send thank you mail to the donars
2.Create report
3.Add donars
4.quit
enter your choice 1 or 2 or 3 or 4:       3
enter no   26
enter name   hema
enter city  India
enter amount to donate   120
do you want to add any donars
enter y/n  y
enter no   27
enter name   Vanaja
enter city  London
enter amount to donate   33
do you want to add any donars
enter y/n  n
...........................This is the  Donars Report..................................
           Donar_Name        Donar_City           Donated_amount      No.of Times Donated

              George              Seattle                  $60                   1
            Larry uv           California                  $90                   1
           Lora stev               Canada                  $10                   1
              Ramesh                India                  $50                   1
          Sreeni Rao                China                 $240                   2
            Tim stev              Seattle                  $40                   1
              Vanaja               London                  $33                   1
               Vedha              Seattle                 $320                   3
                hema                India                 $120                   1
              kavita                   90                  $40                   1

Process finished with exit code 0
