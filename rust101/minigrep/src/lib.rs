use std::env;
use std::error::Error;
use std::fs;

pub struct Config {
    query: String,
    file_path: String,
    ignore_case: bool,
}

impl Config {
    pub fn build(mut args: impl Iterator<Item = String>) -> Result<Config, &'static str> {
        args.next();

        let mut query = match args.next() {
            Some(arg) => arg,
            None => return Err("Missing arguments"),
        };

        let ignore_case = query == "-i" || env::var("IGNORE_CASE").is_ok();

        if query == "-i" {
            match args.next() {
                Some(arg) => query = arg,
                None => return Err("Missing arguments"),
            }
        }

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Missing arguments"),
        };

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    search(
        &config.query,
        &fs::read_to_string(config.file_path)?,
        config.ignore_case,
    )
    .iter()
    .for_each(|line| println!("{line}"));

    Ok(())
}

fn search<'a>(query: &str, content: &'a str, ignore_case: bool) -> Vec<&'a str> {
    content
        .lines()
        .filter(|line| {
            ignore_case && line.to_lowercase().contains(&query.to_lowercase())
                || line.contains(&query)
        })
        .collect()
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
