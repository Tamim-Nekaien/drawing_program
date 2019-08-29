import sys
import math

class Color:
    def __init__(self,r,g,b,):
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)

    def printColor(self):
        print(self.r,self.g,self.b,'setrgbcolor')

class Linewidth:
    def __init__(self,w):
        self.w = float(w)

    def printLinewidth(self):
        print(self.w,'setlinewidth')

class Line:

    def __init__(self,xi,yi,xf,yf):
        self.xi = float(xi)
        self.yi = float(yi)
        self.xf = float(xf)
        self.yf = float(yf)

    def Translate(self,dx,dy):
        self.xi += float(dx)
        self.xf += float(dx)
        self.yi += float(dy)
        self.yf += float(dy)

    def Rotate(self,deg):
        x = self.xi * math.cos(math.radians(float(deg))) - self.yi * math.sin(math.radians(float(deg)))
        x1 = self.xf * math.cos(math.radians(float(deg))) - self.yf * math.sin(math.radians(float(deg)))
        y = self.xi * math.sin(math.radians(float(deg))) + self.yi * math.cos(math.radians(float(deg)))
        y1 = self.xf * math.sin(math.radians(float(deg))) + self.yf * math.cos(math.radians(float(deg)))
        self.xi = x
        self.xf = x1
        self.yi = y
        self.yf = y1
    def printLine(self):
        print(self.xi,self.yi,'moveto')
        print(self.xf,self.yf,'lineto')
        print('stroke')

class Rect:

    def __init__(self,xi,yi,xf,yf):
        self.x1 = float(xi)
        self.y1 = float(yi)
        self.x2 = self.x1 + float(xf)
        self.y2 = float(yf)
        self.x3 = self.x1 + float(xf)
        self.y3 = self.y1 + float(yf)
        self.x4 = float(xi)
        self.y4 = self.y1 + float(yf)

    def Translate(self,dx,dy):
        self.x1 += float(dx)
        self.x2 += float(dx)
        self.x3 += float(dx)
        self.x4 += float(dx)
        self.y1 += float(dy)
        self.y2 += float(dy)
        self.y3 += float(dy)
        self.y4 += float(dy)

    def Rotate(self,deg):
        x1 = self.x1 * math.cos(math.radians(float(deg))) - self.y1 * math.sin(math.radians(float(deg)))
        x2 = self.x2 * math.cos(math.radians(float(deg))) - self.y2 * math.sin(math.radians(float(deg)))
        x3 = self.x3 * math.cos(math.radians(float(deg))) - self.y3 * math.sin(math.radians(float(deg)))
        x4 = self.x4 * math.cos(math.radians(float(deg))) - self.y4 * math.sin(math.radians(float(deg)))
        y1 = self.x1 * math.sin(math.radians(float(deg))) + self.y1 * math.cos(math.radians(float(deg)))
        y2 = self.x2 * math.sin(math.radians(float(deg))) + self.y2 * math.cos(math.radians(float(deg)))
        y3 = self.x3 * math.sin(math.radians(float(deg))) + self.y3 * math.cos(math.radians(float(deg)))
        y4 = self.x4 * math.sin(math.radians(float(deg))) + self.y4 * math.cos(math.radians(float(deg)))
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4

    def printRect(self):
        print(self.x1,self.y1,'moveto')
        print(self.x2,self.y2,'lineto')
        print(self.x3,self.y3,'lineto')
        print(self.x4,self.y4,'lineto')
        print(self.x1,self.y1,'lineto')
        print('stroke')

stack = sys.stdin.read()
new_stack = []#just in case
stack = stack.replace('(',' ')
stack = stack.replace(')',' ')
stack = stack.split()

def shape():
    def methodapps():
        for method in reversed(list(new_stack)):
            if method == 'translate':
                a = new_stack.index('translate')
                dx = float(new_stack[a+1])
                dy = float(new_stack[a+2])
                new_stack.remove('translate')
                pip.Translate(dx,dy)
            elif method == 'rotate':
                a = new_stack.index('rotate')
                deg = float(new_stack[a+1])
                new_stack.remove('rotate')
                pip.Rotate(deg)
    for command in stack:
        if command == 'color':
            a = stack.index('color')
            r = stack[a+1]
            g = stack[a+2]
            b = stack[a+3]
            stack.remove('color')
            color = Color(r,g,b)
            color.printColor()
        elif command == 'linewidth':
            a = stack.index('linewidth')
            w = stack[a+1]
            line = Linewidth(w)
            stack.remove('linewidth')
            line.printLinewidth()
        elif command == 'translate':
                    a = stack.index('translate')
                    new_stack.append(stack[a])
                    new_stack.append(stack[a+1])
                    new_stack.append(stack[a+2])
                    stack.remove('translate')
        elif command == 'rotate':
                    a = stack.index('rotate')
                    new_stack.append(stack[a])
                    new_stack.append(stack[a+1])
                    stack.remove('rotate')
        elif command == 'line':
                    a = stack.index('line')
                    new_stack.append(stack[a])
                    new_stack.append(stack[a+1])
                    new_stack.append(stack[a+2])
                    new_stack.append(stack[a+3])
                    new_stack.append(stack[a+4])
                    stack.remove('line')


                    for sub_command in new_stack:
                        if sub_command  == 'line':
                            a = new_stack.index(sub_command)
                            xi = float(new_stack[a+1])
                            yi = float(new_stack[a+2])
                            xf = float(new_stack[a+3])
                            yf = float(new_stack[a+4])
                            new_stack.remove(sub_command)
                            pip = Line(xi,yi,xf,yf)
                            methodapps()
                            pip.printLine()
        elif command == 'rect':
                    a = stack.index('rect')
                    new_stack.append(stack[a])
                    new_stack.append(stack[a+1])
                    new_stack.append(stack[a+2])
                    new_stack.append(stack[a+3])
                    new_stack.append(stack[a+4])
                    stack.remove('rect')
                    for sub_command in new_stack:
                        if sub_command == 'rect':
                            a = new_stack.index(sub_command)
                            xi = float(new_stack[a+1])
                            yi = float(new_stack[a+2])
                            xf = float(new_stack[a+3])
                            yf = float(new_stack[a+4])
                            new_stack.remove(sub_command)
                            pip = Rect(xi,yi,xf,yf)
                            methodapps()
                            pip.printRect()


print('%!PS-Adobe-3.1')
shape()
print('showpage')
