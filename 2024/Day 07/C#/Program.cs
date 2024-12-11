(long, long[]) parseline(string line)
{
    string[] split = line.Split(": ");
    long val = long.Parse(split[0]);
    long[] nums = split[1].Split(" ").Select(long.Parse).ToArray();
    return (val, nums);
}

bool check(long val, long[] nums, bool part2)
{
    if (nums.Length == 1)
    {
        return val == nums[0];
    }
    long[] next_nums = new long[nums.Length - 1];
    Array.Copy(nums, 2, next_nums, 1, nums.Length - 2);
    next_nums[0] = nums[0] + nums[1];
    if (check(val, next_nums, part2))
    {
        return true;
    }
    next_nums[0] = nums[0] * nums[1];
    if (check(val, next_nums, part2))
    {
        return true;
    }
    if (part2)
    {
        next_nums[0] = (nums[0] * (long)Math.Pow(10, (long)Math.Log10(nums[1]) + 1) ) + nums[1];
        if (check(val, next_nums, part2))
        {
            return true;
        }
    }
    return false;
}

List<string> lines = [];
while (Console.ReadLine() is string line) { lines.Add(line); }
(long, long[])[] input = lines.Select(parseline).ToArray();
Console.WriteLine(input.Where(tup => check(tup.Item1, tup.Item2, false)).Select(tup => tup.Item1).Sum());
Console.WriteLine(input.Where(tup => check(tup.Item1, tup.Item2, true)).Select(tup => tup.Item1).Sum());