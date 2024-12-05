using System.Text.RegularExpressions;

List<string> lines = [];
while (Console.ReadLine() is string line) { lines.Add(line); }
string input = string.Join("", lines);

Regex pattern1 = new(@"mul\((\d+),(\d+)\)");
Console.WriteLine(pattern1.Matches(input).Select(match => int.Parse(match.Groups[1].ToString()) * int.Parse(match.Groups[2].ToString())).Sum());

Regex pattern2 = new(@"do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)");
bool enabled = true;
int sum = 0;
foreach (GroupCollection groups in pattern2.Matches(input).Select(match => match.Groups))
{
    if (groups[0].ToString() == "do()")
    {
        enabled = true;
    }
    else if (groups[0].ToString() == "don't()")
    {
        enabled = false;
    }
    else if (enabled)
    {
        sum += int.Parse(groups[1].ToString()) * int.Parse(groups[2].ToString());
    }
}
Console.WriteLine(sum);