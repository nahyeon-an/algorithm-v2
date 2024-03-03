package com.anna.datastructure;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class DoublyLinkedListTest {
    DoublyLinkedList<Integer> ddl;
    private final int initSize = 10;

    void initList() {
        for (int i = 1; i <= initSize; i++)
            ddl.add(i);
    }

    @BeforeEach
    void setUp() {
        ddl = new DoublyLinkedList<>();
        initList();
    }

    @AfterEach
    void tearDown() {
        ddl.clear();
    }

    @Test
    void testSize() {
        assert ddl.size() == initSize;
    }

    @Test
    void testIsEmpty() {
        assert !ddl.isEmpty();
    }

    @Test
    void testAddFirst() {
        ddl.addFirst(0);
        assert ddl.size() == initSize + 1;
        assert ddl.getFirst() == 0;
    }

    @Test
    void testAddLast() {
        ddl.addLast(11);
        assert ddl.size() == initSize + 1;
        assert ddl.getLast() == 11;
    }

    @Test
    void testRemoveFirst() {
        ddl.removeFirst();
        assert ddl.size() == initSize - 1;
        assert ddl.getFirst() == 2;
    }

    @Test
    void testRemoveLast() {
        ddl.removeLast();
        assert ddl.size() == initSize - 1;
        assert ddl.getLast() == 9;
    }

    @Test
    void testRemoveAt() {
        int removed = ddl.removeAt(5);
        assert ddl.size() == initSize - 1;
        assert removed == 6;
    }

    @Test
    void testRemove() {
        assert ddl.remove(3);
    }

    @Test
    void testIndexOf() {
        assert ddl.indexOf(5) == 4;
    }

    @Test
    void testContains() {
        assert ddl.contains(7);
    }

    @Test
    void testIterator() {
        for (Integer i : ddl)
            System.out.println(i);
    }
}
