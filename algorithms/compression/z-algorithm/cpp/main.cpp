#include <iostream>
#include "ZAlgo.h"

int main() {
    std::string text = "abababab";
    std::string pattern = "aba";
    std::vector<int> occurrences = z_algorithm(pattern + "$" + text);

    std::cout << "Occurrences of pattern '" << pattern << "' in text '" << text << "': ";
    for (int index : occurrences) {
        std::cout << index << " ";
    }
    std::cout << std::endl;

    return 0;
}
