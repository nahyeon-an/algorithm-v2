package com.anna.datastructure;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class DynamicArrayTest {
    DynamicArray<Integer> arr;

    @BeforeEach
    void setUp() {
        arr = new DynamicArray<>();
    }

    @Test
    @DisplayName("Test size() method")
    void testSize() {
        arr.add(1);
        arr.add(2);
        arr.add(3);
        assert arr.size() == 3;
    }

    @Test
    void testIsEmpty() {
        assert arr.isEmpty();
    }

    @Test
    void testGet() {
        arr.add(1);
        arr.add(2);
        arr.add(3);
        assert arr.get(0) == 1;
        assert arr.get(1) == 2;
        assert arr.get(2) == 3;
    }

    @Test
    void testSet() {
        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.set(0, 4);
        arr.set(1, 5);
        arr.set(2, 6);
        assert arr.get(0) == 4;
        assert arr.get(1) == 5;
        assert arr.get(2) == 6;
    }

    @Test
    void testClear() {
        arr.add(1);
        arr.add(2);
        arr.add(3);
        assert arr.size() == 3;
        arr.clear();
        assert arr.isEmpty();
    }

    @Test
    void testAdd() {
        arr.add(1);
        arr.add(2);
        arr.add(3);
        assert arr.get(0) == 1;
        assert arr.get(1) == 2;
        assert arr.get(2) == 3;
    }

    @Test
    void testRemoveAt() {
        arr.add(1);
        arr.add(2);
        arr.add(3);
        Integer removed = arr.removeAt(1);
        assert removed == 2;
        assert arr.get(0) == 1;
        assert arr.get(1) == 3;
    }

    @Test
    void testRemove() {
        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.remove(2);
        assert arr.get(0) == 1;
        assert arr.get(1) == 3;
    }

    @Test
    void testIndexOf() {
        arr.add(1);
        arr.add(2);
        arr.add(3);
        assert arr.indexOf(2) == 1;
    }

    @Test
    void testContains() {
        arr.add(1);
        arr.add(2);
        arr.add(3);
        assert arr.contains(2);
    }

    @Test
    void testIterator() {
        arr.add(1);
        arr.add(2);
        arr.add(3);
        int i = 0;
        for (Integer item : arr) {
            assert item == arr.get(i);
            i++;
        }
    }
}
