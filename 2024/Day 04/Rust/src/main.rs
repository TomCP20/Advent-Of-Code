use regex::Regex;
use std::io;

fn overlapping(pattern: &str, input: &str) -> usize {
    println!("{}", pattern);
    let mut count = 0;
    let mut start = 0;
    let regex = Regex::new(pattern).unwrap();
    while start < input.len() {
        let m = regex.find_at(input, start);
        match m {
            None => break,
            Some(ms) => {
                count += 1;
                start = ms.start() + 1;
            }
        }
    }
    count
}

fn get_pattern_1(offset: usize) -> String {
    let o = &(r".{".to_owned() + &offset.to_string() + r"}");
    r"X".to_owned() + o + r"M" + o + r"A" + o + r"S|S" + o + r"A" + o + r"M" + o + r"X"
}

fn get_pattern_2(perm: (&str, &str, &str, &str), n: &str) -> String {
    perm.0.to_owned() + r"." + perm.1 + r".{" + n + r"}A.{" + n + r"}" + perm.2 + r"." + perm.3
}

fn main() {
    let lines = io::stdin()
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap();
    let row = lines[0].len() + 6;
    let input = lines
        .into_iter()
        .map(|line| "...".to_owned() + &line + "...")
        .collect::<Vec<String>>()
        .join("");
    let count1: usize = [0, row, row - 1, row - 2]
        .into_iter()
        .map(|o| overlapping(&(get_pattern_1(o)), &input))
        .sum();
    println!("{}", count1);
    let count2: usize = [
        ("M", "M", "S", "S"),
        ("M", "S", "M", "S"),
        ("S", "M", "S", "M"),
        ("S", "S", "M", "M"),
    ]
    .into_iter()
    .map(|p| overlapping(&get_pattern_2(p, &(row - 2).to_string()), &input))
    .sum();
    println!("{}", count2);
}
