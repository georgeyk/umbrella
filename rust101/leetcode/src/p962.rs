pub fn main() {
    // entrypoint here
    Solution::max_width_ramp(vec![2, 0, 0, 0, 0, 0, 0, 3]);
}

struct Solution;
impl Solution {
    pub fn max_width_ramp(nums: Vec<i32>) -> i32 {
        let mut stack = Vec::<usize>::new();

        for i in 0..nums.len() {
            if stack.is_empty() || nums[*stack.last().unwrap()] > nums[i] {
                stack.push(i);
            }
        }

        let mut ramp = 0;
        for j in (0..nums.len()).rev() {
            while !stack.is_empty() && nums[*stack.last().unwrap()] <= nums[j] {
                let top = stack.pop().unwrap();
                ramp = std::cmp::max(ramp, j - top);
            }
        }

        ramp as i32
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::max_width_ramp(vec![6, 0, 8, 2, 1, 5]), 4);
    }

    #[test]
    fn test2() {
        assert_eq!(
            Solution::max_width_ramp(vec![9, 8, 1, 0, 1, 9, 4, 0, 4, 1]),
            7
        );
    }

    #[test]
    fn test3() {
        assert_eq!(Solution::max_width_ramp(vec![2, 2, 1]), 1);
    }
}
