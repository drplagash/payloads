# 🧬 Payload Analysis

`71eda9d2e5ba6c6dc024c451580319f2444cfc5e0dc26d101c0aefca5f28d54f`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `71eda9d2e5ba6c6dc024c451580319f2444cfc5e0dc26d101c0aefca5f28d54f`
- **SHA1:** `7da9cb8830a3ec0125567f3ba79d61bcf87da6b3`
- **MD5:** `9de28da44bbafc60febb984e66cbd2b6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text |
| Tamaño | 85 B |
| Entropía | 4.92 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.144.XXX | static_analysis |
| hash | 71eda9d2e5ba6c6dc024c451580319f2444cfc5e0dc26d101c0aefca5f28d54f | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 47.251.248.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
