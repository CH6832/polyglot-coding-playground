#include <iostream>
#include <string>
#include <memory>

// Product class
class Pizza {
public:
    void setDough(const std::string& dough) {
        dough_ = dough;
    }

    void setSauce(const std::string& sauce) {
        sauce_ = sauce;
    }

    void setTopping(const std::string& topping) {
        topping_ = topping;
    }

    void showPizza() const {
        std::cout << "Pizza with dough: " << dough_
                  << ", sauce: " << sauce_
                  << " and topping: " << topping_ << std::endl;
    }

private:
    std::string dough_;
    std::string sauce_;
    std::string topping_;
};

// Abstract builder class
class PizzaBuilder {
public:
    virtual ~PizzaBuilder() {}
    virtual void buildDough() = 0;
    virtual void buildSauce() = 0;
    virtual void buildTopping() = 0;
    virtual std::unique_ptr<Pizza> getPizza() = 0;
};

// Concrete builder class
class HawaiianPizzaBuilder : public PizzaBuilder {
public:
    HawaiianPizzaBuilder() : pizza(std::make_unique<Pizza>()) {}

    void buildDough() override {
        pizza->setDough("cross");
    }

    void buildSauce() override {
        pizza->setSauce("mild");
    }

    void buildTopping() override {
        pizza->setTopping("ham and pineapple");
    }

    std::unique_ptr<Pizza> getPizza() override {
        return std::move(pizza);
    }

private:
    std::unique_ptr<Pizza> pizza;
};

// Director class
class Waiter {
public:
    void setPizzaBuilder(std::unique_ptr<PizzaBuilder> builder) {
        pizzaBuilder = std::move(builder);
    }

    std::unique_ptr<Pizza> getPizza() {
        return pizzaBuilder->getPizza();
    }

    void constructPizza() {
        pizzaBuilder->buildDough();
        pizzaBuilder->buildSauce();
        pizzaBuilder->buildTopping();
    }

private:
    std::unique_ptr<PizzaBuilder> pizzaBuilder;
};

int main() {
    Waiter waiter;

    // Creating Hawaiian pizza
    waiter.setPizzaBuilder(std::make_unique<HawaiianPizzaBuilder>());
    waiter.constructPizza();
    std::unique_ptr<Pizza> pizza = waiter.getPizza();
    pizza->showPizza();

    return 0;
}
