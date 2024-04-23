#include <iostream>
#include <memory>

// Abstract Product
class Product {
public:
    virtual void operation() = 0;
    virtual ~Product() {}
};

// Concrete Products
class ConcreteProduct1 : public Product {
public:
    void operation() override {
        std::cout << "ConcreteProduct1 operation\n";
    }
};

class ConcreteProduct2 : public Product {
public:
    void operation() override {
        std::cout << "ConcreteProduct2 operation\n";
    }
};

// Abstract Creator
class Creator {
public:
    virtual std::unique_ptr<Product> factoryMethod() = 0;
    virtual ~Creator() {}
    
    // The creator may also contain some business logic
    void someOperation() {
        std::cout << "Some operation before creating the product\n";
    }
};

// Concrete Creators
class ConcreteCreator1 : public Creator {
public:
    std::unique_ptr<Product> factoryMethod() override {
        return std::make_unique<ConcreteProduct1>();
    }
};

class ConcreteCreator2 : public Creator {
public:
    std::unique_ptr<Product> factoryMethod() override {
        return std::make_unique<ConcreteProduct2>();
    }
};

int main() {
    // Client code
    std::unique_ptr<Creator> creator1 = std::make_unique<ConcreteCreator1>();
    std::unique_ptr<Product> product1 = creator1->factoryMethod();
    creator1->someOperation();
    product1->operation();

    std::unique_ptr<Creator> creator2 = std::make_unique<ConcreteCreator2>();
    std::unique_ptr<Product> product2 = creator2->factoryMethod();
    creator2->someOperation();
    product2->operation();

    return 0;
}
