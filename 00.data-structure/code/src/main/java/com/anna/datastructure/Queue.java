package com.anna.datastructure;

import java.util.Iterator;
import java.util.LinkedList;

public class Queue<T> implements Iterable<T> {
    private LinkedList<T> list = new LinkedList<>();

    public Queue() {}

    public Queue(T element) {
        offer(element);
    }

    public int size() {
        return list.size();
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    public void offer(T element) {
        list.addLast(element);
    }

    public T peek() {
        if (isEmpty())
            throw new RuntimeException("Empty Queue");
        return list.peekFirst();
    }

    public T poll() {
        if (isEmpty())
            throw new RuntimeException("Empty Queue");
        return list.removeFirst();
    }

    @Override
    public Iterator<T> iterator() {
        return list.iterator();
    }
}
