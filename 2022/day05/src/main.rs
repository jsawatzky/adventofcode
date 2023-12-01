use std::fs;

fn part1(input: &str) {
    let mut stacks = Vec::<Vec<char>>::new();
    let mut lines = input.lines();
    loop {
        let line = lines.next();
        match line {
            None => { panic!("unexpected EOF"); }
            Some(line) => {
                if line.is_empty() {
                    break;
                }

                let mut chars = line.chars();
                let mut stack = 0;
                loop {
                    let char = chars.next();
                    match char {
                        None => { break; }
                        Some(char) => {
                            if char == '[' {
                                while stacks.len() < stack + 1 {
                                    stacks.push(Vec::new());
                                }
                                stacks[stack].push(chars.next().unwrap());
                                chars.next();
                                chars.next();
                            } else {
                                chars.next();
                                chars.next();
                                chars.next();
                            }
                            stack = stack + 1;
                        }
                    }
                }
            }
        }
    }
    for s in &mut stacks {
        s.reverse()
    }
    for line in lines {
        let line = line.strip_prefix("move ").unwrap();
        let (count, srcs) = line.split_once(" from ").unwrap();
        let count: usize = count.parse().unwrap();
        let (src, dst) = srcs.split_once(" to ").unwrap();
        let src: usize = src.parse().unwrap();
        let dst: usize = dst.parse().unwrap();

        for _ in 0..count {
            let item = stacks[src-1].pop().unwrap();
            stacks[dst-1].push(item)
        }
    }
    let mut output = String::new();
    for s in &mut stacks {
        if let Some(top) = s.pop() {
            output.push(top);
        }
    }
    println!("part1: {:?}", output)
}

fn part2(input: &str) {
    let mut stacks = Vec::<Vec<char>>::new();
    let mut lines = input.lines();
    loop {
        let line = lines.next();
        match line {
            None => { panic!("unexpected EOF"); }
            Some(line) => {
                if line.is_empty() {
                    break;
                }

                let mut chars = line.chars();
                let mut stack = 0;
                loop {
                    let char = chars.next();
                    match char {
                        None => { break; }
                        Some(char) => {
                            if char == '[' {
                                while stacks.len() < stack + 1 {
                                    stacks.push(Vec::new());
                                }
                                stacks[stack].push(chars.next().unwrap());
                                chars.next();
                                chars.next();
                            } else {
                                chars.next();
                                chars.next();
                                chars.next();
                            }
                            stack = stack + 1;
                        }
                    }
                }
            }
        }
    }
    for s in &mut stacks {
        s.reverse()
    }
    for line in lines {
        let line = line.strip_prefix("move ").unwrap();
        let (count, srcs) = line.split_once(" from ").unwrap();
        let count: usize = count.parse().unwrap();
        let (src, dst) = srcs.split_once(" to ").unwrap();
        let src: usize = src.parse().unwrap();
        let dst: usize = dst.parse().unwrap();

        let mut tmp = Vec::new();
        for _ in 0..count {
            let item = stacks[src-1].pop().unwrap();
            tmp.push(item)
        }
        tmp.reverse();
        for i in tmp {
            stacks[dst-1].push(i)
        }
    }
    let mut output = String::new();
    for s in &mut stacks {
        if let Some(top) = s.pop() {
            output.push(top);
        }
    }
    println!("part2: {:?}", output)
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