fn trim_me(input: &str) -> &str {
    let mut left = 0;
    let mut right = input.len() - 1;
    while left < right {
        if input.chars().nth(left).unwrap() == ' ' {
            left += 1;
        }
        else {
            break
        }
    }
    while right > left {
        if input.chars().nth(right).unwrap() == ' ' {
            right -= 1;
        }
        else {
            break
        }
    }

    &input[left..=right]
}

fn compose_me(input: &str) -> String {
    format!("{input} world!")
}

fn replace_me(input: &str) -> String {
    let mut words = Vec::<&str>::new();
    for word in input.split_whitespace() {
        match word {
            "cars" => words.push("balloons"),
            _ => words.push(word),
        }
    }

    words.join(" ")
}

fn main() {
    // You can optionally experiment here.
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn trim_a_string() {
        assert_eq!(trim_me("Hello!     "), "Hello!");
        assert_eq!(trim_me("  What's up!"), "What's up!");
        assert_eq!(trim_me("   Hola!  "), "Hola!");
    }

    #[test]
    fn compose_a_string() {
        assert_eq!(compose_me("Hello"), "Hello world!");
        assert_eq!(compose_me("Goodbye"), "Goodbye world!");
    }

    #[test]
    fn replace_a_string() {
        assert_eq!(
            replace_me("I think cars are cool"),
            "I think balloons are cool",
        );
        assert_eq!(
            replace_me("I love to look at cars"),
            "I love to look at balloons",
        );
    }
}
