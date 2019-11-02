def rankIndex(values, rank):
    # Write your code here
    result = []
    for i, student_scores in enumerate(values):
        total = 0
        for student in student_scores:
            total += student
        result.append((i, total))
    sorted_scores_with_rank = sorted(result, key=lambda a: a[1], reverse=True)
    return sorted_scores_with_rank[rank-1][0]

arr = [[80, 96, 81, 77 ],
[78, 71, 93, 75 ],
[71, 98, 70, 95 ],
[80, 96, 89, 77]]

print(rankIndex(arr, 3))