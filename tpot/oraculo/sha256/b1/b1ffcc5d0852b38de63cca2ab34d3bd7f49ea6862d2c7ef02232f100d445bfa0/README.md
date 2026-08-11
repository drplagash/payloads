# 🧬 Payload Analysis

`b1ffcc5d0852b38de63cca2ab34d3bd7f49ea6862d2c7ef02232f100d445bfa0`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/b1ffcc5d0852b38de63cca2ab34d3bd7f49ea6862d2c7ef02232f100d445bfa0.md](../../../../../malware-like/oraculo/botnet/b1ffcc5d0852b38de63cca2ab34d3bd7f49ea6862d2c7ef02232f100d445bfa0.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b1ffcc5d0852b38de63cca2ab34d3bd7f49ea6862d2c7ef02232f100d445bfa0`
- **SHA1:** `dbabe2b28d42ff01ddbde0df5af785d5105c27e2`
- **MD5:** `f047957a6d63cd53c068d76de853572e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.79 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.61.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.61.1 | strings |
| hash | b1ffcc5d0852b38de63cca2ab34d3bd7f49ea6862d2c7ef02232f100d445bfa0 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
