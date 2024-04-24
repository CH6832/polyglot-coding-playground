#include <iostream>
#include <string>
#include <memory>
#include <vector>

// Command interface
class Command {
public:
    virtual ~Command() {}
    virtual void execute() = 0;
};

// Receiver class
class Light {
public:
    void turnOn() {
        std::cout << "Light is on\n";
    }

    void turnOff() {
        std::cout << "Light is off\n";
    }
};

// Concrete command to turn on the light
class TurnOnCommand : public Command {
public:
    TurnOnCommand(Light& light) : light(light) {}

    void execute() override {
        light.turnOn();
    }

private:
    Light& light;
};

// Concrete command to turn off the light
class TurnOffCommand : public Command {
public:
    TurnOffCommand(Light& light) : light(light) {}

    void execute() override {
        light.turnOff();
    }

private:
    Light& light;
};

// Invoker class
class RemoteControl {
public:
    void setCommand(std::shared_ptr<Command> command) {
        slot = command;
    }

    void pressButton() {
        if (slot) {
            slot->execute();
        } else {
            std::cout << "No command assigned\n";
        }
    }

private:
    std::shared_ptr<Command> slot;
};

int main() {
    // Receiver
    Light light;

    // Concrete commands
    std::shared_ptr<Command> turnOn = std::make_shared<TurnOnCommand>(light);
    std::shared_ptr<Command> turnOff = std::make_shared<TurnOffCommand>(light);

    // Invoker
    RemoteControl remote;

    // Assign and execute turn on command
    remote.setCommand(turnOn);
    std::cout << "Pressing the remote to turn on the light:\n";
    remote.pressButton();

    // Assign and execute turn off command
    remote.setCommand(turnOff);
    std::cout << "Pressing the remote to turn off the light:\n";
    remote.pressButton();

    return 0;
}
