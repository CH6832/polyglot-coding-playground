#include <iostream>
#include <vector>
#include <memory>
#include <algorithm>

// Forward declaration of Subject class
class Subject;

// Observer interface
class Observer {
public:
    virtual void update(const Subject& subject) = 0;
    virtual ~Observer() {}
};

// Subject class
class Subject {
public:
    void attach(std::shared_ptr<Observer> observer) {
        observers.push_back(observer);
    }

    void detach(std::shared_ptr<Observer> observer) {
        observers.erase(std::remove(observers.begin(), observers.end(), observer), observers.end());
    }

    void notify() const {
        for (const auto& observer : observers) {
            observer->update(*this);
        }
    }

    virtual int getState() const = 0;
    virtual void setState(int state) = 0;

    virtual ~Subject() {}

private:
    std::vector<std::shared_ptr<Observer>> observers;
};

// Concrete subject class
class ConcreteSubject : public Subject {
public:
    int getState() const override {
        return state;
    }

    void setState(int state) override {
        this->state = state;
        notify();
    }

private:
    int state = 0;
};

// Concrete observer class
class ConcreteObserver : public Observer {
public:
    ConcreteObserver(std::string name) : name(name) {}

    void update(const Subject& subject) override {
        std::cout << name << " received update. New state: " << subject.getState() << std::endl;
    }

private:
    std::string name;
};

int main() {
    // Create a concrete subject
    std::shared_ptr<ConcreteSubject> subject = std::make_shared<ConcreteSubject>();

    // Create concrete observers
    std::shared_ptr<ConcreteObserver> observer1 = std::make_shared<ConcreteObserver>("Observer 1");
    std::shared_ptr<ConcreteObserver> observer2 = std::make_shared<ConcreteObserver>("Observer 2");

    // Attach observers to the subject
    subject->attach(observer1);
    subject->attach(observer2);

    // Set the state of the subject
    subject->setState(10);

    // Detach observer1
    subject->detach(observer1);

    // Set the state of the subject again
    subject->setState(20);

    return 0;
}
