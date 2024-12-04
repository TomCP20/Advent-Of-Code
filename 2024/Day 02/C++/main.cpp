#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

bool isSafe(std::vector<int> &report)
{
    std::vector<int> diffs;
    for (int i = 0; i < report.size() - 1; i++)
    {
        diffs.push_back(report[i + 1] - report[i]);
    }
    bool inc = std::all_of(diffs.begin(), diffs.end(), [](int i)
                           { return 1 <= i && i <= 3; });
    bool dec = std::all_of(diffs.begin(), diffs.end(), [](int i)
                           { return 1 <= -i && -i <= 3; });
    return inc || dec;
}

bool isSafeish(std::vector<int> &report)
{
    if (isSafe(report))
    {
        return true;
    }
    for (int i = 0; i < report.size(); i++)
    {
        std::vector<int> newReport;
        for (int j = 0; j < report.size(); j++)
        {
            if (i != j)
            {
                newReport.push_back(report[j]);
            }
        }
        if (isSafe(newReport))
        {
            return true;
        }
    }
    return false;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::vector<std::vector<int>> reports;
    while (std::getline(std::cin, line))
    {
        std::stringstream ss(line);
        std::string word;
        std::vector<int> report;
        while (ss >> word)
        {
            report.push_back(std::stoi(word));
        }
        reports.push_back(report);
    }

    int safe1 = 0;
    for (int i = 0; i < reports.size(); i++)
    {
        if (isSafe(reports[i]))
        {
            safe1++;
        }
    }
    std::cout << safe1 << std::endl;

    int safe2 = 0;
    for (int i = 0; i < reports.size(); i++)
    {
        if (isSafeish(reports[i]))
        {
            safe2++;
        }
    }
    std::cout << safe2 << std::endl;
}