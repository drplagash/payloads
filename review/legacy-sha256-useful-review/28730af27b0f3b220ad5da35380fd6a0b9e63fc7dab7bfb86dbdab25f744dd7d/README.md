# 🧬 Payload Analysis

`28730af27b0f3b220ad5da35380fd6a0b9e63fc7dab7bfb86dbdab25f744dd7d`

## 📌 Resumen

Artefacto de 83 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.80. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:00:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `28730af27b0f3b220ad5da35380fd6a0b9e63fc7dab7bfb86dbdab25f744dd7d`
- **SHA1:** `431e292f555fff4ca7480b33d8396a0c7fc425c7`
- **MD5:** `bea3929780d29d591f52bbb07cdcd88c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.8 |
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
| ip | 190.179.160.XXX | static_analysis |
| command | User-Agent: curl/7.68.0 | strings |
| hash | 28730af27b0f3b220ad5da35380fd6a0b9e63fc7dab7bfb86dbdab25f744dd7d | static_analysis |
| ip | 198.235.24.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
