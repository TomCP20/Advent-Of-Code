#include <string>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <utility>

int main(int argc, char *argv[])
{
    std::string line;
    int y = 0;
    std::unordered_map<char, std::vector<std::pair<int, int>>> antennas;
    while (std::getline(std::cin, line))
    {
        for (int x = 0; x < line.length(); x++)
        {
            if (line[x] != '.')
            {
                antennas[line[x]].push_back(std::make_pair(x, y));
            }
        }
        y++;
    }
    const int width = line.length();
    const int height = y;

    std::unordered_set<int> antinodes1;
    std::unordered_set<int> antinodes2;
    for (auto const &[key, locations] : antennas)
    {
        for (std::pair<int, int> a : locations)
        {
            for (std::pair<int, int> b : locations)
            {
                if (a != b)
                {
                    std::pair<int, int> pos1 = std::make_pair(2 * a.first - b.first, 2 * a.second - b.second);
                    if (0 <= pos1.first && pos1.first < width && 0 <= pos1.second && pos1.second < height)
                    {
                        antinodes1.insert(pos1.first + pos1.second * width);
                    }

                    std::pair<int, int> diff = std::make_pair(a.first - b.first, a.second - b.second);
                    std::pair<int, int> pos2 = a;
                    while (0 <= pos2.first && pos2.first < width && 0 <= pos2.second && pos2.second < height)
                    {
                        antinodes2.insert(pos2.first + pos2.second * width);
                        pos2 = std::make_pair(pos2.first + diff.first, pos2.second + diff.second);
                    }
                }
            }
        }
    }
    std::cout << antinodes1.size() << "\n";
    std::cout << antinodes2.size() << "\n";
}