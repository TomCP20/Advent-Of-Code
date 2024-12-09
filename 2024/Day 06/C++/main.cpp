#include <string>
#include <vector>
#include <iostream>
#include <unordered_set>

std::pair<int, int> get_dir(int turns)
{
    std::pair<int, int> p;
    if (turns == 0)
    {
        p.first = 0;
        p.second = -1;
    }
    else if (turns == 1)
    {
        p.first = 1;
        p.second = 0;
    }
    else if (turns == 2)
    {
        p.first = 0;
        p.second = 1;
    }
    else if (turns == 3)
    {
        p.first = -1;
        p.second = 0;
    }
    return p;
}

int coord_to_int(int x, int y)
{
    return x * 256 + y;
}

int coord_to_int(std::pair<int, int> pos)
{
    return coord_to_int(pos.first, pos.second);
}

int state_to_int(std::pair<std::pair<int, int>, int> state)
{
    return 40 * coord_to_int(state.first) + state.second;
}

bool in_bounds(std::pair<int, int> &pos, int w, int h)
{
    return 0 <= pos.first && pos.first < w && 0 <= pos.second && pos.second < h;
}

std::pair<std::pair<int, int>, int> step(std::pair<std::pair<int, int>, int> state, std::unordered_set<int> &obstacles)
{
    std::pair<int, int> guard_pos = state.first;
    int turns = state.second;
    std::pair<int, int> guard_dir = get_dir(turns);
    std::pair<int, int> next_guard_pos;
    next_guard_pos.first = guard_pos.first + guard_dir.first;
    next_guard_pos.second = guard_pos.second + guard_dir.second;
    if (obstacles.find(coord_to_int(next_guard_pos)) != obstacles.end())
    {
        state.second = (turns + 1) % 4;
    }
    else
    {
        state.first = next_guard_pos;
    }
    return state;
}

int part1(std::pair<std::pair<int, int>, int> state, std::unordered_set<int> obstacles, int w, int h)
{
    std::unordered_set<int> traversed;
    while (in_bounds(state.first, w, h))
    {
        traversed.insert(coord_to_int(state.first));
        state = step(state, obstacles);
    }
    return traversed.size();
}

bool detect_loop(std::pair<std::pair<int, int>, int> &initial_state, std::unordered_set<int> &obstacles, int w, int h)
{
    std::pair<std::pair<int, int>, int> state = initial_state;
    std::unordered_set<int> state_set;
    while (in_bounds(state.first, w, h))
    {
        int x = state_to_int(state);
        if (state_set.find(x) != obstacles.end())
        {
            return true;
        }
        state_set.insert(x);
        state = step(state, obstacles);
    }
    return false;
}

int part2(std::pair<std::pair<int, int>, int> state, std::unordered_set<int> obstacles, int w, int h)
{
    int count = 0;
    std::vector<std::pair<std::pair<int, int>, int>> path;
    while (in_bounds(state.first, w, h))
    {
        path.push_back(state);
        state = step(state, obstacles);
    }
    std::unordered_set<int> checked;
    for (int i = 0; i < path.size() - 1; i++)
    {
        std::pair<std::pair<int, int>, int> new_state = path[i];
        int obstacle_pos = coord_to_int(path[i + 1].first);
        if (checked.find(obstacle_pos) == checked.end())
        {
            checked.insert(obstacle_pos);
            std::unordered_set<int> new_obstacles = obstacles;
            new_obstacles.insert(obstacle_pos);
            if (detect_loop(new_state, new_obstacles, w, h))
            {
                count++;
            }
        }
    }
    return count;
}

int main(int argc, char *argv[])
{
    std::string line;
    int y = 0;
    std::unordered_set<int> obstacles;
    std::pair<std::pair<int, int>, int> state;
    while (std::getline(std::cin, line))
    {
        for (int x = 0; x < line.length(); x++)
        {
            if (line[x] == '#')
            {
                obstacles.insert(coord_to_int(x, y));
            }
            else if (line[x] == '^')
            {
                state = std::make_pair(std::make_pair(x, y), 0);
            }
            else if (line[x] == '>')
            {
                state = std::make_pair(std::make_pair(x, y), 1);
            }
            else if (line[x] == 'v')
            {
                state = std::make_pair(std::make_pair(x, y), 2);
            }
            else if (line[x] == '<')
            {
                state = std::make_pair(std::make_pair(x, y), 3);
            }
        }
        y++;
    }
    int h = y;
    int w = line.length();
    std::cout << part1(state, obstacles, h, w) << std::endl;
    std::cout << part2(state, obstacles, h, w) << std::endl;
}