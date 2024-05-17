''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 2, 4, 1, 1, 3, 0, 1, 0, 5, 2, 1, 0, 2]

ITEM_INDEX_THREE = student_pet_count_list[3]
ITEM_THREE_FROM_BACK = student_pet_count_list[-3]

NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)
SUM_PETS = 0

for INDIVIDUAL_PET_COUNT in student_pet_count_list:
  SUM_PETS = SUM_PETS + INDIVIDUAL_PET_COUNT

print("petCount: " + str(SUM_PETS))

# Find mean: avg num pets per student
MEAN = SUM_PETS / NUM_OF_STUDENTS
print("AvgNumPetsPerStudent: " + str(MEAN))