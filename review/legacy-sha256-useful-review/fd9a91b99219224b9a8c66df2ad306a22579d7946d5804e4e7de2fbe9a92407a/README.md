# 🧬 Payload Analysis

`fd9a91b99219224b9a8c66df2ad306a22579d7946d5804e4e7de2fbe9a92407a`

## 📌 Resumen

Artefacto de 94 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.90. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fd9a91b99219224b9a8c66df2ad306a22579d7946d5804e4e7de2fbe9a92407a`
- **SHA1:** `459bfd013ec3461440dadc260d87e423fad39957`
- **MD5:** `9fc6f4854b7551bf69cbbad8e0a91396`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.9 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.81.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| command | User-Agent: curl/7.81.0 | strings |
| hash | fd9a91b99219224b9a8c66df2ad306a22579d7946d5804e4e7de2fbe9a92407a | static_analysis |
| ip | 34.45.86.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
