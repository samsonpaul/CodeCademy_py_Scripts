grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(score):
    total = 0
    for item in score:
        total += item
    return total
print grades_sum(grades)

def grades_average(grades):
    total = grades_sum(grades)
    average = total / float(len(grades))
    return average
    
print grades_average(grades)