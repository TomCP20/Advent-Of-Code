List<string> lines = [];
while (Console.ReadLine() is string line) { lines.Add(line); }
int[][] lists = lines.Select(x => x.Split("   ").Select(x => int.Parse(x)).ToArray()).ToArray();
int[] left = [.. lists.Select(x => x[0]).Order()];
int[] right = [.. lists.Select(x => x[1]).Order()];

Console.WriteLine(left.Zip(right, (l, r) => Math.Abs(l - r)).Sum());

Dictionary<int, int> count = right.GroupBy(x => x).ToDictionary(g => g.Key, g => g.Count());
Console.WriteLine(left.Where(count.ContainsKey).Select(x => x*count[x]).Sum());