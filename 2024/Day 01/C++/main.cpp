#include <iostream>
#include <string>
#include <regex>
#include <vector>
#include <map>

int main(int argc, char* argv[])
{
    std::regex const regex = std::regex("^(\\d+)   (\\d+)$");
    std::smatch match;
    std::string line;
    std::vector<int> left;
    std::vector<int> right;
    while (std::getline(std::cin, line))
    {
        if (std::regex_match(line, match, regex))
        {
            if (match.size() == 3)
            {
                left.push_back(std::stoi(match[1]));
                right.push_back(std::stoi(match[2]));
            }
        }
    }

    std::sort (left.begin(), left.end());
    std::sort (right.begin(), right.end());
    int result1 = 0;
    for (size_t i = 0; i < left.size(); i++)
    {
        result1 += abs(left[i] - right[i]);
    }
    std::cout << result1 <<std::endl;
    
    std::map<int, int> count;
    for (const int& r : right)
    {
        if (count.find(r) == count.end())
        {
            count[r] = 1;
        }
        else
        {
            count[r] += 1;
        }
    }
    int result2 = 0;
    for (const int& l : left)
    {
        if (count.find(l) != count.end())
        {
            result2 += l*count[l];
        }
    }
    std::cout << result2 <<std::endl;
    return 0;
}