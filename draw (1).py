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

    def Scale(self,s):
        self.xi *= float(s)
        self.yi *= float(s)
        self.xf *= float(s)
        self.yf *= float(s)

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
        self.xi = float(xi)
        self.yi = float(yi)
        self.xf = float(xf)
        self.yf = float(yf)
        self.x1 = self.xi
        self.y1 = self.yi
        self.x2 = self.x1 + self.xf
        self.y2 = self.yf
        self.x3 = self.x1 + self.xf
        self.y3 = self.y1 + self.yf
        self.x4 = self.xi
        self.y4 = self.y1 + self.yf

    def Translate(self,dx,dy):
        self.x1 += float(dx)
        self.x2 += float(dx)
        self.x3 += float(dx)
        self.x4 += float(dx)
        self.y1 += float(dy)
        self.y2 += float(dy)
        self.y3 += float(dy)
        self.y4 += float(dy)

    def Scale(self,s):
        self.x1 *= float(s)
        self.x2 *= float(s)
        self.x3 *= float(s)
        self.x4 *= float(s)
        self.y1 *= float(s)
        self.y2 *= float(s)
        self.y3 *= float(s)
        self.y4 *= float(s)

    def Rotate(self,deg):

            x1 = self.x1 * math.cos(math.radians(float(deg))) - self.y1 * math.sin(math.radians(float(deg)))
            x2 = (self.x2 * math.cos(math.radians(float(deg)))) - (self.y2 * math.sin(math.radians(float(deg))))
            x3 = self.x3 * math.cos(math.radians(float(deg))) - self.y3 * math.sin(math.radians(float(deg)))
            x4 = self.x4 * math.cos(math.radians(float(deg))) - self.y4 * math.sin(math.radians(float(deg)))
            y1 = self.x1 * math.sin(math.radians(float(deg))) + self.y1 * math.cos(math.radians(float(deg)))
            y2 = (self.x2 * math.sin(math.radians(float(deg)))) + (self.y2 * math.cos(math.radians(float(deg))))
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

class filledRect(Rect):
    def __init__(self,xi,yi,xf,yf):
        super().__init__(xi,yi,xf,yf)

    def printfilledRect(self):
        print(self.x1,self.y1,'moveto')
        print(self.x2,self.y2,'lineto')
        print(self.x3,self.y3,'lineto')
        print(self.x4,self.y4,'lineto')
        print(self.x1,self.y1,'lineto')
        print('fill')


class Tri:
    def __init__(self,xi,yi,r,sides):
        self.xi = float(xi)
        self.yi = float(yi)
        self.r = float(r)
        self.angle = float(360/sides)
        self.x1 = self.xi + self.r
        self.y1 = self.yi
        self.y2 = (self.r * math.sin(math.radians(self.angle))) + self.yi
        self.x2 = (self.r * math.cos(math.radians(self.angle))) + self.xi
        self.y3 = (self.r * math.sin(math.radians(2*self.angle))) + self.yi
        self.x3 = (self.r * math.cos(math.radians(2*self.angle))) + self.xi

    def Translate(self,dx,dy):
        self.x1 += float(dx)
        self.y1 += float(dy)
        self.x2 += float(dx)
        self.y2 += float(dy)
        self.x3 += float(dx)
        self.y3 += float(dy)

    def Scale(self,s):
        self.x1 *= float(s)
        self.y1 *= float(s)
        self.x2 *= float(s)
        self.y2 *= float(s)
        self.x3 *= float(s)
        self.y3 *= float(s)

    def Rotate(self,deg):
        ptx1 = self.x1 * math.cos(math.radians(float(deg))) -self.y1 * math.sin(math.radians(float(deg)))
        pty1 = self.x1 * math.sin(math.radians(float(deg))) +self.y1 * math.cos(math.radians(float(deg)))
        ptx2 = self.x2 * math.cos(math.radians(float(deg))) - self.y2 * math.sin(math.radians(float(deg)))
        pty2 = self.x2 * math.sin(math.radians(float(deg))) + self.y2 * math.cos(math.radians(float(deg)))
        ptx3 = self.x3 * math.cos(math.radians(float(deg))) - self.y3 * math.sin(math.radians(float(deg)))
        pty3 = self.x3 * math.sin(math.radians(float(deg))) + self.y3 * math.cos(math.radians(float(deg)))
        self.x1 = ptx1
        self.y1 = pty1
        self.x2 = ptx2
        self.y2 = pty2
        self.x3 = ptx3
        self.y3 = pty3

    def printTri(self):
        print(self.x1,self.y1, 'moveto')
        print(self.x2,self.y2, 'lineto')
        print(self.x3,self.y3, 'lineto')
        print(self.x1,self.y1, 'lineto')
        print('stroke')

class filledTri(Tri):
    def __init__(self,xi,yi,r,sides):
        super().__init__(xi,yi,r,sides)

    def printfilledTri(self):
        print(self.x1,self.y1, 'moveto')
        print(self.x2,self.y2, 'lineto')
        print(self.x3,self.y3, 'lineto')
        print(self.x1,self.y1, 'lineto')
        print('fill')

class Square(Tri):
    def __init__(self,xi,yi,r,sides):
        super().__init__(xi,yi,r,sides)
        self.y4 = (self.r * math.sin(math.radians(3*self.angle))) + self.yi
        self.x4 = (self.r * math.cos(math.radians(3*self.angle))) + self.xi

    def Translate(self,dx,dy):
        self.x1 += float(dx)
        self.y1 += float(dy)
        self.x2 += float(dx)
        self.y2 += float(dy)
        self.x3 += float(dx)
        self.y3 += float(dy)
        self.x4 += float(dx)
        self.y4 += float(dy)

    def Scale(self,s):
        self.x1 *= float(s)
        self.y1 *= float(s)
        self.x2 *= float(s)
        self.y2 *= float(s)
        self.x3 *= float(s)
        self.y3 *= float(s)
        self.x4 *= float(s)
        self.y4 *= float(s)

    def Rotate(self,deg):
        ptx1 = self.x1 * math.cos(math.radians(float(deg))) -self.y1 * math.sin(math.radians(float(deg)))
        pty1 = self.x1 * math.sin(math.radians(float(deg))) +self.y1 * math.cos(math.radians(float(deg)))
        ptx2 = self.x2 * math.cos(math.radians(float(deg))) - self.y2 * math.sin(math.radians(float(deg)))
        pty2 = self.x2 * math.sin(math.radians(float(deg))) + self.y2 * math.cos(math.radians(float(deg)))
        ptx3 = self.x3 * math.cos(math.radians(float(deg))) - self.y3 * math.sin(math.radians(float(deg)))
        pty3 = self.x3 * math.sin(math.radians(float(deg))) + self.y3 * math.cos(math.radians(float(deg)))
        ptx4 = self.x4 * math.cos(math.radians(float(deg))) - self.y4 * math.sin(math.radians(float(deg)))
        pty4 = self.x4 * math.sin(math.radians(float(deg))) + self.y4 * math.cos(math.radians(float(deg)))
        self.x1 = ptx1
        self.y1 = pty1
        self.x2 = ptx2
        self.y2 = pty2
        self.x3 = ptx3
        self.y3 = pty3
        self.x4 = ptx4
        self.y4 = pty4

    def printSquare(self):
        print(self.x1,self.y1, 'moveto')
        print(self.x2,self.y2, 'lineto')
        print(self.x3,self.y3, 'lineto')
        print(self.x4,self.y4, 'lineto')
        print(self.x1,self.y1, 'lineto')
        print('stroke')

class filledSquare(Square):
    def __init__(self,xi,yi,r,sides):
        super().__init__(xi,yi,r,sides)

    def printfilledSquare(self):
        print(self.x1,self.y1, 'moveto')
        print(self.x2,self.y2, 'lineto')
        print(self.x3,self.y3, 'lineto')
        print(self.x4,self.y4, 'lineto')
        print(self.x1,self.y1, 'lineto')
        print('fill')

class Penta(Square):
    def __init__(self,xi,yi,r,sides):
        super().__init__(xi,yi,r,sides)
        self.y5 = (self.r * math.sin(math.radians(4*self.angle))) + self.yi
        self.x5 = (self.r * math.cos(math.radians(4*self.angle))) + self.xi

    def Translate(self,dx,dy):
        self.x1 += float(dx)
        self.y1 += float(dy)
        self.x2 += float(dx)
        self.y2 += float(dy)
        self.x3 += float(dx)
        self.y3 += float(dy)
        self.x4 += float(dx)
        self.y4 += float(dy)
        self.x5 += float(dx)
        self.y5 += float(dy)

    def Scale(self,s):
        self.x1 *= float(s)
        self.y1 *= float(s)
        self.x2 *= float(s)
        self.y2 *= float(s)
        self.x3 *= float(s)
        self.y3 *= float(s)
        self.x4 *= float(s)
        self.y4 *= float(s)
        self.x5 *= float(s)
        self.y5 *= float(s)

    def Rotate(self,deg):
        ptx1 = self.x1 * math.cos(math.radians(float(deg))) -self.y1 * math.sin(math.radians(float(deg)))
        pty1 = self.x1 * math.sin(math.radians(float(deg))) +self.y1 * math.cos(math.radians(float(deg)))
        ptx2 = self.x2 * math.cos(math.radians(float(deg))) - self.y2 * math.sin(math.radians(float(deg)))
        pty2 = self.x2 * math.sin(math.radians(float(deg))) + self.y2 * math.cos(math.radians(float(deg)))
        ptx3 = self.x3 * math.cos(math.radians(float(deg))) - self.y3 * math.sin(math.radians(float(deg)))
        pty3 = self.x3 * math.sin(math.radians(float(deg))) + self.y3 * math.cos(math.radians(float(deg)))
        ptx4 = self.x4 * math.cos(math.radians(float(deg))) - self.y4 * math.sin(math.radians(float(deg)))
        pty4 = self.x4 * math.sin(math.radians(float(deg))) + self.y4 * math.cos(math.radians(float(deg)))
        ptx5 = self.x5 * math.cos(math.radians(float(deg))) - self.y5 * math.sin(math.radians(float(deg)))
        pty5 = self.x5 * math.sin(math.radians(float(deg))) + self.y5 * math.cos(math.radians(float(deg)))
        self.x1 = ptx1
        self.y1 = pty1
        self.x2 = ptx2
        self.y2 = pty2
        self.x3 = ptx3
        self.y3 = pty3
        self.x4 = ptx4
        self.y4 = pty4
        self.x5 = ptx5
        self.y5 = pty5

    def printPenta(self):
        print(self.x1,self.y1, 'moveto')
        print(self.x2,self.y2, 'lineto')
        print(self.x3,self.y3, 'lineto')
        print(self.x4,self.y4, 'lineto')
        print(self.x5,self.y5, 'lineto')
        print(self.x1,self.y1, 'lineto')
        print('stroke')

class filledPenta(Penta):
    def __init__(self,xi,yi,r,sides):
        super().__init__(xi,yi,r,sides)

    def printfilledPenta(self):
        print(self.x1,self.y1, 'moveto')
        print(self.x2,self.y2, 'lineto')
        print(self.x3,self.y3, 'lineto')
        print(self.x4,self.y4, 'lineto')
        print(self.x5,self.y5, 'lineto')
        print(self.x1,self.y1, 'lineto')
        print('fill')

class Hexa(Penta):
    def __init__(self,xi,yi,r,sides):
        super().__init__(xi,yi,r,sides)
        self.y6 = (self.r * math.sin(math.radians(5*self.angle))) + self.yi
        self.x6 = (self.r * math.cos(math.radians(5*self.angle))) + self.xi

    def Translate(self,dx,dy):
        self.x1 += float(dx)
        self.y1 += float(dy)
        self.x2 += float(dx)
        self.y2 += float(dy)
        self.x3 += float(dx)
        self.y3 += float(dy)
        self.x4 += float(dx)
        self.y4 += float(dy)
        self.x5 += float(dx)
        self.y5 += float(dy)
        self.x6 += float(dx)
        self.y6 += float(dy)

    def Scale(self,s):
        self.x1 *= float(s)
        self.y1 *= float(s)
        self.x2 *= float(s)
        self.y2 *= float(s)
        self.x3 *= float(s)
        self.y3 *= float(s)
        self.x4 *= float(s)
        self.y4 *= float(s)
        self.x5 *= float(s)
        self.y5 *= float(s)
        self.x6 *= float(s)
        self.y6 *= float(s)

    def Rotate(self,deg):
        ptx1 = self.x1 * math.cos(math.radians(float(deg))) -self.y1 * math.sin(math.radians(float(deg)))
        pty1 = self.x1 * math.sin(math.radians(float(deg))) +self.y1 * math.cos(math.radians(float(deg)))
        ptx2 = self.x2 * math.cos(math.radians(float(deg))) - self.y2 * math.sin(math.radians(float(deg)))
        pty2 = self.x2 * math.sin(math.radians(float(deg))) + self.y2 * math.cos(math.radians(float(deg)))
        ptx3 = self.x3 * math.cos(math.radians(float(deg))) - self.y3 * math.sin(math.radians(float(deg)))
        pty3 = self.x3 * math.sin(math.radians(float(deg))) + self.y3 * math.cos(math.radians(float(deg)))
        ptx4 = self.x4 * math.cos(math.radians(float(deg))) - self.y4 * math.sin(math.radians(float(deg)))
        pty4 = self.x4 * math.sin(math.radians(float(deg))) + self.y4 * math.cos(math.radians(float(deg)))
        ptx5 = self.x5 * math.cos(math.radians(float(deg))) - self.y5 * math.sin(math.radians(float(deg)))
        pty5 = self.x5 * math.sin(math.radians(float(deg))) + self.y5 * math.cos(math.radians(float(deg)))
        ptx6 = self.x6 * math.cos(math.radians(float(deg))) - self.y6 * math.sin(math.radians(float(deg)))
        pty6 = self.x6 * math.sin(math.radians(float(deg))) + self.y6 * math.cos(math.radians(float(deg)))
        self.x1 = ptx1
        self.y1 = pty1
        self.x2 = ptx2
        self.y2 = pty2
        self.x3 = ptx3
        self.y3 = pty3
        self.x4 = ptx4
        self.y4 = pty4
        self.x5 = ptx5
        self.y5 = pty5
        self.x6 = ptx6
        self.y6 = pty6

    def printHexa(self):
            print(self.x1,self.y1, 'moveto')
            print(self.x2,self.y2, 'lineto')
            print(self.x3,self.y3, 'lineto')
            print(self.x4,self.y4, 'lineto')
            print(self.x5,self.y5, 'lineto')
            print(self.x6,self.y6, 'lineto')
            print(self.x1,self.y1, 'lineto')
            print('stroke')

class filledHexa(Hexa):
    def __init__(self,xi,yi,r,sides):
        super().__init__(xi,yi,r,sides)

    def printfilledHexa(self):
        print(self.x1,self.y1, 'moveto')
        print(self.x2,self.y2, 'lineto')
        print(self.x3,self.y3, 'lineto')
        print(self.x4,self.y4, 'lineto')
        print(self.x5,self.y5, 'lineto')
        print(self.x6,self.y6, 'lineto')
        print(self.x1,self.y1, 'lineto')
        print('fill')

class Ngon:
    def __init__(self,xi,yi,r,n):
        self.xi = float(xi)
        self.yi = float(yi)
        self.r = float(r)
        self.angle  = float(360/n)
        self.n  = int(n)
        self.x = {}
        self.y = {}
        for i in range(self.n):
            self.x['self.x{}'.format(i)] = self.r * math.cos(math.radians(i * self.angle)) + self.xi
            self.y['self.y{}'.format(i)] = self.r * math.sin(math.radians(i * self.angle)) + self.yi

    def Translate(self,dx,dy):
            for i in range(self.n):
                self.x['self.x{}'.format(i)] += float(dx)
                self.y['self.y{}'.format(i)] += float(dy)

    def Scale(self,s):
            for i in range(self.n):
                self.x['self.x{}'.format(i)] *= float(s)
                self.y['self.y{}'.format(i)] *= float(s)


    def Rotate(self,deg):
            ptx = {}
            pty = {}
            for i in range(self.n):
                ptx['ptx{}'.format(i)] = self.x['self.x{}'.format(i)] * math.cos(math.radians(float(deg))) - self.y['self.y{}'.format(i)] * math.sin(math.radians(float(deg)))
                pty['pty{}'.format(i)] = self.x['self.x{}'.format(i)] * math.sin(math.radians(float(deg))) + self.y['self.y{}'.format(i)] * math.cos(math.radians(float(deg)))
            for i in range(self.n):
                self.x['self.x{}'.format(i)] = ptx['ptx{}'.format(i)]
                self.y['self.y{}'.format(i)] = pty['pty{}'.format(i)]


    def printNgon(self):
        print(self.x['self.x0'],self.y['self.y0'],'moveto')
        for i in range(1,self.n):
            print(self.x['self.x{}'.format(i)],self.y['self.y{}'.format(i)],'lineto')
        print(self.x['self.x0'],self.y['self.y0'],'lineto')
        print('stroke')

class filledNgon(Ngon):
    def __init__(self,xi,yi,r,n):
        super().__init__(xi,yi,r,n)

    def printfilledNgon(self):
        print(self.x['self.x0'],self.y['self.y0'],'moveto')
        for i in range(1,self.n):
            print(self.x['self.x{}'.format(i)],self.y['self.y{}'.format(i)],'lineto')
        print(self.x['self.x0'],self.y['self.y0'],'lineto')
        print('fill')

stack = sys.stdin.read()
new_stack = []#just in case
stack = stack.replace('(',' ')
stack = stack.replace(')', ' ')
stack = stack.split()

def shape():
    def subapps():
        a = new_stack.index(sub_command)
        xi = float(new_stack[a+1])
        yi = float(new_stack[a+2])
        xf = float(new_stack[a+3])
        yf = float(new_stack[a+4])
        new_stack.remove(sub_command)
    def subappstri():
        a = new_stack.index(sub_command)
        xi = float(new_stack[a+1])
        yi = float(new_stack[a+2])
        r = float(new_stack[a+3])
        new_stack.remove(sub_command)
    def subappsngon():
        a = new_stack.index(sub_command)
        xi = float(new_stack[a+1])
        yi = float(new_stack[a+2])
        r = float(new_stack[a+3])
        n = float(new_stack[a+4])
        new_stack.remove(sub_command)
    def methodapps():

        for var,method in reversed(list(enumerate(new_stack))):
            if method == 'translate':
                            del new_stack[var]
                            dx = new_stack.pop(var)
                            dy = new_stack.pop(var)
                            shape.Translate(dx,dy)
            elif method == 'rotate':
                            del new_stack[var]
                            deg = new_stack.pop(var)
                            shape.Rotate(deg)
            elif method == 'scale':
                            del new_stack[var]
                            s = new_stack.pop(var)
                            shape.Scale(s)

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


        elif command == 'scale':
                    a = stack.index('scale')
                    new_stack.append(stack[a])
                    new_stack.append(stack[a+1])
                    stack.remove('scale')

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
                            shape = Line(xi,yi,xf,yf)
                            methodapps()
                            shape.printLine()

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
                            shape = Rect(xi,yi,xf,yf)
                            methodapps()
                            shape.printRect()

        elif command == 'filledrect':
                    a = stack.index('filledrect')
                    new_stack.append(stack[a])
                    new_stack.append(stack[a+1])
                    new_stack.append(stack[a+2])
                    new_stack.append(stack[a+3])
                    new_stack.append(stack[a+4])
                    stack.remove('filledrect')

                    for sub_command in new_stack:
                        if sub_command == 'filledrect':
                            a = new_stack.index(sub_command)
                            xi = float(new_stack[a+1])
                            yi = float(new_stack[a+2])
                            xf = float(new_stack[a+3])
                            yf = float(new_stack[a+4])
                            new_stack.remove(sub_command)
                            shape = filledRect(xi,yi,xf,yf)
                            methodapps()
                            shape.printfilledRect()


        elif command == 'tri':
            a = stack.index('tri')
            new_stack.append(stack[a])
            new_stack.append(stack[a+1])
            new_stack.append(stack[a+2])
            new_stack.append(stack[a+3])
            stack.remove('tri')

            for sub_command in new_stack:
                if sub_command == 'tri':
                    sides = 3
                    a = new_stack.index(sub_command)
                    xi = float(new_stack[a+1])
                    yi = float(new_stack[a+2])
                    r = float(new_stack[a+3])
                    new_stack.remove(sub_command)
                    shape = Tri(xi,yi,r,sides)
                    #shape.triPoints()
                    methodapps()
                    shape.printTri()

        elif command == 'filledtri':
            a = stack.index('filledtri')
            new_stack.append(stack[a])
            new_stack.append(stack[a+1])
            new_stack.append(stack[a+2])
            new_stack.append(stack[a+3])
            stack.remove('filledtri')

            for sub_command in new_stack:
                if sub_command == 'filledtri':
                    sides = 3
                    a = new_stack.index(sub_command)
                    xi = float(new_stack[a+1])
                    yi = float(new_stack[a+2])
                    r = float(new_stack[a+3])
                    new_stack.remove(sub_command)
                    shape = filledTri(xi,yi,r,sides)
                    methodapps()
                    shape.printfilledTri()

        elif command == 'square':
            a = stack.index('square')
            new_stack.append(stack[a])
            new_stack.append(stack[a+1])
            new_stack.append(stack[a+2])
            new_stack.append(stack[a+3])
            stack.remove('square')

            for sub_command in new_stack:
                if sub_command == 'square':
                    sides = 4
                    a = new_stack.index(sub_command)
                    xi = float(new_stack[a+1])
                    yi = float(new_stack[a+2])
                    r = float(new_stack[a+3])
                    new_stack.remove(sub_command)
                    shape = Square(xi,yi,r,sides)
                    methodapps()
                    shape.printSquare()

        elif command == 'filledsquare':
            a = stack.index('filledsquare')
            new_stack.append(stack[a])
            new_stack.append(stack[a+1])
            new_stack.append(stack[a+2])
            new_stack.append(stack[a+3])
            stack.remove('filledsquare')

            for sub_command in new_stack:
                if sub_command == 'filledsquare':
                    sides = 4
                    a = new_stack.index(sub_command)
                    xi = float(new_stack[a+1])
                    yi = float(new_stack[a+2])
                    r = float(new_stack[a+3])
                    new_stack.remove(sub_command)
                    shape = filledSquare(xi,yi,r,sides)
                    methodapps()
                    shape.printfilledSquare()

        elif command == 'penta':
            a = stack.index('penta')
            new_stack.append(stack[a])
            new_stack.append(stack[a+1])
            new_stack.append(stack[a+2])
            new_stack.append(stack[a+3])
            stack.remove('penta')

            for sub_command in new_stack:
                if sub_command == 'penta':
                    sides = 5
                    a = new_stack.index(sub_command)
                    xi = float(new_stack[a+1])
                    yi = float(new_stack[a+2])
                    r = float(new_stack[a+3])
                    new_stack.remove(sub_command)
                    shape = Penta(xi,yi,r,sides)
                    methodapps()
                    shape.printPenta()

        elif command == 'filledpenta':
            a = stack.index('filledpenta')
            new_stack.append(stack[a])
            new_stack.append(stack[a+1])
            new_stack.append(stack[a+2])
            new_stack.append(stack[a+3])
            stack.remove('filledpenta')

            for sub_command in new_stack:
                if sub_command == 'filledpenta':
                    sides = 5
                    a = new_stack.index(sub_command)
                    xi = float(new_stack[a+1])
                    yi = float(new_stack[a+2])
                    r = float(new_stack[a+3])
                    new_stack.remove(sub_command)
                    shape = filledPenta(xi,yi,r,sides)
                    methodapps()
                    shape.printfilledPenta()

        elif command == 'hexa':
            a = stack.index('hexa')
            new_stack.append(stack[a])
            new_stack.append(stack[a+1])
            new_stack.append(stack[a+2])
            new_stack.append(stack[a+3])
            stack.remove('hexa')

            for sub_command in new_stack:
                if sub_command == 'hexa':
                    sides = 6
                    a = new_stack.index(sub_command)
                    xi = float(new_stack[a+1])
                    yi = float(new_stack[a+2])
                    r = float(new_stack[a+3])
                    new_stack.remove(sub_command)
                    shape = Hexa(xi,yi,r,sides)
                    methodapps()
                    shape.printHexa()

        elif command == 'filledhexa':
            a = stack.index('filledhexa')
            new_stack.append(stack[a])
            new_stack.append(stack[a+1])
            new_stack.append(stack[a+2])
            new_stack.append(stack[a+3])
            stack.remove('filledhexa')

            for sub_command in new_stack:
                if sub_command == 'filledhexa':
                    sides = 6
                    a = new_stack.index(sub_command)
                    xi = float(new_stack[a+1])
                    yi = float(new_stack[a+2])
                    r = float(new_stack[a+3])
                    new_stack.remove(sub_command)
                    shape = filledHexa(xi,yi,r,sides)
                    methodapps()
                    shape.printfilledHexa()

        elif command == 'ngon':
            a = stack.index('ngon')
            new_stack.append(stack[a])
            new_stack.append(stack[a+1])
            new_stack.append(stack[a+2])
            new_stack.append(stack[a+3])
            new_stack.append(stack[a+4])
            stack.remove('ngon')

            for sub_command in new_stack:
                if sub_command == 'ngon':
                    a = new_stack.index(sub_command)
                    xi = float(new_stack[a+1])
                    yi = float(new_stack[a+2])
                    r = float(new_stack[a+3])
                    n = float(new_stack[a+4])
                    new_stack.remove(sub_command)
                    shape = Ngon(xi,yi,r,n)
                    methodapps()
                    shape.printNgon()

        elif command == 'filledngon':
            a = stack.index('filledngon')
            new_stack.append(stack[a])
            new_stack.append(stack[a+1])
            new_stack.append(stack[a+2])
            new_stack.append(stack[a+3])
            new_stack.append(stack[a+4])
            stack.remove('filledngon')

            for sub_command in new_stack:
                if sub_command == 'filledngon':
                    a = new_stack.index(sub_command)
                    xi = float(new_stack[a+1])
                    yi = float(new_stack[a+2])
                    r = float(new_stack[a+3])
                    n = float(new_stack[a+4])
                    new_stack.remove(sub_command)
                    shape = filledNgon(xi,yi,r,n)
                    methodapps()
                    shape.printfilledNgon()




print('%!PS-Adobe-3.1')
shape()
print('showpage')
