#include <iostream>
#include <memory>

// Component interface
class Pizza {
public:
    virtual std::string getDescription() const = 0;
    virtual double cost() const = 0;
    virtual ~Pizza() {}
};

// Concrete component
class PlainPizza : public Pizza {
public:
    std::string getDescription() const override {
        return "Plain pizza";
    }

    double cost() const override {
        return 5.0; // Base price of plain pizza
    }
};

// Decorator base class
class PizzaDecorator : public Pizza {
public:
    PizzaDecorator(std::shared_ptr<Pizza> pizza) : pizza(pizza) {}

    std::string getDescription() const override {
        return pizza->getDescription();
    }

    double cost() const override {
        return pizza->cost();
    }

protected:
    std::shared_ptr<Pizza> pizza;
};

// Concrete decorator class
class CheeseDecorator : public PizzaDecorator {
public:
    CheeseDecorator(std::shared_ptr<Pizza> pizza) : PizzaDecorator(pizza) {}

    std::string getDescription() const override {
        return pizza->getDescription() + ", with extra cheese";
    }

    double cost() const override {
        return pizza->cost() + 1.0; // Additional cost for extra cheese
    }
};

// Concrete decorator class
class PepperoniDecorator : public PizzaDecorator {
public:
    PepperoniDecorator(std::shared_ptr<Pizza> pizza) : PizzaDecorator(pizza) {}

    std::string getDescription() const override {
        return pizza->getDescription() + ", with pepperoni";
    }

    double cost() const override {
        return pizza->cost() + 2.0; // Additional cost for pepperoni
    }
};

int main() {
    // Create a plain pizza
    std::shared_ptr<Pizza> pizza = std::make_shared<PlainPizza>();
    std::cout << "Description: " << pizza->getDescription() << ", Cost: $" << pizza->cost() << std::endl;

    // Decorate the plain pizza with extra cheese
    pizza = std::make_shared<CheeseDecorator>(pizza);
    std::cout << "Description: " << pizza->getDescription() << ", Cost: $" << pizza->cost() << std::endl;

    // Decorate the pizza with pepperoni
    pizza = std::make_shared<PepperoniDecorator>(pizza);
    std::cout << "Description: " << pizza->getDescription() << ", Cost: $" << pizza->cost() << std::endl;

    return 0;
}
