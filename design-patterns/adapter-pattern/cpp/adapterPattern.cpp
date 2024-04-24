#include <iostream>
#include <memory>
#include <vector>

// Adaptee interface
class OldInterface {
public:
    virtual void legacyMethod() const = 0;
    virtual ~OldInterface() {}
};

// Adaptee
class LegacyClass : public OldInterface {
public:
    void legacyMethod() const override {
        std::cout << "LegacyClass::legacyMethod() called\n";
    }
};

// Target interface
class NewInterface {
public:
    virtual void newMethod() const = 0;
    virtual ~NewInterface() {}
};

// Adapter
class Adapter : public NewInterface {
private:
    std::unique_ptr<OldInterface> adaptee;

public:
    Adapter(std::unique_ptr<OldInterface> adaptee) : adaptee(std::move(adaptee)) {}

    void newMethod() const override {
        adaptee->legacyMethod();
    }
};

// Client code
int main() {
    // Create the legacy object
    std::unique_ptr<OldInterface> legacyObject = std::make_unique<LegacyClass>();

    // Create the adapter with the legacy object
    std::unique_ptr<NewInterface> adapter = std::make_unique<Adapter>(std::move(legacyObject));

    // Use the adapter to call the new method
    adapter->newMethod();

    return 0;
}
