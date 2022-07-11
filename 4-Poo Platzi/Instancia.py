from dis import dis
from re import X


class Cordenadas:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    
    def distancia(self,otra_distancia):
        x_diff = (self.x - otra_distancia.x)**2
        y_diff = (self.y - otra_distancia.y)**2
        
        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord_1 = (Cordenadas(30,30))
    coord_2 = (Cordenadas(2,8))
    
    print(coord_1.distancia(coord_2))