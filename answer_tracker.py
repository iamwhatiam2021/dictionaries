students = {"padi": 0, "carlos": 0, "andres": 0, "eduardo": 0}
#there are 10 questions so we need to add a for with 10 steps
for i in range(10):
    name = input(f"Who got the answer right for question number {i+1}?")
    if name in students:
        students[name] = students[name] + 1
    else:
        # this means that the student was not in the dictionary, so put value 1
        students[name] = 1

print(f"Here is the list of students and answers: {students}")
# find the winner (find the key with the highest value)
# 1. get a list of all the keys
values = list(students.values())
values.sort(reverse=True) #sorts the list descending
winner = values[0]
# 2 - once I have the winner, go over each key and see if she is the winner
for key in students:
    if students[key] == winner:
        print(f"{key} is the winner! Congrats")
