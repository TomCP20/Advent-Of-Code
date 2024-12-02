static bool isSafe(IEnumerable<int> report)
{
    int[] differeces = report.Zip(report.Skip(1), (a, b) => a - b).ToArray();
    return Array.TrueForAll(differeces, x => 1 <= x && x <= 3) || Array.TrueForAll(differeces, x => 1 <= -x && -x <= 3);
}

List<string> lines = [];
while (Console.ReadLine() is string line) { lines.Add(line); }
int[][] reports = lines.Select(x => x.Split(" ").Select(x => int.Parse(x)).ToArray()).ToArray();

Console.WriteLine(reports.Count(isSafe));

Console.WriteLine(reports.Count(report => isSafe(report) || Enumerable.Range(0, report.Length).Any(i => isSafe(report.Where((_, ri) => ri != i)))));