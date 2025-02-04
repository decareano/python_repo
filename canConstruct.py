class Solution:
    
    def canConstruct(ransomNote, magazine):
        magazi_hash = {}
        for c in magazine:
            
            magazi_hash[c] = 1 + magazi_hash.get(c, 0)
            #maga_hash[c] = 1 + maga_hash.get(c, 0)
            print(magazi_hash)
            #compare c with every letter in ransomNote. if 
            #they match: bingo return True else False
        for c in ransomNote:
            if c not in magazi_hash or magazi_hash[c] <= 0:
                return False
            magazi_hash[c] -= 1
        return True
                
                    
                    
myVar = Solution
myVar.canConstruct(ransomNote="abcde", magazine="aabbcde")
