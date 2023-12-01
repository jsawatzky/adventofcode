use std::fs;

fn part1(input: &str) {
    let mut count = 0;
    for line in input.lines() {
        let (e1, e2) = line.split_once(",").unwrap();
        let (e1r1, e1r2) = e1.split_once("-").unwrap();
        let (e2r1, e2r2) = e2.split_once("-").unwrap();
        let e1r1: u32 = e1r1.parse().expect("must be int");
        let e1r2: u32 = e1r2.parse().expect("must be int");
        let e2r1: u32 = e2r1.parse().expect("must be int");
        let e2r2: u32 = e2r2.parse().expect("must be int");

        if (e1r1 >= e2r1 && e1r2 <= e2r2) || (e2r1 >= e1r1 && e2r2 <= e1r2) {
            count += 1
        }
    }
    println!("part1: {}", count)
}

fn part2(input: &str) {
    let mut count = 0;
    for line in input.lines() {
        let (e1, e2) = line.split_once(",").unwrap();
        let (e1r1, e1r2) = e1.split_once("-").unwrap();
        let (e2r1, e2r2) = e2.split_once("-").unwrap();
        let e1r1: u32 = e1r1.parse().expect("must be int");
        let e1r2: u32 = e1r2.parse().expect("must be int");
        let e2r1: u32 = e2r1.parse().expect("must be int");
        let e2r2: u32 = e2r2.parse().expect("must be int");

        if (e1r1 <= e2r2 && e1r2 >= e2r1) || (e2r1 <= e1r2 && e2r2 >= e1r1) {
            count += 1
        }
    }
    println!("part2: {}", count)
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