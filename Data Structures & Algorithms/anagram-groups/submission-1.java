class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();
        for(String s: strs) {
                int[] count = new int[26];
                for(char c: s.toCharArray()) {
                    // count each character inside the string to see if it
                    // is inside the hash map, if it is then add to that key
                    // index of the map, otherwise make a new key with a new
                    // ArrayList and put the string in there
                    count[c - 'a']++;
                }
            // turn count array into a string, check if it is in the list,
            // if this is the case, then add the string at that key, otherwise
            // make a new Array with the new key and add the value 
            // (still a little confused why we need to do this)
            String key = Arrays.toString(count);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(s);
        }
        return new ArrayList<>(res.values());
    }

}
