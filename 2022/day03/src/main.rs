use std::fs;

use itertools::Itertools;

fn priority(c: char) -> u32 {
    if c.is_uppercase() {
        return 27 + (c as u32 - 'A' as u32);
    } else {
        return 1 + (c as u32 - 'a' as u32)
    }
}

fn part1(input: &str) {
    let mut total = 0;
    for line in input.lines() {
        let (bag1, bag2) = line.split_at(line.len()/2);
        for c in bag1.chars() {
            if bag2.contains(c) {
                total = total + priority(c);
                break;
            }
        }
    }
    println!("part1: {}", total)
}

fn part2(input: &str) {
    let mut total = 0;
    for group in input.lines().chunks(3).into_iter() {
        let group: Vec<&str> = group.collect();
        for c in group[0].chars() {
            if group[1].contains(c) && group[2].contains(c) {
                total = total + priority(c);
                break;
            }
        }
    }
    println!("part2: {}", total)
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