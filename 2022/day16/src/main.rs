use std::{fs, collections::{HashMap}};

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
struct Valve {
    rate: u32,
    tuns: Vec<u64>,
}

impl Valve {
    fn new(rate: u32, connected: Vec<u64>) -> Self {
        Self { rate, tuns: connected }
    }
}

#[derive(Debug, PartialEq, Eq, Hash)]
struct Memo {
    cur: u64,
    opened: u64,
    time_left: u32
}

impl Memo {
    fn new(cur: u64, opened: u64, time_left: u32) -> Self {
        Self { cur, opened, time_left }
    }
}

struct ValveNet {
    memo: HashMap<Memo, u32>,
}

impl ValveNet {
    fn new() -> Self {
        Self {memo: HashMap::new()}
    }

    fn get_path(&mut self, cur: u64, opened: u64, time_left: u32, valves: &HashMap<u64, Valve>) -> u32 {
        if time_left <= 1 {
            return 0;
        }
        if let Some(r) = self.memo.get(&Memo::new(cur, opened, time_left)) {
            return *r;
        }
        let c_valve = valves.get(&cur).unwrap();
        let mut max = 0;
        if opened&cur == 0 && c_valve.rate > 0 {
            let new_opened = opened|cur;
            max = self.get_path(cur, new_opened, time_left-1, valves);
            max += c_valve.rate * (time_left-1);
        }
        
        for o in &c_valve.tuns {
            let m = self.get_path(*o, opened, time_left-1, valves);
            max = max.max(m);
        }

        self.memo.insert(Memo::new(cur, opened, time_left), max);
        max
    }

    fn get_path_2(&mut self, you: u64, elephant: u64, opened: u64, time_left: u32, valves: &HashMap<u64, Valve>) -> u32 {
        if time_left <= 1 {
            return 0;
        }
        if let Some(r) = self.memo.get(&Memo::new(you|elephant, opened, time_left)) {
            return *r;
        }
        let y_valve = valves.get(&you).unwrap();
        let e_valve = valves.get(&elephant).unwrap();
        let mut max = 0;
        if you == elephant {
            if opened&you == 0 && y_valve.rate > 0 {
                let new_opened = opened|you;
                for o in &e_valve.tuns {
                    max = max.max(self.get_path_2(you, *o, new_opened, time_left-1, valves) + (y_valve.rate * (time_left-1)))
                }
            }
        } else {
            if opened&you == 0 && y_valve.rate > 0 && opened&elephant == 0 && e_valve.rate > 0 {
                let new_opened = opened|you|elephant;
                max = max.max(self.get_path_2(you, elephant, new_opened, time_left-1, valves) + (y_valve.rate * (time_left-1)) + (e_valve.rate * (time_left-1)));
            }
            if opened&you == 0 && y_valve.rate > 0 {
                let new_opened = opened|you;
                for o in &e_valve.tuns {
                    max = max.max(self.get_path_2(you, *o, new_opened, time_left-1, valves) + (y_valve.rate * (time_left-1)));
                }
            }
            if opened&elephant == 0 && e_valve.rate > 0 {
                let new_opened = opened|elephant;
                for o in &y_valve.tuns {
                    max = max.max(self.get_path_2(*o, elephant, new_opened, time_left-1, valves) + (e_valve.rate * (time_left-1)));
                }
            }
        }
        
        for y in &y_valve.tuns {
            for e in &e_valve.tuns {
                max = max.max(self.get_path_2(*y, *e, opened, time_left-1, valves));
            }
        }

        self.memo.insert(Memo::new(you|elephant, opened, time_left), max);
        max
    }
}

fn parse_input2(input: &str) -> (HashMap<u64, Valve>, u64) {
    let mut valves = HashMap::new();
    let mut res = HashMap::new();
    let mut cur_valve: u64 = 1;

    for line in input.lines() {
        if line.is_empty() { continue; }
        let line = line.strip_prefix("Valve ").unwrap();
        let (v, _) = line.split_once(" ").unwrap();
        valves.insert(String::from(v), cur_valve);
        cur_valve = cur_valve << 1;
    }

    for line in input.lines() {
        if line.is_empty() { continue; }
        let line = line.strip_prefix("Valve ").unwrap();
        let (v, line) = line.split_once(" ").unwrap();
        let line = line.strip_prefix("has flow rate=").unwrap();
        let (f, ts) = line.split_once("; tunnels lead to valves ").unwrap();
        let f: u32 = f.parse().unwrap();
        let ts: Vec<u64> = ts.split(", ").map(|s| *valves.get(&String::from(s)).unwrap()).collect();
        res.insert(*valves.get(&String::from(v)).unwrap(), Valve::new(f, ts));
    }

    (res, *valves.get(&String::from("AA")).unwrap())
}

fn part1(input: &str) {
    let (valves, start) = parse_input2(input);

    let mut net = ValveNet::new();
    let m = net.get_path(start, 0, 30, &valves);

    println!("part1: {}", m)
}

fn part2(input: &str) {
    let (valves, start) = parse_input2(input);

    let mut net = ValveNet::new();
    let m = net.get_path_2(start, start, 0, 26, &valves);

    println!("part2: {}", m)
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