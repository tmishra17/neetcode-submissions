class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return []
        return '|'.join(strs)
    
    def decode(self, s: str) -> List[str]:
        if type(s) != str:
            return []
        
        return s.split('|')
