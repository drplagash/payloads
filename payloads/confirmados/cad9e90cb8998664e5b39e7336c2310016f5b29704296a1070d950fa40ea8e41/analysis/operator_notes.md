# Operator Notes

Artifact: `82064`  
SHA256: `cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41`  
SHA1: `5e848778ec4fbfddc94b5a76e5a56bf2e5173ce3`  
MD5: `620c007093f64dfe672252c0bd483f25`  
Size: `448624` bytes  
Format: `ELF32 big-endian, machine=MIPS, entry=0x400260`  
Source URL: `hxxp://154[.]90[.]70[.]23/mips`  
State: `needs_review`  
Quarantined: `1`

## What to read first

1. `analysis/human_readable.md`
2. `analysis/strings_annotated.md`
3. `analysis/pseudocode_notes.md`
4. `analysis/disassembly_entry.txt`
5. `analysis/iocs.json`
6. YARA rule under `yara/`

## Analyst note

This is not a shell script. It is a compiled MIPS payload, so readable output means annotated reverse-engineering notes, not original source.
