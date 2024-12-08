(int, int)[] dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)];

IEnumerable<((int, int), int)> traverse(((int, int), int) initial_guard_state, HashSet<(int, int)> obstacles, int w, int h)
{
    ((int, int) guard_pos, int turns) = initial_guard_state;
    while (0 <= guard_pos.Item1 && guard_pos.Item1 < w && 0 <= guard_pos.Item2 && guard_pos.Item2 < h)
    {
        yield return (guard_pos, turns);
        (int, int) guard_dir = dirs[turns];
        (int, int) next_guard_pos = (guard_dir.Item1 + guard_pos.Item1, guard_dir.Item2 + guard_pos.Item2);
        if (obstacles.Contains(next_guard_pos))
        {
            turns = (turns + 1) % 4;
        }
        else
        {
            guard_pos = next_guard_pos;
        }
    }
}

IEnumerable<(((int, int), int), (int, int))> get_obstacle_pos(((int, int), int) initial_guard_state, HashSet<(int, int)> obstacles, int w, int h)
{
    ((int, int), int)[] path = traverse(initial_guard_state, obstacles, w, h).ToArray();
    HashSet<(int, int)> checked_posistions = [];
    foreach (var (new_start, (obstacle_pos, _)) in path.Zip(path.Skip(1)))
    {
        if (!checked_posistions.Contains(obstacle_pos))
        {
            checked_posistions.Add(obstacle_pos);
            yield return (new_start, obstacle_pos);
        }
    }
}

bool detect_loop(((int, int), int) initial_guard_state, HashSet<(int, int)> obstacles, int w, int h)
{
    HashSet<((int, int), int)> state_set = [];
    foreach (((int, int), int) state in traverse(initial_guard_state, obstacles, w, h))
    {
        if (state_set.Contains(state))
        {
            return true;
        }
        state_set.Add(state);
    }
    return false;
}

List<string> lines = [];
while (Console.ReadLine() is string line) { lines.Add(line); }
HashSet<(int, int)> obstacles = [];
((int, int), int) guard_state = ((-1, -1), -1);
int w = lines[0].Length;
int h = lines.Count;
for (int y = 0; y < h; y++)
{
    for (int x = 0; x < w; x++)
    {
        switch (lines[y][x])
        {
            case '#':
                obstacles.Add((x, y));
                break;
            case '^':
                guard_state = ((x, y), 0);
                break;
            case '>':
                guard_state = ((x, y), 1);
                break;
            case 'v':
                guard_state = ((x, y), 2);
                break;
            case '<':
                guard_state = ((x, y), 3);
                break;
            default:
                break;
        } 
    }
}

Console.WriteLine(traverse(guard_state, obstacles, w, h).Select((x) => x.Item1).ToHashSet().Count);
Console.WriteLine(get_obstacle_pos(guard_state, obstacles, w, h).Where((x) => detect_loop(x.Item1, [.. obstacles, x.Item2], w, h)).Count());