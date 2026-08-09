# 🧬 Payload Analysis

`336ffb224663e829c38692610b3f7afcd5bfdf64fe85e4c67f000a313d2ae78b`

## 📌 Resumen

Artefacto de 548 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `mailm` en `hxxps://lists[.]wikimedia[.]org/mailm`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `336ffb224663e829c38692610b3f7afcd5bfdf64fe85e4c67f000a313d2ae78b`
- **SHA1:** `a3aec37c0c23fbb8910e1f0bd5a6edd2b8523760`
- **MD5:** `a092166abfbed5f3c20e7f8181f6a254`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.31 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://lists[.]wikimedia[.]org/mailm | strings |
| url | hxxps://www[.]mediawiki[.]org/wiki/Special:MyLanguage/Manual:FAQ | strings |
| url | hxxps://www[.]mediawiki[.]org/wiki/Special:MyLanguage/Manual:Configuration_settings | strings |
| hash | 336ffb224663e829c38692610b3f7afcd5bfdf64fe85e4c67f000a313d2ae78b | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
