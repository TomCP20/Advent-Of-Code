using System.Linq;
using System.Text.RegularExpressions;

List<string> lines = [];
while (Console.ReadLine() is string line) { lines.Add(line); }
int row = lines[0].Length + 6;
string input = string.Join("", lines.Select(line => "..." + line + "...")) ;
int[] offsets = [0, row, row-1, row-2];
Console.WriteLine(offsets.Select(o => new Regex(@"(?=(X.{" + o + @"}M.{" + o + @"}A.{" + o + @"}S|S.{" + o + @"}A.{" + o + @"}M.{" + o + @"}X))").Matches(input).Count).Sum());
string[] orientation = ["MMSS", "MSMS", "SMSM", "SSMM"];
int n = row-2;
Console.WriteLine(orientation.Select(o => new Regex(@"(?=(" + o[0] + @"." + o[1] + @".{" + n + @"}A.{" + n + @"}" + o[2] + @"." + o[3] + @"))").Matches(input).Count).Sum());