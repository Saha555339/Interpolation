import numpy as np
import matplotlib.pyplot as plt
from Interpolation import Interpolation

def main():
    print("Введите начальное значение х и конечное")
    start, end= map(int, (input().split()))    
    if end<start:
        print("Некорректные входные данные")
    print("Введите шаг")
    step= int (input())
    x = np.linspace(start, end, step) #массив элеметнов x
    y = np.cos(x) #функция
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2.0)
    print("Введите массив исходных значений х для интерполяции")
    xin = list(map(np.double, (input().split()))) #узлы интерполяции
    for i in range(len(xin)):
        if(xin[i]<start or xin[i]>end):
            print("Некорректные входные данные")
    interp=Interpolation(x,y,xin) #класс интреполяции
    interp.InY() #функция подсчета значений yin
    print("Введите точки для сравнения")
    xp=list(map(np.double, input().split())) #точки для сравнения значений функции и интреполирующей функции
    k=0
    for i in range(len(xp)):
        if(xp[i]<xin[0] or xp[i]>xin[len(xin)-1]):
            k=k+1
    if(k>0):        
        print("Некорректные входные данные")
    print("Значения функции:")
    yp=np.cos(xp) #значения функции в заданных точках
    print(yp)
    interp.ShowInt(xp) #функция подсчета значений интерполирующей функции
    print("Значение интерполирующей функции:")
    print(interp.yinxp)
    ax.plot(interp.xin, interp.yin, linewidth = 1.0, c = 'orange') 
    plt.show()

if __name__=="__main__":
    main()