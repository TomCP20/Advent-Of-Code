use itertools::Itertools;
use std::io;

fn main() {
    let lines = io::stdin()
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap();
    let rows: Vec<Vec<&str>> = lines
        .iter()
        .map(|x| x.split("   ").collect::<Vec<_>>())
        .collect();
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    for row in rows {
        left.push(row[0].parse().unwrap());
        right.push(row[1].parse().unwrap());
    }
    left.sort();
    right.sort();
    let result1: i32 = left
        .iter()
        .zip(right.iter())
        .map(|(l, r)| i32::abs(l - r))
        .sum();
    println!("{}", result1);
    let counter = right.into_iter().counts();
    let result2: usize = left
        .into_iter()
        .map(|x| x as usize * counter.get(&x).unwrap_or(&0))
        .sum();
    println!("{}", result2);
}
