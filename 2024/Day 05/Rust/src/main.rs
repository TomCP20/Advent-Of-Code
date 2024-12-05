use std::io;
use std::cmp::Ordering;

fn get_cmp(rules: Vec<(i32, i32)>) -> impl Fn(&i32, &i32) -> Ordering {
    move |a:&i32, b:&i32|
    if rules.contains(&(*a, *b)) { Ordering::Less }
    else if rules.contains(&(*b, *a)) { Ordering::Greater }
    else {Ordering::Equal}
}

fn main() {
    let binding = io::stdin()
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap()
        .join("\n");
    let mut input = binding.split("\n\n");
    let rules: Vec<(i32, i32)> = input
        .next()
        .unwrap()
        .split("\n")
        .map(|rule| rule.split("|").map(|r| r.parse::<i32>().unwrap()))
        .map(|mut r| (r.next().unwrap(), r.next().unwrap()))
        .collect();
    let updates: Vec<Vec<i32>> = input
        .next()
        .unwrap()
        .split("\n")
        .map(|rule| rule.split(",").map(|r| r.parse::<i32>().unwrap()).collect())
        .collect();

    let cmp = get_cmp(rules.clone());

    let mut sum1 = 0;
    let mut sum2 = 0;
    for mut update in updates {
        let mid = (update.len() - 1) / 2;
        if rules
            .iter()
            .map(|(l, r)| {
                !(update.contains(l) && update.contains(r) && !(update.iter().position(|x| x == l) < update.iter().position(|x| x == r)))
            })
            .all(|x| x)
        {
            sum1 += update[mid];
        }
        else
        {
            update.sort_unstable_by(&cmp);
            sum2 += update[mid];
        }
    }
    println!("{}", sum1);
    println!("{}", sum2);
}
