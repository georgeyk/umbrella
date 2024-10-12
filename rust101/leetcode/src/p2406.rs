// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/
use std::cmp::max;
use std::collections::HashMap;

pub fn main() {
    // entrypoint here
    println!(
        "{:?}",
        Solution::min_groups(vec![
            vec![5, 10],
            vec![6, 8],
            vec![1, 5],
            vec![2, 3],
            vec![1, 10]
        ])
    );
}

struct Solution;
impl Solution {
    pub fn min_groups(intervals: Vec<Vec<i32>>) -> i32 {
        let mut points = HashMap::<i32, i32>::new();

        for point in intervals {
            let start = point[0];
            let start_entry = points.entry(start).or_insert(0);
            *start_entry += 1;

            let end = point[1];
            let end_entry = points.entry(end + 1).or_insert(0);
            *end_entry -= 1;
        }

        let mut groups = 0;
        let mut counter = 0;
        let mut keys = points.keys().collect::<Vec<_>>();
        keys.sort();
        for k in keys {
            counter += points[k];
            groups = max(groups, counter);
        }

        groups
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::min_groups(vec![vec![1, 1]]), 1);
    }

    #[test]
    fn test2() {
        assert_eq!(
            Solution::min_groups(vec![vec![1, 3], vec![5, 6], vec![8, 10], vec![11, 13]]),
            1
        );
    }

    #[test]
    fn test3() {
        assert_eq!(
            Solution::min_groups(vec![
                vec![5, 10],
                vec![6, 8],
                vec![1, 5],
                vec![2, 3],
                vec![1, 10]
            ]),
            3
        );
    }
}
