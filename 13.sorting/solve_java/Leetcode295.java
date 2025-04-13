import java.util.Collections;
import java.util.PriorityQueue;

public class Leetcode295 {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    public Leetcode295() {

    }

    public void addNum(int num) {
        // 둘 다 비어있는 경우 max 에 넣으면서 시작
        if (minHeap.isEmpty() && maxHeap.isEmpty()) {
            maxHeap.add(num);
            return;
        }

        if (minHeap.size() == maxHeap.size()) {
            if (num > minHeap.peek()) {
                // minHeap peek 을 maxHeap 으로 이동
                maxHeap.add(minHeap.poll());
                minHeap.add(num);
            } else {
                maxHeap.add(num);
            }
        } else {
            if (num <= maxHeap.peek()) {
                minHeap.add(maxHeap.poll());
                maxHeap.add(num);
            } else {
                minHeap.add(num);
            }
        }
    }

    public double findMedian() {
        if (minHeap.size() == maxHeap.size()) {
            return (double) (minHeap.peek() + maxHeap.peek()) / 2;
        } else {
            return (double) maxHeap.peek();
        }
    }

    public static void main(String[] args) {
        /**
         * Find median
         * 배열의 길이가 홀수이면 -> 가운뎃값
         * 배열의 길이가 짝수이면 -> 가운데 2개 값의 평균값
         * 배열 길의 <= 5 * 10^4
         *
         * try1. linked list + binary search -> insert 수행 시 최악의 경우 O(n^2)
         */
        Leetcode295 app = new Leetcode295();
        app.addNum(1);
        System.out.println(app.findMedian());
        app.addNum(2);
        System.out.println(app.findMedian()); // 1.5
        app.addNum(3);
        System.out.println(app.findMedian()); // 2.0
        app.addNum(1);
        System.out.println(app.findMedian()); // 1.5
        app.addNum(5);
        System.out.println(app.findMedian()); // 2.0
    }
}
