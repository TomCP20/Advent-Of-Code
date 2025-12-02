static int part1(List<(int, int)> rotations)
{
    int dial = 50;
    int password = 0;
    foreach (var (direction, distance) in rotations)
    {
        dial = (dial + direction * distance) % 100;
        if (dial == 0) { password++; }
    }
    return password;
}

static int part2(List<(int, int)> rotations)
{
    int dial = 50;
    int password = 0;
    foreach (var (direction, distance) in rotations)
    {
        for (int i = 0; i < distance; i++)
        {
            dial = (dial + direction) % 100;
            if (dial == 0) { password++; }
        }
    }
    return password;
}

List<(int, int)> rotations = [];
while (Console.ReadLine() is string line)
{
    int direction = line[0] == 'R' ? 1 : -1;
    int distance = Int32.Parse(line.Substring(1));
    rotations.Add((direction, distance));
}

Console.WriteLine(part1(rotations));
Console.WriteLine(part2(rotations));