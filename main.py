def calculate_average (*grades ):
    total_grades = len(grades)
    result = 0 # initialize result

    # Add each grade to the result
    for grade in grades:
        result += grade

    # calculate the average by diving the result by the number of grades
    # if total_grades > 0:
    #     return result / total_grades
    # else:
    #     return 0
    return result / total_grades if total_grades > 0 else 0

#Test cases
print(calculate_average(85, 90, 78, 92))    #Expected Average
print(calculate_average(100, 95))    #Expected average