#include <string>
#include <vector>
#include <iostream>
#include <regex>
#include <sstream>

std::vector<std::string> generate_possible_designs(const std::vector<std::string> &towls, const std::vector<std::string> &designs)
{
    std::stringstream pattern;
    pattern << "(" + towls[0];
    for (int i = 1; i < towls.size(); i++)
    {
        pattern << "|" << towls[i];
    }
    pattern << ")+";
    std::regex r(pattern.str());
    std::vector<std::string> possible_designs;
    for (std::string d : designs)
    {
        std::smatch m;
        if (std::regex_match(d, m, r))
        {
            possible_designs.push_back(d);
        }
        
    }
    return possible_designs;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<std::string> towls;
    std::vector<std::string> designs;
    bool isDesign = false;
    while (std::getline(std::cin, line))
    {
        if (line == "")
        {
            isDesign = true;
        }
        else if (isDesign)
        {
            designs.push_back(line);
        }
        else
        {
            std::regex r("[wubrg]+");
            std::sregex_iterator words_begin = std::sregex_iterator(line.begin(), line.end(), r);
            std::sregex_iterator words_end = std::sregex_iterator();
            for (std::sregex_iterator i = words_begin; i != words_end; ++i)
            {
                std::smatch match = *i;
                std::string match_str = match.str();
                towls.push_back(match_str);
            }
        }
    }
    std::cout << generate_possible_designs(towls, designs).size() << "\n";
}