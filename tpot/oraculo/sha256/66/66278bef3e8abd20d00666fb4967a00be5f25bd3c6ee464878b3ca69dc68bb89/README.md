# 🧬 Payload Analysis

`66278bef3e8abd20d00666fb4967a00be5f25bd3c6ee464878b3ca69dc68bb89`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `66278bef3e8abd20d00666fb4967a00be5f25bd3c6ee464878b3ca69dc68bb89`
- **SHA1:** `521a6c73d204e1058be8dcff94b5379cf01a01b8`
- **MD5:** `7696ed76ff710b3845b90c9cd8e87b72`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 182 B |
| Entropía | 5.36 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: Wget/1.21.4 (HelpMeEscapeFromBelarus@proton.me)
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| hash | 66278bef3e8abd20d00666fb4967a00be5f25bd3c6ee464878b3ca69dc68bb89 | static_analysis |
| command | User-Agent: Wget/1.21.4 (HelpMeEscapeFromBelarus@proton.me) | strings |
| ip | 124.164.251.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
