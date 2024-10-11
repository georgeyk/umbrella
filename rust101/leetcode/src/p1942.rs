// use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub fn main() {
    // entrypoint here
    println!(
        "{}",
        Solution::smallest_chair(vec![vec![1, 4], vec![2, 3], vec![4, 6]], 1)
    );

    println!(
        "{}",
        Solution::smallest_chair(vec![vec![3, 10], vec![1, 5], vec![2, 6]], 0)
    );
}

struct Solution;
impl Solution {
    pub fn smallest_chair(times: Vec<Vec<i32>>, target_friend: i32) -> i32 {
        let target = target_friend as usize;
        let mut next_chair = 0;
        let mut indexes = Vec::from_iter(0..times.len());
        indexes.sort_unstable_by_key(|&k| times[k][0]);

        let mut occ_chairs = BinaryHeap::<(i32, i32)>::new();
        let mut avail_chairs = BinaryHeap::new();
        for i in indexes {
            let arrive = times[i][0];
            let leave = times[i][1];

            while let Some(&(leave, chair)) = occ_chairs.peek() {
                if arrive < -leave {
                    break;
                }
                occ_chairs.pop();
                avail_chairs.push(-chair);
            }

            if avail_chairs.is_empty() {
                avail_chairs.push(-next_chair);
                next_chair += 1;
            }

            let chair = avail_chairs.pop().unwrap();
            occ_chairs.push((-leave, -chair));

            if i == target {
                return chair.abs();
            }
        }
        -1
    }
}

#[cfg(test)]
mod tests {

    // use super::*;

    // #[test]
    // fn test1() {
    //     assert_eq!(Solution::search(vec![-1, 0, 3, 5, 9, 12], 9), 4);
    // }

    // #[test]
    // fn test2() {
    //     assert_eq!(Solution::search(vec![-1, 0, 3, 5, 9, 12], 2), -1);
    // }
}
