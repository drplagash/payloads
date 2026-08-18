# Raw Captured Sample Archive

This directory stores the captured payload bytes as inert base64 text.

## Files

- `sample.b64.txt`: base64-encoded captured bytes.
- `sample.sha256.txt`: expected SHA256 for decoded bytes.
- `manifest.json`: metadata and safety note.

## Artifact

- Artifact ID: `82064`
- SHA256: `cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41`
- Size: `448624` bytes
- Source URL: `hxxp://154[.]90[.]70[.]23/mips`

## Safety note

The raw executable is not stored as a directly runnable ELF/binary file. To prevent accidental execution, the captured bytes are represented as base64 text. Decode only inside an isolated malware-analysis lab.
