def sherlockAndAnagrams(s):
   
    ## start simple:
    keys = {}
    for size in range(1, len(s)):
        for i in range(len(s) - size + 1):
            sub = s[i:i+size] # create substring

            #create vector representation of the substring
            rep = [0]*26
            for char in sub:
                rep[ord(char) - ord("a")] += 1
                
            rep = tuple(rep)
            if rep in keys:
                keys[rep] += 1 
            else: 
                keys[rep] = 1
                
    return sum([value * (value - 1) // 2 for key,value in keys.items() if 
value > 1])
       
