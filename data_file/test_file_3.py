from xlrd import open_workbook

class node:
    def __init__(self,data1,data2,next = None):
        self.data1 = data1
        self.data2 = data2
        self.next = next

class list_data:

    def __init__(self):
        self.head = None

    def  append_data(self,ob1,ob2):
         if(self.head == None):
             self.head = node(ob1,ob2)
         else:
             curr = self.head
             while(curr.next != None):
                 curr = curr.next
             curr.next = node(ob1,ob2)

    def  print_data(self):
        curr = self.head
        print(curr.data1,curr.data2)
        while(curr.next != None):
            curr = curr.next
            print(curr.data1,curr.data2)

    def count_list(self):
        curr = self.head
        ct = 1
        if (curr == None):
            return None
        else:
            while (curr.next != None):
                curr = curr.next
                ct = ct + 1
            return ct

    def pop_node(self):
        if (self.head == None):
            return None
        else:
            k = self.head
            self.head = self.head.next
            return k

    def  remove_dup(self):
        curr =self.head
        prev = None
        dup_values = dict()
        while(curr != None):
               if((curr.data1 and curr.data2) in dup_values):
                   prev.next = curr.next
                   curr = None
               else:
                   dup_values[curr.data2]=1
                   prev = curr
               curr = prev.next

class  in_sort:
    def __init__(self):
        self.head = None

    def  insertion_sort(self,ob):
         k  = ob
         k.next = None
         if(self.head == None):
             self.head = k
         else:
             curr = self.head
             if(k.data1 <curr.data1):
                 temp = curr
                 self.head = k
                 self.head.next = temp
             else:
                 curr = self.head
                 while(curr.next!= None):
                     if(curr.next.data1 >k.data1):
                          temp = curr.next
                          curr.next = k
                          curr.next.next = temp
                          break
                     else:
                         curr = curr.next
                 else:
                     curr = self.head
                     while(curr.next != None):
                         curr = curr.next
                     curr.next = k


    def  print_insort(self):
         curr = self.head
         while(curr.next != None):
             print(curr.data1,"............>",curr.data2)
             curr = curr.next
         print(curr.data1," ......>",curr.data2)

    def count_insort(self):
        curr = self.head
        ct = 1
        if (curr == None):
            return None
        else:
            while (curr.next != None):
                curr = curr.next
                ct = ct + 1
            return ct

    def pop_insort(self):
        if (self.head == None):
            return None
        else:
            k = self.head
            self.head = self.head.next
            return k

class  sort_subcatagory:
     def __init__(self):
         self.head = None

     def  append_data(self,ob):
          node_data = ob
          node_data.next = None
          if(self.head == None):
             self.head = node_data
          else:
              curr = self.head
              while(curr.next != None):
                  curr = curr.next
              curr.next = node_data

     def  print_list(self):
         curr = self.head
         while(curr.next != None):
             print(curr.data1,"...........>",curr.data2)
             curr = curr.next
         print(curr.data1,"............>",curr.data2)

     def first_node_return(self, pos,num_times):
         st_node = in_sort()
         curr = self.head
         node_pos = 1
         if (pos == 1):
               self.bubblesort_list(curr,num_times)
         else:
             while (curr.next != None):
                 curr = curr.next
                 node_pos = node_pos + 1
                 if (node_pos == pos):
                     self.bubblesort_list(curr, num_times)

     def bubblesort_list(self, start, num_ele):
        ct = 1
        k = num_ele
        final = start
        curr = start
        while (ct != k):
            curr = curr.next
            ct = ct + 1
        final = curr.next
        for i in range(k):
            curr = start
            while (curr.next != final):
                if (curr.next.data2 == None):
                    break
                else:
                    if (curr.data2 > curr.next.data2):
                        tmp = curr.next.data2
                        curr.next.data2 = curr.data2
                        curr.data2 = tmp
                        curr = curr.next
                    else:
                        curr = curr.next
            final = curr.next

def unique_list(list):
    uniq_list = []
    uniq_set = set()
    for item in list:
        if item not in uniq_set:
            uniq_list.append(item)
            uniq_set.add(item)
    return uniq_list

def read_excel():
    import collections
    l = list_data()
    ins = in_sort()
    sort_sub = sort_subcatagory()
    list_subcatagory =[]
    list_countsubcatagory =[]
    list_finalcountsubcatagory =[]
    number_of_subcatory =[]
    start_node =[]
    wb = open_workbook('test_excel.xlsx')
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols
    for i in range(number_of_rows):
            a = sheet.cell_value(i,0)
            b = sheet.cell_value(i,1)
            l.append_data(a,b)

    input_enter = input("Do you want to print all the data read from the file: enter y/n:     ")
    if((input_enter == 'Y') or(input_enter == 'y')):
        l.print_data()
        print("Total number of rows  is ..........>:",l.count_list())
        l.remove_dup()
        print("removed duplicate data and  unique data is............>: ",l.count_list())
    input_enter2 = input("Do you want to print the catagory in ascending order and number of subcatagory : enter y/n:      ")
    if((input_enter2 == 'Y') or(input_enter2 == 'y')):
        l.remove_dup()
        for i in range(l.count_list()):
            k = l.pop_node()
            ins.insertion_sort(k)
        k = ins.count_insort()
        for i in range(k):
           item = ins.pop_insort()
           list_subcatagory.append(item.data1)
           sort_sub.append_data(item)
        #print(list_subcatagory)
        for i in list_subcatagory:
            k = list_subcatagory.count(i)
            c =(i,k)
            list_countsubcatagory.append(c)

        k = unique_list(list_countsubcatagory)
        list_finalcountsubcatagory = k
        #print(list_finalcountsubcatagory)
        count_subcatagory = len(list_finalcountsubcatagory)
        for i in range(count_subcatagory):
            print(list_finalcountsubcatagory[i][0],"....>",list_finalcountsubcatagory[i][1])
            number_of_subcatory.append(list_finalcountsubcatagory[i][1])

        intial_node = 1
        for i in number_of_subcatory:
            start_node.append(intial_node)
            intial_node = intial_node + i
        #print(start_node)
        mapped = zip(start_node, number_of_subcatory)
        mapped = set(mapped)
        #print(mapped)
        print("before bubble sorting.......................................................................................")
        sort_sub.print_list()
        for i in mapped:

            sort_sub.first_node_return(i[0],i[1])
        print("after bubble sort............................................................................................")
        sort_sub.print_list()


read_excel()

