package com.anna.datastructure;

import java.util.Iterator;

public class DoublyLinkedList<T> implements Iterable<T> {
    private int size = 0;
    private Node<T> head = null;
    private Node<T> tail = null;

    private class Node<T> {
        T data;
        Node<T> prev, next;

        public Node(T data, Node<T> prev, Node<T> next) {
            this.data = data;
            this.prev = prev;
            this.next = next;
        }

        @Override
        public String toString() {
            return data.toString();
        }
    }

    // empty this linked list
    public void clear() {
        Node<T> traverse = head;
        while (traverse != null) {
            Node<T> next = traverse.next;
            traverse.prev = traverse.next = null;
            traverse.data = null;
            traverse = next;
        }
        head = tail = null;
        size = 0;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    public void addFirst(T element) {
        if (isEmpty()) {
            head = tail = new Node<>(element, null, null);
        }
        else {
            head.prev = new Node<>(element, null, head);
            head = head.prev;
        }
        size++;
    }

    public void addLast(T element) {
        if (isEmpty()) {
            head = tail = new Node<>(element, null, null);
        }
        else {
            tail.next = new Node<>(element, tail, null);
            tail = tail.next;
        }
        size++;
    }

    public void add(T element) {
        addLast(element);
    }

    public T getFirst() {
        if (isEmpty())
            throw new RuntimeException("Empty list");
        return head.data;
    }

    public T getLast() {
        if (isEmpty())
            throw new RuntimeException("Empty list");
        return tail.data;
    }

    public T removeFirst() {
        if (isEmpty())
            throw new RuntimeException("Empty list");

        T removed = head.data;
        head = head.next;
        size--;

        if (isEmpty())
            tail = null;
        else
            head.prev = null;

        return removed;
    }

    public T removeLast() {
        if (isEmpty())
            throw new RuntimeException("Empty list");

        T removed = tail.data;
        tail = tail.prev;
        size--;

        if (isEmpty())
            head = null;
        else
            tail.next = null;

        return removed;
    }

    private T remove(Node<T> node) {
        if (node.prev == null)
            removeFirst();
        if (node.next == null)
            removeLast();

        T removed = node.data;

        node.prev.next = node.next;
        node.next.prev = node.prev;

        node.data = null;
        node.prev = node.next = null;
        size--;

        return removed;
    }

    public T removeAt(int index) {
        // index condition
        if (index < 0 || index >= size)
            throw new IllegalArgumentException();

        Node<T> traverse;

        if (index < size / 2) {
            // search from the front
            traverse = head;
            for (int i = 0; i != index; i++) {
                traverse = traverse.next;
            }
        }
        else {
            // search from the back
            traverse = tail;
            for (int i = size - 1; i != index; i--) {
                traverse = traverse.prev;
            }
        }

        return remove(traverse);
    }

    public boolean remove(Object obj) {
        boolean isRemoved = false;
        if (obj == null) {
            for (Node<T> traverse = head; traverse != null; traverse = traverse.next) {
                if (traverse.data == null) {
                    remove(traverse);
                    isRemoved = true;
                }
            }
        }
        else {
            for (Node<T> traverse = head; traverse != null; traverse = traverse.next) {
                if (obj.equals(traverse.data)) {
                    remove(traverse);
                    isRemoved = true;
                }
            }
        }
        return isRemoved;
    }

    public int indexOf(Object obj) {
        int index = 0;
        if (obj == null) {
            for (Node<T> traverse = head; traverse != null; traverse = traverse.next, index++) {
                if (traverse.data == null)
                    return index;
            }
        }
        else {
            for (Node<T> traverse = head; traverse != null; traverse = traverse.next, index++) {
                if (obj.equals(traverse.data))
                    return index;
            }
        }
        return -1;
    }

    public boolean contains(Object obj) {
        return indexOf(obj) != -1;
    }

    @Override
    public Iterator<T> iterator() {
        return new Iterator<T>() {
            private Node<T> traverse = head;

            @Override
            public boolean hasNext() {
                return traverse.next != null;
            }

            @Override
            public T next() {
                T data = traverse.data;
                traverse = traverse.next;
                return data;
            }
        };
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[ ");
        for (Node<T> traverse = head; traverse != null; traverse = traverse.next) {
            sb.append(traverse.data);
            if (traverse.next != null)
                sb.append(", ");
        }
        sb.append("]");
        return sb.toString();
    }
}
