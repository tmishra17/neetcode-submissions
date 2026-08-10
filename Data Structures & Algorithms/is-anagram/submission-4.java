
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        HashMap<Character, Integer> count_s = new HashMap<>();
        HashMap<Character, Integer> count_t = new HashMap<>();

        for(int i = 0; i < s.length(); i++) {
            // both of the statements below are the same
            // I am just using put and get because I understand 
            // it better
            // get the characters at index i for each string and
            // add them to the map first if they are not already there
            // or add 1 to its current count
            char sc = s.charAt(i);
            char tc = t.charAt(i);

            count_s.put(sc, count_s.getOrDefault(sc, 0) + 1);
            count_t.put(tc, count_t.getOrDefault(tc, 0) + 1);
        }
    
    return count_s.equals(count_t);
    // TC = O(s)
    // SC = O(s + t)
    }
}
