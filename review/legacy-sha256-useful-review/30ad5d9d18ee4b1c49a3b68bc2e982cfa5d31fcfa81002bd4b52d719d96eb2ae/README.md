# 🧬 Payload Analysis

`30ad5d9d18ee4b1c49a3b68bc2e982cfa5d31fcfa81002bd4b52d719d96eb2ae`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/30ad5d9d18ee4b1c49a3b68bc2e982cfa5d31fcfa81002bd4b52d719d96eb2ae.md](../../../../../malware-like/oraculo/botnet/30ad5d9d18ee4b1c49a3b68bc2e982cfa5d31fcfa81002bd4b52d719d96eb2ae.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `30ad5d9d18ee4b1c49a3b68bc2e982cfa5d31fcfa81002bd4b52d719d96eb2ae`
- **SHA1:** `c7e7b0d5695632e6efe0e1e8c2cbc4451fa009d9`
- **MD5:** `d18e1cf9070d1092ad0a0c1d4a0616d6`

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
User-Agent: curl/7.61.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.61.1 | strings |
| hash | 30ad5d9d18ee4b1c49a3b68bc2e982cfa5d31fcfa81002bd4b52d719d96eb2ae | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
