use itertools::Itertools;
use std::{collections::HashSet, io};

#[derive(Hash, Eq, PartialEq)]
struct GuardState {
    pos: (i32, i32),
    turns: usize,
}

impl Clone for GuardState {
    fn clone(&self) -> Self {
        GuardState {
            pos: self.pos,
            turns: self.turns,
        }
    }
}

struct GuardStateIterator {
    guard_state: GuardState,
    h: i32,
    w: i32,
    obstacles: HashSet<(i32, i32)>,
}

const DIRS: [(i32, i32); 4] = [(0, -1), (1, 0), (0, 1), (-1, 0)];

impl Iterator for GuardStateIterator {
    type Item = GuardState;

    fn next(&mut self) -> Option<GuardState> {
        if 0 <= self.guard_state.pos.0
            && self.guard_state.pos.0 < self.w
            && 0 <= self.guard_state.pos.1
            && self.guard_state.pos.1 < self.h
        {
            let s = Some(self.guard_state.clone());
            let guard_dir = DIRS[self.guard_state.turns];
            let new_pos = (
                self.guard_state.pos.0 + guard_dir.0,
                self.guard_state.pos.1 + guard_dir.1,
            );
            if self.obstacles.contains(&new_pos) {
                self.guard_state.turns = (self.guard_state.turns + 1) % 4
            } else {
                self.guard_state.pos = new_pos;
            }
            return s;
        } else {
            None
        }
    }
}

fn detect_loop(
    initial_guard_state: &GuardState,
    obstacles: HashSet<(i32, i32)>,
    w: i32,
    h: i32,
) -> bool {
    let mut state_set: HashSet<GuardState> = HashSet::new();
    for state in (GuardStateIterator {
        guard_state: initial_guard_state.clone(),
        h: h,
        w: w,
        obstacles: obstacles,
    }) {
        if state_set.contains(&state) {
            return true;
        }
        state_set.insert(state);
    }
    return false;
}

fn add_set(mut obstacles: HashSet<(i32, i32)>, pos: (i32, i32)) -> HashSet<(i32, i32)> {
    obstacles.insert(pos);
    return obstacles;
}

fn main() {
    let lines = io::stdin()
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap();
    let h: i32 = lines.len().try_into().unwrap();
    let w: i32 = lines[0].len().try_into().unwrap();
    let mut obstacles: HashSet<(i32, i32)> = HashSet::new();
    let mut guard_state: GuardState = GuardState {
        pos: (-1, -1),
        turns: usize::MAX,
    };
    for (y, line) in lines.iter().enumerate() {
        for (x, char) in line.chars().enumerate() {
            let pos = (x.try_into().unwrap(), y.try_into().unwrap());
            if char == '#' {
                obstacles.insert(pos);
            } else if char != '.' {
                guard_state.pos = pos;
                if char == '^' {
                    guard_state.turns = 0;
                } else if char == '>' {
                    guard_state.turns = 1;
                } else if char == 'v' {
                    guard_state.turns = 2;
                } else if char == '<' {
                    guard_state.turns = 3;
                }
            }
        }
    }
    let set: HashSet<(i32, i32)> = HashSet::from_iter(
        GuardStateIterator {
            guard_state: guard_state.clone(),
            h,
            w,
            obstacles: obstacles.clone(),
        }
        .map(|state| state.pos),
    );
    println!("{}", set.len());
    let mut checked: HashSet::<(i32, i32)> = HashSet::new();
    let mut loop_count = 0;
    for (a, b) in (GuardStateIterator {
        guard_state,
        h,
        w,
        obstacles: obstacles.clone(),
    })
    .tuple_windows::<(GuardState, GuardState)>() {
        if !checked.contains(&b.pos){
            checked.insert(b.pos);
            if detect_loop(&a.clone(), add_set(obstacles.clone(), b.pos), w, h) {
                loop_count+=1;
            }
        }
    }
    
    println!("{}", loop_count);
}
