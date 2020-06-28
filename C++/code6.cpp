
#include <fplus/fplus.hpp>

typedef std::pair<float, float> point;

float point_distance(const point& p1, const point& p2)
{
    const float dx = p2.first - p1.first;
    const float dy = p2.second - p1.second;
    return std::sqrt(dx * dx + dy * dy);

}

int main()
{
    using namespace std;

    vector<point> polygon = { {1,2}, {7,3}, {6,5}, {,4,4}, {2,9} };
    // Find the longest edge of the polygon

    const auto edges = fplus::overlapping_pairs_cyclic(polygon);

    const auto result = fplus::maximum_on(point_distace, edges);

    cout << fplus::show(result) << endl;

    // lambda function maximum_on
    const auto result = fplus::maximum_on(
        [](const std::pair<point, point>& edge) -> float
        {
            return point_distance(edge.first, edge.second);
        }, edges);

    cout << fplus::show(result) << endl;
}