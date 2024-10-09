use leetcode::*;
use std::{env, process};

fn main() {
    let problem = env::args().nth(1).unwrap_or_else(|| {
        println!("Usage: leetcode <problem number>");
        std::process::exit(1);
    });

    match problem.to_lowercase().trim() {
        "1331" => p1331::main(),
        "debug" => template::main(),
        _ => {
            println!("Problem not found");
            process::exit(1);
        }
    }
}
