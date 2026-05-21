class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1 = defaultdict(int)
        for i in range(len(s1)):
            set1[s1[i]]+=1

        set2 = defaultdict(int)
        l=0
        for r in range(len(s2)):
            set2[s2[r]] +=1
            if r >= len(s1):
                set2[s2[l]]-=1
                if set2[s2[l]] == 0:
                    del set2[s2[l]]
                l+=1
            print(set2)
            if set1 == set2:
                return True
        
        return False
                
            
