#include <iostream>
#include <string>
#include <memory>

// Subject interface
class Subject {
public:
    virtual void request() const = 0;
    virtual ~Subject() {}
};

// RealSubject class
class RealSubject : public Subject {
public:
    void request() const override {
        std::cout << "RealSubject: Handling request\n";
    }
};

// Proxy class
class Proxy : public Subject {
public:
    Proxy(std::shared_ptr<RealSubject> realSubject) : realSubject(realSubject) {}

    void request() const override {
        if (checkAccess()) {
            realSubject->request();
            logAccess();
        } else {
            std::cout << "Proxy: Access denied\n";
        }
    }

private:
    std::shared_ptr<RealSubject> realSubject;

    bool checkAccess() const {
        // Check access rights here (dummy implementation)
        return true;
    }

    void logAccess() const {
        std::cout << "Proxy: Logging the request\n";
    }
};

int main() {
    // Create a RealSubject object
    std::shared_ptr<RealSubject> realSubject = std::make_shared<RealSubject>();

    // Create a Proxy object
    std::shared_ptr<Proxy> proxy = std::make_shared<Proxy>(realSubject);

    // Perform request through the proxy
    proxy->request();

    return 0;
}
