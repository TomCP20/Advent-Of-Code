"""Advent of Code - 2023 - Day 20"""


import copy


def part_1(modules: dict[str, tuple[str, list[str], str | dict[str, str] | None]]):
    """Solves part 1"""
    low_count = 0
    high_count = 0

    for _ in range(1000):
        queue: list[tuple[str, str, str]] = [("button", "low", "broadcaster")]
        while queue:
            source, signal, name = queue.pop(0)
            if signal == "low":
                low_count += 1
            elif signal == "high":
                high_count += 1
            else:
                assert False, signal
            module_type, destinations, state = modules[name]
            match module_type:
                case "broadcaster":
                    for destination in destinations:
                        queue.append((name, signal, destination))
                case "flip-flop":
                    if signal == "low":
                        if state == "off":
                            state = "on"
                            out = "high"
                        elif state == "on":
                            state = "off"
                            out = "low"
                        else:
                            assert False, state
                        for destination in destinations:
                            queue.append((name, out, destination))
                case "conjunction":
                    assert isinstance(state, dict)
                    state[source] = signal
                    if all(val == "high" for val in state.values()):
                        out = "low"
                    else:
                        out = "high"
                    for destination in destinations:
                        queue.append((name, out, destination))
                case "output":
                    pass
                case _:
                    assert False, module_type
            modules[name] = (module_type, destinations, state)

    return low_count * high_count

def part_2(modules: dict[str, tuple[str, list[str], str | dict[str, str] | None]]):
    """Solves part 2"""
    result = 1
    to_activate = {"bh", "jf", "sh", "mz"} # hardcoded

    for i in range(1, 20_000):
        queue: list[tuple[str, str, str]] = [("button", "low", "broadcaster")]
        while queue:
            source, signal, name = queue.pop(0)
            module_type, destinations, state = modules[name]
            match module_type:
                case "broadcaster":
                    for destination in destinations:
                        queue.append((name, signal, destination))
                case "flip-flop":
                    if signal == "low":
                        if state == "off":
                            state = "on"
                            out = "high"
                        elif state == "on":
                            state = "off"
                            out = "low"
                        else:
                            assert False, state
                        for destination in destinations:
                            queue.append((name, out, destination))
                case "conjunction":
                    assert isinstance(state, dict)
                    state[source] = signal
                    if all(val == "high" for val in state.values()):
                        out = "low"
                    else:
                        out = "high"
                    if name in to_activate and out == "high":
                        to_activate.remove(name)
                        result *= i
                    for destination in destinations:
                        queue.append((name, out, destination))
                case "output":
                    pass
                case _:
                    assert False, module_type
            modules[name] = (module_type, destinations, state)
    return result


def main():
    """Solves Part 1 and 2 of Day 20"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
    modules: dict[str, tuple[str, list[str], str | dict[str, str] | None]] = {}
    for line in lines:
        name, destinations = line.split(" -> ")
        destinations = destinations.split(", ")
        if name[0] == "%":
            name = name[1:]
            modules[name] = ("flip-flop", destinations, "off")
        elif name[0] == "&":
            name = name[1:]
            modules[name] = ("conjunction", destinations, {})
        else:
            modules[name] = ("broadcaster", destinations, None)

    to_add: dict[str, tuple[str, list[str], str | dict[str, str] | None]] = {}
    for name, module in modules.items():
        for destination in module[1]:
            if destination not in modules:
                to_add[destination] = ("output", [], None)
            elif modules[destination][0] == "conjunction":
                conjunction_module_state = modules[destination][2]
                assert isinstance(conjunction_module_state, dict)
                conjunction_module_state[name] = "low"
    modules.update(to_add)

    print(part_1(copy.deepcopy(modules)))
    print(part_2(modules))



main()
