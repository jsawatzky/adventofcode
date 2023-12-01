use std::{fs::{self, File}, collections::{HashSet}, io::Write};

fn part1(input: &str) {
    let mut surf_area = 0;
    let mut cubes = HashSet::new();
    for line in input.lines() {
        let coords: Vec<i32> = line.split(",").map(|x| x.parse().unwrap()).collect();
        let coords = (coords[0], coords[1], coords[2]);
        cubes.insert(coords);
        let mut covered = 0;
        if cubes.contains(&(coords.0-1, coords.1, coords.2)) {
            covered += 1
        }
        if cubes.contains(&(coords.0+1, coords.1, coords.2)) {
            covered += 1
        }
        if cubes.contains(&(coords.0, coords.1-1, coords.2)) {
            covered += 1
        }
        if cubes.contains(&(coords.0, coords.1+1, coords.2)) {
            covered += 1
        }
        if cubes.contains(&(coords.0, coords.1, coords.2-1)) {
            covered += 1
        }
        if cubes.contains(&(coords.0, coords.1, coords.2+1)) {
            covered += 1
        }
        surf_area += 6 - (2*covered)
    }
    println!("part1: {}", surf_area)
}

fn part2(input: &str) {
    let mut cubes = HashSet::new();
    let mut max = (0, 0, 0);
    for line in input.lines() {
        let coords: Vec<i32> = line.split(",").map(|x| x.parse().unwrap()).collect();
        let coords = (coords[0], coords[1], coords[2]);
        max.0 = max.0.max(coords.0);
        max.1 = max.1.max(coords.1);
        max.2 = max.2.max(coords.2);
        cubes.insert(coords);
    }
    max = (max.0+1, max.1+1, max.2+1);

    let mut out_surf_area = 0;
    let mut outer = HashSet::new();
    let mut stack = Vec::new();
    stack.push((-1, -1, -1));
    while stack.len() > 0 {
        let c = stack.pop().unwrap();
        if !outer.contains(&c) {
            if c.0-1 >= -1 { 
                if cubes.contains(&(c.0-1, c.1, c.2)) {
                    out_surf_area += 1;
                } else if !outer.contains(&(c.0-1, c.1, c.2)) {
                    stack.push((c.0-1, c.1, c.2));
                }
            }
            if c.0+1 <= max.0 {
                if cubes.contains(&(c.0+1, c.1, c.2)) {
                    out_surf_area += 1;
                } else if !outer.contains(&(c.0+1, c.1, c.2)) {
                    stack.push((c.0+1, c.1, c.2));
                }
            }
            if c.1-1 >= -1 {
                if cubes.contains(&(c.0, c.1-1, c.2)) {
                    out_surf_area += 1;
                } else if !outer.contains(&(c.0, c.1-1, c.2)) {
                    stack.push((c.0, c.1-1, c.2));
                }
            }
            if c.1+1 <= max.1 {
                if cubes.contains(&(c.0, c.1+1, c.2)) {
                    out_surf_area += 1;
                } else if !outer.contains(&(c.0, c.1+1, c.2)) {
                    stack.push((c.0, c.1+1, c.2));
                }
            }
            if c.2-1 >= -1 {
                if cubes.contains(&(c.0, c.1, c.2-1)) {
                    out_surf_area += 1;
                } else if !outer.contains(&(c.0, c.1, c.2-1)) {
                    stack.push((c.0, c.1, c.2-1));
                }
            }
            if c.2+1 <= max.2 {
                if cubes.contains(&(c.0, c.1, c.2+1)) {
                    out_surf_area += 1;
                } else if !outer.contains(&(c.0, c.1, c.2+1)) {
                    stack.push((c.0, c.1, c.2+1));
                }
            }
            outer.insert(c);
        }
    }

    println!("part2: {}", out_surf_area)
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