class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        sta = []
        for int in asteroids:
            if not sta or int > 0:
                sta.append(int)
            else:
                while True:
                    stTop = sta[-1]
                    if stTop < 0:
                        sta.append(int)

                        break
                    # very tricky part below....not at my level
                    # advanced level to run a -negative of the
                    # int so it matches the top of the stack
                    # very very tricky and i try to solve it
                    # regularly
                    elif sta[-1] == -int:
                        sta.pop()

                        break
                    elif sta[-1] > -int:
                        break
                    else:
                        sta.pop()
                    # if not stack...as if: not in the stack
                    if not sta:
                        sta.append(int)
                        break
        return sta


myVar = Solution()     
myVar.asteroidCollision([6,5,-5])
