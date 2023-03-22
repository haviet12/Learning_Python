import math
def calcu(height, width):
    coverage = 5 # 1 can of paint can cover 5 square meter
    # area of the wall
    area = height*width
    # number of paints bucket can cover arae square meter
    cans = math.ceil(area/coverage)
    print(f'number of paints bucket is:{cans} ')

h = int(input('enter height of wall: '))
w = int(input('enter width of wall: '))
calcu(height=h, width=w)
