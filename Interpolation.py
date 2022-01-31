import numpy as np
class Interpolation:
    def __init__(self, x, y, xin):
        self.x=x
        self.y=y
        self.xin=xin
        self.yin=[]
        self.yinxp=[]

    def InY(self):
        for i in range(len(self.xin)):
            for j in range(len(self.x)-1):
                if (self.xin[i])>=(self.x[j]) and (self.xin[i]<=self.x[j+1]):
                    t = self.y[j+1] + (self.xin[i]-self.x[j+1])*(self.y[j]-self.y[j+1])/(self.x[j]-self.x[j+1]) #функция интерполяции
                    self.yin.append(t)
                    break
    
    def ShowInt(self, x):
        for i in range(len(x)):
            for j in range(len(self.xin)-1):
                if(self.xin[j]<=x[i]) and (self.xin[j+1]>=x[i]):
                    t=self.yin[j]+(self.yin[j+1]-self.yin[j])/(self.xin[j+1]-self.xin[j])*(x[i]-self.xin[j])
                    self.yinxp.append(t)
                    break