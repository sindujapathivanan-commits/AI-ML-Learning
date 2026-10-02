#Dataset

#10 student markes

# 85, 72, 91, 68, 77, 95, 80, 88, 60, 74

#Store the marks

marks = [85, 72, 91, 68, 77, 95, 80, 88, 60, 74]

print(marks)


#Mean = average

mean = sum(marks) / len(marks)

print("Mean:", mean)

#Median

import statistics

median = statistics.median(marks)

print("Median:", median)

maximum = max(marks)
minimum = min(marks)

#Maximum and Minimum

print("Maximum:", maximum)
print("Minimum:", minimum)

# Variance
variance = statistics.pvariance(marks)

# Pass Count
pass_count = 0

for mark in marks:
    if mark >= 50:
        pass_count = pass_count + 1

print("Pass Count:", pass_count)

# Fail Count
fail_count = 0

for mark in marks:
    if mark < 50:
        fail_count = fail_count + 1

print("Fail Count:", fail_count)


#Probability Analysis

passed = sum(mark >= 50 for mark in marks)
above_80 = sum(mark > 80 for mark in marks)
failed = sum(mark < 50 for mark in marks)

