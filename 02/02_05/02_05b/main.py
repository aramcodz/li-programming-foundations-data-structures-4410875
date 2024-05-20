seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

# a. print out rownum and inner list -> student-names
for i, row in enumerate(seating_chart):
    print(f"row {i+1}, students {row}")

print('-----------------------')

#b. print out studnent    
for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        print(f"{student_name} is in row {i+1}, seat {j+1}")
