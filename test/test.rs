fn main() {
    let lines: Vec<String> = std::io::stdin().lines().collect::<Result<_, _>>().unwrap();
    let s = lines.join("\n");
    println!("{}", s);
}
