#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <optional>
const std::pair<int, int> UP = {0, -1};
const std::pair<int, int> DOWN = {0, 1};
const std::pair<int, int> LEFT = {-1, 0};
const std::pair<int, int> RIGHT = {1, 0};

const std::map<char, std::pair<int, int>> DIRS = {{'^', UP}, {'v', DOWN}, {'<', LEFT}, {'>', RIGHT}};

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
    *std::find(boxes.begin(), boxes.end(), box_pos) = npos;
    return true;
}

std::optional<std::pair<int, int>> check_intersect(std::pair<int, int> &pos, std::vector<std::pair<int, int>> &boxes)
{
    if (has(boxes, pos))
    {
        return pos;
    }
    std::pair<int, int> adj = pos + LEFT;
    if (has(boxes, adj))
    {
        return adj;
    }
    return {};
}

bool move_box2(std::pair<int, int> &box_pos, std::pair<int, int> &dir, std::vector<std::pair<int, int>> &boxes, std::vector<std::pair<int, int>> &walls)
{
    std::pair<int, int> npos = box_pos + dir;
    if (dir == RIGHT) // right
    {
        std::pair<int, int> right2 = box_pos + std::make_pair(2, 0);
        if (has(walls, right2))
        {
            return false;
        }
        if (has(boxes, right2))
        {
            if (move_box2(right2, dir, boxes, walls))
            {
                *std::find(boxes.begin(), boxes.end(), box_pos) = npos;
                return true;
            }
            return false;
        }
        *std::find(boxes.begin(), boxes.end(), box_pos) = npos;
        return true;
    }
    if (dir == LEFT) // left
    {
        std::pair<int, int> left2 = box_pos + std::make_pair(-2, 0);
        if (has(walls, npos))
        {
            return false;
        }
        if (has(boxes, left2))
        {
            if (move_box2(left2, dir, boxes, walls))
            {
                *std::find(boxes.begin(), boxes.end(), box_pos) = npos;
                return true;
            }
            return false;
        }
        *std::find(boxes.begin(), boxes.end(), box_pos) = npos;
        return true;
    }
    // up or down
    std::pair<int, int> rnpos = npos + RIGHT;
    if (has(walls, npos) || has(walls, rnpos))
    {
        return false;
    }
    std::optional<std::pair<int, int>> il = check_intersect(npos, boxes);
    std::optional<std::pair<int, int>> ir = check_intersect(rnpos, boxes);

    if (il && ir)
    {
        if (*il != *ir)
        {
            std::vector<std::pair<int, int>> copy_boxes = boxes;
            if (move_box2(*il, dir, copy_boxes, walls) && move_box2(*ir, dir, copy_boxes, walls))
            {
                //boxes = std::move(copy_boxes);
                boxes.clear();
                for (std::pair<int, int> box : copy_boxes)
                {
                    boxes.push_back(box);
                }
                
                *std::find(boxes.begin(), boxes.end(), box_pos) = npos;
                return true;
            }
            return false;
        }
        if (move_box2(*il, dir, boxes, walls))
        {
            *std::find(boxes.begin(), boxes.end(), box_pos) = npos;
            return true;
        }
        return false;
    }
    if (il)
    {
        if (move_box2(*il, dir, boxes, walls))
        {
            *std::find(boxes.begin(), boxes.end(), box_pos) = npos;
            return true;
        }
        return false;
    }
    if (ir)
    {
        if (move_box2(*ir, dir, boxes, walls))
        {
            *std::find(boxes.begin(), boxes.end(), box_pos) = npos;
            return true;
        }
        return false;
    }
    *std::find(boxes.begin(), boxes.end(), box_pos) = npos;
    return true;
}

int score(std::vector<std::pair<int, int>> &boxes)
{
    int score = 0;
    for (std::pair<int, int> pos : boxes)
    {
        score += pos.first + 100 * pos.second;
    }
    return score;
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
    std::vector<std::pair<int, int>> walls2;
    std::vector<std::pair<int, int>> boxes2;
    std::pair<int, int> robot2;
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
                    walls2.push_back({2 * x, y});
                    walls2.push_back({2 * x + 1, y});
                    break;
                case 'O':
                    boxes1.push_back({x, y});
                    boxes2.push_back({2 * x, y});
                    break;
                case '@':
                    robot1 = {x, y};
                    robot2 = {2 * x, y};
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

    for (char move : moves)
    {
        std::pair<int, int> dir = DIRS.at(move);
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

    std::cout << score(boxes1) << "\n";

    for (char move : moves)
    {
        std::pair<int, int> dir = DIRS.at(move);
        std::pair<int, int> npos = robot2 + dir;
        std::optional<std::pair<int, int>> intersect = check_intersect(npos, boxes2);
        if (intersect)
        {
            if (move_box2(*intersect, dir, boxes2, walls2))
            {
                robot2 = npos;
            }
        }
        else if (!has(walls2, npos))
        {
            robot2 = npos;
        }
    }
    
    std::cout << score(boxes2) << "\n";
}