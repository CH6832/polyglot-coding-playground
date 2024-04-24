#include <iostream>
#include <memory>

// Abstract Product A
class AbstractProductA {
public:
    virtual void operationA() = 0;
    virtual ~AbstractProductA() {}
};

// Concrete Product A1
class ConcreteProductA1 : public AbstractProductA {
public:
    void operationA() override {
        std::cout << "ConcreteProductA1 operation\n";
    }
};

// Concrete Product A2
class ConcreteProductA2 : public AbstractProductA {
public:
    void operationA() override {
        std::cout << "ConcreteProductA2 operation\n";
    }
};

// Abstract Product B
class AbstractProductB {
public:
    virtual void operationB() = 0;
    virtual ~AbstractProductB() {}
};

// Concrete Product B1
class ConcreteProductB1 : public AbstractProductB {
public:
    void operationB() override {
        std::cout << "ConcreteProductB1 operation\n";
    }
};

// Concrete Product B2
class ConcreteProductB2 : public AbstractProductB {
public:
    void operationB() override {
        std::cout << "ConcreteProductB2 operation\n";
    }
};

// Abstract Factory
class AbstractFactory {
public:
    virtual std::unique_ptr<AbstractProductA> createProductA() = 0;
    virtual std::unique_ptr<AbstractProductB> createProductB() = 0;
    virtual ~AbstractFactory() {}
};

// Concrete Factory 1
class ConcreteFactory1 : public AbstractFactory {
public:
    std::unique_ptr<AbstractProductA> createProductA() override {
        return std::make_unique<ConcreteProductA1>();
    }

    std::unique_ptr<AbstractProductB> createProductB() override {
        return std::make_unique<ConcreteProductB1>();
    }
};

// Concrete Factory 2
class ConcreteFactory2 : public AbstractFactory {
public:
    std::unique_ptr<AbstractProductA> createProductA() override {
        return std::make_unique<ConcreteProductA2>();
    }

    std::unique_ptr<AbstractProductB> createProductB() override {
        return std::make_unique<ConcreteProductB2>();
    }
};

int main() {
    // Client code
    std::unique_ptr<AbstractFactory> factory1 = std::make_unique<ConcreteFactory1>();
    std::unique_ptr<AbstractProductA> productA1 = factory1->createProductA();
    std::unique_ptr<AbstractProductB> productB1 = factory1->createProductB();
    productA1->operationA();
    productB1->operationB();

    std::unique_ptr<AbstractFactory> factory2 = std::make_unique<ConcreteFactory2>();
    std::unique_ptr<AbstractProductA> productA2 = factory2->createProductA();
    std::unique_ptr<AbstractProductB> productB2 = factory2->createProductB();
    productA2->operationA();
    productB2->operationB();

    return 0;
}
