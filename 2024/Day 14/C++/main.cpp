#include <string>
#include <regex>
#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>

const std::regex PATTERN("p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)");

const int W = 101;
const int H = 103;
const int MX = W / 2;
const int MY = H / 2;

std::vector<std::pair<int, int>> skip(int t, std::vector<std::tuple<int, int, int, int>> &drones)
{
    std::vector<std::pair<int, int>> results;
    for (auto const &[px, py, vx, vy] : drones)
    {
        results.push_back(std::make_pair((((px + t * vx) % W) + W) % W, (((py + t * vy) % H) + H) % H));
    }
    return results;
}

void print_state(std::vector<std::pair<int, int>> &state)
{
    for (int y = 0; y < H; y++)
    {
        for (int x = 0; x < W; x++)
        {
            if (std::find(state.begin(), state.end(), std::make_pair(x, y)) != state.end())
            {
                std::cout << "#";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "\n";
    }
}

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<std::tuple<int, int, int, int>> drones;
    while (std::getline(std::cin, line))
    {
        std::smatch m;
        std::regex_match(line, m, PATTERN);
        drones.push_back({stoi(m[1]), stoi(m[2]), stoi(m[3]), stoi(m[4])});
    }

    int q1 = 0;
    int q2 = 0;
    int q3 = 0;
    int q4 = 0;
    for (auto const &[x, y] : skip(100, drones))
    {
        if (x < MX && y < MY)
        {
            q1 += 1;
        }
        else if (x > MX && y < MY)
        {
            q2 += 1;
        }
        else if (x < MX && y > MY)
        {
            q3 += 1;
        }
        else if (x > MX && y > MY)
        {
            q4 += 1;
        }
    }
    std::cout << q1 * q2 * q3 * q4 << "\n";
    std::vector<std::pair<int, int>> state =skip(8270, drones);
    print_state(state);
}