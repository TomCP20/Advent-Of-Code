open System
open System.Text.RegularExpressions

let read _ = Console.ReadLine()
let isValid = function null -> false | _ -> true
let input = Seq.initInfinite read |> Seq.takeWhile isValid |> String.concat ""

let pattern1 = Regex(@"mul\((\d+),(\d+)\)")
printfn "%A" (pattern1.Matches(input) |> Seq.map (fun m -> int(m.Groups[1].ToString()) * int(m.Groups[2].ToString())) |> Seq.sum)

let pattern2 = Regex(@"do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)")
let rec calc (matches: Match list) (total: int) (enabled: bool)  =
    match matches with
    | [] -> total
    | head :: tail -> 
        match head.Groups[0].ToString() with
        | "do()" -> calc tail total true
        | "don't()" -> calc tail total false
        | _ -> 
            match enabled with
            | false -> calc tail total enabled
            | true -> calc tail (total+int(head.Groups[1].ToString()) * int(head.Groups[2].ToString())) enabled

printfn "%A" (calc (pattern2.Matches(input) |> Seq.toList) 0 true)