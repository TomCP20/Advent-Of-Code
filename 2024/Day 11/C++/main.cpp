#include <string>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>

struct input_data
{
    unsigned long long stone;
    int blinks;
    int max_blinks;

    input_data(unsigned long long stone, int blinks, int max_blinks) : stone(stone), blinks(blinks), max_blinks(max_blinks) {}

    bool operator==(const input_data &other) const
    {
        return stone == other.stone && blinks == other.blinks && max_blinks == other.max_blinks;
    }
};

struct input_data_hasher
{
    size_t operator()(const input_data &p) const
    {
        return (std::hash<unsigned long long>()(p.stone) << 14) ^ (std::hash<int>()(p.blinks) << 7) ^ (std::hash<int>()(p.max_blinks));
    }
};

unsigned long long num_stones(input_data i)
{
    static std::unordered_map<input_data, unsigned long long, input_data_hasher> cache;
    if (cache.find(i) != cache.end())
    {
        return cache[i];
    }

    if (i.blinks >= i.max_blinks)
    {
        cache[i] = 1;
        return 1;
    }

    if (i.stone == 0)
    {
        cache[i] = num_stones(input_data(1, i.blinks + 1, i.max_blinks));
        return cache[i];
    }

    unsigned long long digits = (unsigned long long)(log10(i.stone)) + 1;
    if (digits % 2 == 0)
    {
        unsigned long long a = i.stone / (unsigned long long)std::pow(10, ((digits / 2)));
        unsigned long long b = i.stone % (unsigned long long)std::pow(10, ((digits / 2)));
        cache[i] = num_stones(input_data(a, i.blinks + 1, i.max_blinks)) + num_stones(input_data(b, i.blinks + 1, i.max_blinks));
        return cache[i];
    }
    cache[i] = num_stones(input_data(i.stone * 2024, i.blinks + 1, i.max_blinks));
    return cache[i];
}

int main(int argc, char *argv[])
{
    std::string str;
    unsigned long long sum1 = 0;
    unsigned long long sum2 = 0;
    while (std::getline(std::cin, str, ' '))
    {
        sum1 += num_stones(input_data(stoi(str), 0, 25));
        sum2 += num_stones(input_data(stoi(str), 0, 75));
    }
    std::cout << sum1 << "\n";
    std::cout << sum2 << "\n";
}
