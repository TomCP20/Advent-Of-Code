#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <queue>
#include <limits>

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

const Vec dirs[] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
std::vector<Vec> get_neighbors(std::vector<std::string> &maze, Vec n, int w, int h)
{
    std::vector<Vec> neighbors;
    for (Vec direction : dirs)
    {
        Vec next = n + direction;
        if (0 <= next.first && next.first < w && 0 <= next.second && next.second < h && maze[next.second][next.first] != '#')
        {
            neighbors.push_back(next);
        }
    }
    return neighbors;
}

std::unordered_map<Vec, int> bfs(Vec end, std::vector<std::string> &maze, int w, int h)
{
    std::queue<Vec> q;
    q.push(end);
    std::unordered_map<Vec, int> dist = {{end, 0}};
    while (!q.empty())
    {
        Vec current = q.front();
        q.pop();
        for (Vec neighbor : get_neighbors(maze, current, w, h))
        {
            if (dist.find(neighbor) == dist.end())
            {
                dist[neighbor] = dist[current] + 1;
                q.push(neighbor);
            }
        }
    }
    return dist;
}

int manhattan(Vec a, Vec b)
{
    return abs(a.first - b.first) + abs(a.second - b.second);
}

const int MIN_SAVE = 100;
bool saves(int cheat_len, std::unordered_map<Vec, int> &dist, Vec a, Vec b)
{
    if (dist[a] < dist[b])
    {
        Vec tmp = a;
        a = b;
        b = tmp;
    }
    if (dist[a] - dist[b] >= MIN_SAVE)
    {
        int m = manhattan(a, b);
        if (m <= cheat_len)
        {
            if (dist[a] - dist[b] - m >= MIN_SAVE)
            {
                return true;
            }
        }
    }
    return false;
}

int solve(int cheat_len, std::unordered_map<Vec, int> &dist)
{
    std::vector<Vec> positions;
    for (auto kp : dist)
    {
        positions.push_back(kp.first);
    }
    int out = 0;
    for (int i = 0; i < positions.size()-1; i++)
    {
        for (int j = i + 1; j < positions.size(); j++)
        {
            if (saves(cheat_len, dist, positions[i], positions[j]))
            {
                out++;
            }
        }
    }
    return out;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<std::string> maze;
    Vec end;
    int y = 0;
    while (std::getline(std::cin, line))
    {
        for (int x = 0; x < line.size(); x++)
        {
            if (line[x] == 'E')
            {
                end = {x, y};
            }
        }
        maze.push_back(line);
        y++;
    }
    int h = maze.size();
    int w = maze[0].size();
    std::unordered_map<Vec, int> dist = bfs(end, maze, w, h);
    std::cout << solve(2, dist) << "\n";
    std::cout << solve(20, dist) << "\n";
}