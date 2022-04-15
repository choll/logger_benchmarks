# Logger Benchmarks

## Results

### Integer Benchmark, One Thread:

| Library             |   50 |   75 |   90 |   95 |   99 |   99.9 |   Max | Version           |
|---------------------|------|------|------|------|------|--------|-------|-------------------|
| xtr                 |    7 |    7 |    8 |    8 |    8 |      9 |    20 | 2.0.0             |
| platformlab_nanolog |    8 |   30 |   30 |   33 |   45 |     51 |    55 | 85b71b6           |
| reckless            |   12 |   12 |   12 |   13 |   13 |     21 |   902 | v3.0.3            |
| quill               |   14 |   14 |   14 |   15 |   15 |     15 |    17 | v1.6.3            |
| ms_binlog           |   23 |   23 |   24 |   24 |   26 |     32 |    37 | 2021-04-16        |
| iyengar_nanolog     |   98 |  106 |  112 |  116 |  127 |    147 |   204 | 3ffc74a           |
| spdlog              |  184 |  189 |  194 |  197 |  206 |    221 |   357 | v1.10.0           |
| g3log               | 1891 | 1948 | 1976 | 1992 | 2362 |   2447 |  3132 | 1.3.4-19-gc51128f |

### Integer Benchmark, Four Threads:

| Library             |   50 |   75 |   90 |   95 |   99 |   99.9 |   Max | Version           |
|---------------------|------|------|------|------|------|--------|-------|-------------------|
| xtr                 |    7 |    8 |    8 |    8 |    8 |     25 |   148 | 2.0.0             |
| reckless            |   12 |  630 | 1103 | 1270 | 1999 |   2523 |  9210 | v3.0.3            |
| quill               |   13 |   14 |   14 |   14 |   15 |     50 | 59492 | v1.6.3            |
| ms_binlog           |   23 |   24 |   24 |   24 |   27 |     63 |   167 | 2021-04-16        |
| platformlab_nanolog |   29 |   31 |   34 |   41 |   50 |     87 |   168 | 85b71b6           |
| iyengar_nanolog     |  103 |  132 |  157 |  181 |  222 |    282 |   398 | 3ffc74a           |
| spdlog              |  204 |  303 |  436 |  492 |  639 |    798 |   939 | v1.10.0           |
| g3log               | 1850 | 1951 | 2048 | 2107 | 2247 |   2504 |  3084 | 1.3.4-19-gc51128f |

### String Benchmark, One Thread:

| Library             |   50 |   75 |   90 |   95 |   99 |   99.9 |   Max | Version           |
|---------------------|------|------|------|------|------|--------|-------|-------------------|
| xtr                 |    8 |    8 |    8 |    8 |    8 |      9 |    21 | 2.0.0             |
| quill               |   12 |   13 |   13 |   13 |   14 |     17 |    33 | v1.6.3            |
| reckless            |   25 |   26 |   26 |   27 |   38 |     42 |   388 | v3.0.3            |
| ms_binlog           |   26 |   26 |   26 |   26 |   26 |     29 |    52 | 2021-04-16        |
| platformlab_nanolog |   34 |   35 |   38 |   45 |   61 |     69 |    73 | 85b71b6           |
| iyengar_nanolog     |   77 |   89 |   97 |  101 |  110 |    122 |   152 | 3ffc74a           |
| spdlog              |  187 |  191 |  194 |  196 |  202 |    225 |   282 | v1.10.0           |
| g3log               | 1587 | 1667 | 2092 | 2139 | 2197 |   2247 |  2585 | 1.3.4-19-gc51128f |

### String Benchmark, Four Threads:

| Library             |   50 |   75 |   90 |   95 |   99 |   99.9 |   Max | Version           |
|---------------------|------|------|------|------|------|--------|-------|-------------------|
| xtr                 |    8 |    8 |    8 |    8 |    8 |     48 |  5314 | 2.0.0             |
| platformlab_nanolog |    9 |   15 |   34 |   37 |   57 |     70 |   170 | 85b71b6           |
| quill               |   12 |   12 |   13 |   13 |   40 |     90 | 60563 | v1.6.3            |
| reckless            |   23 |   28 |  291 |  307 |  346 |    493 |  5878 | v3.0.3            |
| ms_binlog           |   26 |   26 |   27 |   27 |   27 |     83 |   170 | 2021-04-16        |
| iyengar_nanolog     |   89 |   92 |  112 |  141 |  171 |    222 |   316 | 3ffc74a           |
| spdlog              |  176 |  244 |  390 |  443 |  596 |    755 |   934 | v1.10.0           |
| g3log               | 1636 | 1737 | 1835 | 1897 | 2035 |   2238 |  2720 | 1.3.4-19-gc51128f |

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
    - `noibrs`
    - `noibpb`
    - `no_stf_barrier`
    - `mitigations=off`
    - `transparent_hugepage=never`
    - `isolcpus=0,1,2,3,4`
    - `nohz_full=0,1,2,3,4`
    - `rcu_nocbs=0,1,2,3,4`
    - `rcu_nocb_poll`

## Notes

* The Reckless buffer size was increased to 256KB (default is 64KB).
* Affinity settings were applied to the Reckless worker thread.
* The Iyengar roll size was increased to 10GB.
* The number of messages in the test loop was increased to 1000 to ensure
  stable readings for all loggers. The default of 20 is possibly too low,
  resulting in frequency-scaling not occurring. PlatformLab, Reckless and XTR
  all had unexpectedly high timings with only 20 messages.
* PlatformLab runs either at 7-8ns or ~30ns, possibly the number of messages
  needs to be increased further.

## Building

```
mkdir build
cd build
conan install ../third_party/xtr -g cmake_find_package
cmake .. -DCMAKE_MODULE_PATH=${PWD}
```
