#Файл - сборник функций на питоне для всей игры

init python:
    from random import randint
    
    #Получить целое рандомное число
    def MyGetRandomInt( n_rand_start, n_rand_end ):
        return randint( n_rand_start, n_rand_end )
