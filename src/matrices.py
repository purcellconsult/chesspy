import const

'''
63 62 61 60 59 58 57 56
55 54 53 52 51 50 49 48
47 46 45 44 43 42 41 40
39 38 37 36 35 34 33 32
31 30 29 28 27 26 25 24
23 22 21 20 19 18 17 16
15 14 13 12 11 10 09 08
07 06 05 04 03 02 01 00
'''


BLANCBOARD = [           0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0 ]


TESTBOARD1 = [            4, 0, 0, 5, 0, 4, 6, 0,
                         0, 1, 1, 0, 3, 1, 1, 1,
                         0, 2, 0, 0, 3, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         1, 0, 0, 1,-1,-3, 0, 0,
                        -1, 0, 0,-1, 0, 0, 0, 0,
                         0,-1,-5,-2,-3,-1,-1,-1,
                        -4, 0, 0, 0, 0,-4,-6, 0 ]

TESTBOARD = [            4, 0, 0, 0, 6, 0, 0, 4,
                         1, 0, 0, 0, 0, 0, 0, 1,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                        -1, 0, 0, 0, 0, 0, 0,-1,
                        -4, 0, 0, 0,-6, 0, 0,-4 ]

# default setup at game start
STARTBOARD = [           4, 2, 3, 5, 6, 3, 2, 4,
                         1, 1, 1, 1, 1, 1, 1, 1,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                        -1,-1,-1,-1,-1,-1,-1,-1,
                        -4,-2,-3,-5,-6,-3,-2,-4 ]


#----- diagonals start points -----#
diagonal_lr_start = [   0,  1,  2,  3,  4,  5,  6,  7,
                        1,  2,  3,  4,  5,  6,  7, 15,
                        2,  3,  4,  5,  6,  7, 15, 23,
                        3,  4,  5,  6,  7, 15, 23, 31,
                        4,  5,  6,  7, 15, 23, 31, 39,
                        5,  6,  7, 15, 23, 31, 39, 47,
                        6,  7, 15, 23, 31, 39, 47, 55,
                        7, 15, 23, 31, 39, 47, 55, 63 ]

diagonal_rl_start = [    0,  1,  2,  3,  4,  5,  6,  7,
                         8,  0,  1,  2,  3,  4,  5,  6,
                        16,  8,  0,  1,  2,  3,  4,  5,
                        24, 16,  8,  0,  1,  2,  3,  4,
                        32, 24, 16,  8,  0,  1,  2,  3,
                        40, 32, 24, 16,  8,  0,  1,  2,
                        48, 40, 32, 24, 16,  8,  0,  1,
                        56, 48, 40, 32, 24, 16,  8,  0 ]

#----- lenght of each diagonal -----#
diagonal_lr_lenght = [  1, 2, 3, 4, 5, 6, 7, 8,
                        2, 3, 4, 5, 6, 7, 8, 7,
                        3, 4, 5, 6, 7, 8, 7, 6,
                        4, 5, 6, 7, 8, 7, 6, 5,
                        5, 6, 7, 8, 7, 6, 5, 4,
                        6, 7, 8, 7, 6, 5, 4, 3,
                        7, 8, 7, 6, 5, 4, 3, 2,
                        8, 7, 6, 5, 4, 3, 2, 1 ]
        
diagonal_rl_lenght = [  8, 7, 6, 5, 4, 3, 2, 1,
                        7, 8, 7, 6, 5, 4, 3, 2,
                        6, 7, 8, 7, 6, 5, 4, 3,
                        5, 6, 7, 8, 7, 6, 5, 4,
                        4, 5, 6, 7, 8, 7, 6, 5,
                        3, 4, 5, 6, 7, 8, 7, 6,
                        2, 3, 4, 5, 6, 7, 8, 7,
                        1, 2, 3, 4, 5, 6, 7, 8 ]