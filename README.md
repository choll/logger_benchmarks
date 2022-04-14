# Logger Benchmarks

## Results

### One thread:

| Library             |   50 |   75 |   90 |   95 |   99 |   99.9 |   Max | Version           |
|---------------------|------|------|------|------|------|--------|-------|-------------------|
| xtr                 |    7 |    8 |    8 |    8 |    8 |     27 |    30 | 2.0.0             |
| platformlab_nanolog |    7 |   10 |   21 |   25 |   33 |     50 |    65 | 3377bb5           |
| reckless            |   12 |   12 |   13 |   13 |   13 |    104 | 36350 | v3.0.3            |
| quill               |   14 |   14 |   14 |   14 |   15 |     34 |    40 | v1.6.3            |
| ms_binlog           |   23 |   23 |   23 |   24 |   26 |     43 | 14124 | 2021-04-16        |
| iyengar_nanolog     |   53 |   59 |   65 |   70 |   83 |    115 |   154 | 3377bb5           |
| spdlog              |  206 |  212 |  224 |  232 |  267 |    354 |   395 | v1.10.0           |
| g3log               | 1303 | 1941 | 2303 | 2433 | 2518 |   2603 |  2763 | 1.3.4-19-gc51128f |

### Four threads:

| Library             |   50 |   75 |   90 |   95 |   99 |   99.9 |   Max | Version           |
|---------------------|------|------|------|------|------|--------|-------|-------------------|
| xtr                 |    7 |    8 |    8 |    8 |    8 |     12 |   112 | 2.0.0             |
| platformlab_nanolog |    7 |    8 |   18 |   22 |   30 |     51 |   208 | 3377bb5           |
| reckless            |   12 |  622 | 1103 | 1277 | 1969 |   2581 | 47217 | v3.0.3            |
| quill               |   13 |   13 |   14 |   14 |   15 |     46 | 49979 | v1.6.3            |
| ms_binlog           |   23 |   23 |   24 |   24 |   27 |     54 |   155 | 2021-04-16        |
| iyengar_nanolog     |   89 |   93 |  113 |  143 |  178 |    230 |   307 | 3377bb5           |
| spdlog              |  201 |  303 |  437 |  498 |  656 |    829 |   933 | v1.10.0           |
| g3log               | 1822 | 1939 | 2048 | 2110 | 2222 |   2413 |  4430 | 1.3.4-19-gc51128f |

Note that these timings are not really percentiles, they are instead timings collected into
buckets, the average of the bucket is recorded, then percentiles of the bucket averages are
calculated.

## Test Environment

* Stock AMD 5950X
* GCC 11.2.0
* Linux 5.16.0-6-amd64, Debian "bookworm"
* SMT disabled
* cpupower governor set to 'performance'
* Kernel command line parameters:
** `noibrs`
** `noibpb`
** `no_stf_barrier`
** `mitigations=off`
** `transparent_hugepage=never`
** `isolcpus=0,1,2,3,4`
** `nohz_full=0,1,2,3,4`
** `rcu_nocbs=0,1,2,3,4`
** `rcu_nocb_poll`

## Notes

* The Reckless buffer size was increased to 256KB (default is 64KB).
* Affinity settings were applied to the Reckless worker thread.
* The Iyengar roll size was increased to 10GB.
* The number of messages in the test loop was increased to 1000 to ensure
  stable readings for all loggers. The default of 20 is possibly too low,
  resulting in frequency-scaling not occurring. PlatformLab, Reckless and XTR
  all had unexpectedly high timings with only 20 messages.

## Building

```
mkdir build
cd build
conan install ../third_party/xtr -g cmake_find_package
cmake .. -DCMAKE_MODULE_PATH=${PWD}
```
