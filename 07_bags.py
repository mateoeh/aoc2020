import re
from dataclasses import dataclass

from typing import List, Dict


class Rule:
    outer: str
    inner: List[str]

    def __init__(self, rule_str: str):
        rule_str = re.sub(" bags?\\.?", "", rule_str)
        parts = rule_str.split(" contain ")
        self.outer = parts[0]
        self.inner = parts[1].split(", ")


with open("inputs/7") as f:
    rules = [Rule(r) for r in f.read().rstrip().split("\n")]


def bag_types(rules, target, output_set):
    for rule in rules:
        for bag in rule.inner:
            color = bag.split(" ", 1)[1]
            if color == target:
                output_set.add(rule.outer)
                bag_types(rules, rule.outer, output_set)


# Problem 1
output = set()
bag_types(rules, "shiny gold", output)
print(len(output))


def num_bags(rule_map: Dict[str, Rule], target):
    total = 0
    for bag in rule_map[target].inner:
        num, color = bag.split(" ", 1)
        if num == "no":
            return 0
        total += int(num)
        total += int(num) * num_bags(rule_map, color)
    return total


rule_map = {r.outer: r for r in rules}
print(num_bags(rule_map, "shiny gold"))
