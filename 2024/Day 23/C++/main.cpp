#include <string>
#include <iostream>
#include <unordered_map>
#include <unordered_set>

bool contains(std::unordered_set<std::string> set, std::string val)
{
    return set.find(val) != set.end();
}



int main(int argc, char *argv[])
{
    std::unordered_map<std::string, std::unordered_set<std::string>> connections;
    std::string line;
    while (std::getline(std::cin, line))
    {
        std::string a = line.substr(0, 2);
        std::string b = line.substr(3, 2);
        connections[a].insert(b);
        connections[b].insert(a);
    }
    int part1 = 0;
    std::unordered_set<std::string> checked_ts;
    for (auto &[k, v] : connections)
    {
        if (k[0] == 't')
        {
            for (auto a = v.begin(); a != v.end(); ++a)
            {
                for (auto b = a; ++b != v.end(); /**/)
                {
                    if (contains(connections[*b], *a) && !contains(checked_ts, *a) && !contains(checked_ts, *b))
                    {
                        part1++;
                    }
                }
            }
            checked_ts.insert(k);
        }
    }
    std::cout << part1 << "\n";
}