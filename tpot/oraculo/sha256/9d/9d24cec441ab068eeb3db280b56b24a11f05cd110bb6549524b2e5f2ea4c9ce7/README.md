# 🧬 Payload Analysis

`9d24cec441ab068eeb3db280b56b24a11f05cd110bb6549524b2e5f2ea4c9ce7`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9d24cec441ab068eeb3db280b56b24a11f05cd110bb6549524b2e5f2ea4c9ce7`
- **MD5:** `a616e17ba0d720376640cc81461476d7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 417 B |
| Entropía | 5.09 |
| Strings | 18 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /wget.sh HTTP/1.1
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.130.151.XXX | static_analysis |
| hash | 9d24cec441ab068eeb3db280b56b24a11f05cd110bb6549524b2e5f2ea4c9ce7 | static_analysis |
| command | GET /wget.sh HTTP/1.1 | strings |
| command | User-Agent: curl/7.73.0 | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
