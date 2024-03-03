package com.anna.datastructure;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class StackTest {
    Stack<Integer> stack;

    @BeforeEach
    void setUp() {
        stack = new Stack<>();
    }

    @Test
    void testPush() {
        stack.push(1);
        stack.push(2);
        stack.push(3);
        assert stack.size() == 3;
    }

    @Test
    void testPop() {
        stack.push(1);
        stack.push(2);
        stack.push(3);
        assert stack.pop() == 3;
        assert stack.pop() == 2;
        assert stack.pop() == 1;
    }

    @Test
    void testPeek() {
        stack.push(1);
        stack.push(2);
        stack.push(3);
        assert stack.peek() == 3;
        assert stack.peek() == 3;
    }
}
