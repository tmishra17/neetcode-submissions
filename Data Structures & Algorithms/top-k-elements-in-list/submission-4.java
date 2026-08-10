class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        Map<Integer, Integer> count = new HashMap<>();
        for (int n: nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(count.entrySet());
        entries.sort((a, b) -> b.getValue() - a.getValue());
        // System.out.println(entries);
        for(int i = 0; i < k; i++) {
            res[i] = entries.get(i).getKey();
        }
        return res;

    }
}
