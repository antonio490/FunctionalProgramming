
// Lambdas

#include <fplus/fplus.hpp>
#include <iostream>

std::vector<int> xs = {0,1,2,3,4};
const auto ys = fplus::keep_if([](int x) -> bool
    {
        return x % 2 == 0;
    }, xs);

// [capture list] (parameters) > return type
// {
//    body
// }

int main()
{
    int val = 42;
    const auto add_value = [&val](int x) -> int 
    {
        return x + val;
    };

    std::cout << add_value(10) << std::endl;
    val = 23;
    std::cout << add_value(10) << std::endl;
}