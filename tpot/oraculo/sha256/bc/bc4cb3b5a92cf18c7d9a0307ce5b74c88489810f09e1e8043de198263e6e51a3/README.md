# 🧬 Payload Analysis

`bc4cb3b5a92cf18c7d9a0307ce5b74c88489810f09e1e8043de198263e6e51a3`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:18:27+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bc4cb3b5a92cf18c7d9a0307ce5b74c88489810f09e1e8043de198263e6e51a3`
- **SHA1:** `caab7b0c99b98a34ce037a2051aa657af5f6fef4`
- **MD5:** `e822303b507f96fdcc7cbc835f3aa093`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
| Entropía | 4.86 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | bc4cb3b5a92cf18c7d9a0307ce5b74c88489810f09e1e8043de198263e6e51a3 | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 47.245.142.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
