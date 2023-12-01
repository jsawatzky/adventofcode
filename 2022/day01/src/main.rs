use std::fs;

fn part1(input: &str) {
    let input: Vec<&str> = input.split("\n").collect();
    let mut max = 0;
    let mut sum = 0;
    for line in input {
        match line {
            "" => {
                if sum > max {
                    max = sum;
                }
                sum = 0;
            }
            val => {
                let val: u32 = val.parse().expect("must be an int");
                sum = sum + val;
            }
        }
    }
    println!("part1: {}", max)
}

fn part2(input: &str) {
    let input: Vec<&str> = input.split("\n").collect();
    let mut sums = Vec::new();
    let mut sum = 0;
    for line in input {
        match line {
            "" => {
                sums.push(sum);
                sum = 0;
            }
            val => {
                let val: u32 = val.parse().expect("must be an int");
                sum = sum + val;
            }
        }
    }
    sums.sort();
    sums.reverse();
    println!("part2: {}", sums[0] + sums[1] + sums[2])
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("input.txt should exist");
    part1(&input);
    part2(&input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        let input = fs::read_to_string("test.txt").expect("test.txt should exist");
        part1(&input);
        part2(&input);
    }
}