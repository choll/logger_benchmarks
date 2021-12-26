#!/usr/bin/python

import subprocess

root_dir = "build/benchmarks/call_site_latency/"

benchmark_quill_no_dual_mode_unbounded = "benchmark_quill_no_dual_mode_unbounded_call_site_latency"
benchmark_quill_dual_mode_unbounded = "benchmark_quill_dual_mode_unbounded_call_site_latency"
benchmark_quill_dual_mode_bounded = "benchmark_quill_dual_mode_bounded_call_site_latency"
benchmark_g3log = "benchmark_g3log_call_site_latency"
benchmark_iyengar_nanolog = "benchmark_iyengar_nanolog_call_site_latency"
benchmark_ms_binlog = "benchmark_ms_binlog_call_site_latency"
benchmark_platformlab = "benchmark_platformlab_call_site_latency"
benchmark_reckless = "benchmark_reckless_call_site_latency"
benchmark_spdlog = "benchmark_spdlog_call_site_latency"
benchmark_xtr = "benchmark_xtr_call_site_latency"

benchmarks = [benchmark_quill_no_dual_mode_unbounded, benchmark_quill_dual_mode_unbounded, benchmark_quill_dual_mode_bounded, benchmark_platformlab, benchmark_ms_binlog, benchmark_spdlog, benchmark_g3log, benchmark_iyengar_nanolog, benchmark_reckless, benchmark_xtr]

for benchname in benchmarks:
    s = "bench_results_{}.txt".format(benchname)
    bench = root_dir + benchname
    print("Writing to {} for {}".format(s, bench))
    output = open(s, "w")

    print("Running {}".format(bench))
    subprocess.call(bench, stdout=output)
