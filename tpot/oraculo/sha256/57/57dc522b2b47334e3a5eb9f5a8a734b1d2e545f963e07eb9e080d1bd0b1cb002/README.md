# 🧬 Payload Analysis

`57dc522b2b47334e3a5eb9f5a8a734b1d2e545f963e07eb9e080d1bd0b1cb002`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/57dc522b2b47334e3a5eb9f5a8a734b1d2e545f963e07eb9e080d1bd0b1cb002.md](../../../../../malware-like/oraculo/botnet/57dc522b2b47334e3a5eb9f5a8a734b1d2e545f963e07eb9e080d1bd0b1cb002.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `57dc522b2b47334e3a5eb9f5a8a734b1d2e545f963e07eb9e080d1bd0b1cb002`
- **SHA1:** `a2f0af01b60d87b6b1544387541381b23d85b72b`
- **MD5:** `a0538d419c520c2d91c50e7d12a97c14`

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
| hash | 57dc522b2b47334e3a5eb9f5a8a734b1d2e545f963e07eb9e080d1bd0b1cb002 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
