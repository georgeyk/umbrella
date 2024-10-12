use leetcode::*;
use std::{env, process};

fn main() {
    let problem = env::args().nth(1).unwrap_or_else(|| {
        println!("Usage: leetcode <problem number>");
        std::process::exit(1);
    });

    match problem.to_lowercase().trim() {
        "962" => p962::main(),
        "1331" => p1331::main(),
        "1942" => p1942::main(),
        "2406" => p2406::main(),
        "debug" => template::main(),
        _ => {
            println!("Problem not found");
            process::exit(1);
        }
    }
}
