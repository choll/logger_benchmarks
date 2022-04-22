# Logger Benchmarks

## Results

### Integer Benchmark, One Thread

| Library             |   50 |   75 |   90 |   95 |   99 |   99.9 |   Max | Version           |
|---------------------|------|------|------|------|------|--------|-------|-------------------|
| xtr                 |    8 |    8 |    8 |    8 |    8 |      9 |    16 | 2.0.0             |
| platformlab_nanolog |    8 |   13 |   22 |   28 |   33 |     39 |    44 | 85b71b6           |
| reckless            |   12 |   13 |   13 |   13 |   13 |     13 |  4515 | v3.0.3            |
| quill               |   15 |   15 |   15 |   15 |   15 |     16 |    45 | v1.6.3            |
| ms_binlog           |   24 |   24 |   25 |   25 |   27 |     32 |    41 | 2021-04-16        |
| iyengar_nanolog     |   47 |   48 |   52 |   72 |  102 |    117 |   166 | 3ffc74a           |
| spdlog              |  212 |  217 |  226 |  230 |  237 |    277 |   367 | v1.10.0           |
| g3log               | 1427 | 2005 | 2044 | 2073 | 2608 |   2723 |  2966 | 1.3.4-19-gc51128f |

### Integer Benchmark, Four Threads

| Library             |   50 |   75 |   90 |   95 |   99 |   99.9 |   Max | Version           |
|---------------------|------|------|------|------|------|--------|-------|-------------------|
| xtr                 |    8 |    8 |    8 |    8 |    8 |      9 |    75 | 2.0.0             |
| platformlab_nanolog |    8 |    8 |   11 |   14 |   23 |     31 |    51 | 85b71b6           |
| reckless            |   13 |   13 |   13 |  332 | 1726 |   2775 | 51201 | v3.0.3            |
| quill               |   13 |   14 |   15 |   15 |   17 |     41 | 59487 | v1.6.3            |
| ms_binlog           |   24 |   24 |   25 |   25 |   27 |     32 |    42 | 2021-04-16        |
| iyengar_nanolog     |   94 |   98 |  114 |  146 |  177 |    222 |   269 | 3ffc74a           |
| spdlog              |  251 |  352 |  481 |  550 |  708 |    885 |  1059 | v1.10.0           |
| g3log               | 1569 | 1727 | 1872 | 1971 | 2148 |   2285 |  2431 | 1.3.4-19-gc51128f |


### String Benchmark, One Thread

| Library             |   50 |   75 |   90 |   95 |   99 |   99.9 |   Max | Version           |
|---------------------|------|------|------|------|------|--------|-------|-------------------|
| xtr                 |   11 |   12 |   13 |   15 |   16 |     19 |    24 | 2.0.0             |
| platformlab_nanolog |   14 |   15 |   17 |   18 |   24 |     37 |    80 | 85b71b6           |
| quill               |   15 |   17 |   18 |   19 |   22 |     59 |   125 | v1.6.3            |
| ms_binlog           |   27 |   27 |   27 |   27 |   28 |     29 |    49 | 2021-04-16        |
| reckless            |   32 |   36 |   40 |   41 |   55 |     64 |  1438 | v3.0.3            |
| iyengar_nanolog     |   59 |   67 |   77 |   79 |   98 |    161 |   225 | 3ffc74a           |
| spdlog              |  202 |  215 |  239 |  265 |  347 |    458 |   527 | v1.10.0           |
| g3log               | 1066 | 1090 | 1519 | 1575 | 1823 |   2284 |  2427 | 1.3.4-19-gc51128f |

### String Benchmark, Four Threads

| Library             |   50 |   75 |   90 |   95 |   99 |   99.9 |    Max | Version           |
|---------------------|------|------|------|------|------|--------|--------|-------------------|
| xtr                 |   12 |   13 |   15 |   16 |   19 |     19 |   2411 | 2.0.0             |
| platformlab_nanolog |   14 |   16 |   17 |   20 |   24 |     66 |    165 | 85b71b6           |
| quill               |   15 |   17 |   19 |   22 |   92 |    135 | 121839 | v1.6.3            |
| ms_binlog           |   27 |   28 |   29 |   31 |   36 |     43 |  36385 | 2021-04-16        |
| reckless            |   35 |   40 |   48 |   59 |  400 |  15678 |  53942 | v3.0.3            |
| iyengar_nanolog     |  104 |  129 |  160 |  181 |  227 |    291 |    428 | 3ffc74a           |
| spdlog              |  261 |  408 |  550 |  657 |  897 |   1298 |   1747 | v1.10.0           |
| g3log               | 1565 | 1701 | 1815 | 1883 | 2024 |   2246 |   2597 | 1.3.4-19-gc51128f |

Note that these timings are not really percentiles, they are instead timings collected into
buckets, the average of the bucket is recorded, then percentiles of the bucket averages are
calculated.

## Test Environment

* Stock AMD 5950X
* Samsung 970 EVO Plus 1TB SSD
* GCC 11.2.0
* Linux 5.16.0-6-amd64, Debian "bookworm"
* SMT disabled
* cpupower governor set to 'performance'
* Kernel command line parameters:
    - `mitigations=off`
    - `transparent_hugepage=never`
    - `isolcpus=0,1,2,3,4`
    - `nohz_full=0,1,2,3,4`
    - `rcu_nocbs=0,1,2,3,4`
    - `rcu_nocb_poll`
    - `processor.max_cstate=1`
    - `idle=poll`
    - `skew_tick=1`
* Run `irqbalance` (`IRQBALANCE_BANNED_CPULIST` is not set as irqbalance will automatically add isolated and nohz cpus to the banned list).
* Run ``for i in `pgrep rcu[^c]`; do taskset -pc 5-15 $i; done`` to move RCU threads away from isolated cores.
* Run `echo ffffffe0 > /sys/bus/workqueue/devices/writeback/cpumask` to prevent bdi-flush threads from running on isolated cores.

## Changes From Upstream

* The Reckless buffer size was increased to 512KB (default is 64KB).
* Affinity settings were applied to the Reckless worker thread.
* The Iyengar roll size was increased to 10GB.
* PlatformLab's Config.h was modified; `O_DSYNC` was removed from from
  `FILE_PARAMS`, `POLL_INTERVAL_NO_WORK_US` was set to `0` and
  `POLL_INTERVAL_DURING_IO_US` was set to `0`.
* The number of messages in the test loop was increased to 1000 to ensure
  stable readings for all loggers---PlatformLab, Reckless and XTR had timings
  that were sometimes fast but mostly unexpectedly slow with only 20 messages.
  Possibly 20 messages is too low for frequency-scaling to occur.

# Notes

* PlatformLab runs either at 7-8ns or ~30ns, possibly the number of messages
  needs to be increased further.

## Building

```
mkdir build
cd build
conan install ../third_party/xtr -g cmake_find_package
cmake .. -DCMAKE_MODULE_PATH=${PWD}
```
