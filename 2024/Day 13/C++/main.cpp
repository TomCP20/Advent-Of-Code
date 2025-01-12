#include <string>
#include <regex>
#include <iostream>

const std::regex PATTERN("Button A: X\\+(\\d+), Y\\+(\\d+)Button B: X\\+(\\d+), Y\\+(\\d+)Prize: X=(\\d+), Y=(\\d+)");

long long get_price(int ax, int ay, int bx, int by, long long px, long long py)
{
    long long det = ax * by - ay * bx;
    long long wi = px * by - py * bx;
    long long wj = py * ax - px * ay;
    if (wi % det == 0 && wj % det == 0)
    {
        return 3 * (wi / det) + (wj / det);
    }
    return 0;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::string lines;
    while (std::getline(std::cin, line))
    {
        lines += line;
    }
    std::sregex_iterator b = std::sregex_iterator(lines.begin(), lines.end(), PATTERN);
    std::sregex_iterator e = std::sregex_iterator();
    long long cost1 = 0;
    long long cost2 = 0;
    for (std::sregex_iterator i = b; i != e; ++i)
    {
        std::smatch match = *i;
        std::string match_str = match.str();
        int ax = stoi(match[1]);
        int ay = stoi(match[2]);
        int bx = stoi(match[3]);
        int by = stoi(match[4]);
        int px = stoi(match[5]);
        int py = stoi(match[6]);
        cost1 += get_price(ax, ay, bx, by, px, py);
        cost2 += get_price(ax, ay, bx, by, px + 10000000000000, py + 10000000000000);
    }
    std::cout << cost1 << "\n";
    std::cout << cost2 << "\n";
}