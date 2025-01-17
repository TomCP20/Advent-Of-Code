#include <iostream>
#include <string>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <limits>
#include <algorithm>
#include <stack>

using Vec = std::pair<int, int>;
using State = std::pair<Vec, int>;
using QState = std::pair<int, State>;
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

std::vector<Vec> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
std::vector<std::pair<State, int>> get_neighbors(State n, std::vector<std::string> maze)
{
    auto [pos, turns] = n;
    Vec direction = dirs[turns];
    Vec npos = pos + direction;
    std::vector<std::pair<State, int>> out;
    if (maze[npos.second][npos.first] != '#')
    {
        out.push_back({{npos, turns}, 1});
    }
    out.push_back({{pos, (turns + 1) % 4}, 1000});
    out.push_back({{pos, (turns + 3) % 4}, 1000});
    return out;
}

int dfs(State current, std::unordered_map<State, std::unordered_set<State>> prev)
{
    std::stack<State> s;
    s.push(current);
    std::unordered_set<Vec> tiles;
    while (!s.empty())
    {
        State v = s.top();
        s.pop();
        tiles.insert(v.first);
        for (State p : prev[v])
        {
            s.push(p);
        }
    }
    return tiles.size();    
}

std::pair<int, int> dijkstra(State start_state, Vec goal, std::vector<std::string> maze)
{
    auto comp = [](QState a, QState b)
    { return a.first > b.first; };
    std::priority_queue<QState, std::vector<QState>, decltype(comp)> q(comp);
    q.push({0, start_state});
    std::unordered_map<State, int> dist_map = {{start_state, 0}};
    std::unordered_map<State, std::unordered_set<State>> prev;
    State current;
    while (!q.empty())
    {
        current = q.top().second;
        q.pop();
        if (current.first == goal)
        {
            break;
        }
        for (auto [neighbor, d] : get_neighbors(current, maze))
        {
            int alt = dist_map[current] + d;
            bool in_map = dist_map.find(neighbor) != dist_map.end();
            if (!in_map || alt < dist_map[neighbor])
            {
                
                prev[neighbor] = {current};
                dist_map[neighbor] = alt;
                q.push({alt, neighbor});
            }
            else if (in_map && alt == dist_map[neighbor])
            {
                prev[neighbor].insert(current);
            }
        }
    }
    
    return {dist_map[current], dfs(current, prev)};
}

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<std::string> maze;
    std::pair<int, int> start;
    std::pair<int, int> end;
    int y = 0;
    while (std::getline(std::cin, line))
    {
        for (int x = 0; x < line.size(); x++)
        {
            if (line[x] == 'S')
            {
                start = {x, y};
            }
            else if (line[x] == 'E')
            {
                end = {x, y};
            }
        }
        y++;
        maze.push_back(line);
    }
    auto [dist, unique_tiles] = dijkstra({start, 0}, end, maze);
    std::cout << dist << "\n" << unique_tiles << "\n";
}