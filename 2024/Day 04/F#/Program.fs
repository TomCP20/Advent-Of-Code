open System
open System.Text.RegularExpressions

let read _ = Console.ReadLine()
let isValid = function null -> false | _ -> true
let lines = Seq.initInfinite read |> Seq.takeWhile isValid |> Seq.map (fun line -> "..." + line + "...") |> Seq.toArray
let input = lines |> String.concat ""
let row = lines |> Seq.head |> fun f -> f.Length 

printfn "%A" ([|0; row; row-1; row-2|] |> Array.map string |> Array.map (fun o -> @"(?=(X.{" + o + @"}M.{" + o + @"}A.{" + o + @"}S|S.{" + o + @"}A.{" + o + @"}M.{" + o + @"}X))") |> Array.map (fun p -> Regex(p).Matches(input).Count) |> Array.sum)

let n = string(row-2)
printfn "%A" ([|"MMSS"; "MSMS"; "SMSM"; "SSMM"|] |> Array.map (fun perm -> @"(?=(" + string perm[0] + @"." + string perm[1] + @".{" + n + @"}A.{" + n + @"}" + string perm[2] + @"." + string perm[3] + @"))") |> Array.map (fun p -> Regex(p).Matches(input).Count) |> Array.sum)