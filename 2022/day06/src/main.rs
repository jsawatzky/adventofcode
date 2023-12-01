use std::{fs, collections::HashSet};

use circular_queue::CircularQueue;

fn part1(input: &str) {
    let mut queue = CircularQueue::with_capacity(4);
    for (i, c) in input.chars().enumerate() {
        queue.push(c);
        if queue.is_full() {
            let mut uniq = HashSet::new();
            if queue.iter().all(move |x| uniq.insert(x)) {
                println!("part1: {}", i+1);
                return;
            }
        }
    }
    println!("part1: {}", 0)
}

fn part2(input: &str) {
    let mut queue = CircularQueue::with_capacity(14);
    for (i, c) in input.chars().enumerate() {
        queue.push(c);
        if queue.is_full() {
            let mut uniq = HashSet::new();
            if queue.iter().all(move |x| uniq.insert(x)) {
                println!("part2: {}", i+1);
                return;
            }
        }
    }
    println!("part2: {}", 0)
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