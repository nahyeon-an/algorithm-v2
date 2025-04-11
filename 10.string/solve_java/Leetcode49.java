import java.util.*;

public class Leetcode49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for(String word: strs) {
            // word 의 문자들을 정렬 (ex. eat -> aet, tea -> aet, ...)
            char[] chars = word.toCharArray();
            Arrays.sort(chars);

            // 이것을 키로 그루핑
            String key = new String(chars);
            if (!groups.containsKey(key)) {
                List<String> values = new LinkedList<>();
                values.add(word);
                groups.put(key, values);
            } else {
                List<String> values = groups.get(key);
                values.add(word);
            }
        }

        return groups.values().stream().toList();
    }

    public static void main(String[] args) {
        /**
         * group anagrams
         * what is anagrams? 각 문자의 순서를 변경해서 만들수 있는 단어들
         * ex) eat, tea, ate
         *
         * 1 <= strs.length <= 10^4
         * 0 <= strs[0].length <= 100
         * O(n log n)
         */
        Leetcode49 app = new Leetcode49();

        String[] strs = {"eat","tea","tan","ate","nat","bat"};
        System.out.println(app.groupAnagrams(strs));
    }
}
