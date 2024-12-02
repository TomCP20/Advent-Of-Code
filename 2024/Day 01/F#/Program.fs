open System

let read _ = Console.ReadLine()
let isValid = function null -> false | _ -> true
let inputList: string list = Seq.initInfinite read |> Seq.takeWhile isValid |> Seq.toList
let lists = [ for item: string in inputList -> item.Split "   "] 
let left = [ for item in lists -> int(item[0])]
let right = [ for item in lists -> int(item[1])]

printfn "%A" (List.sumBy (fun (l, r) -> abs (l-r)) (List.zip (List.sort left) (List.sort right)))

let count =  right |> Seq.countBy id |> Map.ofSeq
printfn "%A" (List.sumBy (fun x -> x*(count.TryFind(x) |> Option.defaultValue 0)) left)