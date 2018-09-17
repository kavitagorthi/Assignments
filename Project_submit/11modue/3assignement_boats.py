''' this class boats _door_upstream class is having a 1 set of updoors.once the boat is alloted the corresponding door will open
and the resources will be work.this init method is dictionary with cooresponding door and boat name will be passed to the init method as key and value is the door
this was implemented by using context manager '''


class boats_door_upstream:

       def __init__(self,ob):
           self.boats_updoor= {'Ids01': 'updoor_Ids01', 'Ids02': 'updoor_Ids02', 'Ids03': 'updoor_Ids03',
                               'Ids04': 'updoor_Ids04', 'Ids05': 'updoor_Ids05','Idb11': 'updoor_Idb11',
                                'Idb12': 'updoor_Idb12', 'Idb13': 'updoor_Idb13','Idb14': 'updoor_Idb14',
                                'Idb15': 'updoor_Idb15', 'Idb16': 'updoor_Idb16', 'Idb17': 'updoor_Idb17',
                                'Idb18': 'updoor_Idb18', 'Idb19': 'updoor_Idb19', 'Idb20': 'updoor_Idb20'}
           self.boat =ob


       def __enter__(self):

              print( self.boats_updoor[self.boat]," The door is open")
              print(self.boat," clear the door")
              print("Restarting the pump")

       def __exit__(self,type, value, traceback):
           print( self.boats_updoor[self.boat],"The door is closed")


''' this class  boats _door_downstream class is having a 1 set of downdoors.once the boat is retuned the corresponding door will open
and the resources will be work.this init method is dictionary with cooresponding door and boat name will be passed to the init method as key and value is the door
this was implemented by using context manager '''

class boats_door_downstream:

    def __init__(self,ob):

        self.boats_downdoor = {'Ids01': 'downdoor_Ids01', 'Ids02': 'downdoor_Ids02', 'Ids03': 'downdoor_Ids03',
                               'Ids04': 'downdoor_Ids04', 'Ids05': 'downdoor_Ids05','Idb11': 'downdoor_Idb11',
                               'Idb12': 'downdoor_Idb12', 'Idb13': 'downdoor_Idb13','Idb14': 'downdoor_Idb14',
                               'Idb15': 'downdoor_Idb15','Idb16': 'downdoor_Idb16', 'Idb17': 'downdoor_Idb17',
                                'Idb18': 'downdoor_Idb18','Idb19': 'downdoor_Idb19', 'Idb20': 'downdoor_Idb20'}
        self.boat = ob

    def __enter__(self):
              print( self.boats_downdoor[self.boat]," The door is open")
              print(self.boat," clear the door")
              print("Stopping the pump")

    def __exit__(self,type, value, traceback):
           print( self.boats_downdoor[self.boat],"The door is closed")


''' this class boats is designed  : init method is implemented for total small boats is 5(with unique id names) and large 10(with unique 10 id names) boats.
 once we requested for small boat the boat is alloted with id name and will call context manager for the resources to take care and alloted boat will be append to the return 
 list of boats and process same for large boats too .The return request of boats is also same'''





class boats:

    def __init__(self):
            self.lock_small =['Ids01','Ids02','Ids03','Ids04','Ids05']
            self.lock_large = ['Idb11','Idb12','Idb13','Idb14','Idb15','Idb16','Idb17','Idb18','Idb19','Idb20']
            self.lock_small_down =[]
            self.lock_large_down =[]


    def boat_small_upstream(self):
           if(len(self.lock_small)== 0):
               return None
           else:
               return self.lock_small.pop(0)

    def boat_large_upstream(self):
           if(len(self.lock_large) == 0):
              return None
           else:
              return self.lock_large.pop(0)

    def  boat_small_downstream(self):
           if (len(self.lock_small_down)== 0):
               return None
           else:
               return self.lock_small_down.pop(0)

    def  boat_large_downstream(self):
           if (len(self.lock_large_down)== 0):
               return None
           else:
               return self.lock_large_down.pop(0)

    def   boats_available(self):
            print("Total number of boats available is :",len(self.lock_small)+len(self.lock_large))
            print("The number of small boats available :",len(self.lock_small))
            print("The number of large boats available :",len(self.lock_large))
            print("Do you want boats : Enter your option: 's' for small (or) 'l' for large or 'n' for no")
            userentered  = input("enter s or l or n:     " )
            print(userentered)
            if(userentered == 's'):
                  c1 = self.boat_small_upstream()
                  print("the boat alloted is :",c1)
                  if(c1 == None):
                      print("No small boats available")
                  else :
                      self.lock_small_down.append(c1)
                      with boats_door_upstream(c1):
                          print('')
                      self.boats_available()
            elif(userentered == 'l'):
                  c2 = self.boat_large_upstream()
                  print("the boat alloted is :", c2)
                  if (c2 == None):
                      print("No large boats available")
                  else:
                      self.lock_large_down.append(c2)
                      with boats_door_upstream(c2):
                          print('')
                      self.boats_available()
            else:
                  return None

    def boats_return(self):
            print("Total number of boats to return(downstream) is : ",len(self.lock_small_down)+len(self.lock_large_down))
            print("The number of small boats have to return(downstream) is :",len(self.lock_small_down))
            print("The number of large boats have to return(downstream) is :",len(self.lock_large_down))
            print("Enter the boat to return : Enter your option: 's' for small (or) 'l' for large or 'n' for no")
            userentered  = input("enter s or l or n:     " )
            print(userentered)
            if(userentered == 's'):
                  c1 = self.boat_small_downstream()
                  print("the boat alloted is :",c1)

                  if (c1 == None):
                      print("No small boats to return")
                  else:
                      self.lock_small.append(c1)
                      with boats_door_downstream(c1):
                          print('')
                      self.boats_return()
            elif(userentered == 'l'):
                  c2 = self.boat_large_downstream()
                  print("the boat alloted is :", c2)

                  if(c2 == None):
                      print("No Large boats to return")

                  else :
                      self.lock_large.append(c2)
                      with boats_door_downstream(c2):
                          print('')
                      self.boats_return()
            else:
                  return None

    def print_boats(self):
            print("the number of small boats availabe( upstream) :",self.lock_small)
            print("the number of large boats available(upstream) :",self.lock_large)
            print("the number of small boats have to return back(down stream) :",self.lock_small_down)
            print("the number of large boats have to return back(down stream):",self.lock_large_down)



b = boats()
b.boats_available()
b.print_boats()
b.boats_return()
b.print_boats()