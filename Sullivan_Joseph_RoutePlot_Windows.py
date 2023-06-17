# Drone-Mapping-Assessment
# This was the first validation of my skill set as a python programmer. I'd appreciate any feedback. 
# !!!  THIS VERSION IS FOR WINDOWS SYSTEMS ONLY  !!!

from IPython.display import clear_output

#THE MAP
N0 = ['#']    
N1 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N2 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N3 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N4 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N5 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N6 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N7 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N8 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N9 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N10 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N11 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
N12 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']


map_grids = [N0,N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11,N12]

def visual_map(map_grids):

    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(':12 : '+N12[1]+' : '+N12[2]+' : '+N12[3]+' : '+N12[4]+' : '+N12[5]+' : '+N12[6]+' : '+N12[7]+' : '+N12[8]+' : '+N12[9]+' : '+N12[10]+' : '+N12[11]+' : '+N12[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(':11 : '+N11[1]+' : '+N11[2]+' : '+N11[3]+' : '+N11[4]+' : '+N11[5]+' : '+N11[6]+' : '+N11[7]+' : '+N11[8]+' : '+N11[9]+' : '+N11[10]+' : '+N11[11]+' : '+N11[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(':10 : '+N10[1]+' : '+N10[2]+' : '+N10[3]+' : '+N10[4]+' : '+N10[5]+' : '+N10[6]+' : '+N10[7]+' : '+N10[8]+' : '+N10[9]+' : '+N10[10]+' : '+N10[11]+' : '+N10[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(': 9 : '+N9[1]+' : '+N9[2]+' : '+N9[3]+' : '+N9[4]+' : '+N9[5]+' : '+N9[6]+' : '+N9[7]+' : '+N9[8]+' : '+N9[9]+' : '+N9[10]+' : '+N9[11]+' : '+N9[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(': 8 : '+N8[1]+' : '+N8[2]+' : '+N8[3]+' : '+N8[4]+' : '+N8[5]+' : '+N8[6]+' : '+N8[7]+' : '+N8[8]+' : '+N8[9]+' : '+N8[10]+' : '+N8[11]+' : '+N8[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(': 7 : '+N7[1]+' : '+N7[2]+' : '+N7[3]+' : '+N7[4]+' : '+N7[5]+' : '+N7[6]+' : '+N7[7]+' : '+N7[8]+' : '+N7[9]+' : '+N7[10]+' : '+N7[11]+' : '+N7[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(': 6 : '+N6[1]+' : '+N6[2]+' : '+N6[3]+' : '+N6[4]+' : '+N6[5]+' : '+N6[6]+' : '+N6[7]+' : '+N6[8]+' : '+N6[9]+' : '+N6[10]+' : '+N6[11]+' : '+N6[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(': 5 : '+N5[1]+' : '+N5[2]+' : '+N5[3]+' : '+N5[4]+' : '+N5[5]+' : '+N5[6]+' : '+N5[7]+' : '+N5[8]+' : '+N5[9]+' : '+N5[10]+' : '+N5[11]+' : '+N5[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(': 4 : '+N4[1]+' : '+N4[2]+' : '+N4[3]+' : '+N4[4]+' : '+N4[5]+' : '+N4[6]+' : '+N4[7]+' : '+N4[8]+' : '+N4[9]+' : '+N4[10]+' : '+N4[11]+' : '+N4[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(': 3 : '+N3[1]+' : '+N3[2]+' : '+N3[3]+' : '+N3[4]+' : '+N3[5]+' : '+N3[6]+' : '+N3[7]+' : '+N3[8]+' : '+N3[9]+' : '+N3[10]+' : '+N3[11]+' : '+N3[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(': 2 : '+N2[1]+' : '+N2[2]+' : '+N2[3]+' : '+N2[4]+' : '+N2[5]+' : '+N2[6]+' : '+N2[7]+' : '+N2[8]+' : '+N2[9]+' : '+N2[10]+' : '+N2[11]+' : '+N2[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(': 1 : '+N1[1]+' : '+N1[2]+' : '+N1[3]+' : '+N1[4]+' : '+N1[5]+' : '+N1[6]+' : '+N1[7]+' : '+N1[8]+' : '+N1[9]+' : '+N1[10]+' : '+N1[11]+' : '+N1[12]+' :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')
    print(':   : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 :10 :11 :12 :')
    print(':---:---:---:---:---:---:---:---:---:---:---:---:---:')

    
    #Start Point / CALLING THE FILE

def file_name():
    
    
    finish = False
    file = ''
    
    while finish == False:
        
        file = (input('Please input file name or STOP:'))
        
        #STOP FUNCTION
        if file == 'STOP':
            
            finish = True
        
        #OPENING THE FILE
        else:
            
            #USING EXCEPTION HANDLING TO AVOID SYNTAX ERRORS BREAKING THE WHILE LOOP.
            try:
                RootDir = 'C:\\'
                for relPath,dirs,files in os.walk(RootDir):
                    if(file in files):
                        FullPath = os.path.join(RootDir, relPath, file)
                        
    
                
                
                f = open(FullPath, "r", encoding = "UTF-8")
                
                #READING THE COORDINATES
                read_coordinates = f.readlines()
                
                #EXTRACTING THE COORDINATES AND ASSIGNING THEM TO X,Y(START POSITION) AND DIRECTIONS
                coordinates = []  

                for num in read_coordinates:
                    coords = num.replace('\n','')
                    coordinates.append(coords)

                x = int(coordinates[0])
                y = int(coordinates[1])
                directions = coordinates[2:]


                return x,y, directions, file
            
            #IF SYNTAX ERROR OCCURS, EXCEPT WILL MAINTAIN THE WHILE LOOP
            except:
                clear_output()
                print('File Not Found')
            
    #IF STOP IS CALLED, FINISH WILL RETURN 'TRUE'    
    else:
        return finish    
      
      
    #START POSITION, USING X,Y FROM FILE_NAME() FUNCTION

def start_place_marker(board, N, E, marker):
    board[N][E] = marker

    
#DIRECTIONS THAT FOLLOW THE START POSITION.

def direction_func(directions):
    
    #'VALID' = VALIDATE IF A DIRECTION IS INVALID OR OUT OF BOUNDS
    valid = True
    #'FINISH' = DIRECTIONS VALID AND WILL RETURN THE ROUTE
    finish = False
    
    #VARIABLES
    navigation = ['N','E','S','W']
    route = []
    
    #START POINT (NORTH AND SOUTH) ARE DEFINED ONCE THE X,Y ARE CALLABLE
    position_N = sp_N
    position_E = sp_E
    
    
    while finish == False and valid == True:
    
        
        for num in directions[0]:
                
                if num == 'N':
                    position_N = position_N+1

                if num == 'E':
                    position_E = position_E+1

                if num == 'S':
                    position_N = position_N-1

                if num == 'W':
                    position_E = position_E-1 
                    
                
                #VALIDATE OUT OF BOUNDS
                if position_N not in range(1,13) or position_E not in range(1,13):
                    valid = False
                
                #VALIDATE DIRECTION
                else:
                    if num not in navigation:
                        valid = False
                    
                    #VALIDATE DIRECTIONS ONLY MOVE VERTICALLY AND HORIZONTALLY AND IDENTIFY FAULTS IN FILE ie.'NZ'
                    else:   
                        if len(num)>1:
                            valid = False
                        
                        #DIRECTION IS VALID - ADD GRID POSITION TO A 'COORDINATES' LIST AND REMOVE FROM 
                        else:
                        
                            coordinates = position_E, position_N

                            directions.pop(0)

                            route.extend([coordinates])
                            
                            #ENSURES EVERY DIRECTION HAS BEEN TESTED AND TESTED ONLY ONCE
                            if len(directions)== 0:

                                finish = True
    

    else:
        #BOOLEN 'FALSE' WILL BE CALLED TO REPORT AN ERROR
        if valid == False:
            return valid
        
        #RETURNS ROUTE (LISTED TUPLES)
        else:
            return route
            

            
#PLACE HOLDER FUNCTION

def place_marker(map_grids, y, x, marker):
    map_grids[y][x] = marker

    
    

#'COMPLETED' = TRUE WILL BE TRIGGERED ONCE 'STOP' IS CALLED. THEREFORE DICTATE THE PRIMARY WHILE LOOP.

completed = False
while completed == False:
    
    #VARIABLES / Within While Loop to reset
    N0 = ['#']    
    N1 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N2 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N3 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N4 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N5 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N6 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N7 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N8 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N9 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N10 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N11 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    N12 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    map_grids = [N0,N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11,N12]
    
    #WHILE LOOP VARIABLES
    game_on = True
    output = False
    route = []
    
    
    f_name = file_name()
    
    #IF F_NAME = TRUE, STOP HAS BEEN CALLED / BREAKS PRIMARY WHILE LOOP
    if f_name == True:
        completed = True
        
        
        
    #PLOTTING COORDINATES    
    else:
        
        #EXTRACTING ASSIGNING OUTPUTS FROM 'FILE_NAME()' FUNCTION - X,Y,DIRECTIONS
        x = f_name[0]
        y = f_name[1]
        directions = f_name[2]
        
        starting_position = x, y
        
        #IDENTIFY INITIAL EASTING AND NORTHING
        sp_E = starting_position[0]  
        sp_N = starting_position[1]
        
        #RUNNING 'DRIECTION_FUNC' TO MAKE ROUTE CALLABLE OR RETURN ERROR.
        move_position = direction_func(directions)  
        
        #VALIDATIING MOVE POSITIONS (DIRECTION_FUNC)
        if move_position == False:
            clear_output()
            print('Error: The route is outside of the grid.')
            
            
        
        else:
            #GRID PLOTTING PHASE
            
            #INITIAL GRID
            start_place_marker(map_grids, sp_N, sp_E, 'x')

            
            while game_on == True:
                
                #CALLS NUM IN TUPLE WITHIN 'ROUTE' LIST FROM DIRECTION_FUNC(), ASSINGS EASTING AND NORTHING
                move_positionE = move_position[0][0]
                move_positionN = move_position[0][1]
                
                #PLOT ROUTE ON MAP
                place_marker(map_grids, move_positionN, move_positionE, 'x')
                
                #POSITIONS ADDED TO ROUTE TO BE PRINTED IN OUTPUT
                route.extend((move_positionE, move_positionN))
                move_position.pop(0)
                
                #VALIDATES WHEN ALL POSITIONS HAVE BEEN PLOTTED
                if len(move_position) == 0:
                    game_on = False
                    
                    #OUTPUT DISPLAY ORDER
                    clear_output()
                    print(f_name[3])
                    visual_map(map_grids)
                    print('Coordinates')

            #PRINTS ROUTE IN GRID REFERENCES
            while output == False:
                print(route[0],route[1])
                route.pop(0)
                route.pop(0)
                if len(route)==0:
                    output = True
                    

else:
    completed
