use std::fs;

fn part1(input: &str) {
    let grid: Vec<Vec<u32>> = input.lines().map(|l| l.chars().map(|c| c.to_digit(10).unwrap()).collect()).collect();
    let mut visible = 0;
    for (i, r) in grid.iter().enumerate() {
        for (j, v) in r.iter().enumerate() {
            if i == 0 || i == grid.len()-1 {
                visible += 1;
            } else if j == 0 || j == r.len()-1 {
                visible += 1;
            } else {
                let left = &r[..j];
                let right = &r[j+1..];
                if left.iter().all(|v2| v2 < v) || right.iter().all(|v2| v2 < v) {
                    visible += 1;
                } else {
                    let col: Vec<u32> = grid.iter().map(|r| r[j]).collect();
                    let up = &col[..i];
                    let down = &col[i+1..];
                    if up.iter().all(|v2| v2 < v) || down.iter().all(|v2| v2 < v) {
                        visible += 1;
                    }
                }
            }
        }
    }
    println!("part1: {}", visible)
}

fn part2(input: &str) {
    let grid: Vec<Vec<u32>> = input.lines().map(|l| l.chars().map(|c| c.to_digit(10).unwrap()).collect()).collect();
    let mut max_score = 0;
    for (i, r) in grid.iter().enumerate() {
        for (j, v) in r.iter().enumerate() {
            if i == 0 || i == grid.len()-1 || j == 0 || j == r.len()-1 {
                continue;
            } else {
                let left = &r[..j];
                let right = &r[j+1..];
                let col: Vec<u32> = grid.iter().map(|r| r[j]).collect();
                let up = &col[..i];
                let down = &col[i+1..];
                
                let left = left.iter().rev().position(|x| x >= v).unwrap_or(left.len()-1) + 1;
                let right = right.iter().position(|x| x >= v).unwrap_or(right.len()-1) + 1;
                let up = up.iter().rev().position(|x| x >= v).unwrap_or(up.len()-1) + 1;
                let down = down.iter().position(|x| x >= v).unwrap_or(down.len()-1) + 1;

                max_score = max_score.max(left*right*up*down);
            }
        }
    }
    println!("part2: {}", max_score)
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