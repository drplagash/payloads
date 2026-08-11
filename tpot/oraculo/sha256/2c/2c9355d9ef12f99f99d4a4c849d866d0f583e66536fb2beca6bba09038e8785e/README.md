# 🧬 Payload Analysis

`2c9355d9ef12f99f99d4a4c849d866d0f583e66536fb2beca6bba09038e8785e`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/2c9355d9ef12f99f99d4a4c849d866d0f583e66536fb2beca6bba09038e8785e.md](../../../../../malware-like/oraculo/botnet/2c9355d9ef12f99f99d4a4c849d866d0f583e66536fb2beca6bba09038e8785e.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2c9355d9ef12f99f99d4a4c849d866d0f583e66536fb2beca6bba09038e8785e`
- **SHA1:** `43917c5b413dc3f7ae177ab509047a487ce3647e`
- **MD5:** `5758bc8632396b50597c714968171e57`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.86 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.68.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.68.0 | strings |
| hash | 2c9355d9ef12f99f99d4a4c849d866d0f583e66536fb2beca6bba09038e8785e | static_analysis |
| ip | 94.237.67.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
