#include <string>
#include <iostream>
#include <unordered_map>
#include <tuple>
#include <regex>
#include <vector>

using REG = std::unordered_map<std::string, bool>;
using GATES = std::unordered_map<std::string, std::tuple<std::string, std::string, std::string>>;

bool get_val(const REG &reg, const GATES &gates, const std::string &name)
{
    if (reg.find(name) != reg.end())
    {
        return reg.at(name);
    }
    auto [l, r, operand] = gates.at(name);
    int l_val = get_val(reg, gates, l);
    int r_val = get_val(reg, gates, r);
    if (operand == "AND")
    {
        return l_val & r_val;
    }
    else if (operand == "or")
    {
        return l_val | r_val;
    }
    else
    {
        return l_val ^ r_val;
    }    
}

long long solve(const REG &reg, const GATES &gates, const std::vector<std::string> &zgates)
{
    long long num = 0;
    for (auto &gate : zgates)
    {
        num = (num << 1) + get_val(reg, gates, gate);
    }
    return num;
}

int main(int argc, char *argv[])
{
    std::string line;

    REG reg;
    while (std::getline(std::cin, line))
    {
        if (line == "")
        {
            break;
        }
        reg[line.substr(0, 3)] = line.substr(5, 1) == "1";
    }

    GATES gates;
    std::regex r("(...) (AND|OR|XOR) (...) -> (...)");
    while (std::getline(std::cin, line))
    {
        std::smatch m;
        if(std::regex_match(line, m, r))
        {
            gates[m[4]] = {m[1], m[3], m[2]};
        }
    }
    std::vector<std::string> zgates;
    for (auto &[k, _] : gates)
    {
        if (k[0] == 'z')
        {
            zgates.push_back(k);
        }
    }
    std::sort(zgates.begin(), zgates.end(), std::greater<std::string>());
    std::cout << solve(reg, gates, zgates) << "\n";
}