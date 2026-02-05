t_input = input()
if t_input:
    t = int(t_input)
    for _ in range(t):
        n = int(input())
        s = list(input())
        
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        max_char = ""
        max_val = -1
        for char in counts:
            if counts[char] > max_val:
                max_val = counts[char]
                max_char = char
        
        min_char = ""
        min_val = n + 1
        for char in counts:
            if counts[char] < min_val:
                min_val = counts[char]
                min_char = char
            elif counts[char] == min_val and char != max_char:
                min_char = char

        for i in range(n):
            if s[i] == min_char:
                s[i] = max_char
                break
        
        print("".join(s))