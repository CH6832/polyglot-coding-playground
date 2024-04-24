#include <iostream>
#include <memory>

// Strategy interface
class Strategy {
public:
    virtual void execute() const = 0;
    virtual ~Strategy() {}
};

// Concrete strategy 1
class ConcreteStrategy1 : public Strategy {
public:
    void execute() const override {
        std::cout << "Executing strategy 1\n";
    }
};

// Concrete strategy 2
class ConcreteStrategy2 : public Strategy {
public:
    void execute() const override {
        std::cout << "Executing strategy 2\n";
    }
};

// Context class
class Context {
public:
    Context(std::shared_ptr<Strategy> strategy) : strategy(strategy) {}

    void setStrategy(std::shared_ptr<Strategy> strategy) {
        this->strategy = strategy;
    }

    void executeStrategy() const {
        strategy->execute();
    }

private:
    std::shared_ptr<Strategy> strategy;
};

int main() {
    // Create strategies
    std::shared_ptr<ConcreteStrategy1> strategy1 = std::make_shared<ConcreteStrategy1>();
    std::shared_ptr<ConcreteStrategy2> strategy2 = std::make_shared<ConcreteStrategy2>();

    // Create context with strategy 1
    Context context(strategy1);
    context.executeStrategy();

    // Change strategy to strategy 2 and execute again
    context.setStrategy(strategy2);
    context.executeStrategy();

    return 0;
}
