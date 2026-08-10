class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freq_list = new List[nums.length + 1];
        for (int i = 0; i < freq_list.length; i++) {
            freq_list[i] = new ArrayList<>();
        }
        for (int n: nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq_list[entry.getValue()].add(entry.getKey());
        }

        int spaces = 0;
        for (int i = freq_list.length - 1; i >= 1 && spaces != k; i--) {
            for(int n: freq_list[i]) {
                res[spaces++] = n;
                if (spaces == k) {
                    return res;
                }
            }
        }
        return res;

    }
}
