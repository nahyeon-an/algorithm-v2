#include <vector>

template <typename T>
class DynamicArray {
    // todo : pointer 를 이용한 dynamic allocation 
  T *const arr;
  int length = 0;
  int capacity = 0;

 public:
  DynamicArray();
  DynamicArray(int);
  void init(int) {}
  int size() { return length; }
  bool isEmpty() { return size() == 0; }
  T get(int);
  void set(int, T);
  void clear();
  void add(T);
  int removeAt(T);
  bool remove(T);
  int indexOf(T);
  bool contains(T);
};

template <typename T>
DynamicArray<T>::DynamicArray(int c) {
    init(c);
}

template <typename T>
DynamicArray<T>::DynamicArray() {
    init(16);
}

template <typename T>
void DynamicArray<T>::init(int capacity) {
    if (capacity < 0) {
        exit(1);
    }

    this->capacity = capacity;
    this->arr = {};
}

template <typename T>
T DynamicArray<T>::get(int index) {
    return this->arr[index];
}

template <typename T>
void DynamicArray<T>::set(int index, T element) {
    this->arr[index] = element;
}

template <typename T>
void DynamicArray<T>::clear () {
    int i;
    for (i = 0; i < this->capacity; i++) {
        this->arr[i] = NULL;
    }
    this->length = 0;
}

int main() {
    DynamicArray<int> array = DynamicArray<int>();

    std::printf("Array isEmpty ? %d\n", array.isEmpty());
    array.set(0, 3);
    array.set(1, 2);

    std::printf("Array size ? %d\n", array.size());

    std::printf("Array[0]? %d, Array[1]? %d\n", array.get(0), array.get(1));


    return 0;
}
