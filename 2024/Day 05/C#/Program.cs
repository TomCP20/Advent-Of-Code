static Comparison<int> getCompare((int, int)[] rules)
{
    return (a, b) =>
    {
        foreach ((int l, int r) in rules)
        {
            if (a == l && b == r) { return 1; }
            if (b == l && a == r) { return -1; }
        }
        return 0;
    };
}

List<string> lines = [];
while (Console.ReadLine() is string line) { lines.Add(line); }
string input = string.Join("\n", lines);
string[] split_input = input.Split("\n\n", 2);
(int, int)[] rules = split_input[0].Split("\n").Select(r => r.Split("|", 2).Select(int.Parse).ToArray()).Select(rule => (rule[0], rule[1])).ToArray();
int[][] updates = split_input[1].Split("\n").Select(r => r.Split(",").Select(int.Parse).ToArray()).ToArray();

int sum1 = 0;
int sum2 = 0;

foreach (int[] update in updates)
{
    int mid = (update.Length - 1) / 2;
    if (!rules.Any((rule) => update.Contains(rule.Item1) && update.Contains(rule.Item2) && !(Array.IndexOf(update, rule.Item1) < Array.IndexOf(update, rule.Item2))))
    {
        sum1 += update[mid];
    }
    else
    {
        Array.Sort(update, getCompare(rules));
        sum2 += update[mid];
    }
}
Console.WriteLine(sum1);
Console.WriteLine(sum2);