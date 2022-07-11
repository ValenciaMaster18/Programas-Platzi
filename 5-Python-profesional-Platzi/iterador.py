import time
                                             
class Fibonachi:
    
    def __iter__(self):
      self.a = 0
      self.b = 1
      self.count = 0
      return self
  
    
    def __next__(self):
        if self.count == 0:
            self.count +=1
            return self.a
        elif self.count == 1:
            self.count +=1
            return self.b
        else:
            self.aux = self.a + self.b
            self.a , self.b = self.b, self.aux
            self.count +=1
            return self.aux
            

if __name__ == "__main__":
    fibo = Fibonachi()
    for elemento in fibo:
        print(elemento)
        time.sleep(1)
        
   