#include <algorithm>
#include <map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        // if (s.size()!= t.size()) return false;
        // map<int> lettersOfs, lettersOft;
        // for(int i = 0; i < s.size(); i++) {
        //     if(lettersOfs.count(s[i]) == 0) {
        //         lettersOfs[s[i]] = 1; 
        //     } 
        //     else lettersOfs[s[i]]++;
        //     if(lettersOfs.count(t[i]) == 0) {
        //         lettersOfs[t[i]] = 1; 
        //     } 
        //     else lettersOfs[t[i]]++;
        // }
        // map<int>::iterator itS = lettersOfs.begin();
        // map<int>::iterator itT = lettersOft.begin();
        // while(itS != lettersOfs.begin()) {
        //     if (*itS != *itT) return false;
        //     itS++;
        //     itT++;
        // }
        // return true;
        //figure how to iterate through map
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
};
