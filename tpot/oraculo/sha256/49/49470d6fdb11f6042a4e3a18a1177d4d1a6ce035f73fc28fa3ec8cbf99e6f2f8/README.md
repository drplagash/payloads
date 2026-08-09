# 🧬 Payload Analysis

`49470d6fdb11f6042a4e3a18a1177d4d1a6ce035f73fc28fa3ec8cbf99e6f2f8`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:08:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `49470d6fdb11f6042a4e3a18a1177d4d1a6ce035f73fc28fa3ec8cbf99e6f2f8`
- **SHA1:** `2bcbe88fb858b0f35304a806dd098c2a3a7d36a3`
- **MD5:** `b1df7a6dee0b4e458524c5753565edb3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 146 B |
| Entropía | 5.11 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 160.30.18.XXX | static_analysis |
| hash | 49470d6fdb11f6042a4e3a18a1177d4d1a6ce035f73fc28fa3ec8cbf99e6f2f8 | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
