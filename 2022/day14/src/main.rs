use std::fs;

#[derive(Clone, PartialEq, Eq)]
enum Tile {
    Air,
    Rock,
    Sand,
}

fn part1(input: &str) {
    let mut grid = vec![vec![Tile::Air; 200]; 600];
    for line in input.lines() {
        let points: Vec<(usize, usize)> = line.split(" -> ").map(|x| x.split_once(",").map(|t| -> (usize, usize) { (t.0.parse().unwrap(), t.1.parse().unwrap()) }).unwrap()).collect();
        for i in 1..points.len() {
            let p1 = points[i-1];
            let p2 = points[i];
            if p1.0 == p2.0 {
                for j in p1.1.min(p2.1)..=p1.1.max(p2.1) {
                    grid[p1.0][j] = Tile::Rock;
                }
            } else if p1.1 == p2.1 {
                for j in p1.0.min(p2.0)..=p1.0.max(p2.0) {
                    grid[j][p1.1] = Tile::Rock;
                }
            } else {
                panic!("Ahhhhh")
            }
        }
    }

    let mut count = 0;
    'outer: loop {
        let mut pos = (500, 0);
        'inner: loop {
            if pos.1 >= 199 { break 'outer; }
            if grid[pos.0][pos.1+1] == Tile::Air {
                pos.1 += 1;
            } else if grid[pos.0-1][pos.1+1] == Tile::Air {
                pos.0 -= 1;
                pos.1 += 1;
            } else if grid[pos.0+1][pos.1+1] == Tile::Air {
                pos.0 += 1;
                pos.1 += 1;
            } else {
                grid[pos.0][pos.1] = Tile::Sand;
                break 'inner;
            }
        }
        count += 1;
    }

    println!("part1: {}", count)
}

fn part2(input: &str) {
    let mut grid = vec![vec![Tile::Air; 200]; 1000];
    let mut max_y = 0;
    for line in input.lines() {
        let points: Vec<(usize, usize)> = line.split(" -> ").map(|x| x.split_once(",").map(|t| -> (usize, usize) { (t.0.parse().unwrap(), t.1.parse().unwrap()) }).unwrap()).collect();
        for i in 1..points.len() {
            let p1 = points[i-1];
            let p2 = points[i];
            if p1.0 == p2.0 {
                for j in p1.1.min(p2.1)..=p1.1.max(p2.1) {
                    grid[p1.0][j] = Tile::Rock;
                }
            } else if p1.1 == p2.1 {
                for j in p1.0.min(p2.0)..=p1.0.max(p2.0) {
                    grid[j][p1.1] = Tile::Rock;
                }
            } else {
                panic!("Ahhhhh")
            }
            max_y = max_y.max(p1.1).max(p2.1);
        }
    }
    for i in 0..grid.len() {
        grid[i][max_y+2] = Tile::Rock;
    }

    let mut count = 0;
    'outer: loop {
        let mut pos = (500, 0);
        'inner: loop {
            if pos.1 >= 199 { panic!("ahh") }
            if grid[pos.0][pos.1+1] == Tile::Air {
                pos.1 += 1;
            } else if grid[pos.0-1][pos.1+1] == Tile::Air {
                pos.0 -= 1;
                pos.1 += 1;
            } else if grid[pos.0+1][pos.1+1] == Tile::Air {
                pos.0 += 1;
                pos.1 += 1;
            } else {
                grid[pos.0][pos.1] = Tile::Sand;
                break 'inner;
            }
        }
        count += 1;
        if pos.0 == 500 && pos.1 == 0 {
            break 'outer;
        }
    }
    println!("part2: {}", count)
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