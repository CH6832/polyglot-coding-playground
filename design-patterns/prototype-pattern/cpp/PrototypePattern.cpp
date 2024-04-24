#include <iostream>
#include <unordered_map>
#include <memory>

// Abstract base class for prototypes
class Prototype {
public:
    virtual ~Prototype() {}
    virtual std::unique_ptr<Prototype> clone() const = 0;
    virtual void printInfo() const = 0;
};

// Concrete prototype class
class ConcretePrototype : public Prototype {
public:
    ConcretePrototype(int id) : id(id) {}

    std::unique_ptr<Prototype> clone() const override {
        return std::make_unique<ConcretePrototype>(*this);
    }

    void printInfo() const override {
        std::cout << "ConcretePrototype with ID: " << id << std::endl;
    }

private:
    int id;
};

// Prototype factory class
class PrototypeFactory {
public:
    static std::unique_ptr<Prototype> createPrototype(int id) {
        if (prototypes.find(id) != prototypes.end()) {
            return prototypes[id]->clone();
        }
        return nullptr;
    }

    static void registerPrototype(int id, std::unique_ptr<Prototype> prototype) {
        prototypes[id] = std::move(prototype);
    }

private:
    static std::unordered_map<int, std::unique_ptr<Prototype>> prototypes;
};

std::unordered_map<int, std::unique_ptr<Prototype>> PrototypeFactory::prototypes;

int main() {
    // Register prototypes
    PrototypeFactory::registerPrototype(1, std::make_unique<ConcretePrototype>(1));
    PrototypeFactory::registerPrototype(2, std::make_unique<ConcretePrototype>(2));

    // Clone prototypes
    std::unique_ptr<Prototype> prototype1 = PrototypeFactory::createPrototype(1);
    if (prototype1) {
        prototype1->printInfo();
    } else {
        std::cout << "Prototype with ID 1 not found\n";
    }

    std::unique_ptr<Prototype> prototype2 = PrototypeFactory::createPrototype(2);
    if (prototype2) {
        prototype2->printInfo();
    } else {
        std::cout << "Prototype with ID 2 not found\n";
    }

    return 0;
}
