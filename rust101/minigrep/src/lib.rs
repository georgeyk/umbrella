use std::env;
use std::error::Error;
use std::fs;

pub struct Config {
    query: String,
    file_path: String,
    ignore_case: bool,
}

impl Config {
    pub fn build(args: &Vec<String>) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("Not enough arguments");
        }

        match (args[1].as_str(), args.len()) {
            ("-i", 4) => Ok(Config {
                query: args[2].clone(),
                file_path: args[3].clone(),
                ignore_case: true,
            }),
            ("-i", _) => return Err("Invalid arguments"),
            (query, 3) => Ok(Config {
                query: query.to_string(),
                file_path: args[2].clone(),
                ignore_case: env::var("IGNORE_CASE").is_ok(),
            }),
            _ => return Err("Invalid arguments"),
        }
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;
    for line in search(&config.query, &contents, config.ignore_case) {
        println!("{line}");
    }

    Ok(())
}

fn search<'a>(query: &str, content: &'a str, ignore_case: bool) -> Vec<&'a str> {
    let mut res = Vec::new();
    for line in content.lines() {
        if (ignore_case && line.to_lowercase().contains(&query.to_lowercase()))
            || line.contains(query)
        {
            res.push(line);
        }
    }

    res
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents, false)
        );
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Trust me.";

        assert_eq!(vec!["Rust:", "Trust me."], search(query, contents, true));
    }
}
