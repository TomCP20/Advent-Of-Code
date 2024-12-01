fn main() {
    let lines = std::io::stdin().lines().collect::<Result<Vec<String>, std::io::Error>>().unwrap().join("\n");
    println!("{}", lines);
}
