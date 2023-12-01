use std::{fs, collections::HashSet};

fn part1(input: &str) {
    let mut visited: HashSet<(isize, isize)> = HashSet::new();
    let mut head: (isize, isize) = (0, 0);
    let mut tail: (isize, isize) = (0, 0);

    visited.insert(tail);

    for line in input.lines() {
        let (dir, count) = line.split_once(' ').unwrap();
        let count: isize = count.parse().unwrap();
        for _ in 0..count {
            head = match dir {
                "D" => (head.0, head.1-1),
                "U" => (head.0, head.1+1),
                "R" => (head.0+1, head.1),
                "L" => (head.0-1, head.1),
                _ => panic!("invalid direction")
            };

            tail = if head.0.abs_diff(tail.0) > 1 {
                if head.1 == tail.1 {
                    (tail.0 + 1*if head.0 < tail.0 { -1 } else { 1 }, tail.1)
                } else {
                    (tail.0 + 1*if head.0 < tail.0 { -1 } else { 1 }, tail.1 + 1*if head.1 < tail.1 { -1 } else { 1 })
                }
            } else if head.1.abs_diff(tail.1) > 1 {
                if head.0 == tail.0 {
                    (tail.0, tail.1 + 1*if head.1 < tail.1 { -1 } else { 1 })
                } else {
                    (tail.0 + 1*if head.0 < tail.0 { -1 } else { 1 }, tail.1 + 1*if head.1 < tail.1 { -1 } else { 1 })
                }
            } else {
                tail
            };
            visited.insert(tail);
        }
    }
    println!("part1: {}", visited.len())
}

fn part2(input: &str) {
    let mut visited: HashSet<(isize, isize)> = HashSet::new();
    let mut rope: Vec<(isize, isize)> = vec![(0, 0); 10];

    visited.insert(*rope.last().unwrap());

    for line in input.lines() {
        let (dir, count) = line.split_once(' ').unwrap();
        let count: isize = count.parse().unwrap();
        for _ in 0..count {
            let head = rope.get_mut(0).unwrap();
            match dir {
                "D" => { head.1 -= 1; },
                "U" => { head.1 += 1; },
                "R" => { head.0 += 1; },
                "L" => { head.0 -= 1; },
                _ => panic!("invalid direction")
            };

            for i in 1..rope.len() {
                let head = rope[i-1];
                let tail = rope.get_mut(i).unwrap();

                if head.0.abs_diff(tail.0) > 1 {
                    if head.1 == tail.1 {
                        tail.0 += 1*if head.0 < tail.0 { -1 } else { 1 };
                    } else {
                        tail.0 += 1*if head.0 < tail.0 { -1 } else { 1 };
                        tail.1 += 1*if head.1 < tail.1 { -1 } else { 1 };
                    }
                } else if head.1.abs_diff(tail.1) > 1 {
                    if head.0 == tail.0 {
                        tail.1 += 1*if head.1 < tail.1 { -1 } else { 1 };
                    } else {
                        tail.0 += 1*if head.0 < tail.0 { -1 } else { 1 };
                        tail.1 += 1*if head.1 < tail.1 { -1 } else { 1 };
                    }
                }
            }
            visited.insert(*rope.last().unwrap());
        }
    }
    println!("part2: {}", visited.len())
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