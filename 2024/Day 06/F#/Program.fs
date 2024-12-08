open System
open System.Collections.Generic
let read _ = Console.ReadLine()
let isValid = function null -> false | _ -> true

let rec parse (w: int) (h: int) (input: string array) (pos: int * int) (obstacles: HashSet<int * int>) (state: (int * int) * int) = 
    match pos with
    | (_, y) when y=h -> (obstacles, state)
    | (x, y) when x = w -> parse w h input (0, y+1) obstacles state
    | (x, y) -> 
        match input[y][x] with
        | '#' -> 
            obstacles.Add((x, y)) |> ignore
            parse w h input (x+1, y) obstacles state
        | '^' -> parse w h input (x+1, y) obstacles ((x, y), 0)
        | '>' -> parse w h input (x+1, y) obstacles ((x, y), 1)
        | 'v' -> parse w h input (x+1, y) obstacles ((x, y), 2)
        | '<' -> parse w h input (x+1, y) obstacles ((x, y), 3)
        | _ -> parse w h input (x+1, y) obstacles state

let dirs: (int * int) list  = [(0, -1); (1, 0); (0, 1); (-1, 0)]

let traverse (w: int) (h: int) (state: (int * int) * int) (obstacles: HashSet<int * int>) = seq {
    let mutable (guard_pos: int * int, turns: int) = state
    while 0 <= fst guard_pos && fst guard_pos < w && 0 <= snd guard_pos && snd guard_pos < h do
        yield (guard_pos, turns)
        let guard_dir = dirs[turns]
        let next_guard_pos = (fst guard_dir + fst guard_pos, snd guard_dir + snd guard_pos)
        if (obstacles.Contains(next_guard_pos)) then
            turns <- (turns + 1) % 4
        else
            guard_pos <- next_guard_pos
}

let rec detect_loop (state_set: HashSet<(int * int) * int>) (original_path: seq<(int * int) * int>) =
    printfn "%A" state_set.Count
    if Seq.isEmpty original_path then
        false
    else
        let h = Seq.head original_path
        if state_set.Contains(h) then
            true
        else
            state_set.Add(h) |> ignore
            detect_loop (state_set) (Seq.tail original_path)

let rec get_obstacle_pos (checked_states: HashSet<int * int>) (sequence: (((int * int) * int) * ((int * int) * int)) seq)  = seq {
    if not (Seq.isEmpty sequence) then
        let (new_start, (obstacle_pos, _)) = Seq.head sequence
        if not (checked_states.Contains(obstacle_pos)) then
            yield (new_start, obstacle_pos)
            checked_states.Add(obstacle_pos) |> ignore
        yield! get_obstacle_pos (checked_states) (Seq.tail sequence)
}

let Add (set: HashSet<'T>) (v: 'T) = 
    let nset = HashSet(set)
    nset.Add(v) |> ignore
    nset

let input: string array = Seq.initInfinite read |> Seq.takeWhile isValid |> Seq.toArray

let w = input[0].Length
let h = input.Length

let (obstacles: HashSet<int * int>, initial_state: (int * int) * int) = (parse w h input (0, 0) (HashSet()) ((-1, -1), -1))

printfn "%A" (traverse w h initial_state obstacles |> Seq.map fst |> Set.ofSeq ).Count

let total = (get_obstacle_pos  (HashSet()) (Seq.pairwise (traverse w h initial_state obstacles))) |> Seq.filter(fun (new_start, obstacle_pos) -> (detect_loop (HashSet()) (traverse w h new_start (Add obstacles obstacle_pos)))) |> Seq.length
printfn "total %A" total
    