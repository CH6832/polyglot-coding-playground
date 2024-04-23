#include <iostream>

// Define the Node structure
struct Node {
    int data;
    Node* prev;
    Node* next;
    Node(int value) : data(value), prev(nullptr), next(nullptr) {}
};

int main() {
    // Create nodes
    Node* head = new Node(1);
    Node* second = new Node(2);
    Node* third = new Node(3);

    // Connect nodes
    head->next = second;
    second->prev = head;
    second->next = third;
    third->prev = second;

    // Traverse forward and print the linked list
    std::cout << "Linked List (forward): ";
    Node* current = head;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;

    // Traverse backward and print the linked list
    std::cout << "Linked List (backward): ";
    current = third;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = current->prev;
    }
    std::cout << std::endl;

    // Cleanup: delete the nodes
    current = head;
    while (current != nullptr) {
        Node* temp = current;
        current = current->next;
        delete temp;
    }

    return 0;
}
