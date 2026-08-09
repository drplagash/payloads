# 🧬 Payload Analysis

`2864912625124b3d567bbda507d553c66a1123920587e32d38ff498599982aa9`

## 📌 Resumen

Artefacto de 110 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.94. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2864912625124b3d567bbda507d553c66a1123920587e32d38ff498599982aa9`
- **SHA1:** `85f908cc74266e802cec53264ef473cbedab9a95`
- **MD5:** `3c796048857d94f06306fc97935afcb7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 110 B |
| Entropía | 4.94 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.74.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| command | User-Agent: curl/7.74.0 | strings |
| hash | 2864912625124b3d567bbda507d553c66a1123920587e32d38ff498599982aa9 | static_analysis |
| ip | 8.219.106.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
