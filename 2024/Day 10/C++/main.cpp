#include <string>
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_set>

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<std::vector<int>> map;
    while (std::getline(std::cin, line))
    {
        std::vector<int> row;
        for (char c : line)
        {
            row.push_back(c - '0');
        }
        map.push_back(row);
    }
    int w = map[0].size();
    int h = map.size();

    int path_count = 0;
    int unique_path_count = 0;
    for (int y = 0; y < h; y++)
    {
        for (int x = 0; x < w; x++)
        {
            if (map[y][x] == 0)
            {
                std::stack<std::pair<int, int>> S;
                S.push(std::make_pair(x, y));
                std::unordered_set<int> unique_paths;
                while (!S.empty())
                {
                    std::pair<int, int> pos = S.top();
                    int px = pos.first;
                    int py = pos.second;
                    S.pop();
                    int val = map[py][px];
                    if (val == 9)
                    {
                        path_count++;
                        unique_paths.insert(px + py * w);
                    }
                    if (py < h - 1 && map[py + 1][px] == val + 1)
                    {
                        S.push(std::make_pair(px, py + 1));
                    }
                    if (py > 0 && map[py - 1][px] == val + 1)
                    {
                        S.push(std::make_pair(px, py - 1));
                    }
                    if (px < w - 1 && map[py][px + 1] == val + 1)
                    {
                        S.push(std::make_pair(px + 1, py));
                    }
                    if (px > 0 && map[py][px - 1] == val + 1)
                    {
                        S.push(std::make_pair(px - 1, py));
                    }
                }
                unique_path_count += unique_paths.size();
            }
        }
    }
    std::cout << unique_path_count << "\n";
    std::cout << path_count << "\n";
}