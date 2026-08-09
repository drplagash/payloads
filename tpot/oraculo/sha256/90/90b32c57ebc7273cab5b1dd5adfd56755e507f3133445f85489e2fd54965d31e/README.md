# 🧬 Payload Analysis

`90b32c57ebc7273cab5b1dd5adfd56755e507f3133445f85489e2fd54965d31e`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `90b32c57ebc7273cab5b1dd5adfd56755e507f3133445f85489e2fd54965d31e`
- **SHA1:** `7db88cd8819828b904c2c525185fdec0090828ed`
- **MD5:** `2ae310f220e877ac398b0bc9f2200581`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text |
| Tamaño | 87 B |
| Entropía | 5.01 |
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
| ip | 190.179.139.XXX | static_analysis |
| hash | 90b32c57ebc7273cab5b1dd5adfd56755e507f3133445f85489e2fd54965d31e | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 47.84.140.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
