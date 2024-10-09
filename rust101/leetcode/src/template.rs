use std::cmp::Ordering;

pub fn main() {
    // entrypoint here
    println!("{}", Solution::search(vec![-1, 0, 3, 5, 9, 12], 9));
    println!("{}", Solution::search(vec![-1, 0, 3, 5, 9, 12], 2));
}

struct Solution;
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;

        loop {
            let mid = (left + right) / 2;
            match nums[mid].cmp(&target) {
                Ordering::Equal => break mid as i32,
                Ordering::Greater => right = mid - 1,
                Ordering::Less => left = mid + 1,
            }
            if left >= right {
                break -1;
            }
        }
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::search(vec![-1, 0, 3, 5, 9, 12], 9), 4);
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::search(vec![-1, 0, 3, 5, 9, 12], 2), -1);
    }
}
