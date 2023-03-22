list_scores = input('Input a list of student score ').split()

#print list scores of student in class
for i in range(0, len(list_scores)):
    list_scores[i]=int(list_scores[i])
print(list_scores)

# compare and export the highest scores in class
highest_score = 0

for score in list_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in class is: {highest_score}") 


