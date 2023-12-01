use std::fs;

const CYCLES: [isize; 6] = [20, 60, 100, 140, 180, 220];

fn part1(input: &str) {
    let mut cycle: isize = 0;
    let mut x: isize = 1;

    let mut total: isize = 0;

    for line in input.lines() {
        if line == "noop" {
            cycle += 1;
            if CYCLES.contains(&cycle) {
                total += x * cycle;
            }
        } else {
            let v: isize = line.strip_prefix("addx ").unwrap().parse().unwrap();
            cycle += 1;
            if CYCLES.contains(&cycle) {
                total += x * cycle;
            }
            cycle += 1;
            if CYCLES.contains(&cycle) {
                total += x * cycle;
            }
            x += v;
        }
    }
    println!("part1: {}", total)
}

fn part2(input: &str) {
    println!("part2:");
    let mut cycle: isize = 0;
    let mut x: isize = 1;

    let mut row = String::new();

    for line in input.lines() {
        if line == "noop" {
            if x.abs_diff(cycle%40) <= 1 {
                row.push('#');
            } else {
                row.push('.');
            }
            cycle += 1;
            if cycle % 40 == 0 {
                println!("{}", row);
                row.clear();
            }
        } else {
            let v: isize = line.strip_prefix("addx ").unwrap().parse().unwrap();
            if x.abs_diff(cycle%40) <= 1 {
                row.push('#');
            } else {
                row.push('.');
            }
            cycle += 1;
            if cycle % 40 == 0 {
                println!("{}", row);
                row.clear();
            }
            if x.abs_diff(cycle%40) <= 1 {
                row.push('#');
            } else {
                row.push('.');
            }
            cycle += 1;
            if cycle % 40 == 0 {
                println!("{}", row);
                row.clear();
            }
            x += v;
        }
    }
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