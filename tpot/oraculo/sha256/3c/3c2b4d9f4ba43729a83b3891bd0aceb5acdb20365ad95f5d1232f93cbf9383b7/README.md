# 🧬 Payload Analysis

`3c2b4d9f4ba43729a83b3891bd0aceb5acdb20365ad95f5d1232f93cbf9383b7`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/3c2b4d9f4ba43729a83b3891bd0aceb5acdb20365ad95f5d1232f93cbf9383b7.md](../../../../../malware-like/oraculo/botnet/3c2b4d9f4ba43729a83b3891bd0aceb5acdb20365ad95f5d1232f93cbf9383b7.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3c2b4d9f4ba43729a83b3891bd0aceb5acdb20365ad95f5d1232f93cbf9383b7`
- **SHA1:** `46efa134a212ba42138a89ccc8c161d1e5f0e1e6`
- **MD5:** `a064558a26d06fd2381bc3b07d2aab22`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.84 |
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
| hash | 3c2b4d9f4ba43729a83b3891bd0aceb5acdb20365ad95f5d1232f93cbf9383b7 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
