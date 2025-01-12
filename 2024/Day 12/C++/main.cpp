#include <string>
#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>
#include <algorithm>

std::pair<int, int> getSeed(int h, int w, std::unordered_set<int> &checked)
{
    for (int y = 0; y < h; y++)
    {
        for (int x = 0; x < w; x++)
        {
            if (checked.find(x + y * w) == checked.end())
            {
                return std::make_pair(x, y);
            }
        }
    }
    return std::make_pair(-1, -1);
}

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<std::string> lines;
    while (std::getline(std::cin, line))
    {
        lines.push_back(line);
    }
    std::unordered_set<int> checked;
    int w = lines.size();
    int h = line.size();
    int price1 = 0;
    int price2 = 0;
    while (checked.size() < w * h)
    {
        std::pair<int, int> seed = getSeed(h, w, checked);
        std::queue<std::pair<int, int>> q;
        q.push(seed);
        char val = lines[seed.second][seed.first];
        std::vector<std::pair<int, int>> region;
        int perimiter = 0;
        int corners = 0;
        while (!q.empty())
        {
            std::pair<int, int> n = q.front();
            q.pop();
            if (std::find(region.begin(), region.end(), n) == region.end())
            {
                region.push_back(n);
                int x = n.first;
                int y = n.second;
                checked.insert(x + y * w);
                bool left = 0 < x && val == lines[y][x - 1];
                bool right = x < w - 1 && val == lines[y][x + 1];
                bool up = 0 < y && val == lines[y - 1][x];
                bool down = y < h - 1 && val == lines[y + 1][x];
                if (left)
                {
                    q.push(std::make_pair(x - 1, y));
                }
                else
                {
                    perimiter++;
                }
                if (right)
                {
                    q.push(std::make_pair(x + 1, y));
                }
                else
                {
                    perimiter++;
                }
                if (up)
                {
                    q.push(std::make_pair(x, y - 1));
                }
                else
                {
                    perimiter++;
                }
                if (down)
                {
                    q.push(std::make_pair(x, y + 1));
                }
                else
                {
                    perimiter++;
                }

                int neighbors = left + right + up + down;
                switch (neighbors)
                {
                case 0:
                    corners += 4;
                    break;
                case 1:
                    corners += 2;
                    break;
                case 2:
                    if (up && left)
                    {
                        corners++;
                        corners += (lines[y - 1][x - 1] != val);
                    }
                    else if (up && right)
                    {
                        corners++;
                        corners += (lines[y - 1][x + 1] != val);
                    }
                    else if (down && right)
                    {
                        corners++;
                        corners += (lines[y + 1][x + 1] != val);
                    }
                    else if (down && left)
                    {
                        corners++;
                        corners += (lines[y + 1][x - 1] != val);
                    }
                    break;
                case 3:
                    if (!up)
                    {
                        corners += (lines[y + 1][x + 1] != val);
                        corners += (lines[y + 1][x - 1] != val);
                    }
                    else if (!down)
                    {
                        corners += (lines[y - 1][x + 1] != val);
                        corners += (lines[y - 1][x - 1] != val);
                    }
                    else if (!left)
                    {
                        corners += (lines[y - 1][x + 1] != val);
                        corners += (lines[y + 1][x + 1] != val);
                    }
                    else if (!right)
                    {
                        corners += (lines[y - 1][x - 1] != val);
                        corners += (lines[y + 1][x - 1] != val);
                    }
                    break;
                case 4:
                    corners += (lines[y - 1][x - 1] != val);
                    corners += (lines[y - 1][x + 1] != val);
                    corners += (lines[y + 1][x + 1] != val);
                    corners += (lines[y + 1][x - 1] != val);
                    break;
                default:
                    break;
                }
            }
        }
        int area = region.size();
        price1 += area * perimiter;
        price2 += area * corners;
    }
    std::cout << price1 << "\n";
    std::cout << price2 << "\n";
}