class Solution:

    def uniquePathsIII(self, grid):

        self.addr_dict = {}
        step = 0
        self.grid = grid
        print (grid)
        self.result_routes = 0
        
        start, flag = self.start_fun()
        print (self.grid)
        print(start)
        self.main_stack = Stack(start)
        self.visited_stack = Stack(start)

        #self.get_surround(start)
        self.just_returned = False
        self.route_squares = (len(grid)*len(grid[0])) - self.walls
        self.current_square = start
        for j in range (100):
            
            # Con el surround se agregan a main_stack
            self.get_surround(self.current_square)
            if self.ret == True:
                
                self.available_coord_temp = self.main_stack.last()
                if self.available_coord_temp == []:
                    self.return1()
                    pass
                self.main_stack.take1()
                self.visited_stack.push(self.available_coord_temp[0])
                self.main_stack.push(self.available_coord_temp[1:])
            else:
                self.return1()

            self.main_stack.print_self()
            self.visited_stack.print_self()
            self.current_square = self.visited_stack.last()
            if self.visited_stack.stack_size() == self.route_squares:
                pass

    
    def return1(self):
        print ("RETURN")
        self.main_stack.take1()
        self.main_stack.take1()
        self.visited_stack.take1()
        self.available_coord_temp = self.main_stack.last()
        if self.available_coord_temp == []:

            self.return1()
            return
            
        self.current_square = self.available_coord_temp[0]
        del self.available_coord_temp [0]
        self.main_stack.push(self.available_coord_temp)
        


    def get_surround (self, coords):
        print(coords)
        
        coords_list = [(coords[0], coords[1]-1), (coords[0]-1, coords[1]), (coords[0], coords[1]+1), (coords[0]+1, coords[1])]
        self.temp_list = []
        self.flag_around = False
        self.ret = False
        for m in range(4):
            try:
                print("m = ", m)
                coord_temp = self.grid[coords_list[m][0]][coords_list[m][1]]
                
                if (coord_temp != -1 and coords_list[m][0] != -1 and coords_list[m][1] != -1):
                    temp_stack_list = self.visited_stack.return_stack()
                    if coords_list[m] not in temp_stack_list:
                        if coord_temp == 2:
                            self.flag_around = True
                            self.flag_coord = coords_list[m]
                            continue
                        
                        print (f"DISPONIBLE: {coords_list[m]} SALIDO DE: {coords}")
                        self.temp_list.append(coords_list[m])
                        
                        self.ret = True
                        #self.main_stack.print_self()  


            except:    
                print("error")
                pass  
                  
        if self.flag_around:
            self.temp_list.append(self.flag_coord)
        self.main_stack.push(self.temp_list)
        


#crear algo para contar apaciciones de -1 en array 

    def start_fun(self):
        self.walls = 0
        for n1 in range(len(self.grid)):
            temp_list = self.grid[n1]
            self.walls += temp_list.count(-1)

            if 1 in temp_list:                   
                n2 = temp_list.index(1)      
                start_coord = (n1, n2)

            if 2 in temp_list:
                flagx = temp_list.index(2)
                flag_coord = (n1, flagx)

        print(f"Incio = {start_coord} End = {flag_coord}")        
        return start_coord, flag_coord     
        

#### Se checa si hay algo despues
# Si sí hay, se avanza. 
# Se guarda lo encontrado en una lista dentro del stack de main_stack. 
# Se vuelve a checar si hay algo despues
# El resulado de lo que haya alrededor se guarda en una lista dentro de stack llamado main_stack
# Se accede al primer elemento de esta lista, y se borra dicho elemento
#En caso de regresar. Se borra último elemento de lista de main_stack. En caso de que haya una lista con 0 elementos, se borra y se 
# regrersa uno mas. Si hay una lista con n elementos, se accede al primero. 
# Si se detecta la banera, se a;ade al final de lista.
# Cada que los elementos sean iguales al numero buscado, se revisa que se termine en bandera. De lo contrario, se regresa uno. 



class Stack (object):
    def __init__ (self, start):
        self.list = [start]

    def last(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return []

    def stack_size (self):
        return len(self.list)

    def push(self, coord_local):
        self.list.append(coord_local)

    def return_stack (self):
        return self.list

    def print_self(self):
        print("STACK:")
        print(self.list)

    def take1 (self):
        try:
            del self.list [-1]
        except:
            print(f"LEN = {self.stack_size()}")
            self.print_self()
