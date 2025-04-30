class Solution:
    def generate_permutations(self, arr):
        if len(arr) <= 1:
            return [arr]
        
        result = []
        for i in range(len(arr)):
            # Take current element
            current = arr[i]
            # Generate permutations of remaining elements
            remaining_elements = arr[:i] + arr[i+1:]
            remaining_permutations = self.generate_permutations(remaining_elements)
            
            # Add current element to each permutation of remaining elements
            for perm in remaining_permutations:
                result.append([current] + perm)
        
        return result
myVar = Solution()
arr = [1,2,3]
#myVar.generate_permutations(arr)
#perms = generate_permutations(arr)
print(f"Permutations of {[1,2,3]}: {myVar.generate_permutations(arr)}")

