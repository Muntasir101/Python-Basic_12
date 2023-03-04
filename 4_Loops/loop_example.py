marks = [20, 22, 34, 55, 60, 66, 70, 77, 80, 90, 99, 0]
pass_marks = []
fail_marks = []

for i in marks:
    if i >= 40:
        pass_marks.append(i)
        pass_marks.sort(reverse=False)
    else:
        fail_marks.append(i)
        fail_marks.sort(reverse=False)

print("Pass Marks are: " + str(pass_marks))
print("Fail Marks are: " + str(fail_marks))
