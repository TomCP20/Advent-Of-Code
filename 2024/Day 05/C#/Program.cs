using System.Diagnostics.CodeAnalysis;

bool isSorted((int, int)[] rules, int[] update)
{
    foreach ((int l, int r) in rules)
    {
        if (update.Contains(l) && update.Contains(r) && !(Array.IndexOf(update, l) < Array.IndexOf(update, r)))
        {
            return false;
        }
    }
    return true;
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
    if (isSorted(rules, update))
    {
        sum1 += update[mid];
    }
    else
    {
        do
        {
            foreach ((int l, int r) in rules)
            {
                if (update.Contains(l) && update.Contains(r))
                {
                    int li = Array.IndexOf(update, l);
                    int ri = Array.IndexOf(update, r);
                    if (!(li < ri))
                    {
                        (update[ri], update[li]) = (update[li], update[ri]);
                    }
                }
            }
        } while (!isSorted(rules, update));
        sum2 += update[mid];
    }

}
Console.WriteLine(sum1);
Console.WriteLine(sum2);