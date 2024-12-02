open System

let read _ = Console.ReadLine()
let isValid = function null -> false | _ -> true
let isSafe (report: int seq) = report |> Seq.pairwise |> Seq.map (fun (a, b) -> b-a) |> (fun s -> Seq.forall (fun x -> 1 <= x && x <= 3) s || Seq.forall (fun x -> 1 <= -x && -x <= 3) s)
let inputList: string array = Seq.initInfinite read |> Seq.takeWhile isValid |> Seq.toArray
let reports = inputList |> Array.map(fun x -> x.Split(" ") |> Array.map(int))

printfn "%A" (reports |> Seq.filter isSafe |> Seq.length)

let isSafeish (report: int array) = isSafe report || seq {0 .. report.Length - 1} |> Seq.map (fun i -> report |> Array.mapi (fun ri x -> (ri, x)) |> Array.filter (fun (ri, x) -> ri<>i) |> Array.map (fun (ri, x) -> x)) |> Seq.exists isSafe
printfn "%A" (reports |> Seq.filter isSafeish |> Seq.length)