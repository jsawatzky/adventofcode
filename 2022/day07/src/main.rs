use std::{fs, collections::HashMap, rc::Rc, cell::RefCell, borrow::Borrow};

#[derive(Debug)]
struct Dir {
    parent: Option<Rc<RefCell<Dir>>>,
    sub_dirs: HashMap<String, Rc<RefCell<Dir>>>,
    file_size: u64,
}

impl Dir {
    fn new() -> Dir {
        return Dir {
            parent: None,
            sub_dirs: HashMap::new(),
            file_size: 0,
        };
    }

    fn sub_dir(&mut self, n: &str) -> Rc<RefCell<Dir>> {
        let child = self.sub_dirs.get(n);
        return match child {
            None => {
                let subdir = Rc::new(RefCell::new(Dir::new()));
                self.sub_dirs.insert(n.to_owned(), Rc::clone(&subdir));
                subdir
            },
            Some(sub_dir) => Rc::clone(sub_dir),
        };
    }

    fn add_file(&mut self, size: u64) {
        self.file_size = self.file_size + size;
    }

    fn total_size(&self) -> u64 {
        self.file_size + self.sub_dirs.values().fold(0, |acc, d| acc + <Rc<RefCell<Dir>> as Borrow<RefCell<Dir>>>::borrow(d).borrow().total_size())
    }

    fn do_part1(&self) -> u64 {
        let total = self.sub_dirs.values().fold(0, |acc, d| acc + <Rc<RefCell<Dir>> as Borrow<RefCell<Dir>>>::borrow(d).borrow().do_part1());
        if self.total_size() < 100000 {
            return self.total_size() + total;
        } else {
            return total;
        }
    }

    fn do_part2(&self, needed: u64) -> u64 {
        if self.total_size() < needed {
            return u64::MAX;
        }
        self.sub_dirs.values().fold(self.total_size(), |acc, d| acc.min(<Rc<RefCell<Dir>> as Borrow<RefCell<Dir>>>::borrow(d).borrow().do_part2(needed)))
    }
    
}

fn parse_input(input: &str) -> Rc<RefCell<Dir>> {
    let root = Rc::new(RefCell::new(Dir::new()));
    let mut line_iter = input.lines().peekable();
    let mut cur_dir = Rc::clone(&root);
    loop {
        let line = line_iter.next();
        let line = match line {
            None => { break; },
            Some(l) => l,
        };
        if line.starts_with('$') {
            let line = line.strip_prefix("$ ").unwrap();
            if line == "ls" {
                loop {
                    if let Some(l) = line_iter.peek() {
                        if l.starts_with("$") {
                            break;
                        }
                        let l = line_iter.next().unwrap();
                        let (size, _) = l.split_once(' ').unwrap();
                        if size != "dir" {
                            let size: u64 = size.parse().unwrap();
                            cur_dir.borrow_mut().add_file(size);
                        }
                    } else {
                        break;
                    }
                }
            } else if line.starts_with("cd") {
                let new_dir;
                let line = line.strip_prefix("cd ").unwrap();
                if line == "/" {
                    new_dir = Rc::clone(&root);
                } else if line == ".." {
                    new_dir = Rc::clone(<Rc<RefCell<Dir>> as Borrow<RefCell<Dir>>>::borrow(&cur_dir).borrow().parent.as_ref().unwrap());
                } else {
                    new_dir = cur_dir.borrow_mut().sub_dir(line);
                    {
                        new_dir.borrow_mut().parent = Some(Rc::clone(&cur_dir));
                    }
                }
                cur_dir = new_dir;
            } else {
                panic!("invalid command")
            }
        }
    }
    return root;
}

fn part1(input: &str) {
    let root = parse_input(input);
    println!("part1: {}", <Rc<RefCell<Dir>> as Borrow<RefCell<Dir>>>::borrow(&root).borrow().do_part1());
}

fn part2(input: &str) {
    let root = parse_input(input);
    let needed = 30000000 - (70000000 - <Rc<RefCell<Dir>> as Borrow<RefCell<Dir>>>::borrow(&root).borrow().total_size());
    println!("part2: {}", <Rc<RefCell<Dir>> as Borrow<RefCell<Dir>>>::borrow(&root).borrow().do_part2(needed));
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