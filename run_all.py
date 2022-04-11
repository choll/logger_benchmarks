#!/usr/bin/python3

import json
import subprocess
from tabulate import tabulate

root_dir = "build/benchmarks/call_site_latency"
loggers = ["g3log", "iyengar_nanolog", "ms_binlog", "platformlab_nanolog", "quill", "reckless", "spdlog", "xtr"]

results_map = {}
versions = {}

for name in loggers:
    try:
        version = subprocess.check_output(["git", "describe", "--tags"], cwd="third_party/{}".format(name), stderr=subprocess.DEVNULL)
    except:
        version = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd="third_party/{}".format(name))
    versions[name] = version

for name in loggers:
    bench = "{}/benchmark_{}_call_site_latency".format(root_dir,name)

    print("Running {}".format(name))

    results = json.loads(subprocess.check_output(bench))

    for result in results:
        if not result["thread_count"] in results_map:
            results_map[result["thread_count"]] = {}
        results_map[result["thread_count"]][name] = result

for thread_count in results_map:
    table = []

    for name in results_map[thread_count]:
        table += [[name] + results_map[thread_count][name]["centiles"] + [versions[name]]]

    table.sort(key=lambda row: (row[1], row[2], row[3])) # Sort by median

    print(tabulate(table, headers=["Library", "50", "75", "90", "95", "99", "99.9", "Max", "Version"], tablefmt="github"))
