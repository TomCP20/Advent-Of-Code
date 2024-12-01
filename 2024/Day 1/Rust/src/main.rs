use itertools::Itertools;
use std::{collections::HashMap, convert::TryFrom};

fn main() {
    let lines = std::io::stdin().lines().collect::<Result<Vec<String>, std::io::Error>>().unwrap();
    let rows: Vec<Vec<&str>> = lines.iter().map(|x| x.split("   ").collect::<Vec<_>>()).collect();
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    for row in rows {
        left.push(row[0].parse().unwrap());
        right.push(row[1].parse().unwrap());
    }
    left.sort();
    right.sort();
    let result1: i32 = left.iter().zip(right.iter()).map(|(l, r)| i32::abs(l-r)).sum();
    println!("{}", result1);
    let counter = right.into_iter().counts();
    let result2: i32 = left.into_iter().map(|x| x*get_count(&counter, x)).sum();
    println!("{}", result2);
}

fn get_count(counter: &HashMap<i32, usize>, key: i32) -> i32 {
    return match counter.get(&key) {
        None => 0,
        Some(count) => i32::try_from(count.clone()).unwrap(),
    };
}