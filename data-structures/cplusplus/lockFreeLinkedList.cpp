#include <iostream>
#include <atomic>

template <typename T>
struct Node {
    T data;
    std::atomic<Node*> next;
    Node(T d) : data(d), next(nullptr) {}
};

template <typename T>
class LockFreeLinkedList {
private:
    std::atomic<Node<T>*> head;

public:
    LockFreeLinkedList() : head(nullptr) {}

    ~LockFreeLinkedList() {
        Node<T>* current = head.load();
        while (current) {
            Node<T>* temp = current;
            current = current->next.load();
            delete temp;
        }
    }

    void append(T data) {
        Node<T>* newNode = new Node<T>(data);
        Node<T>* current = head.load();
        Node<T>* prev = nullptr;

        while (true) {
            if (!current) {
                if (head.compare_exchange_weak(current, newNode)) {
                    return;
                }
            } else {
                while (current) {
                    prev = current;
                    current = current->next.load();
                }
                if (prev->next.compare_exchange_weak(current, newNode)) {
                    return;
                }
            }
        }
    }

    void display() {
        Node<T>* current = head.load();
        while (current) {
            std::cout << current->data << " ";
            current = current->next.load();
        }
        std::cout << std::endl;
    }
};

int main() {
    LockFreeLinkedList<int> list;

    // Append elements to the linked list
    list.append(1);
    list.append(2);
    list.append(3);
    list.append(4);
    list.append(5);

    // Display the linked list
    std::cout << "Linked List: ";
    list.display();

    return 0;
}
