## Stack based solution to the LeetCode question: Basic Calculator II
def calculate(self, s: str) -> int:
        
        total = 0
        
        ## divid s into nums and operations
        
        stack = []
        
        op ='+'
        
        i = 0
        while i < len(s):
            
            if s[i].isnumeric():
                num = s[i]
                j = i + 1
                while j < len(s) and s[j].isnumeric():
                    num += s[j]
                    j += 1

                i = j - 1
                
                if op == "+":
                    stack.append(int(num))
                elif op == "-":
                    stack.append(-int(num))
                elif op == "*":
                    stack.append(stack.pop() * int(num))
                elif op == "/":
                                        
                    stack.append(int(stack.pop() / int(num)))
                    
            
            elif s[i] in ["+", "-", "*", "/"]:
                op = s[i]

            i += 1
                
        return sum(stack)
