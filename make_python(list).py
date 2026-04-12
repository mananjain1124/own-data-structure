import ctypes

class mylist:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a c type array with size = self.size
        self.A = self.make_array(self.size)
        
    def __len__(self):
        return self.n
    
    def append(self,item):
        #check if vacant
        if self.n == self.size:
           # double the size
           self.__resize(2*self.size)
           
        self.A[self.n] = item
        self.n += 1   
    
    def pop(self):
        if  self.n == 0:
            return "List is empty"
        print(self.A[self.n-1])
        self.n -= 1
    
    def clear(self):
        self.n = 0
        self.size = 1
        
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "Item not found"
    
    def remove(self,item):
        # search and get pos
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos
        
    def __resize(self,new_capacity):
        # create a new array with new capacity
        B = self.make_array(new_capacity)
        self.size = new_capacity
        # copy the old array to new array
        for i in range(self.n):
            B[i] = self.A[i]
            # reassign A
        self.A = B
        
    def __str__(self):
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ','   
        return '[' + result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0<= index <self.n:
            return self.A[index]
        else:
            return "index error"
        
    def __delitem__(self,pos):
        if 0<= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1  
    
    def make_array(self,capacity): 
        return (capacity * ctypes.py_object)()       
    




    
