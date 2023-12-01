use std::fs;

fn part1(input: &str) {
    let mut score = 0;
    for line in input.lines() {
        let game: Vec<&str> = line.split_whitespace().collect();

        match game[1] {
            "X" => { score = score + 1 }
            "Y" => { score = score + 2 }
            "Z" => { score = score + 3 }
            _ => panic!("invalid move")
        }

        match game[0] {
            "A" => { 
                match game[1] {
                    "X" => { score = score + 3 }
                    "Y" => { score = score + 6 }
                    "Z" => { }
                    _ => panic!("invalid move")
                }
             }
            "B" => { 
                match game[1] {
                    "X" => { }
                    "Y" => { score = score + 3 }
                    "Z" => { score = score + 6 }
                    _ => panic!("invalid move")
                }
             }
            "C" => { 
                match game[1] {
                    "X" => { score = score + 6 }
                    "Y" => { }
                    "Z" => { score = score + 3 }
                    _ => panic!("invalid move")
                }
             }
            _ => panic!("invalid move")
        }
    }
    println!("part1: {}", score)
}

fn part2(input: &str) {
    let mut score = 0;
    for line in input.lines() {
        let game: Vec<&str> = line.split_whitespace().collect();
        match game[0] {
            "A" => { 
                match game[1] {
                    "X" => { score = score + 3 }
                    "Y" => { score = score + 4 }
                    "Z" => { score = score + 8 }
                    _ => panic!("invalid move")
                }
             }
            "B" => { 
                match game[1] {
                    "X" => { score = score + 1 }
                    "Y" => { score = score + 5 }
                    "Z" => { score = score + 9 }
                    _ => panic!("invalid move")
                }
             }
            "C" => { 
                match game[1] {
                    "X" => { score = score + 2 }
                    "Y" => { score = score + 6 }
                    "Z" => { score = score + 7 }
                    _ => panic!("invalid move")
                }
             }
            _ => panic!("invalid move")
        }
    }
    println!("part2: {}", score)
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