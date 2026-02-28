from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map ={}
        t_map={}
        for char in s:
            s_map[char] = s_map.get(char,0)+1

        for char in t:
            t_map[char] = t_map.get(char,0)+1

        for char in s_map:
            if s_map[char] != t_map.get(char,0):
                return False
        return True


        
        
# easier since i studied hashmaps before but after watching the sol i found we can do it with just one hmap and just compare .. the tc stays same though 
