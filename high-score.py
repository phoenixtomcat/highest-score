# input the list of student scores separated by a space
student_scores = input("Input a list of student scores (separated by a space): ").split()
# convert the list of strings into a list of integers
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# initialise the highest score to 0
highscore = 0
# loop through the list of student scores
for score in student_scores:
  # if the current score is higher than the highest score
  if highscore < score:
    # update the highest score
    highscore = score
      # print the highest score
print(f"The highest score in the class is: {highscore}")