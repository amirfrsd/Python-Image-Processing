import numpy as np
import matplotlib.pyplot as plot
import matplotlib.ticker as mtick
import time
import functools as fnt
from collections import Counter
from PIL import Image

def recognitionFunc(filePath):
    recognized=[]
    exampleNumberColors=open('numtext.txt','r').read()
    exampleNumberColors=exampleNumberColors.split('\n')
    i=Image.open(filePath)
    iArray=np.array(i)
    iArrayList=iArray.tolist()
    inquestion=str(iArrayList)
    for examples in exampleNumberColors:
        if(len(examples)>3):
            splitTexts=examples.split('::')
            numberIs=splitTexts[0]
            pixelArrayIs=splitTexts[1]
            eachPixelEx=pixelArrayIs.split('],')
            eachPixelInq=inquestion.split('],')
            a=0
            while(a<len(eachPixelEx)):
                if(eachPixelEx[a]==eachPixelInq[a]):
                    recognized.append(int(numberIs))
                a += 1
    c=Counter(recognized)
    print(c)
    print(max(c.values()))
    xAxis=[]
    yAxis=[]
    for eachNumber in c:
        xAxis.append(eachNumber)
        yAxis.append(c[eachNumber])
    ax1=plot.subplot2grid((4,4),(0,0),rowspan=1,colspan=4)
    ax2=plot.subplot2grid((4,4),(1,0),rowspan=3,colspan=4)
    ax1.imshow(iArray)
    print(xAxis,yAxis)
    ax2.bar(xAxis,yAxis,align="center")
    plot.ylim(350)
    plot.show()
recognitionFunc('test.png')