#include <iostream>
#include <string>
#include <regex>
#include <stack>

long combo(long a, long b, long c, int operand)
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

std::vector<long> execute(long a, long b, long c, std::vector<int> program)
{
    int pointer = 0;
    std::vector<long> output;
    while (pointer < program.size() - 1)
    {
        int opcode = program[pointer];
        int operand = program[pointer + 1];
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

long dfs(long b, long c, std::vector<int> program)
{
    int l = program.size() - 1;
    std::stack<std::pair<int, long>> s;
    s.push({0, 0});
    while (!s.empty())
    {
        auto [n, candidate] = s.top();
        s.pop();
        if (n == l + 1)
        {
            return candidate;
        }
        for (int i = 0; i < 8; i++)
        {
            long a = candidate | (i << (3 * l - n));
            if (a != 0)
            {
                std::vector<long> out = execute(a, b, c, program);
                if (out[l - n] == program[l - n])
                {
                    s.push({n + 1, a});
                }
            }
        }
    }
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
    int a = std::stoi(m[1]);
    int b = std::stoi(m[2]);
    int c = std::stoi(m[3]);
    std::string nums = m[4];
    std::vector<int> program;
    for (int i = 0; i < nums.length(); i += 2)
    {
        program.push_back((int)(nums[i]) - '0');
    }
    std::vector<long> output = execute(a, b, c, program);
    std::cout << output[0];
    for (int i = 1; i < output.size(); i++)
    {
        std::cout << "," << output[i];
    }
    std::cout << "\n";
}