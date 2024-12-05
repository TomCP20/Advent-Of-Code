use std::io;

fn is_safe(report: &[i32]) -> bool {
    let differences: Vec<i32> = report
        .iter()
        .zip(report.iter().skip(1))
        .map(|(a, b)| b - a)
        .collect();
    let inc: bool = differences.iter().all(|x| (1 <= *x) && (*x <= 3));
    let dec: bool = differences.into_iter().all(|x| (1 <= -x) && (-x <= 3));
    inc || dec
}

fn is_safeish(report: &[i32]) -> bool {
    is_safe(report) || { 0..report.len() }.any(|i| {
        is_safe(
            &report
                .iter()
                .enumerate()
                .filter(|&(ir, _)| ir != i)
                .map(|(_, v)| *v)
                .collect::<Vec<i32>>(),
        )
    })
}

fn main() {
    let lines = io::stdin()
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap();
    let reports: Vec<Vec<i32>> = lines
        .iter()
        .map(|x| x.split(" ").map(|y| y.parse().unwrap()).collect::<Vec<_>>())
        .collect();
    let safe1 = reports.iter().filter(|report| is_safe(report)).count();
    println!("{}", safe1);
    let safe2 = reports
        .into_iter()
        .filter(|report| is_safeish(report))
        .count();
    println!("{}", safe2);
}
