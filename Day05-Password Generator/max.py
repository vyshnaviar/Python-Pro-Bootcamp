student_score=[150,171,150,180,166,120,190,140,176,138]

max_score=0
for score in student_score:
    if score>max_score:
        max_score=score
print(max_score)

#Gauss value 5050=50pairs*101 
total=0
for number in range(1,101):
    total+=number
print(total)