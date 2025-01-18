#include <iostream>
#include <string>
#include <regex>
#include <stack>
#include <bitset>

unsigned long long combo(unsigned long long a, unsigned long long b, unsigned long long c, unsigned long long operand)
{
    if (0 <= operand && operand <= 3)
    {
        return operand;
    }
    if (operand == 4)
    {
        return a;
    }
    if (operand == 5)
    {
        return b;
    }
    if (operand == 6)
    {
        return c;
    }
    std::cout << "Invalid operand";
    return 0;
}

std::vector<unsigned long long> execute(unsigned long long a, unsigned long long b, unsigned long long c, std::vector<unsigned long long> program)
{
    unsigned long long pointer = 0;
    std::vector<unsigned long long> output;
    while (pointer < program.size() - 1)
    {
        unsigned long long opcode = program[pointer];
        unsigned long long operand = program[pointer + 1];
        bool skip = false;
        switch (opcode)
        {
        case 0:
            a = a >> combo(a, b, c, operand);
            break;
        case 1:
            b = b ^ operand;
            break;
        case 2:
            b = combo(a, b, c, operand) % 8;
            break;
        case 3:
            if (a != 0)
            {
                pointer = operand;
                skip = true;
            }
            break;
        case 4:
            b = b ^ c;
            break;
        case 5:
            output.push_back(combo(a, b, c, operand) % 8);
            break;
        case 6:
            b = a >> combo(a, b, c, operand);
            break;
        case 7:
            c = a >> combo(a, b, c, operand);
            break;
        default:
            std::cout << "Invalid opcode: " << opcode << "\n";
            break;
        }

        if (!skip)
        {
            pointer += 2;
        }
    }

    return output;
}

void print_output(std::vector<unsigned long long> output)
{
    std::cout << output[0];
    for (int i = 1; i < output.size(); i++)
    {
        std::cout << "," << output[i];
    }
    std::cout << "\n";
}

unsigned long long dfs(unsigned long long b, unsigned long long c, std::vector<unsigned long long> program)
{
    const int l = 16 - 1; // length of program minus 1
    const int size = 48;
    std::stack<std::pair<int, std::bitset<size>>> s;
    s.push({0, 0});
    while (!s.empty())
    {
        auto [n, candidate] = s.top();
        s.pop();
        if (n > l)
        {
            return candidate.to_ullong();
        }
        for (int i = 8; i >= 0; i--)
        {
            std::bitset<size> shift (i);
            shift = shift << (3 * (l-n));
            std::bitset<size> a = (candidate | shift);
            if (a.any())
            {
                std::vector<unsigned long long> out = execute(a.to_ullong(), b, c, program);
                if (out[l - n] == program[l - n])
                {
                    s.push({n + 1, a});
                }
            }
        }
    }
    std::cout << "error\n";
    return -1;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::string s;
    while (std::getline(std::cin, line))
    {
        s += line;
    }
    std::regex r("Register A: (\\d+)Register B: (\\d+)Register C: (\\d+)Program: (\\d(,\\d)*)");
    std::smatch m;
    std::regex_match(s, m, r);
    unsigned long long a = std::stoi(m[1]);
    unsigned long long b = std::stoi(m[2]);
    unsigned long long c = std::stoi(m[3]);
    std::string nums = m[4];
    std::vector<unsigned long long> program;
    for (int i = 0; i < nums.length(); i += 2)
    {
        program.push_back((int)(nums[i]) - '0');
    }
    print_output(execute(a, b, c, program));
    std::cout << dfs(b, c, program) << "\n";
}