#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char *argv[])
{
    std::string line;
    bool firstHalf = true;
    std::vector<std::pair<int, int>> rules;
    std::vector<std::vector<int>> updates;
    while (std::getline(std::cin, line))
    {
        if (line == "")
        {
            firstHalf = false;
        }
        else if (firstHalf)
        {
            rules.push_back(std::make_pair(std::stoi(line.substr(0, 2)), std::stoi(line.substr(3, 2))));
        }
        else
        {
            std::vector<int> update;
            int count = (line.length() + 1) / 3;
            for (int i = 0; i < count; i++)
            {
                update.push_back(std::stoi(line.substr(3 * i, 2)));
            }
            updates.push_back(update);
        }
    }
    auto comp = [&](int a, int b) -> bool { return std::find(rules.begin(), rules.end(), std::make_pair(a, b)) != rules.end(); };
    int sum1 = 0;
    int sum2 = 0;
    for (int i = 0; i < updates.size(); i++)
    {
        std::vector<int> update = updates[i];
        int mid = (update.size() - 1) / 2;
        if (std::is_sorted(update.begin(), update.end(), comp))
        {
            sum1 += update[mid];
        }
        else
        {
            std::sort(update.begin(), update.end(), comp);
            sum2 += update[mid];
        }
    }
    std::cout << sum1 << std::endl;
    std::cout << sum2 << std::endl;
}