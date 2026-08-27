class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        [1,2]
        2 + 1
        [3,3]
        3 * 3
        [9,4]
        9 - 4 = 5
        '''
        s = []
        for t in tokens:
            if t.lstrip("+-").isdigit():
                s.append(int(t))
            else:
                print('Before doing calc: ', s)
                val = s.pop()
                init = s.pop()
                if t == '+':
                    calc = init + val

                elif t == '-':
                    calc = init - val
                elif t == '*':
                    calc = init * val
                else:
                    calc = int(init / val)
                
                s.append(calc)
            print('after ifs: ', s)



        return s[0]

