#include <string>
#include <unordered_set>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <limits>
#include <optional>

template <class A, class B>
struct std::hash<std::pair<A, B>>
{
    size_t operator()(const pair<A, B> &p) const
    {
        return ((hash<A>{}(p.first) << 1) | (hash<A>{}(p.first) >> (std::numeric_limits<size_t>::digits - 1))) ^ hash<B>{}(p.second);
    }
};

template <typename T, typename U>
std::pair<T, U> operator+(const std::pair<T, U> &l, const std::pair<T, U> &r)
{
    return {l.first + r.first, l.second + r.second};
}

using Vec = std::pair<int, int>;

const int SIZE = 70;
const int BYTES = 1024;
const Vec dirs[] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

std::vector<Vec> neighbors(std::unordered_set<Vec> corrupted, Vec n)
{
    std::vector<Vec> out;
    for (auto direction : dirs)
    {
        Vec next = n + direction;
        if (corrupted.find(next) == corrupted.end() && 0 <= next.first && next.first <= SIZE && 0 <= next.second && next.second <= SIZE)
        {
            out.push_back(next);
        }
    }
    return out;
}

std::optional<int> bfs(std::unordered_set<Vec> corrupted)
{
    std::queue<Vec> q;
    q.push({0, 0});
    std::unordered_map<Vec, int> dist = {{{0, 0}, 0}};
    while (!q.empty())
    {
        Vec current = q.front();
        q.pop();
        if (current == std::make_pair(SIZE, SIZE))
        {
            return dist[current];
        }
        for (Vec neighbor : neighbors(corrupted, current))
        {
            if (dist.find(neighbor) == dist.end())
            {
                dist[neighbor] = dist[current] + 1;
                q.push(neighbor);
            }
        }
    }
    return {};
}

int binary_search(std::vector<Vec> all_corrupted)
{
    int low = BYTES + 1;
    int high = all_corrupted.size() - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        std::unordered_set<Vec> corrupted(all_corrupted.begin(), all_corrupted.begin() + mid + 1);
        if (bfs(corrupted).has_value())
        {
            low = mid + 1;
        }
        else if (low != mid)
        {
            high = mid;
        }
        else
        {
            return mid;
        }
    }
    return -1;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<Vec> all_corrupted;
    while (std::getline(std::cin, line))
    {
        int com = line.find(",");
        all_corrupted.push_back({std::stoi(line.substr(0, com)), std::stoi(line.substr(com + 1))});
    }
    std::unordered_set<Vec> corrupted(all_corrupted.begin(), all_corrupted.begin() + BYTES);
    std::cout << bfs(corrupted).value() << "\n";
    int s = binary_search(all_corrupted);
    std::cout << all_corrupted[s].first << "," << all_corrupted[s].second << "\n";
}