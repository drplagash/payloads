# 🧬 Payload Analysis

`6f3c5fd171d408b626b6bce42e429f38e835621dd724704891355f865d0497f9`

## 📌 Resumen

Artefacto de 82 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.82. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:12:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6f3c5fd171d408b626b6bce42e429f38e835621dd724704891355f865d0497f9`
- **SHA1:** `3e93a75038e994bae9302d2f13550a4e99801163`
- **MD5:** `57f745ccde79236ac4a4e7b83c61d41a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 82 B |
| Entropía | 4.82 |
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
| ip | 190.179.153.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 6f3c5fd171d408b626b6bce42e429f38e835621dd724704891355f865d0497f9 | static_analysis |
| ip | 47.250.160.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
