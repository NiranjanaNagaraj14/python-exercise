def triangle(a,b,c):
        if a + b <= c or a + c <= b or b + c <= a:
            print("Invalid triangle sides.")
            return
    peri = (a + b + c) / 2
    print("The Semi Perimeter of Triangle:", peri)
    area = (peri * (peri - a) * (peri - b) * (peri - c)) ** 0.5
    print("The Area of Triangle is:", area)

def rectangle(a,b):
   semi_peri = a + b
    print("The Semi Perimeter of Rectangle:", semi_peri)
    area = a * b
    print("The Area of Rectangle is:", area)
def square(a):
     semi_peri = 2 * a
    print("The Semi Perimeter of Square:", semi_peri)
    area = a * a
    print("The Area of Square is:", area)
triangle(5,6,7)
rectangle(5,10)
square(5)
