# Payload Analysis Index

Human-readable and machine-readable catalog of Oraculo payload analysis entries.

| Artifact | SHA256 | Type | Format | Human | SOC | AI | Raw |
|---|---|---|---|---|---|---|---|
| `82064` | `cad9e90cb8998664` | `payload` | `ELF32 big-endian executable/shared object, machine=MIPS, entry=0x400260` | [tpot/oraculo/sha256/ca/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/analysis/human_readable.md](tpot/oraculo/sha256/ca/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/analysis/human_readable.md) | [tpot/oraculo/sha256/ca/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/analysis/soc_brief.md](tpot/oraculo/sha256/ca/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/analysis/soc_brief.md) | [tpot/oraculo/sha256/ca/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/metadata/ai_context.json](tpot/oraculo/sha256/ca/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/metadata/ai_context.json) | [tpot/oraculo/sha256/ca/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/raw/README.md](tpot/oraculo/sha256/ca/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/raw/README.md) |

## Format policy

- Human learning material lives under `analysis/`.
- SOC/admin operational summaries live in `analysis/soc_brief.md`.
- AI/tool context lives in `metadata/ai_context.json`.
- Raw captured bytes, when archived, are stored as base64 text under `raw/`, never as directly runnable binaries.
