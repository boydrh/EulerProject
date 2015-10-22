def main():
    Threes = [x for x in range(1000)[1::] if (x % 3) ==0]
    Fives = [x for x in range(1000)[1::] if (x % 5) ==0]
    Doubles = [x for x in range(1000)[1::] if (x % 15) ==0]
    
    sum = 0
    for item in Threes:
        sum += item
    
    for item in Fives:
        sum += item
    
    for item in Doubles:
        sum -= item
    
    return sum
    
if __name__ == "__main__":
    Problem1 = main()
