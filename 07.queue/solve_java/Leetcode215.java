import java.util.Collections;
import java.util.PriorityQueue;

public class Leetcode215 {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for(int n: nums) {
            maxHeap.add(n);
        }
        int answer = 0;
        for(int i = 0; i < k; i++) {
            answer = maxHeap.poll();
        }

        return answer;
    }

    public static void main(String[] args) {
        Leetcode215 app = new Leetcode215();
        int k = 2;
        int[] nums = {3,2,1,5,6,4};

        System.out.println(app.findKthLargest(nums, k));
    }
}
