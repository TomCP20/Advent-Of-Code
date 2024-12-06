open System
let read _ = Console.ReadLine()
let isValid = function null -> false | _ -> true
let input: string array = Seq.initInfinite read |> Seq.takeWhile isValid |> Seq.toArray |> String.concat "\n" |> fun f -> f.Split("\n\n", 2)
let rules: (int * int) list = input[0].Split("\n") |> Array.map(fun rule -> rule.Split("|", 2) |> Array.map(int) |> fun r -> (r[0], r[1])) |> Array.toList
let updates: int list list = input[1].Split("\n") |> Array.map(fun rule -> rule.Split(",") |> Array.map(int) |> Array.toList) |> Array.toList

let isOrdered (update: int list) (rules: (int * int) list) = rules |> Seq.map(fun (l, r) -> not ((update |> List.contains l) && (update |> List.contains r) && not ((update |> List.findIndex (fun u -> u = l)) < (update |> List.findIndex (fun u -> u = r))))) |> Seq.forall id

let rec compare (rules: (int * int) list) (a: int) (b: int) =
    match rules with
    | [] -> 0
    | (r, l)::tail -> 
        if (a = l && b = r) then 1
        elif (b = l && a = r) then -1
        else compare tail a b

let rec sumMiddle (updates: int list list) (rules: (int * int) list) (sum1: int) (sum2: int) =
    match updates with
    | [] -> (sum1, sum2)
    | head :: tail -> 
        let mid = (head.Length - 1)/2
        match isOrdered head rules with
        | true -> sumMiddle tail rules (sum1+head[mid]) sum2
        | false -> 
            let sotedHead: list<int> = List.sortWith (compare rules) head
            sumMiddle tail rules  sum1 (sum2+sotedHead[mid])

printfn "%A" (sumMiddle updates rules 0 0)