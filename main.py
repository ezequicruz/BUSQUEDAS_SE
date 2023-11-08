#CRUZ JUAREZ EZEQUIEL AMADO
#SISTEMAS EXPERTOS

#IMPORT CLASS Search include Breadth_first_search | Steepest_ascent_hill_climbing_search | Best_first_search
from Search import Search

print('TEST_SEARCH_NODELIST'.center(50,'-'))
#adjacency list
ady_list = [None,   #row 0
            [3,[6,117],[13,699],[4,701]], #row 1
            [3,[22,171],[12,137],[9,245]], #row 2
            [4,[14,317],[23,235],[19,638],[18,291]], #row 3
            [3,[9,202],[1,687],[13,98]], # row 4
            [2,[15,220],[11,705]], # row 5
            [2,[16,288],[1,117]], # row 6
            [3,[27,475],[8,662],[11,696]], # row 7
            [3,[27,268],[15,309],[7,662]], # row 8
            [5,[28,320],[2,245],[17,321],[4,202],[24,214]], # row 9
            [2,[16,381],[12,54]], # row 10
            [2,[7,696],[5,705]], # row 11
            [2,[10,54],[2,137]], # row 12
            [3,[4,98],[1,699],[24,446]], # row 13
            [2,[23,499],[3,317]], # row 14
            [3,[8,309],[24,286],[5,220]], # row 15
            [6,[19,95],[25,118],[20,123],[6,288],[26,66],[10,381]], # row 16
            [2,[26,259],[9,321]], # row 17
            [3,[14,328],[3,291],[21,89]], # row 18
            [3,[23,391],[16,95],[3,638]], # row 19
            [2,[25,33],[16,123]], # row 20
            [4,[18,89],[22,449],[28,380],[27,262]], # row 21
            [4,[23,401],[2,171],[28,190],[21,449]], # row 22
            [4,[14,499],[19,391],[22,401],[3,235]], # row 23
            [3,[9,214],[13,446],[15,286]], # row 24
            [0], #row 25
            [2,[16,66],[17,259]], # row 26
            [4,[21,262],[28,390],[8,268],[7,475]], # row 27
            [6,[27,390],[21,380],[22,190],[2,131],[9,320],[8,310]] # row 28
            ]
#Nodes values
node_values = [
    [0], #row 1
    [908,0], #row 2
    [117,515,0], #row 3
    [687,448,886,0], #row 4
    [1651,970,1373,922,0], #row 5
    [117,791,999,804,1540,0], #row 6
    [1882,1013,117,1404,1191,1765,0], #row 7
    [1310,441,844,832,529,1193,662,0], #row 8
    [889,246,684,202,720,840,1202,630,0], #row 9
    [760,181,559,479,997,643,1194,622,277,0], #row 10
    [2348,1707,1811,1619,697,2237,694,1223,1417,1694,0], #row 11
    [782,127,541,426,943,665,1140,568,223,54,1640,0], #row 12
    [697,546,984,98,952,814,1502,930,300,577,1649,523,0],#row 13
    [1370,928,317,1319,1463,1253,1154,934,1117,774,1848,756,1417,0], #row 14
    [1431,750,1153,702,220,1320,971,309,500,777,917,723,732,1250,0], #row 15
    [395,513,721,744,1262,278,1407,915,542,365,1959,387,842,975,1042,0], #row 16
    [697,316,739,504,1022,580,1329,757,302,180,1719,202,602,954,802,302,0], #row 17
    [1328,600,291,991,1148,1211,826,606,789,729,1520,711,1089,328,928,933,913,0], #row 18
    [490,540,626,817,1335,373,1553,981,615,392,2032,414,915,890,1115,95,397,960,0], #row 19
    [481,636,813,867,1385,364,1610,1038,665,480,2082,510,965,1077,1165,123,425,1056,187,0], #row 20
    [1244,511,300,902,1046,1127,737,517,700,664,1431,646,1000,417,826,849,844,89,895,972,0], #row 21
    [810,171,344,542,1029,693,1072,500,340,215,1766,197,640,559,809,416,395,514,446,538,449,0], #row 22
    [881,572,235,943,1430,764,1352,901,741,616,2046,598,1041,499,1210,486,796,526,391,578,615,401,0], #row 23
    [1145,460,898,416,506,1034,1257,595,214,491,1203,437,446,1331,286,756,516,1003,829,879,914,554,955,0], #row 24
    [513,631,780,862,1380,396,1605,1033,660,483,2077,505,960,1044,1160,118,420,1051,154,33,967,533,545,874,0], #row 25
    [461,497,704,678,1195,344,1432,938,476,349,1893,371,776,1041,976,66,236,898,161,189,852,360,552,690,184,0], #row 26
    [1407,538,642,929,784,1290,475,255,727,719,1169,665,1027,679,564,1012,854,351,1043,1135,262,597,877,850,1130,957,0], #row 27
    [1000,131,534,522,839,883,882,310,320,312,1576,258,620,797,619,605,447,469,636,728,380,190,591,534,723,550,407,0] #row 28
]
#Creacion del objeto busqueda para utilizar las distintas busquedas
busqueda = Search(ady_list, node_values)

#for node in busqueda.node_list:
    #print(node)
print('TEST BFS'.center(100,'-'))
print(f'RUTA POR BUSQUEDA A LO ANCHO: {busqueda.Breadth_first_search(8,18)}')
print('FIN TEST BFS'.center(100,'-'))
print('TEST SAHCS'.center(100,'-'))
print(f'RUTA escalada maxima pendiente: {busqueda.Steepest_ascent_hill_climbing_search(8,18)}')
print('FIN TEST SAHCS'.center(100,'-'))
print('TEST BFS'.center(100,'-'))
print(f'RUTA primero mejor: {busqueda.Best_first_search(8,18)}')
print('FIN TEST BFS'.center(100,'-'))