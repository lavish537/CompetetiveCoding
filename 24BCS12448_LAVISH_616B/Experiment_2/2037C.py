t_input = input()
if t_input:
    t = int(t_input)
    for _ in range(t):
        n = int(input())
        
        if n < 5:
            print("-1")
            continue
            
        odds = []
        for i in range(1, n + 1, 2):
            if i != 5:
                odds.append(i)
        odds.append(5)
        
        evens = [4]
        for i in range(2, n + 1, 2):
            if i != 4:
                evens.append(i)
        
        result = odds + evens
        
        output = []
        for num in result:
            output.append(str(num))
        print(" ".join(output))