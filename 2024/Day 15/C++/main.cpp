#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

template <typename T, typename U>
std::pair<T, U> operator+(const std::pair<T, U> &l, const std::pair<T, U> &r)
{
    return {l.first + r.first, l.second + r.second};
}

bool has(std::vector<std::pair<int, int>> &vec, std::pair<int, int> &val)
{
    return std::find(vec.begin(), vec.end(), val) != vec.end();
}

bool move_box1(std::pair<int, int> &box_pos, std::pair<int, int> &dir, std::vector<std::pair<int, int>> &boxes, std::vector<std::pair<int, int>> &walls)
{
    std::pair<int, int> npos = box_pos + dir;
    if (has(walls, npos) || (has(boxes, npos) && !move_box1(npos, dir, boxes, walls)))
    {
        return false;
    }
    std::vector<std::pair<int, int>>::iterator it = std::find(boxes.begin(), boxes.end(), box_pos);
    if (it != boxes.end())
    {
        *it = npos;
    }
    else
    {
        std::cout << "error\n";
    }
    return true;
}

int main(int argc, char *argv[])
{
    std::string line;
    bool isMaze = true;
    std::string moves;
    int y = 0;
    std::vector<std::pair<int, int>> walls1;
    std::vector<std::pair<int, int>> boxes1;
    std::pair<int, int> robot1;
    while (std::getline(std::cin, line))
    {
        if (line == "")
        {
            isMaze = false;
        }
        else if (isMaze)
        {
            for (int x = 0; x < line.length(); x++)
            {
                switch (line[x])
                {
                case '#':
                    walls1.push_back({x, y});
                    break;
                case 'O':
                    boxes1.push_back({x, y});
                    break;
                case '@':
                    robot1 = {x, y};
                    break;
                default:
                    break;
                }
            }
            y++;
        }
        else
        {
            moves += line;
        }
    }

    const std::map<char, std::pair<int, int>> dirs = {{'^', {0, -1}}, {'v', {0, 1}}, {'<', {-1, 0}}, {'>', {1, 0}}};

    for (char move : moves)
    {
        std::pair<int, int> dir = dirs.at(move);
        std::pair<int, int> npos = robot1 + dir;
        if (has(boxes1, npos))
        {
            if (move_box1(npos, dir, boxes1, walls1))
            {
                robot1 = npos;
            }
        }
        else if (!has(walls1, npos))
        {
            robot1 = npos;
        }
    }

    int score1 = 0;
    for (std::pair<int, int> pos : boxes1)
    {
        score1 += pos.first + 100 * pos.second;
    }
    std::cout << score1 << "\n";
}