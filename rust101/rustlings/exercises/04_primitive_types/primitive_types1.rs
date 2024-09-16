// Booleans (`bool`)

fn main() {
    let is_morning = true;
    if is_morning {
        println!("Good morning!");
    }

    // The value of the variable should be the negation (opposite) of `is_morning`.
    let is_evening = !is_morning;
    if is_evening {
        println!("Good evening!");
    }
}
