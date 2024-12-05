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
        input += "..." + line + "...";
    }
    int row = line.length() + 6;

    int count1 = 0;
    int offsets[4] = {0, row, row - 1, row - 2};
    for (int i = 0; i < 4; i++)
    {
        std::string o = std::to_string(offsets[i]);
        std::regex re("(?=(X.{" + o + "}M.{" + o + "}A.{" + o + "}S|S.{" + o + "}A.{" + o + "}M.{" + o + "}X))");
        std::sregex_iterator next(input.begin(), input.end(), re);
        std::sregex_iterator end;
        while (next != end)
        {
            std::smatch match = *next;
            next++;
            count1++;
        }
    }
    std::cout << count1 << std::endl;

    int count2 = 0;
    std::string n = std::to_string(row - 2);
    std::string perms[4][4] = {{"M", "M", "S", "S"}, {"M", "S", "M", "S"}, {"S", "M", "S", "M"}, {"S", "S", "M", "M"}};
    for (int i = 0; i < 4; i++)
    {
        std::regex re("(?=(" + perms[i][0] + "." + perms[i][1] + ".{" + n + "}A.{" + n + "}" + perms[i][2] + "." + perms[i][3] + "))");

        std::sregex_iterator next(input.begin(), input.end(), re);
        std::sregex_iterator end;
        while (next != end)
        {
            std::smatch match = *next;
            next++;
            count2++;
        }
    }
    std::cout << count2 << std::endl;
}