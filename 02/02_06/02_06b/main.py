# Tuples are immutable array-like structures

point = (5, 2)

x = point[0]
y = point[1]

def calc_square_properties(side_len):
    area = side_len * side_len
    perimiter = side_len * 4
    return (area, perimiter)  

calcRes = calc_square_properties(5)
print("Area: ", calcRes[0])
print("Perimteter: ", calcRes[1])
