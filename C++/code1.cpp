
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

typedef vector<int> Ints;
int square(int x)
{
    return x * x;
}

Ints range_based_for(const Ints& xs)
{
    Ints ys;
    ys.reserve(xs.size());
    for (int x : xs){
        ys.push_back(square(x));
    }
    return ys;
}

Ints sqr_std_transform(const Ints& xs)
{
    Ints ys;
    ys.reserve(xs.size());
    transform(begin(xs), end(xs), back_inserter(ys), square);
    return ys;
}

template <typename F, typename T>
vector<T> transform_vec(F f, const vector<T>& xs)
{
    vector<T> ys;
    ys.reserve(xs.size());
    transform(begin(xs), end(xs), back_inserter(ys), f);
    return ys;
}

Ints sqr_transform_vec(const Ints& xs)
{
    return transform_vec(square, xs);
}

int main()
{
    Ints xs(8192);
    sqr_transform_vec(xs);

}

// clan++ -03 -std=c++14 code1.cpp -o square