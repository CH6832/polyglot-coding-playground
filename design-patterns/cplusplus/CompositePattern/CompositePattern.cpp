#include <iostream>
#include <memory>
#include <vector>

// Component interface
class Graphic {
public:
    virtual void draw() const = 0;
    virtual ~Graphic() {}
};

// Leaf class
class Ellipse : public Graphic {
public:
    void draw() const override {
        std::cout << "Ellipse\n";
    }
};

// Composite class
class CompositeGraphic : public Graphic {
public:
    void add(std::unique_ptr<Graphic> graphic) {
        graphics.push_back(std::move(graphic));
    }

    void draw() const override {
        for (const auto& graphic : graphics) {
            graphic->draw();
        }
    }

private:
    std::vector<std::unique_ptr<Graphic>> graphics;
};

int main() {
    // Create leaf objects
    std::unique_ptr<Graphic> ellipse1 = std::make_unique<Ellipse>();
    std::unique_ptr<Graphic> ellipse2 = std::make_unique<Ellipse>();
    std::unique_ptr<Graphic> ellipse3 = std::make_unique<Ellipse>();

    // Create a composite graphic object
    std::unique_ptr<CompositeGraphic> compositeGraphic = std::make_unique<CompositeGraphic>();

    // Add leaf objects to the composite graphic
    compositeGraphic->add(std::move(ellipse1));
    compositeGraphic->add(std::move(ellipse2));
    compositeGraphic->add(std::move(ellipse3));

    // Draw the composite graphic
    compositeGraphic->draw();

    return 0;
}
