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

bool in_bounds(std::pair<int, int> &pos, int w, int h)
{
    return 0 <= pos.first && pos.first < w && 0 <= pos.second && pos.second < h;
}

std::pair<std::pair<int, int>, int> step(std::pair<std::pair<int, int>, int> &state, std::unordered_set<int> &obstacles)
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

int main(int argc, char *argv[])
{
    std::cout << "start" << std::endl;
    std::string line;
    int y = 0;
    auto hash = [](const std::pair<int, int> &p)
    { return p.first * 256 + p.second; };
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
}