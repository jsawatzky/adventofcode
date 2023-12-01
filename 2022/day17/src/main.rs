use std::{fs, collections::{HashMap}};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Tile {
    Air,
    Rock,
}

#[derive(Debug, Clone)]
struct Rock {
    shape: Vec<Vec<Tile>>,
    hpos: usize,
    vpos: usize,
}

impl Rock {
    fn new(shape: &Vec<Vec<Tile>>, vpos: usize) -> Self {
        Self { shape: shape.clone(), hpos: 2, vpos }
    }

    fn left(&mut self, shaft: &Vec<[Tile; 7]>) {
        if self.hpos > 0 {
            for i in 0..self.shape.len() {
                if self.vpos + i >= shaft.len() {
                    break;
                } else {
                    for j in 0..self.shape[i].len() {
                        if self.shape[i][j] == Tile::Air {
                            continue;
                        } else {
                            if shaft[self.vpos+i][self.hpos+j-1] == Tile::Rock {
                                return;
                            }
                            break;
                        }
                    }
                }
            }
            self.hpos -= 1;
        }
    }

    fn right(&mut self, shaft: &Vec<[Tile; 7]>) {
        if self.hpos < 7 - self.shape[0].len() {
            for i in 0..self.shape.len() {
                if self.vpos + i >= shaft.len() {
                    break;
                } else {
                    for j in (0..self.shape[i].len()).rev() {
                        if self.shape[i][j] == Tile::Air {
                            continue;
                        } else {
                            if shaft[self.vpos+i][self.hpos+j+1] == Tile::Rock {
                                return;
                            }
                            break;
                        }
                    }
                }
            }
            self.hpos += 1;
        }
    }

    fn down(&mut self, shaft: &Vec<[Tile; 7]>) -> bool {
        if self.vpos == 0 { return false; }
        for j in 0..self.shape[0].len() {
            for i in 0..self.shape.len() {
                if self.vpos+i-1 >= shaft.len() {
                    break;
                } else {
                    if self.shape[i][j] == Tile::Air {
                        continue;
                    } else {
                        if shaft[self.vpos+i-1][self.hpos+j] == Tile::Rock {
                            return false;
                        }
                    }
                    break;
                }
            }
            
        }
        self.vpos -= 1;
        return true;
    }

    fn height(&self) -> usize {
        self.shape.len()
    }

    fn width(&self, row: usize) -> usize {
        self.shape[row].len()
    }

    fn at(&self, row: usize, col: usize) -> Tile {
        self.shape[row][col]
    }
}

fn part1(input: &str) {
    let shapes = [
        vec![vec![Tile::Rock, Tile::Rock, Tile::Rock, Tile::Rock]],
        vec![vec![Tile::Air, Tile::Rock, Tile::Air], vec![Tile::Rock, Tile::Rock, Tile::Rock], vec![Tile::Air, Tile::Rock, Tile::Air]],
        vec![vec![Tile::Rock, Tile::Rock, Tile::Rock], vec![Tile::Air, Tile::Air, Tile::Rock], vec![Tile::Air, Tile::Air, Tile::Rock]],
        vec![vec![Tile::Rock], vec![Tile::Rock], vec![Tile::Rock], vec![Tile::Rock]],
        vec![vec![Tile::Rock, Tile::Rock], vec![Tile::Rock, Tile::Rock]]
    ];
    let mut shaft: Vec<[Tile; 7]> = Vec::new();
    let mut dirs = input.chars().cycle();
    for i in 0..2022 {
        let mut r = Rock::new(&shapes[i%5], shaft.len()+3);
        loop {
            let dir = dirs.next().unwrap();
            match dir {
                '<' => r.left(&shaft),
                '>' => r.right(&shaft),
                _ => panic!("invalid dir")
            }
            if !r.down(&shaft) {
                for i in 0..r.height() {
                    if r.vpos+i >= shaft.len() {
                        shaft.push([Tile::Air; 7])
                    }
                    for j in 0..r.width(i) {
                        if r.at(i, j) == Tile::Rock {
                            shaft[r.vpos+i][r.hpos+j] = Tile::Rock;
                        }
                    }
                }
                break;
            }
        }
    }
    // print_shaft(&shaft);
    println!("part1: {}", shaft.len())
}

fn row_2_byte(row: [Tile; 7]) -> u8 {
    let mut res = 0;
    for (i, v) in row.iter().enumerate() {
        res = res|(if *v == Tile::Air { 0 } else { 1 } << i)
    }
    res
}

fn part2(input: &str) {
    let shapes = [
        vec![vec![Tile::Rock, Tile::Rock, Tile::Rock, Tile::Rock]],
        vec![vec![Tile::Air, Tile::Rock, Tile::Air], vec![Tile::Rock, Tile::Rock, Tile::Rock], vec![Tile::Air, Tile::Rock, Tile::Air]],
        vec![vec![Tile::Rock, Tile::Rock, Tile::Rock], vec![Tile::Air, Tile::Air, Tile::Rock], vec![Tile::Air, Tile::Air, Tile::Rock]],
        vec![vec![Tile::Rock], vec![Tile::Rock], vec![Tile::Rock], vec![Tile::Rock]],
        vec![vec![Tile::Rock, Tile::Rock], vec![Tile::Rock, Tile::Rock]]
    ];
    let mut shaft: Vec<[Tile; 7]> = Vec::new();
    let mut dirs = input.chars().enumerate().cycle().peekable();
    let mut memo = HashMap::new();
    let mut i = 0;
    let mut cycle_len = 0;
    let mut cycle_height = 0;
    while i < 1_000_000_000_000 && (cycle_len == 0 || i < 2*cycle_len || (1_000_000_000_000-i)%cycle_len != 0) {
        let mut r = Rock::new(&shapes[i%5], shaft.len()+3);
        if shaft.len() > 0 {
            if let Some((stopped, height)) = memo.get(&(i%5, dirs.peek().unwrap().0, row_2_byte(*shaft.last().unwrap()))) {
                cycle_len = i - stopped;
                cycle_height = shaft.len() - height;
            }
            memo.insert((i%5, dirs.peek().unwrap().0, row_2_byte(*shaft.last().unwrap())), (i, shaft.len()));
        }
        loop {
            let (_, dir) = dirs.next().unwrap();
            match dir {
                '<' => r.left(&shaft),
                '>' => r.right(&shaft),
                _ => panic!("invalid dir")
            }
            if !r.down(&shaft) {
                for i in 0..r.height() {
                    if r.vpos+i >= shaft.len() {
                        shaft.push([Tile::Air; 7])
                    }
                    for j in 0..r.width(i) {
                        if r.at(i, j) == Tile::Rock {
                            shaft[r.vpos+i][r.hpos+j] = Tile::Rock;
                        }
                    }
                }
                break;
            }
        }
        i += 1;
    }
    let result= shaft.len() + ((1_000_000_000_000-i)/cycle_len)*cycle_height;
    println!("part2: {}", result)
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