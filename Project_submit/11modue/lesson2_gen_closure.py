
import csv

class fav_artist:

    def __init__(self):
        with open('singer.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            self.all_rawdata = []
            self.all_artists = []
            self.all_unique = []
            self.fav_unique = []
            for row in reader:  # Number of rows including the death rates
                self.all_rawdata.append(row)
            for item in self.all_rawdata:
                self.all_artists.append(item[2])  # print the rows and columns
            self.all_unique = list(set(self.all_artists))
            for i in range(10,40):
                  self.fav_unique.append(self.all_unique[i])


    def gen_art(self,name):
                for j in range(1, 101):
                    if (name == self.all_rawdata[j][2]):
                       k = ("{:40s} {:30s}{:>10}{:>10}{:>10}".format(self.all_rawdata[j][1], self.all_rawdata[j][2],self.all_rawdata[j][3],
                                                                    self.all_rawdata[j][4],self.all_rawdata[j][5]))
                       yield k

    def  clos_art(self,name):
                def clos_inner():
                    for j in range(1, 101):
                        if (name == self.all_rawdata[j][2]):
                            k =float(self.all_rawdata[j][4])
                            if(k>.50):
                                  k1 = ("{:40s} {:30s}{:>10}{:>10}".format(self.all_rawdata[j][1], self.all_rawdata[j][2],self.all_rawdata[j][3],
                                                                    self.all_rawdata[j][4]))
                                  return k1
                return clos_inner





class gen_artist:

    def artist_g(self):
            c1 = fav_artist()
            print("{:40s} {:30s}{:>10}{:>10}{:>10}".format(c1.all_rawdata[0][1].upper(), c1.all_rawdata[0][2].upper(),
                                                           c1.all_rawdata[0][3].upper(), c1.all_rawdata[0][4].upper(),
                                                           c1.all_rawdata[0][5].upper()))
            for i in c1.fav_unique:
                     k =(list(c1.gen_art(i)))
                     print(k)

    def artist_closure(self):
        c1 = fav_artist()
        print("{:40s} {:30s}{:>10}{:>10}".format(c1.all_rawdata[0][1].upper(), c1.all_rawdata[0][2].upper(),
                                                       c1.all_rawdata[0][3].upper(), c1.all_rawdata[0][4].upper()))

        for i in c1.fav_unique:
                k = c1.clos_art(i)
                print(k())


c1 =gen_artist()
print("-------------------------------This is the artists name and tracks-------------------------------------------------")
c1.artist_g()
print("-------------------------------This is the artists with high energy--------------------------------------------")
c1.artist_closure()