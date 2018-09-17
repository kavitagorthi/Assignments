from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

list_data =[]   #this is donar list adding  to the list
allist =[]   #to keep track how many times the donar name in the list
unique_name = []  # unique donar names
list_sum = []     # donar names and total amount and number of times donated
list_add =[]

class donar():
    def __data(self,name,amount):
        self.donarname = name
        self.donaramount = amount
        alldata = (name,amount,1)
        data = (name)
        list_data.append(alldata)
        allist.append(data)

    def donarname(self):
        self.__data("mike",80)
        self.__data("ketty",175)
        self.__data("john hoop",45)
        self.__data("ravi",780)
        self.__data("david",123)
        self.__data("bratte",45)
        self.__data("mike", 180)
        self.__data("mike", 800)
        self.__data("david",100)

    def  countname(self):
        import collections
        k = allist
        counter = collections.Counter(k)       #how many times the donar name in the donation list
        uniname = set(allist)
        for i in uniname:
            unique_name.append(i)          #this is unique names of the donar

        for i in unique_name:        #this will find the sum of the donation amount and number of times donated
            sum = 0
            times = 0
            for j in list_data:
                 if(i == j[0]):
                    sum = sum+j[1]
                    times = times+j[2]
                    all =(j[0],sum,times)
                    if(counter[i] == times):
                      list_sum.append(all)

    def report(self):
        print("+----------------------------+------------------+-------------------+-------------------+")
        print("|     Donar Name             |  Total given     | Number of gifts   |    Average gift   |")
        print("+----------------------------+------------------+-------------------+--------------------")

        for i in list_sum:
            name = i[0].upper()
            total = '$' + str(i[1])
            avg = i[2]
            k = int(i[1] / i[2])
            avggift = '$' + str(k)
            print("{: >20} {: >20} {: >20} {: >20}".format(name, total, avg, avggift))

    def sendmail(self, listm):
        listd = listm
        for i in listd:
              a = i[0].upper()
              b = '$' + str(i[1])
              file = open("{}"".txt".format(a), 'a+')
              file.write("  Dear  ""{}".format(a))
              file.write("\n")
              file.write(" \n")
              file.write("    Thank you for your very kind donation of ")
              file.write("{}".format(b))
              file.write("\n")
              file.write("\n")
              file.write("    It will be used for very good cause.")
              file.write("\n")
              file.write("           Sincerely, \n")
              file.write("          -The Team  ")
              file.close

class  donarreport(donar):

   def  __init__(self):
        print("Menu:")
        print("1.Send thank you mail")
        print("2.Create report")
        print("3.Add donars")
        print("4.quit")
        i = int(input("enter your choice 1 or 2 or 3 or 4:       "))
        if (i == 2):
            s = donar()
            s.donarname()
            s.countname()
            s.report()
        elif(i == 1):
            s = donar()
            s.donarname()
            s.countname()
            l = list_sum
            s.sendmail(l)
            print("The Thank you mail has been send to the list of donars")
            for i in l:
                print(i[0].upper())


        elif(i == 3):
            self.add_donar()
            s = donar()
            s.donarname()
            s.countname()
            s.report()


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    donation_amount = TextField('Amount:', validators=[validators.required()])


@app.route('/')
def hello_world():
    form = ReusableForm(request.form)
    e = donarreport()
    if request.method == 'POST':
        name = request.form['name']
        donation_amount = request.form['amount']
        email = request.form['email']
        data = (name,donation_amount,1)
        s = donar()
        list_add.append(data)
        list_data.append(data)
        alist.append(name)
        print(name, " ", email, " ", donation_amount)
    return render_template('hello.html', form=form)



if __name__ == '__main__':
    app.run()