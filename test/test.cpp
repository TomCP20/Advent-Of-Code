#include <iostream>
#include <string>

int main(int argc, char* argv[])
{
    std::string s;
    std::string result;
    while (std::getline(std::cin, s))
    {
        if (result == "")
        {
            result = s;
        }
        else
        {
            result += "\n" + s;
        }
    }
    std::cout << result;
    return 0;
}