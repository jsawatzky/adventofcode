use std::{fs, str::Chars, iter::Peekable, cmp::Ordering};

use itertools::Itertools;

#[derive(Debug, Clone, PartialEq, Eq)]
enum Packet {
    List(Box<Vec<Packet>>),
    Int(u32)
}

impl Ord for Packet {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        match compare(self, other) {
            Some(b) => if b { Ordering::Less } else { Ordering::Greater },
            None => Ordering::Equal,
        }
    }
}

impl PartialOrd for Packet {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

struct Parser<'a> {
    iter: &'a mut Peekable<Chars<'a>>,
}

impl<'a> Parser<'a> {
    fn new(iter: &'a mut Peekable<Chars<'a>>) -> Self {
        Parser { iter }
    }

    fn list(&mut self) -> Packet {
        self.iter.next();
        let mut v = Box::new(Vec::new());
        loop {
            let next = self.iter.peek().unwrap();
            match next {
                '[' => {
                    v.push(self.list())
                },
                ']' => {
                    break;
                }
                _ => {
                    v.push(self.int())
                }
            }
            let next = self.iter.peek();
            match next {
                Some(',') => { 
                    self.iter.next();
                    continue;
                },
                Some(']') => { break; },
                None => { break; },
                Some(_) => { panic!("invalid next") }
            }
        }
        self.iter.next();
        Packet::List(v)
    }

    fn int(&mut self) -> Packet {
        let mut x: u32 = 0;
        while self.iter.peek().unwrap().is_digit(10) {
            x = (x * 10) + self.iter.next().unwrap().to_digit(10).unwrap();
        }
        Packet::Int(x)
    }

    fn parse(&mut self) -> Packet {
        self.list()
    }
}

fn compare(lhs: &Packet, rhs: &Packet) -> Option<bool> {
    match lhs {
        Packet::List(v1) => {
            match rhs {
                Packet::List(v2) => {
                    let results: Vec<Option<bool>> = v1.iter().zip(v2.iter()).map(|(l, r)| compare(l, r)).collect();
                    for r in results {
                        match r {
                            Some(b) => {
                                return Some(b);
                            },
                            None => { continue; }
                        }
                    }
                    if v1.len() == v2.len() { None } else { Some(v1.len() < v2.len()) }
                },
                Packet::Int(x) => compare(lhs, &Packet::List(Box::new(vec![Packet::Int(*x)])))
            }
        },
        Packet::Int(x) => {
            match rhs {
                Packet::List(_) => compare(&Packet::List(Box::new(vec![Packet::Int(*x)])), rhs),
                Packet::Int(y) => if x == y { None } else { Some(x < y) }
            }
        }
    }
}

fn part1(input: &str) {
    let mut results: Vec<bool> = Vec::new();
    for mut l in &input.lines().chunks(3) {
        let mut lhs_iter = l.next().unwrap().chars().peekable();
        let mut lhs_parser = Parser::new(&mut lhs_iter);
        let lhs = lhs_parser.parse();
        let mut rhs_iter = l.next().unwrap().chars().peekable();
        let mut rhs_parser = Parser::new(&mut rhs_iter);
        let rhs = rhs_parser.parse();
        if let Some(r) = compare(&lhs, &rhs) {
            results.push(r);
        } else {
            panic!("could not determine orderiness");
        }
    }
    println!("part1: {}", results.iter().enumerate().fold(0, |acc, (i, r)| if *r { acc + i + 1 } else { acc }))
}

fn part2(input: &str) {
    let mut packets: Vec<Packet> = Vec::new();
    for l in input.lines() {
        if l.is_empty() { continue; }
        let mut l_iter = l.chars().peekable();
        let mut l_parser = Parser::new(&mut l_iter);
        let p = l_parser.parse();
        packets.push(p);
    }
    let d1 = &Packet::List(Box::new(vec![Packet::List(Box::new(vec![Packet::Int(2)]))]));
    let d2 = &Packet::List(Box::new(vec![Packet::List(Box::new(vec![Packet::Int(6)]))]));
    packets.push(d1.clone());
    packets.push(d2.clone());
    packets.sort();

    println!("part2: {}", packets.iter().enumerate().fold(1, |acc, (i, p)| if p == d1 || p == d2 { acc * (i+1) } else { acc }))
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