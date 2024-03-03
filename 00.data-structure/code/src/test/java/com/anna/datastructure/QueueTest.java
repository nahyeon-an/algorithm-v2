package com.anna.datastructure;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class QueueTest {
    Queue<Integer> queue;

    @BeforeEach
    void setUp() {
        queue = new Queue<>();
    }

    @Test
    void testOffer() {
        queue.offer(1);
        queue.offer(2);
        queue.offer(3);
        assert queue.size() == 3;
    }

    @Test
    void testPoll() {
        queue.offer(1);
        queue.offer(2);
        queue.offer(3);
        assert queue.poll() == 1;
        assert queue.poll() == 2;
        assert queue.poll() == 3;
    }

    @Test
    void testPeek() {
        queue.offer(1);
        queue.offer(2);
        queue.offer(3);
        assert queue.peek() == 1;
        assert queue.peek() == 1;
    }
}
