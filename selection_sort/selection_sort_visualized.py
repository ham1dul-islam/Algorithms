import matplotlib.pyplot as plt
import matplotlib.animation as animation

def find_smallest(arr, steps=None):
    smallest = arr[0]
    smallest_index = 0
    if steps is not None:
        steps.append((arr[:], smallest_index, -1)) #initial step
    for i in range(1, len(arr)):
        if steps is not None:
          steps.append((arr[:], smallest_index, i)) #each comparison step
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    if steps is not None:
        steps.append((arr[:], smallest_index, -2)) #final step
    return smallest_index

def selection_sort(arr):
    newArr = []
    steps = []
    temp_arr = arr[:] #create a copy to avoid changing the original array during visualization
    for _ in range(len(arr)):
        smallest = find_smallest(temp_arr, steps)
        newArr.append(temp_arr.pop(smallest))
        steps.append(("pop", newArr[:], temp_arr[:], smallest)) #store the pop step
    return newArr, steps

def visualize_sort(arr, steps):
    fig, ax = plt.subplots()
    ax.set_xlim(-1, len(arr))
    ax.set_ylim(0, max(arr) + 2)
    ax.set_title("Selection Sort")

    bars = ax.bar(range(len(arr)), arr, align='center', alpha=0.7)
    text = ax.text(0.5, max(arr) + 1, '', ha='center')

    def animate(i):
        step = steps[i]
        if isinstance(step[0], list): #find smallest step
            arr_state, smallest_index, current_index = step
            for bar, height in zip(bars, arr_state):
                bar.set_height(height)
                bar.set_color('lightblue')
            bars[smallest_index].set_color('green')
            if current_index >= 0:
                bars[current_index].set_color('red')
            if current_index == -2:
              text.set_text(f"Smallest index found: {smallest_index}")
            elif current_index == -1:
                text.set_text(f"Finding smallest...")
            else:
                text.set_text(f"Comparing {arr_state[current_index]} and {arr_state[smallest_index]}")

        else: # pop step
            _, new_arr_state, temp_arr_state, smallest_index = step
            new_arr_len = len(new_arr_state)
            temp_arr_len = len(temp_arr_state)
            combined_arr = new_arr_state + temp_arr_state
            for bar, height in zip(bars, combined_arr):
                bar.set_height(height)
                bar.set_color('lightblue')
            for bar in bars[:new_arr_len]:
                bar.set_color('green')
            text.set_text(f"Popped index: {smallest_index}, New Array: {new_arr_state}")
        return bars + (text,)

    ani = animation.FuncAnimation(fig, animate, frames=len(steps), interval=500, blit=True, repeat_delay=1000)
    plt.show()

def main():
    arr = [5, 3, 6, 2, 10]
    sorted_arr, steps = selection_sort(arr)
    print(sorted_arr)
    visualize_sort(arr, steps)

if __name__ == "__main__":
    main()