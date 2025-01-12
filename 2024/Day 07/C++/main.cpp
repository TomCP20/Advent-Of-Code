#include <vector>
#include <stack>
#include <string>
#include <iostream>
#include <sstream>
#include <math.h>

bool check(unsigned long long &val, std::stack<unsigned long long> &nums, bool part2)
{
    if (nums.size() <= 1)
    {
        return nums.top() == val;
    }
    unsigned long long a = nums.top();
    nums.pop();
    unsigned long long b = nums.top();
    nums.pop();

    unsigned long long sum = a + b;
    nums.push(sum);
    if (check(val, nums, part2))
    {
        return true;
    }
    nums.pop();

    unsigned long long product = a * b;
    nums.push(product);
    if (check(val, nums, part2))
    {
        return true;
    }
    nums.pop();

    if (part2)
    {
        unsigned long long concat = (a * std::pow(10, (int)(log10(b) + 1))) + b;
        nums.push(concat);
        if (check(val, nums, part2))
        {
            return true;
        }
        nums.pop();
    }

    nums.push(b);
    nums.push(a);
    return false;
}

int main(int argc, char *argv[])
{
    std::string line;
    unsigned long long p1 = 0;
    unsigned long long p2 = 0;
    while (std::getline(std::cin, line))
    {
        std::stringstream ss(line);
        std::string s;
        std::getline(ss, s, ' ');
        s.pop_back();
        unsigned long long val = std::stoull(s);
        std::vector<unsigned long long> vec;
        while (std::getline(ss, s, ' '))
        {
            vec.push_back(std::stoull(s));
        }
        std::stack<unsigned long long> nums;
        for (int i = vec.size() - 1; i >= 0; i--)
        {
            nums.push(vec[i]);
        }
        if (check(val, nums, false))
        {
            p1 += val;
        }
        if (check(val, nums, true))
        {
            p2 += val;
        }
    }
    std::cout << p1 << std::endl;
    std::cout << p2 << std::endl;
}