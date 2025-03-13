#include <string>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <tuple>
#include <algorithm>

template <class T1, class T2, class T3, class T4>
struct std::hash<std::tuple<T1, T2, T3, T4>>
{
    size_t operator()(const tuple<T1, T2, T3, T4> &p) const
    {
        return get<0>(p) ^ get<1>(p) ^ get<2>(p) ^ get<3>(p);
    }
};

unsigned long long step(unsigned long long secret_num)
{
    secret_num = ((secret_num * 64) ^ secret_num) % 16777216;
    secret_num = ((secret_num / 32) ^ secret_num) % 16777216;
    secret_num = ((secret_num * 2048) ^ secret_num) % 16777216;
    return secret_num;
}

unsigned long long step2000(unsigned long long secret_num)
{
    for (int _ = 0; _ < 2000; _++)
    {
        secret_num = step(secret_num);
    }
    return secret_num;
}

std::unordered_map<std::tuple<int, int, int, int>, int> sequence_to_price(unsigned long long secret_num)
{
    int p1, p2, p3, p4;
    std::unordered_map<std::tuple<int, int, int, int>, int> prices;

    for (int i = 0; i < 2000; i++)
    {
        if (i >= 4)
        {
            std::tuple<int, int, int, int> key = {p1, p2, p3, p4};
            if (prices.find(key) == prices.end())
            {
                prices[key] = secret_num % 10;
            }
        }
        p1 = p2;
        p2 = p3;
        p3 = p4;
        int next_val = step(secret_num);
        p4 = (next_val % 10) - (secret_num % 10);
        secret_num = next_val;
    }
    return prices;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<unsigned long> initial;
    while (std::getline(std::cin, line))
    {
        initial.push_back(stoul(line));
    }
    unsigned long long part1 = 0;
    for (int n : initial)
    {
        part1 += step2000(n);
    }
    std::cout << part1 << std::endl;

    std::unordered_map<std::tuple<int, int, int, int>, int> all_prices;
    for (int n : initial)
    {
        std::unordered_map<std::tuple<int, int, int, int>, int> prices = sequence_to_price(n);
        for (auto &[k, v] : prices)
        {
            all_prices[k] += v;
        }
        
    }

    std::pair<const std::tuple<int, int, int, int>, int> m = *std::max_element(
        all_prices.begin(), all_prices.end(),
        [](const std::pair<std::tuple<int, int, int, int>, int> &p1, const std::pair<std::tuple<int, int, int, int>, int> &p2)
        {
            return p1.second < p2.second;
        });
    std::cout << m.second << '\n';
}