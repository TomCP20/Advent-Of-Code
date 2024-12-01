open System

let read _ = Console.ReadLine()
let isValid = function null -> false | _ -> true
let inputList = Seq.initInfinite read |> Seq.takeWhile isValid |> Seq.toList
printfn "%A" inputList