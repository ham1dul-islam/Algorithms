def factorial(x):
    if x ==1:
        return 1
    else:
        return x* factorial(x-1)
    
def main():
    print(factorial(3))  # 6   
    print(factorial(5))  # 120
    
if __name__ == "__main__":
    main()