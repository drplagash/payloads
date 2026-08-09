# 🧬 Payload Analysis

`f13d600c1094b4c8a44b808fc1dbcaf119e8c3c776639721cdabee115f24603a`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f13d600c1094b4c8a44b808fc1dbcaf119e8c3c776639721cdabee115f24603a`
- **SHA1:** `853d4e87af3a21842af9675e68e6f0d97cbc31f2`
- **MD5:** `0647548d37f49bd6b0a8441b7256ae1e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 90 B |
| Entropía | 5.02 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.38.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 35.237.91.XXX | static_analysis |
| hash | f13d600c1094b4c8a44b808fc1dbcaf119e8c3c776639721cdabee115f24603a | static_analysis |
| command | User-Agent: curl/7.38.0 | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
