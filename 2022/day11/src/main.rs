use std::{fs};

struct Monkey {
    items: Vec<u128>,
    op: String,
    test: u128,
    t_dest: usize,
    f_dest: usize,
    total_inspects: usize,
}

impl Monkey {
    fn new(items: Vec<u128>, op: String, test: u128, t_dest: usize, f_dest: usize) -> Self {
        Self { items, op, test, t_dest, f_dest, total_inspects: 0 }
    }

    fn do_op(&self, item: u128) -> u128 {
        if self.op.starts_with("old + ") {
            let amt: u128 = self.op.strip_prefix("old + ").unwrap().parse().unwrap();
            item + amt
        } else if self.op.starts_with("old * ") {
            if self.op == "old * old" {
                item * item
            } else {
                let amt: u128 = self.op.strip_prefix("old * ").unwrap().parse().unwrap();
                item * amt
            }
        } else {
            panic!("invalid op");
        }
    }

    fn do_test(&self, item: u128) -> usize {
        if item % self.test == 0 { self.t_dest } else { self.f_dest }
    }
}

fn part1(input: &str) {
    let mut monkeys = Vec::new();
    let mut lines = input.lines();
    loop {
        if let Some(line) = lines.next() {
            if !line.starts_with("Monkey ") {
                panic!("Invalid start of monkey");
            }
            let start = lines.next().unwrap().strip_prefix("  Starting items: ").unwrap();
            let start: Vec<u128> = start.split(", ").map(|x| x.parse().unwrap()).collect();
            let op = lines.next().unwrap().strip_prefix("  Operation: new = ").unwrap();
            let test: u128 = lines.next().unwrap().strip_prefix("  Test: divisible by ").unwrap().parse().unwrap();
            let t_dest: usize = lines.next().unwrap().strip_prefix("    If true: throw to monkey ").unwrap().parse().unwrap();
            let f_dest: usize = lines.next().unwrap().strip_prefix("    If false: throw to monkey ").unwrap().parse().unwrap();
            monkeys.push(Monkey::new(start, op.to_string(), test, t_dest, f_dest));
            lines.next();
        } else {
            break;
        }
    }

    for _ in 0..20 {
        for i in 0..monkeys.len() {
            let cur_items = monkeys[i].items.clone();
            monkeys[i].items.clear();
            for item in cur_items {
                let new_item = monkeys[i].do_op(item) / 3;
                let next_monkey = monkeys[i].do_test(new_item);
                monkeys[next_monkey].items.push(new_item);
                monkeys[i].total_inspects += 1;
            }
        }
    }

    let mut inspections: Vec<usize> = monkeys.iter().map(|m| m.total_inspects).collect();
    inspections.sort();
    inspections.reverse();
    println!("part1: {}", inspections[0] * inspections[1])
}

fn part2(input: &str) {
    let mut monkeys = Vec::new();
    let mut lines = input.lines();
    loop {
        if let Some(line) = lines.next() {
            if !line.starts_with("Monkey ") {
                panic!("Invalid start of monkey");
            }
            let start = lines.next().unwrap().strip_prefix("  Starting items: ").unwrap();
            let start: Vec<u128> = start.split(", ").map(|x| x.parse().unwrap()).collect();
            let op = lines.next().unwrap().strip_prefix("  Operation: new = ").unwrap();
            let test: u128 = lines.next().unwrap().strip_prefix("  Test: divisible by ").unwrap().parse().unwrap();
            let t_dest: usize = lines.next().unwrap().strip_prefix("    If true: throw to monkey ").unwrap().parse().unwrap();
            let f_dest: usize = lines.next().unwrap().strip_prefix("    If false: throw to monkey ").unwrap().parse().unwrap();
            monkeys.push(Monkey::new(start, op.to_string(), test, t_dest, f_dest));
            lines.next();
        } else {
            break;
        }
    }

    let factor = monkeys.iter().fold(1, |acc, x| acc * x.test);

    for _ in 0..10000 {
        for i in 0..monkeys.len() {
            let cur_items = monkeys[i].items.clone();
            monkeys[i].items.clear();
            for item in cur_items {
                let new_item = monkeys[i].do_op(item) % factor;
                let next_monkey = monkeys[i].do_test(new_item);
                monkeys[next_monkey].items.push(new_item);
                monkeys[i].total_inspects += 1;
            }
        }
    }

    let mut inspections: Vec<usize> = monkeys.iter().map(|m| m.total_inspects).collect();
    inspections.sort();
    inspections.reverse();
    println!("part2: {}", inspections[0] * inspections[1])
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