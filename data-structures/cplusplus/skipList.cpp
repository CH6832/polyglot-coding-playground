#include <iostream>
#include <limits>
#include <random>
#include <vector>

// Node structure for Skip List
template <typename T>
struct SkipListNode {
    T key;
    std::vector<SkipListNode*> forward; // Array to hold pointers to next nodes at different levels
    SkipListNode(T k, int level) : key(k), forward(level, nullptr) {}
};

// Skip List class
template <typename T>
class SkipList {
private:
    int maxLevel; // Maximum level of the Skip List
    int currentLevel; // Current level of the Skip List
    SkipListNode<T>* header; // Header node of the Skip List
    float probability; // Probability factor for node promotion

    // Random number generator for determining node levels
    std::random_device rd;
    std::mt19937 gen;
    std::uniform_real_distribution<float> dis;

    // Function to generate random level for a new node
    int randomLevel() {
        int level = 1;
        while (dis(gen) < probability && level < maxLevel)
            level++;
        return level;
    }

public:
    // Constructor
    SkipList(int maxL, float p) : maxLevel(maxL), currentLevel(1), probability(p), gen(rd()), dis(0.0, 1.0) {
        header = new SkipListNode<T>(std::numeric_limits<T>::min(), maxLevel);
    }

    // Destructor
    ~SkipList() {
        SkipListNode<T>* current = header;
        while (current) {
            SkipListNode<T>* temp = current;
            current = current->forward[0];
            delete temp;
        }
    }

    // Function to insert a key into the Skip List
    void insert(T key) {
        SkipListNode<T>* current = header;
        std::vector<SkipListNode<T>*> update(maxLevel, nullptr);

        // Traverse the Skip List to find the insertion position
        for (int i = currentLevel - 1; i >= 0; i--) {
            while (current->forward[i] && current->forward[i]->key < key)
                current = current->forward[i];
            update[i] = current;
        }

        // Generate random level for the new node
        int newLevel = randomLevel();

        // If new level is greater than current level, update the update vector
        if (newLevel > currentLevel) {
            for (int i = currentLevel; i < newLevel; i++)
                update[i] = header;
            currentLevel = newLevel;
        }

        // Create new node and update pointers
        SkipListNode<T>* newNode = new SkipListNode<T>(key, newLevel);
        for (int i = 0; i < newLevel; i++) {
            newNode->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = newNode;
        }
    }

    // Function to search for a key in the Skip List
    bool search(T key) {
        SkipListNode<T>* current = header;
        for (int i = currentLevel - 1; i >= 0; i--) {
            while (current->forward[i] && current->forward[i]->key < key)
                current = current->forward[i];
        }
        current = current->forward[0];
        return current && current->key == key;
    }

    // Function to display the Skip List
    void display() {
        std::cout << "Skip List:" << std::endl;
        for (int i = currentLevel - 1; i >= 0; i--) {
            SkipListNode<T>* current = header->forward[i];
            std::cout << "Level " << i << ": ";
            while (current) {
                std::cout << current->key << " ";
                current = current->forward[i];
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    // Create a Skip List with maximum level 4 and probability 0.5
    SkipList<int> skipList(4, 0.5);

    // Insert some keys into the Skip List
    skipList.insert(3);
    skipList.insert(6);
    skipList.insert(7);
    skipList.insert(9);
    skipList.insert(12);
    skipList.insert(19);
    skipList.insert(17);
    skipList.insert(26);
    skipList.insert(21);
    skipList.insert(25);
    skipList.insert(5);

    // Display the Skip List
    skipList.display();

    // Search for a key in the Skip List
    int keyToSearch = 17;
    if (skipList.search(keyToSearch))
        std::cout << "Key " << keyToSearch << " found in the Skip List." << std::endl;
    else
        std::cout << "Key " << keyToSearch << " not found in the Skip List." << std::endl;

    return 0;
}
