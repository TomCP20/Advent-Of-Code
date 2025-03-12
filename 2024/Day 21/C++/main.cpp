#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <limits>
#include <algorithm>
#include <sstream>

template <class A, class B>
struct std::hash<std::pair<A, B>>
{
    size_t operator()(const pair<A, B> &p) const
    {
        return ((hash<A>{}(p.first) << 1) | (hash<A>{}(p.first) >> (std::numeric_limits<size_t>::digits - 1))) ^ hash<B>{}(p.second);
    }
};

using KEYMAP = std::unordered_map<std::pair<char, char>, std::vector<std::string>>;
using KEYPOS = std::unordered_map<char, std::pair<int, int>>;

const KEYPOS numkeypos = {
    {'9', {2, 0}},
    {'8', {1, 0}},
    {'7', {0, 0}},
    {'6', {2, 1}},
    {'5', {1, 1}},
    {'4', {0, 1}},
    {'3', {2, 2}},
    {'2', {1, 2}},
    {'1', {0, 2}},
    {'0', {1, 3}},
    {'A', {2, 3}},
};

const KEYPOS dirkeypos = {
    {'^', {1, 0}},
    {'A', {2, 0}},
    {'<', {0, 1}},
    {'v', {1, 1}},
    {'>', {2, 1}},
};

KEYMAP build_key_map(const std::unordered_map<char, std::pair<int, int>> &keypos, bool isnum);

const KEYMAP numkeymap = build_key_map(numkeypos, true);
const KEYMAP dirkeymap = build_key_map(dirkeypos, false);

std::vector<std::string> get_key_seq(char fromkey, char tokey, const KEYPOS &keypos, bool isnum)
{
    if (fromkey == tokey)
    {
        return {""};
    }
    std::pair<int, int> frompos = keypos.at(fromkey);
    std::pair<int, int> topos = keypos.at(tokey);
    int xdiff = topos.first - frompos.first;
    int ydiff = topos.second - frompos.second;
    const std::string DOWN = std::string(abs(ydiff), 'v');
    const std::string UP = std::string(abs(ydiff), '^');
    const std::string RIGHT = std::string(abs(xdiff), '>');
    const std::string LEFT = std::string(abs(xdiff), '<');
    if (xdiff == 0) // same column
    {
        if (ydiff > 0)
        {
            return {DOWN};
        }
        return {UP};
    }
    if (ydiff == 0) // same row
    {
        if (xdiff > 0)
        {
            return {RIGHT};
        }
        return {LEFT};
    }
    if (ydiff < 0 && 0 < xdiff) // up right
    {
        if (!isnum && frompos.first == 0 && topos.second == 0)
        {
            return {RIGHT + UP};
        }
        return {RIGHT + UP, UP + RIGHT};
    }
    if (ydiff > 0 && 0 > xdiff) // down left
    {
        if (!isnum && frompos.second == 0 && topos.first == 0)
        {
            return {DOWN + LEFT};
        }
        return {DOWN + LEFT, LEFT + DOWN};
    }
    if (ydiff > 0 && xdiff > 0) // down right
    {
        if (isnum && frompos.first == 0 && topos.second == 3)
        {
            return {RIGHT + DOWN};
        }
        return {RIGHT + DOWN, DOWN + RIGHT};
    }
    // up left
    if (isnum && topos.first == 0 && frompos.second == 3)
    {
        return {UP + LEFT};
    }
    return {UP + LEFT, LEFT + UP};
    return {""};
}

KEYMAP build_key_map(const std::unordered_map<char, std::pair<int, int>> &keypos, bool isnum)
{
    KEYMAP keymap;
    for (const auto &[fromkey, _] : keypos)
    {
        for (const auto &[tokey, _] : keypos)
        {
            keymap[{fromkey, tokey}] = get_key_seq(fromkey, tokey, keypos, isnum);
        }
    }
    return keymap;
}

void build_seq(const std::string &keys, const int index, const char prev_key, const std::string &curr_path, std::vector<std::string> &result, const KEYMAP &keymap)
{
    if (index == keys.size())
    {
        result.push_back(curr_path);
        return;
    }
    std::string pair;
    for (auto &&path : keymap.at(
             {prev_key, keys[index]}))
    {
        build_seq(keys, index + 1, keys[index], curr_path + path + "A", result, keymap);
    }
}

long long shortest_seq(const std::string &keys, const int depth);

long long min_shortest_seq(const std::vector<std::string> &seqlist, const int depth)
{
    std::vector<long long> minseqs;
    for (const std::string seq : seqlist)
    {
        minseqs.push_back(shortest_seq(seq, depth));
    }
    return *std::min_element(minseqs.begin(), minseqs.end());
}

long long shortest_seq(const std::string &keys, const int depth)
{
    if (depth == 0)
    {
        return keys.size();
    }
    static std::unordered_map<std::pair<std::string, int>, long long> cache;
    if (cache.find({keys, depth}) != cache.end())
    {
        return cache.at({keys, depth});
    }
    long long total = 0;
    std::stringstream ss(keys);
    std::string subkey;
    while (std::getline(ss, subkey, 'A'))
    {
        std::vector<std::string> seqlist;
        build_seq(subkey + "A", 0, 'A', "", seqlist, dirkeymap);
        total += min_shortest_seq(seqlist, depth - 1);
    }
    cache[{keys, depth}] = total;
    return total;
}

long long solve(const std::vector<std::string> &codes, const int depth)
{
    long long total = 0;

    for (std::string code : codes)
    {
        std::vector<std::string> seqlist;
        build_seq(code, 0, 'A', "", seqlist, numkeymap);
        long long m = min_shortest_seq(seqlist, depth);
        total += stoll(code) * m;
    }
    return total;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<std::string> codes;
    while (std::getline(std::cin, line))
    {
        codes.push_back(line);
    }
    std::cout << solve(codes, 2) << std::endl;
    std::cout << solve(codes, 25) << std::endl;
}