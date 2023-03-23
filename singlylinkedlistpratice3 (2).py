
class node:
    def __init__(self,data):                                                                     #  |1100| --> |1200| 
        self.data=data               #this is creating node that contains data and link field"""" |30|1200|      |40|1300|"""                          
        self.ref=None
class linkedlist:
    def __init__(self):                                                                    # head none   something reference intially it is none
        self.head=None                #linkedlist starts with head value and it has reference    |data|linknode|
    def printall(self):
        if self.head is None:   
            print("linked list is empty")
        else:
            n=self.head              # assigning self.head as n because writing code shortly while going to the loop n is self.head it checks n is none if it is
                                     #None it prints linked list is empty if not it prints self.head.refference value ie head |1001| -->|1020|  self.head value reference=1001
            while n is not None:     #                                                                                     |30|1020|  |40|1030|data=30  so self.head.data=30
                #print(':reference:',n.ref)                     #                                                                                                                                    
                print(n.data,"-->",end=" ")        # print(n.passed value while creating object)1011.1020=n                                   refrence(linkfield)=1020                                                             
                n=n.ref              #                    reassigning self.head=n to self.head.ref=n ie head has some reference 1020
    def firstofthenode(self,data):   #                                         newnode      head          newnode  head
          newnode=node(data)         #                                          |1020|     |2222| after  |1020|-->|2222|    
          newnode.ref=self.head      #                                       |50|link| -->|60|link|     |50|2222| |60|link| link is none
          self.head=newnode          #assigning the link value of newnoderef ie| mala irruku
                                     #line 22 self.head=newnode means self.head=newnode means self.head=1020 ie reference of newnode in head now 
                                     #             head        newnode
                                     #            |1020| --->  |2222| this for line 22
    def endofnode(self,data):        #           |50|2222|    |60|link|
        if self.head is None:
            self.head=newnode  
        else:
            n=self.head              #               head  linkref=2222
            while n.ref is not None: # this means eg |1020|-->|2222| -->|3333| something if head of the  linkref=2222 is not none is the condition if the linkref is none it stops the loop
                 n=n.ref             #             |50|2222|  |60|3333| |70|link|                                     #
            newnode=node(data)       #         
            newnode.ref=n.ref        #  line 31 checks head.ref ie n.ref is 2222 is none or not it is not goes in loop reassign n=2222.ref is n=3333 is not none so agin in loop n=3333.ref is none hence stop the loop
            n.ref=newnode            # |4444| newnode.link=3333.link|3333| ie  |3333|       |4444|
                                      #|80|link|           |70|link            |70|4444    |80|link
    
    
    """afternode operations what happens
    n=1020 as we alredy know while n is not none until it runs loop if it is none it stop and checks x=70 if x==n.data first it checks head.data which is 50 is not equal
    so reassign n=2222.ref ie n=3333 goes in loop checks none or not checks 70==3333.data ie 70==70 now loop breaks n=3333 now creating node
    |5555|--->|4444| newnode.ref=n.ref  |5555|--->|4444| n.ref=newnode      |5555|<---|4444|
    |90|link| |80|link|                |90|link| |80||                     |90|link| |80|5555|
    
    """                                                                                   
    def afterthenode(self,data,x):     
        n=self.head                  
        while n is not None:         
            if x==n.data:            
                break                
            n=n.ref                  
        if n is None:                
            print("the x element is not there")#  
        else:                                  #
                                               #
                                               #
                                               #
            newnode=node(data)                 #        
            newnode.ref=n.ref                  #
            n.ref=newnode
    """checks whether head data is eaual to x if its newnodelink is the headref and headref is newnoderef              
                                     #            |1020| --->  |2222| 
             #                                   |50|2222|    |70ink|   now goes to while loop n=self.head loop condition is n.ref is none if it is stop now it checks n is head intially it checks n.ref.data==70 ie 
             #   n.ref.data ie 1020.ref.data is 70 its breaks the loop and this does like line 58   """
    def beforethenode(self,data,x):
        if self.head.data==x:
            newnode =node(data)
            newnode.ref=self.head
            self.head=newnode
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
             break
            n=n.ref
        if n.ref is None:
            print("the x elemnet is not there")
        else:
            newnode=node(data)
            newnode.ref=n.ref
            n.ref=newnode
    """head|1020| ---> newnode |2222| self.head=self.head.ref is |1020| ---> head |2222|  
         |50|2222|           |70|ink|                            |50|2222|        |70|ink|"""
    def deletefirst(self):          
        self.head=self.head.ref 
    """1020|-->|2222| -->|3333| 
 |50|2222|  |60|3333| |70|link|   last node link is none or not while loop is checking using n.ref.ref means intially n=self.head ie n=1020 now n.ref.ref is 1020.ref.ref is 2222.ref is 3333 again goes in n=3333.ref is  none now n=2222.ref=none means
 1020|-->|2222|  -->   no!|3333| 
 |50|2222|  |60|none| |70|link| """    
    def deleteend(self):
        n=self.head
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None
    """                                                                                                                         2222   
    1020|-->|2222| -->|3333|    it checks 60==1020.ref.data is 60==2222.data is 60==60 now n=1020 it changes n.ref=n.ref.ref is n.ref=1020.ref.ref  is n.ref=3333 now 
 |50|2222|  |60|3333| |70|link|                                                       
 1020|-->  no!|2222| -->|3333| 
 |50|3333|  |60|3333| |70|link| 
 
 """
    def deleteany(self,x):
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("the required node is not there")
        else:
         n.ref=n.ref.ref
        
     


l=linkedlist()
while True:
    d="""press 1 for adding elemnt first
    press 2 for last element adding
    press 3 for after the node
    press 4 for before the node
    press 5 for delete the first element
    press 6 for delete the last element
    press 7 for deleting any element
    press 8 for displaying
    press 9 for quit"""
    print(d)
    c=int(input("enter ur choice:\n"))
    print()
    if c==1:
        a=int(input("enter the number to insert:"))
        l.firstofthenode(a)
    elif c==2:
        a=int(input("enter the number to insert:"))
        l.endofnode(a)
    elif c==3: 
         a=int(input("enter the number to insert:"))
         b=int(input("enter the number to insert:"))  
         l.afterthenode(a,b)
    elif c==4: 
         a=int(input("enter the number to insert:"))
         b=int(input("enter the number to insert:"))
         l.beforethenode(a,b)
    elif c==5: 
         a=int(input("enter the number to delete:"))
         l.deletefirst()
    elif c==6: 
         a=int(input("enter the number to delete:"))
         l.deleteend()
    elif c==7: 
         a=int(input("enter the number to delete:"))   
         l.deleteany(a)
    elif c==8: 
         l.printall()
    elif c==9:
         quit()
                 
            

                                    

                                             