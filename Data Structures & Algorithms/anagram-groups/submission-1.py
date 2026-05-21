class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #time: o(n*m), space: o(m)
        anagrams_map = defaultdict(list)
        for s in strs: 
            count = [0] * 26
            for char in s:
                count[ord(char)-ord('a')] += 1
            
            # transform count list to a tuple as the key, so that the string has the same count list will be stored under the same key
            anagrams_map[tuple(count)].append(s)
            
        return list(anagrams_map.values())
            
        

            
        
        

        


    
        