#include <iostream>

// Abstract base class defining the template method
class AbstractClass {
public:
    // Template method
    void templateMethod() const {
        primitiveOperation1();
        primitiveOperation2();
    }

    virtual ~AbstractClass() {}

private:
    // Primitive operations to be implemented by subclasses
    virtual void primitiveOperation1() const = 0;
    virtual void primitiveOperation2() const = 0;
};

// Concrete subclass implementing the template method
class ConcreteClass : public AbstractClass {
private:
    void primitiveOperation1() const override {
        std::cout << "ConcreteClass: Primitive Operation 1\n";
    }

    void primitiveOperation2() const override {
        std::cout << "ConcreteClass: Primitive Operation 2\n";
    }
};

int main() {
    // Create a ConcreteClass object and call the template method
    ConcreteClass concreteObject;
    concreteObject.templateMethod();

    return 0;
}
