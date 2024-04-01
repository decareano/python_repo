def compressString(self, chars):
           
           ansNewArr = 0
           i = 0
           while i < len(chars):
                ctConseChars = 0
                letter = chars[i]
               
                while i < len(chars) and chars[i] == letter:
                    
                    ctConseChars += 1
                    i += 1
                    
               #letter a is assigned to ansNewArr
                chars[ansNewArr] = letter
                ansNewArr += 1
               
                   
                if ctConseChars > 1:
                #     chars[ansNewArr] = ctConseChars
                # else: 
                #     print("1")
                
                    for c in str(ctConseChars):
                        chars[ansNewArr] = c
                        ansNewArr += 1
                    #ctConseChars = 0
               
               #a = str(5)      
           return ansNewArr
