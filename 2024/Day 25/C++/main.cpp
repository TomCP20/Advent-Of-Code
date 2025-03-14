#include <string>
#include <iostream>
#include <vector>

const int W = 5;
const int H = 7;

std::vector<int> measure_cols(std::vector<std::string> schematic)
{
    std::vector<int> cols(W, 0);

    for (std::string &row : schematic)
    {
        for (int x = 0; x < W; x++)
        {
            if (row[x] == '#')
            {
                cols[x]++;
            }
        }
    }
    return cols;
}

bool can_match(std::vector<int> lock, std::vector<int> key)
{
    for (int i = 0; i < W; i++)
    {
        if (lock[i] + key[i] > H)
        {
            return false;
        }
    }
    return true;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<std::vector<std::string>> schematics;
    std::vector<std::string> s;
    while (std::getline(std::cin, line))
    {
        if (line == "")
        {
            schematics.push_back(s);
            s.clear();
        }
        else
        {
            s.push_back(line);
        }
    }
    schematics.push_back(s);

    std::vector<std::vector<int>> locks;
    std::vector<std::vector<int>> keys;
    for (auto &schematic : schematics)
    {
        if (schematic[0] == "#####")
        {
            locks.push_back(measure_cols(schematic));
        }
        else
        {
            keys.push_back(measure_cols(schematic));
        }
    }

    int count = 0;
    for (std::vector<int> &key : keys)
    {
        for (std::vector<int> &lock : locks)
        {
            if (can_match(lock, key))
            {
                count++;
            }
        }
    }
    std::cout << count << "\n";
}