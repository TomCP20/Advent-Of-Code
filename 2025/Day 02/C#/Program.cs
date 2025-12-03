using System.Text.RegularExpressions;

static partial class Program
{
    [GeneratedRegex("^(.+)\\1$")]
    private static partial Regex Regex1();
    [GeneratedRegex("^(.+)\\1+$")]
    private static partial Regex Regex2();

    static IEnumerable<long> LongRange(long start, long end)
    {
        for (long i = start; i <= end; i++)
        {
            yield return i;
        }
    }

    static long solve(List<long> ids, int part)
    {
        Regex pattern;
        if (part == 1)
        {
            pattern = Regex1();
        }
        else
        {
            pattern = Regex2();
        }

        return ids.Where(id => pattern.IsMatch(id.ToString())).Sum();
    }

    static void Main(string[] args)
    {
        string line = "";
        while (Console.ReadLine() is string l)
        {
            line += l;
        }
        List<(long start, long end)> ranges = [.. line.Split(",").Select(r =>
            {
                int i = r.IndexOf('-');
                return (long.Parse(r[..i]), long.Parse(r[(i + 1)..]));
            })];

        List<long> ids = [.. ranges.Select((r) => LongRange(r.start, r.end)).SelectMany(x => x)];

        Console.WriteLine(solve(ids, 1));
        Console.WriteLine(solve(ids, 2));
    }

}