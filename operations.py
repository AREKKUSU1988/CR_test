# 四則運算
n1=int(input("數一: "))
n2=int(input("數二: "))
op=input("運算:+, -, *, /: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")


# 高二數學_空間距離
x1=int(input("請先輸入基礎物件座標點的x值: "))
y1=int(input("請先輸入基礎物件座標點的y值: "))
z1=int(input("請先輸入基礎物件座標點的z值: "))
class Point:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def show(self):
        self.x=str(self.x)
        self.y=str(self.y)
        self.z=str(self.z)
        print("您已建立基礎物件的座標為: "+"("+self.x+", "+self.y+", "+self.z+")")
    def distance(self, x2, y2, z2):
        self.x=int(self.x)
        self.y=int(self.y)
        self.z=int(self.z)
        result=(((x2-self.x)**2+(y2-self.y)**2+(z2-self.z)**2)**0.5)
        return result
p1=Point(x1,y1,z1)
p1.show()
command=input("請問是否有要計算空間中某觀測物與您所建立基礎物件的距離，是請按\"y\"/否請按\"n\": ",)
if command=="y":
    x2=int(input("請輸入觀測物座標點的x值: "))
    y2=int(input("請輸入觀測物座標點的y值: "))
    z2=int(input("請輸入觀測物座標點的z值: "))
    d=p1.distance(x2,y2,z2)
    print(d)
elif command=="n":
    print("程式結束，感謝使用")
else:
    print("您的輸入不支援，程式結束")


# OPEN FILES
class File:
    def __init__(self,name):
        self.name=name
        self.file=None
    def open_read(self):
        with open(self.name, mode="r", encoding="utf-8") as self.file:
            return self.file.read()        
f1=File("Q2.txt")
f2=File("Q3.txt")
print(f1.open_read()+f2.open_read())




