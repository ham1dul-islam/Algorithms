import matplotlib.pyplot as plt
import matplotlib.animation as animation

def binary_search_visualized(list, item):
    low = 0
    high = len(list) - 1
    steps = []  # Store steps for visualization

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        steps.append((low, mid, high, guess)) # Store low, mid, high, and guess for each step

        if guess == item:
            return mid, steps
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None, steps

def visualize_search(list, item, steps):
    fig, ax = plt.subplots()
    ax.set_xlim(-1, len(list))
    ax.set_ylim(-1, 2)
    ax.set_yticks([])
    ax.set_title(f"Binary Search for {item}")

    rects = ax.bar(range(len(list)), [0] * len(list), align='center', alpha=0.5)
    text = ax.text(0.5, 1.5, '', ha='center')

    def animate(i):
        low, mid, high, guess = steps[i]
        for rect in rects:
            rect.set_height(0)
            rect.set_color('lightblue')
        for j in range(low, high + 1):
            rects[j].set_height(1)

        rects[mid].set_color('red')

        text.set_text(f"Low: {low}, Mid: {mid}, High: {high}, Guess: {guess}")
        return rects + (text,)

    ani = animation.FuncAnimation(fig, animate, frames=len(steps), interval=500, blit=True, repeat_delay=1000)
    plt.show()

def main():
    my_list = [1, 3, 5, 7, 9, 11, 13, 15]
    item_to_find = 15

    result, steps = binary_search_visualized(my_list, item_to_find)

    if result is not None:
        print(f"Found {item_to_find} at index {result}")
        visualize_search(my_list, item_to_find, steps)
    else:
        print(f"{item_to_find} not found.")
        visualize_search(my_list, item_to_find, steps) #still visualize, even if not found.

if __name__ == "__main__":
    main()