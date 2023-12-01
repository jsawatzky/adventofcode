use std::fs;
use std::cmp::Reverse;
use priority_queue::PriorityQueue;

#[derive(PartialEq, Eq, Hash, Clone, Copy, Debug)]
struct Point {
    height: u32,
    x: usize,
    y: usize,
    visited: bool,
}

impl Point {
    fn new(height: u32, x :usize, y: usize) -> Self {
        Self { height, x, y, visited: false }
    }
}

fn part1(input: &str) {
    let mut start = Point::new(0, 0, 0);
    let mut end = Point::new(0, 0, 0);
    let mut grid = Vec::new();
    let mut pq = PriorityQueue::new();
    for (y, line) in input.lines().enumerate() {
        if line.is_empty() {
            continue;
        }
        let row: Vec<Point> = line.chars().enumerate().map(|(x, c)| {
            match c {
                'S'=> {
                    start = Point::new(1, x, y);
                    start
                },
                'E' => {
                    end = Point::new(26, x, y);
                    end
                },
                c => Point::new(c as u32 - 96, x, y)
            }
        }).collect();
        for p in &row {
            pq.push(*p, Reverse(usize::MAX));
        }
        grid.push(row);
    }

    pq.remove(&start);

    let mut cur = start;
    let mut dist = 0;
    while cur.x != end.x || cur.y != end.y {
        grid[cur.y][cur.x].visited = true;
        if cur.y > 0 {
            let next = grid[cur.y-1][cur.x];
            if !next.visited && (next.height <= cur.height || next.height == cur.height + 1) {
                let Reverse(old_dist) = *pq.get_priority(&next).unwrap();
                if dist+1 < old_dist {
                    pq.change_priority(&next, Reverse(dist+1));
                }
            }
        }
        if cur.y < grid.len()-1 {
            let next = grid[cur.y+1][cur.x];
            if !next.visited && (next.height <= cur.height || next.height == cur.height + 1) {
                let Reverse(old_dist) = *pq.get_priority(&next).unwrap();
                if dist+1 < old_dist {
                    pq.change_priority(&next, Reverse(dist+1));
                }
            }
        }
        if cur.x > 0 {
            let next = grid[cur.y][cur.x-1];
            if !next.visited && (next.height <= cur.height || next.height == cur.height + 1) {
                let Reverse(old_dist) = *pq.get_priority(&next).unwrap();
                if dist+1 < old_dist {
                    pq.change_priority(&next, Reverse(dist+1));
                }
            }
        }
        if cur.x < grid[0].len()-1 {
            let next = grid[cur.y][cur.x+1];
            if !next.visited && (next.height <= cur.height || next.height == cur.height + 1) {
                let Reverse(old_dist) = *pq.get_priority(&next).unwrap();
                if dist+1 < old_dist {
                    pq.change_priority(&next, Reverse(dist+1));
                }
            }
        }
        (cur, Reverse(dist)) = pq.pop().unwrap();
    }

    println!("part1: {}", dist)
}

fn part2(input: &str) {
    let mut start = Point::new(0, 0, 0);
    let mut grid = Vec::new();
    let mut pq = PriorityQueue::new();
    for (y, line) in input.lines().enumerate() {
        if line.is_empty() {
            continue;
        }
        let row: Vec<Point> = line.chars().enumerate().map(|(x, c)| {
            match c {
                'S'=> {
                    Point::new(1, x, y)
                },
                'E' => {
                    start = Point::new(26, x, y);
                    start
                },
                c => Point::new(c as u32 - 96, x, y)
            }
        }).collect();
        for p in &row {
            pq.push(*p, Reverse(usize::MAX));
        }
        grid.push(row);
    }

    pq.remove(&start);

    let mut cur = start;
    let mut dist = 0;
    while cur.height != 1 {
        grid[cur.y][cur.x].visited = true;
        if cur.y > 0 {
            let next = grid[cur.y-1][cur.x];
            if !next.visited && (next.height >= cur.height || next.height == cur.height - 1) {
                let Reverse(old_dist) = *pq.get_priority(&next).unwrap();
                if dist+1 < old_dist {
                    pq.change_priority(&next, Reverse(dist+1));
                }
            }
        }
        if cur.y < grid.len()-1 {
            let next = grid[cur.y+1][cur.x];
            if !next.visited && (next.height >= cur.height || next.height == cur.height - 1) {
                let Reverse(old_dist) = *pq.get_priority(&next).unwrap();
                if dist+1 < old_dist {
                    pq.change_priority(&next, Reverse(dist+1));
                }
            }
        }
        if cur.x > 0 {
            let next = grid[cur.y][cur.x-1];
            if !next.visited && (next.height >= cur.height || next.height == cur.height - 1) {
                let Reverse(old_dist) = *pq.get_priority(&next).unwrap();
                if dist+1 < old_dist {
                    pq.change_priority(&next, Reverse(dist+1));
                }
            }
        }
        if cur.x < grid[0].len()-1 {
            let next = grid[cur.y][cur.x+1];
            if !next.visited && (next.height >= cur.height || next.height == cur.height - 1) {
                let Reverse(old_dist) = *pq.get_priority(&next).unwrap();
                if dist+1 < old_dist {
                    pq.change_priority(&next, Reverse(dist+1));
                }
            }
        }
        (cur, Reverse(dist)) = pq.pop().unwrap();
    }

    println!("part2: {}", dist)
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