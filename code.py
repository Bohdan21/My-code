from math import pi, sqrt, acos

#create class for circle
class Circle(object):
    def __init__(self,r=False,l=False):
        self.r=r
        self.l=l

    def area(self):
        return round(pi*self.r**2, 2)

    def fer(self):
        self.l=round(2*pi*self.r, 2)
        return round(self.l, 2)

    def radius(self):
        self.r = self.l / (2 * pi)
        return round(self.r, 2)

    def mkCir():
        a=input("Choise data to set(radius(r) or circumference(c)): ")
        a=a.lower()
        if a=="r" or a=="radius":
            rad=int(input("Set radius: "))
            cir=Circle(r=rad)
            Circle.fer(cir)
            Circle.outp(cir)
        elif a=="c":
            l=int(input("Set circumference: "))
            cir=Circle(l=l)
            Circle.outp(cir)

    def outp(self):
        print("CIRCLE:")
        print("Radius:",self.radius())
        print("Area:",self.area())
        print("Circumference:", self.fer())

#craete class for qudrangle
class Quadrangle(object):
    def __init__(self,a=False,b=False,p=False,s=False):
        self.a=a
        self.b=b
        self.p=p
        self.s=s

    def area(self):
        return self.a*self.b

    def perim(self):
        self.p=2*(self.a+self.b)
        return self.p

    def side(self):
        if self.p:
            self.b=(self.p-(self.a*2))/2
        elif self.s:
            self.b=self.s/self.a
        return self.b

    def mkQuad():
        aa=input("Choise data to set(sides(s), perimeter(p) or area(a)): ")
        if aa=="s":
            a = int(input("Enter first side: "))
            b = int(input("Enter second side: "))
            quad = Quadrangle(a=a, b=b)
            Quadrangle.outp(quad)
        elif aa=="p":
            p=int(input("Enter perimeter: "))
            a=int(input("Enter also one side: "))
            quad = Quadrangle(a=a,p=p)
            Quadrangle.side(quad)
            Quadrangle.outp(quad)
        elif aa == "a":
            s = int(input("Enter area: "))
            a = int(input("Enter also one side: "))
            quad = Quadrangle(a=a, s=s)
            Quadrangle.side(quad)
            Quadrangle.outp(quad)

    def outp(self):
        print("QUADRANGLE:")
        print("Area:",self.area())
        print("Perimeter:",self.perim())
        print("Sides:",self.a,self.b)

#create class for triangle
class Triangle(object):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        self.res = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return round(self.res,3)

    def per(self):
        return self.a+self.b+self.c

    def angles(self):
        an1=round(acos((self.b**2+self.c**2-self.a**2)/(2*self.b*self.c))*180/pi)
        an2=round(acos((self.a**2+self.c**2-self.b**2)/(2*self.a*self.c))*180/pi)
        an3 = 180 - (an1 + an2)
        return an1,an2,an3

    def outp(self):
        print("For triangle with sides "+str(self.a)+", "+str(self.b)+" and "+str(self.c)+":")
        print("Area:",self.area())
        print("Perimeter:",self.per())
        print("Angels:",self.angles())

#ask user to select
t = input("Select circle(c), quadrangle(q) or triangle(t): ")
t=t.lower()
#if was wrong select, ask again
while t!="circle" and t!="quadrangle" and t!="triangle" and t!="c" and t!="q" and t!="t":
    print("Wrong value!")
    t=input("Select again: ")
    t=t.lower()
if t=="circle" or t=="c":
    Circle.mkCir()
elif t=="quadrangle" or t=="q":
    Quadrangle.mkQuad()
elif t=="triangle" or t=="t":
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
    if a + b > c and a + c > b and b + c > a:
        trian=Triangle(a,b,c)
        Triangle.outp(trian)
    else:
        print("Not possible triangle with that sides.")