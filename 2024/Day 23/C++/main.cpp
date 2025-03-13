#include <string>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <vector>

using SET = std::unordered_set<std::string>;
using MAP = std::unordered_map<std::string, SET>;

bool contains(SET set, std::string val)
{
    return set.find(val) != set.end();
}

int part1(MAP &connections)
{
    int count = 0;
    SET checked_ts;
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
                        count++;
                    }
                }
            }
            checked_ts.insert(k);
        }
    }
    return count;
}

void bron_kerbosch(std::vector<SET> &cliques, MAP &connections, SET &&R, SET &&P, SET &&X)
{
    if (P.empty() && X.empty())
    {
        cliques.push_back(R);
    }
    while (!P.empty())
    {
        std::string v = *P.begin();
        SET next_r = R;
        next_r.insert(v);
        SET next_p;
        for (auto &p : P)
        {
            if (contains(connections[v], p))
            {
                next_p.insert(p);
            }
        }
        SET next_x;
        for (auto &x : X)
        {
            if (contains(connections[v], x))
            {
                next_x.insert(x);
            }
        }
        bron_kerbosch(cliques, connections, move(next_r), move(next_p), move(next_x));
        P.erase(v);
        X.insert(v);
    }
}

int main(int argc, char *argv[])
{
    MAP connections;
    SET computers;
    std::string line;
    while (std::getline(std::cin, line))
    {
        std::string a = line.substr(0, 2);
        std::string b = line.substr(3, 2);
        connections[a].insert(b);
        connections[b].insert(a);
        computers.insert(a);
        computers.insert(b);
    }
    std::cout << part1(connections) << "\n";
    std::vector<SET> cliques;
    bron_kerbosch(cliques, connections, {}, move(computers), {});
    SET max_set = *std::max_element(cliques.begin(), cliques.end(), [](SET a, SET b)
                                    { return a.size() < b.size(); });
    std::vector<std::string> v(max_set.begin(), max_set.end());
    std::sort(v.begin(), v.end());
    for (std::string computer : v)
    {
        std::cout << computer;
        if (computer == v.back())
        {
            std::cout << "\n";
        }
        else
        {
            std::cout << ",";
        }
        
    }
}