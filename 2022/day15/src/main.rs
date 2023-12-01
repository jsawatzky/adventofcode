use std::{fs, collections::HashSet};

#[derive(Debug, Clone, Copy)]
struct Sensor {
    x: isize,
    y: isize,
    dist: usize,
}

impl Sensor {
    fn new(x: isize, y: isize, dist: usize) -> Self {
        Self { x, y, dist }
    }

    fn point(&self) -> (isize, isize) {
        (self.x, self.y)
    }
}

fn mdist(a: (isize, isize), b: (isize, isize)) -> usize {
    a.0.abs_diff(b.0) + a.1.abs_diff(b.1)
}

fn part1(input: &str) {
    let mut sensors = Vec::new();
    let mut beacons = HashSet::new();
    let mut min_x = isize::MAX;
    let mut max_x = isize::MIN;
    for line in input.lines() {
        if line.is_empty() { continue; }
        let (s, b) = line.strip_prefix("Sensor at ").unwrap().split_once(": closest beacon is at ").unwrap();
        let (sx, sy) = s.split_once(", ").unwrap();
        let sx: isize = sx.strip_prefix("x=").unwrap().parse().unwrap();
        let sy: isize = sy.strip_prefix("y=").unwrap().parse().unwrap();
        let (bx, by) = b.split_once(", ").unwrap();
        let bx: isize = bx.strip_prefix("x=").unwrap().parse().unwrap();
        let by: isize = by.strip_prefix("y=").unwrap().parse().unwrap();
        let sens = Sensor::new(sx, sy, mdist((sx, sy), (bx, by)));
        min_x = min_x.min(sens.x-(sens.dist as isize));
        max_x = max_x.max(sens.x+(sens.dist as isize));
        sensors.push(sens);
        beacons.insert((bx, by));
    }

    let mut cnt: usize = 0;
    for x in min_x..=max_x {
        let p = (x, 2000000);
        for s in &sensors {
            if mdist(p, s.point()) <= s.dist && !beacons.contains(&p) {
                cnt += 1;
                break;
            }
        }
    }
    println!("part1: {}", cnt)
}

fn part2(input: &str) {
    let mut sensors = Vec::new();
    let mut beacons = HashSet::new();
    let mut min_x = isize::MAX;
    let mut max_x = isize::MIN;
    for line in input.lines() {
        if line.is_empty() { continue; }
        let (s, b) = line.strip_prefix("Sensor at ").unwrap().split_once(": closest beacon is at ").unwrap();
        let (sx, sy) = s.split_once(", ").unwrap();
        let sx: isize = sx.strip_prefix("x=").unwrap().parse().unwrap();
        let sy: isize = sy.strip_prefix("y=").unwrap().parse().unwrap();
        let (bx, by) = b.split_once(", ").unwrap();
        let bx: isize = bx.strip_prefix("x=").unwrap().parse().unwrap();
        let by: isize = by.strip_prefix("y=").unwrap().parse().unwrap();
        let sens = Sensor::new(sx, sy, mdist((sx, sy), (bx, by)));
        min_x = min_x.min(sens.x-(sens.dist as isize));
        max_x = max_x.max(sens.x+(sens.dist as isize));
        sensors.push(sens);
        beacons.insert((bx, by));
    }

    let mut freq = 0;
    'outer: for s in &sensors {
        let dist = (s.dist + 1) as isize;
        for d in 0..=dist {
            let x = s.x-d;
            if x >= 0 && x <= 4000000 {
                let y = s.y-(dist-d);
                if y >= 0 && y <= 4000000 {
                    if !sensors.iter().any(|s| mdist((x, y), s.point()) <= s.dist) {
                        freq = (x*4000000)+y;
                        break 'outer;
                    }
                }
                let y = s.y+(dist-d);
                if y >= 0 && y <= 4000000 {
                    if !sensors.iter().any(|s| mdist((x, y), s.point()) <= s.dist) {
                        freq = (x*4000000)+y;
                        break 'outer;
                    }
                }
            }
            let x = s.x+d;
            if x >= 0 && x <= 4000000 {
                let y = s.y-(dist-d);
                if y >= 0 && y <= 4000000 {
                    if !sensors.iter().any(|s| mdist((x, y), s.point()) <= s.dist) {
                        freq = (x*4000000)+y;
                        break 'outer;
                    }
                }
                let y = s.y+(dist-d);
                if y >= 0 && y <= 4000000 {
                    if !sensors.iter().any(|s| mdist((x, y), s.point()) <= s.dist) {
                        freq = (x*4000000)+y;
                        break 'outer;
                    }
                }
            }
        }
    }
    println!("part2: {}", freq)
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