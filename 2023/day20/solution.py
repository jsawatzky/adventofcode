import sys
from functools import reduce
from collections import defaultdict
from copy import deepcopy
from operator import itemgetter
from math import lcm

def parse(f):
    modules = {}
    inputs = defaultdict(list)
    outputs = {}
    for l in [l.strip() for l in f if l.strip()]:
        mod, rest = l.split(' -> ')
        dests = rest.split(', ')
        if mod == 'broadcaster':
            outputs[mod] = dests
            for d in dests:
                inputs[d].append(mod)
            continue
        t, n = mod[0], mod[1:]
        modules[n] = (t, False if t == '%' else {})
        outputs[n] = dests
        for d in dests:
            inputs[d].append(n)

    for k, v in modules.items():
        if v[0] == '&':
            for i in inputs[k]:
                v[1][i] = False

    return modules, inputs, outputs

def part1(f):
    modules, _, outputs = parse(f)

    start = deepcopy(modules)

    presses = []
    while len(presses) < 1000:
        pulses = {'H': 0, 'L': 1}
        signals = [(d, 'L', 'broadcaster') for d in outputs['broadcaster']]
        while signals:
            # for (d, s, f) in signals:
            #     print(f'{f} -{"high" if s == "H" else "low"}-> {d}')
            nextSignals = []
            nextModules = deepcopy(modules)
            for (d, s, f) in signals:
                pulses[s] += 1
                if d not in modules:
                    continue
                if modules[d][0] == '%' and s == 'L':
                    nextModules[d] = ('%', not modules[d][1])
                    nextSignals.extend([(d2, 'H' if nextModules[d][1] else 'L', d) for d2 in outputs[d]])
                elif modules[d][0] == '&':
                    nextModules[d][1][f] = s == 'H'
                    nextSignals.extend([(d2, 'L' if all(nextModules[d][1].values()) else 'H', d) for d2 in outputs[d]])
            signals = nextSignals
            modules = nextModules
        presses.append(pulses)
        if modules == start:
            break

    loops = 1000 // len(presses)
    extra = 1000 % len(presses)
    return (loops*sum(map(itemgetter('H'), presses)) + sum(map(itemgetter('H'), presses[:extra]))) * (loops*sum(map(itemgetter('L'), presses)) + sum(map(itemgetter('L'), presses[:extra])))

def part2(f):
    modules, inputs, outputs = parse(f)

    preRx = inputs['rx'][0]
    counts = {m: 0 for m in inputs[preRx]}

    presses = 0
    while True:
        presses += 1
        signals = [(d, 'L', 'broadcaster') for d in outputs['broadcaster']]
        while signals:
            nextSignals = []
            nextModules = deepcopy(modules)
            for (d, s, f) in signals:
                if d == preRx and s == 'H':
                    counts[f] = counts[f] if counts[f] > 0 else presses
                    if all(map(lambda x: x > 0, counts.values())):
                        return lcm(*counts.values())
                if d not in modules:
                    continue
                if modules[d][0] == '%' and s == 'L':
                    nextModules[d] = ('%', not modules[d][1])
                    nextSignals.extend([(d2, 'H' if nextModules[d][1] else 'L', d) for d2 in outputs[d]])
                elif modules[d][0] == '&':
                    nextModules[d][1][f] = s == 'H'
                    nextSignals.extend([(d2, 'L' if all(nextModules[d][1].values()) else 'H', d) for d2 in outputs[d]])
            signals = nextSignals
            modules = nextModules

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))