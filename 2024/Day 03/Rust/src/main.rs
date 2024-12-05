use regex::{Match, Regex};
use std::io;

fn int_parse(str: Option<Match>) -> i32 {
    str.unwrap().as_str().parse::<i32>().unwrap()
}

fn main() {
    let input = io::stdin()
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap()
        .join("");

    let patttern1 = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    let sum1: i32 = patttern1
        .captures_iter(&input)
        .map(|m| int_parse(m.get(1)) * int_parse(m.get(2)))
        .sum();
    println!("{:?}", sum1);

    let patttern2 = Regex::new(r"do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)").unwrap();
    let mut enabled = true;
    let mut sum2 = 0;
    for m in patttern2.captures_iter(&input) {
        let s = m.get(0).unwrap().as_str();
        if s == "do()" {
            enabled = true;
        } else if s == "don't()" {
            enabled = false;
        } else if enabled {
            sum2 += int_parse(m.get(1)) * int_parse(m.get(2));
        }
    }
    println!("{:?}", sum2);
}
