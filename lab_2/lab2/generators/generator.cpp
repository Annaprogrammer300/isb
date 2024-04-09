#include <iostream>
#include <chrono>
#include <random>

/*!
\brief Generates a random binary sequence and prints it to the console.
*/
void generateRandomSequence(int count) {
    std::random_device rd;
    std::mt19937::result_type seed = rd() ^ (
        (std::mt19937::result_type)
        std::chrono::duration_cast<std::chrono::seconds>(
            std::chrono::system_clock::now().time_since_epoch()
        ).count() +
        (std::mt19937::result_type)
        std::chrono::duration_cast<std::chrono::microseconds>(
            std::chrono::high_resolution_clock::now().time_since_epoch()
        ).count());

    std::mt19937 gen(seed);

    for (int j = 0; j < count; ++j)
    {
        std::mt19937::result_type n;
        // Generate random number 0 or 1
        n = gen() % 2;

        std::cout << n;
    }
}

/*!
\brief The main function that generates a random binary sequence.
\return The exit status of the program
*/
int main()
{
    const int BITS = 128;
    generateRandomSequence(BITS);

    return 0;
}