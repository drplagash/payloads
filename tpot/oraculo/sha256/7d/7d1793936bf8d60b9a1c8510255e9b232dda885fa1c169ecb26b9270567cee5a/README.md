# 🧬 Payload Analysis

`7d1793936bf8d60b9a1c8510255e9b232dda885fa1c169ecb26b9270567cee5a`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:03:20+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7d1793936bf8d60b9a1c8510255e9b232dda885fa1c169ecb26b9270567cee5a`
- **SHA1:** `f5767828296fa64ba50568f185eec61e4b86e349`
- **MD5:** `4be1f3ad833fb7d3fefff3ab2824d9f3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 95 B |
| Entropía | 5.01 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /wget.sh HTTP/1.1
User-Agent: curl/7.38.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 103.77.246.XXX | static_analysis |
| hash | 7d1793936bf8d60b9a1c8510255e9b232dda885fa1c169ecb26b9270567cee5a | static_analysis |
| command | GET /wget.sh HTTP/1.1 | strings |
| command | User-Agent: curl/7.38.0 | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
