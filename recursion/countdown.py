def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)


def main():
    countdown(5)
    
if __name__ == "__main__":
    main()