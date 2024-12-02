List<string> lines = [];
while (Console.ReadLine() is string line)
{
    lines.Add(line);
}
List<List<int>> lists = lines.Select(x => x.Split("   ").Select(x => int.Parse(x)).ToList()).ToList();
List<int> left = [.. lists.Select(x => x[0]).Order()];
List<int> right = [.. lists.Select(x => x[1]).Order()];

Console.WriteLine(left.Zip(right, (l, r) => Math.Abs(l - r)).Sum());
Dictionary<int, int> count = right.GroupBy(x => x).ToDictionary(g => g.Key, g => g.Count());
int sum = left.Where(count.ContainsKey).Select(x => x*count[x]).Sum();
Console.WriteLine(sum);