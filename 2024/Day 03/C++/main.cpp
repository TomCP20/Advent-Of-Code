#include <iostream>
#include <string>
#include <vector>
#include <regex>

int main(int argc, char *argv[])
{
    std::string line;
    std::string input;
    while (std::getline(std::cin, line))
    {
        input += line;
    }
    std::smatch match;
    std::string subject;

    std::regex patter1("mul\\((\\d+),(\\d+)\\)");
    subject = input;
    int sum1 = 0;
    while (std::regex_search(subject, match, patter1))
    {
        sum1 += std::stoi(match[1]) * std::stoi(match[2]);
        subject = match.suffix().str();
    }
    std::cout << sum1 << std::endl;

    std::regex patter2("do\\(\\)|don\'t\\(\\)|mul\\((\\d+),(\\d+)\\)");
    subject = input;
    int sum2 = 0;
    bool enabled = true;
    while (std::regex_search(subject, match, patter2))
    {
        if (match[0] == "do()")
        {
            enabled = true;
        }
        else if (match[0] == "don't()")
        {
            enabled = false;
        }
        else if (enabled)
        {
            sum2 += std::stoi(match[1]) * std::stoi(match[2]);
        }
        subject = match.suffix().str();
    }
    std::cout << sum2 << std::endl;
}