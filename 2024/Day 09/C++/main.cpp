#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

const int EMPTY = -1;

long long checksum(std::vector<int> &disk)
{
    long long s = 0;
    for (int i = 0; i < disk.size(); i++)
    {

        if (disk[i] != EMPTY)
        {
            s += i * disk[i];
        }
    }
    return s;
}

long long part1(std::vector<int> disk)
{
    int l = 0;
    int r = disk.size() - 1;
    while (l < r)
    {
        if (disk[r] == EMPTY)
        {
            r--;
        }
        else if (disk[l] != EMPTY)
        {
            l++;
        }
        else
        {
            disk[l] = disk[r];
            disk[r] = EMPTY;
        }
    }
    return checksum(disk);
}

long long part2(std::vector<int> disk, int max_id)
{
    for (int file_id = max_id; file_id >= 0; file_id--)
    {
        int file_size = std::count(disk.begin(), disk.end(), file_id);
        int file_start = std::find(disk.begin(), disk.end(), file_id) - disk.begin();
        int space_size = 0;
        int space_start = -1;
        for (int i = 0; i < file_start; i++)
        {
            if (disk[i] != EMPTY)
            {
                space_size = 0;
                space_start = -1;
            }
            else
            {
                space_size++;
                if (space_start == -1)
                {
                    space_start = i;
                }
                if (space_size >= file_size)
                {
                    for (int j = 0; j < file_size; j++)
                    {
                        disk[space_start + j] = disk[file_start + j];
                        disk[file_start + j] = EMPTY;
                    }
                    break;
                }
            }
        }
    }

    return checksum(disk);
}

int main(int argc, char *argv[])
{
    std::string line;
    std::getline(std::cin, line);
    std::vector<int> disk;
    for (int i = 0; i < line.size(); i++)
    {
        int v = i % 2 == 0 ? i / 2 : EMPTY;
        for (int j = 0; j < line[i] - '0'; j++)
        {
            disk.push_back(v);
        }
    }
    std::cout << part1(disk) << "\n";
    std::cout << part2(disk, (line.size() - 1) / 2) << "\n";
}