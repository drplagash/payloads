# 🧬 Payload Analysis

`2b04927ee6f6733dd91f1e5b89fd447be1c2d81616abf68157c056377573cfdb`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificaron 2 comandos observados o extraídos. Se identificaron 4 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/2b04927ee6f6733dd91f1e5b89fd447be1c2d81616abf68157c056377573cfdb.md](../../../../../malware-like/oraculo/botnet/2b04927ee6f6733dd91f1e5b89fd447be1c2d81616abf68157c056377573cfdb.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:57:27.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2b04927ee6f6733dd91f1e5b89fd447be1c2d81616abf68157c056377573cfdb`
- **SHA1:** `cf243612d88a081dadc0e79970f0096e47e4e53f`
- **MD5:** `44f089a398c09e78312d7ac680efee65`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 423 B |
| Entropía | 5.12 |
| Strings | 16 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
User-Agent: Wget/1.25.0 (linux-gnu)
User-Agent: curl/7.38.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 185.228.26.XXX | static_analysis |
| command | User-Agent: Wget/1.25.0 (linux-gnu) | strings |
| command | User-Agent: curl/7.38.0 | strings |
| hash | 2b04927ee6f6733dd91f1e5b89fd447be1c2d81616abf68157c056377573cfdb | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
