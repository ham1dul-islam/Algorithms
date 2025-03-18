import matplotlib.pyplot as plt

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def sum_recursive(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_recursive(arr[1:])

def main():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result1_iterative = sum(arr1)
    result2_iterative = sum(arr2)
    result1_recursive = sum_recursive(arr1)
    result2_recursive = sum_recursive(arr2)

    print(f"Iterative sum of {arr1}: {result1_iterative}")
    print(f"Iterative sum of {arr2}: {result2_iterative}")
    print(f"Recursive sum of {arr1}: {result1_recursive}")
    print(f"Recursive sum of {arr2}: {result2_recursive}")

    # Visualization
    labels = ['[1,2,3,4,5]', '[1,2,3,4,5,6,7,8,9,10]']
    iterative_sums = [result1_iterative, result2_iterative]
    recursive_sums = [result1_recursive, result2_recursive]

    x = range(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, iterative_sums, width, label='Iterative Sum')
    rects2 = ax.bar([i + width for i in x], recursive_sums, width, label='Recursive Sum')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Sum')
    ax.set_title('Comparison of Iterative and Recursive Sums')
    ax.set_xticks([i + width / 2 for i in x])
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()