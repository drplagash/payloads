# Cleanup Status

Repository cleanup completed.

## Final state

```text
Confirmed payload samples:        1
Legacy review entries:        24739
Archived weak/noise entries:  14998
Archived unknown/noise:        4370
Archived false-useful noise:    454
Legacy SHA tree remaining:        0
```

## Completed migrations

The old layout:

```text
tpot/oraculo/sha256/<prefix>/<sha256>/
```

was replaced by:

```text
payloads/samples/                 # confirmed samples
review/legacy-sha256-useful-review/
archive/
intel/
detections/
```

## Result

The repository is now organized by artifact meaning instead of raw SHA sprawl.

The old SHA tree is empty.
