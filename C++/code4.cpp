
// parse and product

#include <fplus/fplus.hpp>

int str_to_int(const std::string& str)
{
    int result;
    std::istringstream(str) >> result;
    return result;
}

int str_to_double(const std::string& str)
{
    double result;
    std::istringstream(str) >> result;
    return result;
}

int main()
{
    const std::string input = "1,2,3,4,5,3,6,7";
    const auto parts = fplus::split(',', false, input);
    
    const auto nums = fplus::transform(str_to_int, parts);
    const auto nums = fplus::transform(str_to_double, parts);

    const auto result = fplus::reduce(std::multiplies<int>(), 1, nums);
    const auto result = fplus::reduce(std::plus<double>(), 0, nums);

    std::cout << result << std::endl;
}

// clang++ -std=c++14 code4.cpp -o parse_and_product