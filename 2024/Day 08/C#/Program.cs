List<string> lines = [];
while (Console.ReadLine() is string line) { lines.Add(line); }
int h = lines.Count;
int w = lines[0].Length;

Dictionary<char, List<(int, int)>> antennas = [];

foreach (var (line, x) in lines.Select((line, x) => (line, x)))
{
    foreach (var (c, y) in line.Select((c, y) => (c, y)))
    {
        if (c != '.')
        {
            if (antennas.TryGetValue(c, out List<(int, int)>? l))
            {
                l.Add((x, y));
            }
            else
            {
                antennas[c] = [(x, y)];
            }
        }
    }
}

HashSet<(int, int)> antinodes1 = [];
foreach (var (_, locations) in antennas)
{
    foreach (var (a, b) in locations.SelectMany(a => locations.Where((b) => a != b).Select(b => (a, b))))
    {
        (int, int) pos = (2*a.Item1-b.Item1, 2*a.Item2-b.Item2);
        if (0 <= pos.Item1 && pos.Item1 < w && 0 <= pos.Item2 && pos.Item2 < h)
        {
            antinodes1.Add(pos);
        }
    }
}
Console.WriteLine(antinodes1.Count);

HashSet<(int, int)> antinodes2 = [];
foreach (var (_, locations) in antennas)
{
    foreach (var (a, b) in locations.SelectMany(a => locations.Where((b) => a != b).Select(b => (a, b))))
    {
        (int, int) diff = (a.Item1-b.Item1, a.Item2-b.Item2);
        (int, int) pos = a;
        while (0 <= pos.Item1 && pos.Item1 < w && 0 <= pos.Item2 && pos.Item2 < h)
        {
            antinodes2.Add(pos);
            pos = (pos.Item1+diff.Item1, pos.Item2+diff.Item2);
        }
    }
}
Console.WriteLine(antinodes2.Count);