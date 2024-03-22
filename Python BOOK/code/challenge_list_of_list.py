def enrollment_stats(list_of_universities):
    
    total_students = []
    total_tuition = []
    
    for university in list_of_universities:  
        total_students.append(university[1])
        total_tuition.append(university[2])
        
        return total_students, total_tuition

def mean(values):
    """Return the median value of the list values"""
    return sum(values) / len(values)

def median(values):
    """Return the median value of the list values"""
    values.sort()
    
    if len (values) % 2 == 1:
        
        center_index = int(len(values) / 2)
        return values[center_index]
    else:
        left_center_index = (len(values) - 1) // 2
        right_center_index = (len(values) + 1) // 2
        return mean([values[left_center_index], values[right_center_index]])
    
universities = [
        ["Tuks", 2000, 50000],
        ["NWU", 2000, 60000], 
        ["Maties", 1800, 90000],
        ["Wits", 3000, 40000],
        ["UJ", 3000, 30000], 
        ["Unisa", 2000, 50000], 
        ["Akademia", 2000, 50000], 
    ]
    
totals = enrollment_stats(universities)
    
print("\n")
print("*****" * 6)
print(f"Total students:   {sum(totals[0]):,}")
print(f"Total tuition:  R {sum(totals[1]):,}")
print(f"\nStudent mean:     {mean(totals[0]):,.2f}")
print(f"Student median:   {median(totals[0]):,}")
print(f"\nTuition mean:   R {mean(totals[1]):,.2f}")
print(f"Tuition median: R {median(totals[1]):,}")
print("*****" * 6)
print("\n")