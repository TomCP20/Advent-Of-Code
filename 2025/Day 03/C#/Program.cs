
static long maxJoltage(List<int> bank, int digits)
{
    if (digits == 1)
    {
        return bank.Max();
    }
    digits--;
    int l = bank.Count;
    int digit = bank.Take(l - digits).Max();
    return digit * (long)Math.Pow(10, digits) + maxJoltage([.. bank.TakeLast(l - bank.IndexOf(digit) - 1)], digits);
}

List<List<int>> banks = [];
while (Console.ReadLine() is string line)
{
    List<int> bank = [.. line.Select(c => int.Parse(c.ToString()))];
    banks.Add(bank);
}

Console.WriteLine(banks.Select(bank => maxJoltage(bank, 2)).Sum());
Console.WriteLine(banks.Select(bank => maxJoltage(bank, 12)).Sum());
