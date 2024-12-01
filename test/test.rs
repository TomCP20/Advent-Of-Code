fn main() {
    let lines = std::io::stdin().lines();
    for line in lines {
        println!("{}", line.unwrap());
    }
}
