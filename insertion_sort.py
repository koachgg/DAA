# importing libraries 
import random
import matplotlib.pyplot as plt
import numpy as np

# Insertion_sort
def insertion_sort(arr):
    comparisons = 0
    assignments = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1

        arr[j + 1] = key
        assignments += 1

    return comparisons, assignments
# functionn to generate random data
def generate_random_data(n):
    return [random.randint(1, 1000) for _ in range(n)]

def run_insertion_sort_experiment(n_values):
    min_comparisons = []
    max_comparisons = []
    avg_comparisons = []

    min_assignments = []
    max_assignments = []
    avg_assignments = []

    for n in n_values:
        comparisons_list = []
        assignments_list = []

        for _ in range(10):  # Repeat each experiment 10 times
            data = generate_random_data(n)
            comparisons, assignments = insertion_sort(data.copy())
            comparisons_list.append(comparisons)
            assignments_list.append(assignments)

        min_comparisons.append(min(comparisons_list))
        max_comparisons.append(max(comparisons_list))
        avg_comparisons.append(np.mean(comparisons_list))

        min_assignments.append(min(assignments_list))
        max_assignments.append(max(assignments_list))
        avg_assignments.append(np.mean(assignments_list))

    return min_comparisons, max_comparisons, avg_comparisons, min_assignments, max_assignments, avg_assignments

n_values = list(range(10, 101, 5))
min_comp, max_comp, avg_comp, min_assign, max_assign, avg_assign = run_insertion_sort_experiment(n_values)

# Plottinng the Graph
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.plot(n_values, min_comp, label="Min Comparisons")
plt.plot(n_values, max_comp, label="Max Comparisons")
plt.plot(n_values, avg_comp, label="Avg Comparisons")
plt.xlabel("Input Size (n)")
plt.ylabel("Comparisons")
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(n_values, min_assign, label="Min Assignments")
plt.plot(n_values, max_assign, label="Max Assignments")
plt.plot(n_values, avg_assign, label="Avg Assignments")
plt.xlabel("Input Size (n)")
plt.ylabel("Assignments")
plt.legend()

plt.tight_layout()
plt.show()
