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

const std::string cols = "wubrg";
const int cols_num = 5;

struct Trie
{
    Trie *children[cols_num];
    bool end;
    Trie()
    {
        end = false;
        for (int i = 0; i < cols_num; i++)
        {
            children[i] = nullptr;
        }
    }
};

void insert_towl(Trie *root, const std::string &towl)
{
    Trie *ptr = root;
    for (char c : towl)
    {
        int index = cols.find(c);
        if (ptr->children[index] == nullptr)
        {
            Trie *new_node = new Trie();
            ptr->children[index] = new_node;
        }

        ptr = ptr->children[index];
    }
    ptr->end = true;
}

unsigned long long ways_of_forming_design(Trie *root, const std::string &design)
{
    int n = design.size();
    std::vector<unsigned long long> count(n, 0);

    for (int i = 0; i < n; i++)
    {
        Trie *ptr = root;
        for (int j = i; j >= 0; j--)
        {
            int index = cols.find(design[j]);
            if (ptr->children[index] == nullptr)
            {
                break;
            }
            ptr = ptr->children[index];
            if (ptr->end)
            {
                if (j > 0)
                {
                    count[i] += count[j - 1];
                }
                else
                {
                    count[i] += 1;
                }
            }
        }
    }
    return count[n - 1];
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
    std::vector<std::string> possible_designs = generate_possible_designs(towls, designs);
    std::cout << possible_designs.size() << "\n";

    Trie *root = new Trie();
    for (std::string t : towls)
    {
        std::reverse(t.begin(), t.end());
        insert_towl(root, t);
    }
    unsigned long long s = 0;
    for (auto &&d : possible_designs)
    {
        s += ways_of_forming_design(root, d);
    }
    std::cout << s << "\n";
}