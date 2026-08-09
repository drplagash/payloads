# 🧬 Payload Analysis

`4aa425c23db365f0a5b8bb8cb708cd1ef51809c2174f5b6c797e594284627056`

## 📌 Resumen

Artefacto de 129 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.09. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:41:09.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4aa425c23db365f0a5b8bb8cb708cd1ef51809c2174f5b6c797e594284627056`
- **SHA1:** `6d9015bed79105857e390de6f47b94893bfd8aaf`
- **MD5:** `0446ccfd99d2f6a90e5ce436ea2d9c21`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 129 B |
| Entropía | 5.09 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/8.7.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| command | User-Agent: curl/8.7.1 | strings |
| hash | 4aa425c23db365f0a5b8bb8cb708cd1ef51809c2174f5b6c797e594284627056 | static_analysis |
| ip | 137.184.27.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
