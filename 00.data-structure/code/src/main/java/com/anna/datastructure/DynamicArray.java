package com.anna.datastructure;

import java.util.Iterator;

public class DynamicArray<T> implements Iterable<T> {
    private T[] arr;  // internal stack array
    private int length = 0;
    private int capacity = 0;  // actual array size

    public DynamicArray() {
        this(16);
    }

    public DynamicArray(int capacity) {
        if (capacity < 0)
            throw new IllegalArgumentException("Illegal Capacity: " + capacity);
        this.capacity = capacity;
        arr = (T[]) new Object[capacity];
    }

    public int size() {
        return length;
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    public T get(int index) {
        return arr[index];
    }

    public void set(int index, T element) {
        arr[index] = element;
    }

    public void clear() {
        for (int i = 0; i < capacity; i++) {
            arr[i] = null;
        }
        length = 0;
    }

    public void add(T element) {
        // resize internal array
        if (length + 1 >= capacity) {
            if (capacity == 0)
                capacity = 1;
            else
                capacity *= 2;

            T[] new_arr = (T[]) new Object[capacity];
            for (int i = 0; i < length; i++) {
                new_arr[i] = arr[i];
            }
            arr = new_arr;
        }
        // add element
        arr[length++] = element;
    }

    public T removeAt(int index) {
        if (index >= length || index < 0)
            throw new IndexOutOfBoundsException();

        T removed = arr[index];

        T[] new_arr = (T[]) new Object[length - 1];
        for (int i = 0, j = 0; i < length; i++, j++) {
            if (i == index)
                j--;
            else
                new_arr[j] = arr[i];
        }
        arr = new_arr;
        capacity = --length;

        return removed;
    }

    public boolean remove(Object obj) {
        for (int i = 0; i < length; i++) {
            if (arr[i].equals(obj)) {
                removeAt(i);
                return true;
            }
        }
        return false;
    }

    public int indexOf(Object obj) {
        for (int i = 0; i < length; i++) {
            if (arr[i].equals(obj)) {
                return i;
            }
        }
        return -1;
    }

    public boolean contains(Object obj) {
        return indexOf(obj) != -1;
    }

    @Override
    public Iterator<T> iterator() {
        return new Iterator<T> () {
            int index = 0;

            @Override
            public boolean hasNext() {
                return index < length;
            }

            @Override
            public T next() {
                return arr[index++];
            }
        };
    }

    public String toString() {
        if (length == 0)
            return "[]";

        StringBuilder sb = new StringBuilder(length).append("[");
        for (int i = 0; i < length-1; i++) {
            sb.append(arr[i] + ", ");
        }
        return sb.append(arr[length-1] + "]").toString();
    }
}
