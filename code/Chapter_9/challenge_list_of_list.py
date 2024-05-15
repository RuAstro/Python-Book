universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]


# This function takes the list of universities as input and returns two lists:
# one containing all the student enrollment values and the other containing all the tuition fees.
def enrollment_stats(universities):
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions


def mean(lst):
    return sum(lst) / len(lst)


# first sorts the list, then checks if the length of the list is even or odd, and calculates the median accordingly.
def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        return sorted_lst[n // 2]


enrollments, tuitions = enrollment_stats(universities)

total_students = sum(enrollments)
total_tuition = sum(tuitions)
mean_students = mean(enrollments)
median_students = median(enrollments)
mean_tuition = mean(tuitions)
median_tuition = median(tuitions)

print("Total number of students:", total_students)
print("Total tuition fees:", total_tuition)
print("Mean number of students:", mean_students)
print("Median number of students:", median_students)
print("Mean tuition fees:", mean_tuition)
print("Median tuition fees:", median_tuition)
