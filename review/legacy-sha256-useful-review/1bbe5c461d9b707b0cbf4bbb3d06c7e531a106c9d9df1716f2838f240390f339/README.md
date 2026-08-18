# 🧬 Payload Analysis

`1bbe5c461d9b707b0cbf4bbb3d06c7e531a106c9d9df1716f2838f240390f339`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificaron 2 comandos observados o extraídos. Se identificaron 4 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/1bbe5c461d9b707b0cbf4bbb3d06c7e531a106c9d9df1716f2838f240390f339.md](../../../../../malware-like/oraculo/botnet/1bbe5c461d9b707b0cbf4bbb3d06c7e531a106c9d9df1716f2838f240390f339.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:57:27.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1bbe5c461d9b707b0cbf4bbb3d06c7e531a106c9d9df1716f2838f240390f339`
- **SHA1:** `64c9c9124436ac5342b327235481a6b6e8f2488f`
- **MD5:** `6b332a93ed3a8972635b0204619d010d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 520 B |
| Entropía | 5.12 |
| Strings | 20 |

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
| hash | 1bbe5c461d9b707b0cbf4bbb3d06c7e531a106c9d9df1716f2838f240390f339 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
