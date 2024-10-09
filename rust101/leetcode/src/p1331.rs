// https://leetcode.com/problems/rank-transform-of-an-array/

use std::collections::HashMap;

pub fn main() {
    // entrypoint here
    println!("{:?}", Solution::array_rank_transform(vec![40, 10, 20, 30]));
    println!("{:?}", Solution::array_rank_transform(vec![100, 100, 100]));
    println!(
        "{:?}",
        Solution::array_rank_transform(vec![37, 12, 28, 9, 100, 56, 80, 5, 12])
    );
}

struct Solution;
impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let mut nums = arr.clone();
        nums.sort();
        nums.dedup();

        let map: HashMap<i32, i32> = nums
            .into_iter()
            .enumerate()
            .map(|(rank, n)| (n, rank as i32 + 1))
            .collect();

        arr.iter().map(|n| map[n]).collect()
    }
}

#[cfg(test)]
mod tests {

    //     use super::*;

    //     #[test]
    //     fn test1() {
    //         assert_eq!(Solution::search(vec![-1, 0, 3, 5, 9, 12], 9), 4);
    //     }

    //     #[test]
    //     fn test2() {
    //         assert_eq!(Solution::search(vec![-1, 0, 3, 5, 9, 12], 2), -1);
    //     }
}
