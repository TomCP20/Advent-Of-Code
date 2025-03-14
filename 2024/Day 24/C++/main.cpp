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

std::string getswap(const GATES &gates, std::string name)
{
    if (name[0] == 'z')
    {
        std::string s = name.substr(1);
        int num = stoi(s) - 1;
        if (num < 10)
        {
            return "z0" + std::to_string(num);
        }
        return "z" + std::to_string(num);
    }
    for (auto &[out, v] : gates)
    {
        auto &[l, r, op] = v;
        if ((name == l || name == r) && op != "AND")
        {
            return getswap(gates, out);
        }
    }
    std::cout << "ERROR" << "\n";
    return "";
}

std::pair<std::vector<std::string>, std::vector<std::string>> get_rules(const GATES &gates, const std::vector<std::string> &zgates)
{
    std::vector<std::string> rule1;
    std::vector<std::string> rule2;
    for (auto &[gate, v] : gates)
    {
        auto &[l, r, op] = v;
        if (std::find(zgates.begin() + 1, zgates.end(), gate) != zgates.end() && op != "XOR")
        {
            rule1.push_back(gate);
        }
        if (std::find(zgates.begin(), zgates.end(), gate) == zgates.end())
        {
            if (l[0] != 'x' && l[0] != 'y' && r[0] != 'x' && r[0] != 'y' && op == "XOR")
            {
                rule2.push_back(gate);
            }
        }
    }
    return {rule1, rule2};
}

long long get_truenum(const REG &reg)
{
    std::vector<std::string> reg_names;
    for (auto &[name, _] : reg)
    {
        reg_names.push_back(name);
    }
    std::sort(reg_names.begin(), reg_names.end(), std::greater<std::string>());

    long long xnum = 0;
    long long ynum = 0;
    
    for (auto name : reg_names)
    {
        if (name[0] == 'x')
        {
            xnum = (xnum << 1) + reg.at(name);
        }
        else if (name[0] == 'y')
        {
            ynum = (ynum << 1) + reg.at(name);
        }
    }
    return xnum + ynum;
}

std::vector<std::string> get_badgates(const REG &reg, GATES &gates, const std::vector<std::string> &zgates)
{
    auto [rule1, rule2] = get_rules(gates, zgates);

    for (auto &rule : rule2)
    {
        std::string swap = getswap(gates, rule);
        std::swap(gates[rule], gates[swap]);
    }

    long long num = solve(reg, gates, zgates);
    long long truenum = get_truenum(reg);
    long long diff = ((num ^ truenum) & -(num ^ truenum));
    unsigned bits;
    for (bits = 0; diff != 0; bits++)
    {
        diff >>= 1;
    }
    bits--;
    std::vector<std::string> badgates;
    badgates.insert(badgates.end(), rule1.begin(), rule1.end());
    badgates.insert(badgates.end(), rule2.begin(), rule2.end());
    std::string xstr = "x" + std::to_string(bits);
    std::string ystr = "y" + std::to_string(bits);
    for (auto &[gate, v] : gates)
    {
        auto &[l, r, _] = v;
        if ((l == xstr && r == ystr) || (r == xstr && l == ystr))
        {
            badgates.push_back(gate);
        }
    }
    return badgates;
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
        if (std::regex_match(line, m, r))
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

    std::vector<std::string> badgates = get_badgates(reg, gates, zgates);
    std::sort(badgates.begin(), badgates.end());
    for (auto &gate : badgates)
    {
        std::cout << gate;
        if (gate == badgates.back())
        {
            std::cout << "\n";
        }
        else
        {
            std::cout << ",";
        }
        
        
    }
    
    
}