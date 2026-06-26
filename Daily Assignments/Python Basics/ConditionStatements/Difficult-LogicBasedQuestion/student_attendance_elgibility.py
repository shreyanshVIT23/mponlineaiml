classes_held = int(input("Enter total classes held: "))
classes_attended = int(input("Enter classes attended: "))

attendance = (classes_attended / classes_held) * 100

print("Attendance =", attendance, "%")

if attendance >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")
