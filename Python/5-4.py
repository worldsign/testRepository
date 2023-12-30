def bmitest(kg,m):
    bmi = kg / m**2
    print(bmi)
    if bmi < 18.5:
        print("마른체형")
    elif 18.5 <= bmi < 25.0:
        print("표준")
    elif 25.0 <= bmi < 30.0:
        print("비만")
    elif bmi >= 30.0:
        print("고도비만")


def get_traingle_area(width, height):
    return width*height/2

def add_start_to_end(start, end):
    return sum(range(start,end+1))

def add_start_to_end_list(list_1):
    list1 = []
    for i in list_1:
        list1.append(i[:3])

    return list1
    
