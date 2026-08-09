# 🧬 Payload Analysis

`e3f0b7d3bbc4c61b5d409d06d37d3520a91707524b308f1534001dcb9a66de73`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e3f0b7d3bbc4c61b5d409d06d37d3520a91707524b308f1534001dcb9a66de73`
- **MD5:** `1a68a15d8508981aba5e44aa3bfcc309`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 87 B |
| Entropía | 4.84 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Mirai-like indicators in strings; Download indicators (wget/curl + /tmp)
Mirai-like indicators in strings; Download indicators (wget/curl + /tmp)
Mirai-like indicators in strings; Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/8.5.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| hash | e3f0b7d3bbc4c61b5d409d06d37d3520a91707524b308f1534001dcb9a66de73 | static_analysis |
| command | User-Agent: curl/8.5.0 | strings |
| ip | 187.17.224.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
