# Logger Benchmarks

## Results

### Integer Benchmark, One Thread

| Library             |     50 |     75 |     90 |     95 |     99 |   99.9 |     Max | Version                |
|---------------------|--------|--------|--------|--------|--------|--------|---------|------------------------|
| xtr                 |   11   |   12   |   12.5 |   13   |   14   |   41   |    55.5 | 2.0.1                  |
| platformlab_nanolog |   11.5 |   11.5 |   12   |   12   |   12.5 |   14.5 |    33   | 85b71b6                |
| quill               |   12   |   13   |   13.5 |   14   |   14.5 |   16   |   530.5 | v2.0.2                 |
| reckless            |   17   |   17   |   17.5 |   17.5 |   19.5 |   21.5 |    38   | v3.0.3                 |
| ms_binlog           |   29.5 |   31   |   32   |   32.5 |   68   |  105.5 |   384   | 2020-04-26-82-g2de2fa0 |
| iyengar_nanolog     |  142   |  158   |  173.5 |  192.5 |  421   |  484   | 41490   | 3ffc74a                |
| spdlog              |  284.5 |  317   |  346   |  363.5 |  399.5 |  501.5 |   572.5 | v1.10.0                |
| g3log               | 2543   | 2637   | 2724   | 2779   | 2879   | 3015   |  3354   | 1.3.4                  |

### Integer Benchmark, Four Threads

| Library             |     50 |     75 |     90 |     95 |     99 |   99.9 |     Max | Version                |
|---------------------|--------|--------|--------|--------|--------|--------|---------|------------------------|
| xtr                 |   11   |   12   |   12.5 |   13.5 |   14.5 |   41.5 |    73   | 2.0.1                  |
| platformlab_nanolog |   11.5 |   12   |   12.5 |   12.5 |   13   |   17   |    33.5 | 85b71b6                |
| quill               |   13   |   14.5 |   15.5 |   16.5 |   18   |   21.5 |    23   | v2.0.2                 |
| reckless            |   18   |   19.5 |   20.5 |   20.5 |   21.5 |   28   |    65   | v3.0.3                 |
| ms_binlog           |   29.5 |   31   |   32   |   33   |   70.5 |  107.5 |   412   | 2020-04-26-82-g2de2fa0 |
| iyengar_nanolog     |  135   |  152.5 |  172   |  184   |  227   |  507.5 | 63290   | 3ffc74a                |
| spdlog              |  280.5 |  314.5 |  342.5 |  361.5 |  403.5 |  540.5 |   669.5 | v1.10.0                |
| g3log               | 2530   | 2624   | 2710   | 2767   | 2878   | 3017   |  7146   | 1.3.4                  |

### String Benchmark, One Thread

| Library             |     50 |     75 |     90 |     95 |     99 |   99.9 |     Max | Version                |
|---------------------|--------|--------|--------|--------|--------|--------|---------|------------------------|
| xtr                 |   12.5 |   13.5 |   14   |   14.5 |   16   |   41.5 |    51   | 2.0.1                  |
| platformlab_nanolog |   13.5 |   14   |   14.5 |   14.5 |   15.5 |   19   |    35.5 | 85b71b6                |
| quill               |   14.5 |   15.5 |   18   |   18.5 |   20   |   21.5 |    22.5 | v2.0.2                 |
| ms_binlog           |   34   |   35.5 |   36.5 |   38   |   75   |  109.5 |   389.5 | 2020-04-26-82-g2de2fa0 |
| reckless            |   44   |   47.5 |   49.5 |   50.5 |   52.5 |   79.5 |   134.5 | v3.0.3                 |
| iyengar_nanolog     |  120   |  150   |  166.5 |  181   |  379.5 |  492.5 | 41680   | 3ffc74a                |
| spdlog              |  255   |  299   |  344   |  373.5 |  484.5 | 1123   |  1602   | v1.10.0                |
| g3log               | 1975   | 2214   | 2340   | 2416   | 2536   | 2693   |  2888   | 1.3.4                  |

### String Benchmark, Four Threads

| Library             |     50 |     75 |     90 |     95 |     99 |   99.9 |    Max | Version                |
|---------------------|--------|--------|--------|--------|--------|--------|--------|------------------------|
| xtr                 |   13   |   13.5 |   14.5 |   15   |   16.5 |   46   |   66   | 2.0.1                  |
| platformlab_nanolog |   13.5 |   14   |   14.5 |   15   |   16.5 |   22   |   39   | 85b71b6                |
| quill               |   14.5 |   15.5 |   17   |   18   |   20   |   21.5 |   23.5 | v2.0.2                 |
| ms_binlog           |   34.5 |   36   |   37.5 |   38.5 |   75.5 |  115.5 |  408.5 | 2020-04-26-82-g2de2fa0 |
| reckless            |   44   |   48   |   50   |   51   |   52.5 |   68.5 |  216.5 | v3.0.3                 |
| iyengar_nanolog     |   96.5 |  132.5 |  161.5 |  174.5 |  229.5 |  487   | 8354   | 3ffc74a                |
| spdlog              |  256   |  301.5 |  349.5 |  379   |  495.5 | 1177   | 2071   | v1.10.0                |
| g3log               | 1911   | 2245   | 2380   | 2451   | 2582   | 2738   | 6578   | 1.3.4                  |

Note that these timings are not really percentiles, they are instead timings collected into
buckets, the average of the bucket is recorded, then percentiles of the bucket averages are
calculated.

## Test Environment

* Stock AMD 5950X
* Samsung 970 EVO Plus 1TB SSD
* GCC 11.2.0
* Linux 5.17.0-1-amd64, Debian "bookworm"
* SMT disabled
* CPU governor set to 'performance'
* Kernel command line parameters:
    - `mitigations=off`
    - `transparent_hugepage=never`
    - `isolcpus=1,2,3,4,5`
    - `nohz_full=1,2,3,4,5`
    - `rcu_nocbs=1,2,3,4,5`
    - `rcu_nocb_poll`
    - `processor.max_cstate=1`
    - `idle=poll`
    - `skew_tick=1`
* Run `irqbalance` (`IRQBALANCE_BANNED_CPULIST` is not set as irqbalance will automatically add isolated and nohz cpus to the banned list).
* Run `echo ffffffe1 > /sys/bus/workqueue/devices/writeback/cpumask` to prevent writeback tasks from running on isolated cores.
* RCU thread affinities will be `0,6-15` on boot.
* `amd_pstate` scaling driver (this made no difference to the results, it is only listed here for completeness).

## Changes From Upstream

* Reduced iterations from 100,000 to 10,000 as 10,000 was enough to get consistent results.
* The Reckless buffer size was increased to 512KB (default is 64KB).
* Affinity settings were applied to the Reckless background thread.
* The Iyengar roll size was increased to 10GB.
* PlatformLab's Config.h was modified; `O_DSYNC` was removed from from
  `FILE_PARAMS`, `POLL_INTERVAL_NO_WORK_US` was set to `0` and
  `POLL_INTERVAL_DURING_IO_US` was set to `0` (see `platformlab.patch`).
* PlatformLab's background thread has affinity set. This made a big improvement in
  performance---without this it would often run at around 30ns.
* Use cores 1-5 instead of 0-5 as core 0 is by default used as a 'housekeeping'
  core which cannot have `nohz_full` enabled.
* Turned on link time optimization.
* Other minor changes:
    - Changed `static` variables holding RNG state in the `wait()` function to
      `thread_local` as they are mutated by multiple threads.
    - TSC frequency is estimated once and cached.
    - Added fractions to timings.

## Building

```
mkdir build
cd build
conan install ../third_party/xtr -g cmake_find_package
cmake .. -DCMAKE_MODULE_PATH=${PWD}
```
