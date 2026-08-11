# 🧬 Payload Analysis

`4ce276ac1471c6ed7b2f0e53a5612f9bbfa53ebfb41e4c3a11ed80d54c76f479`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/4ce276ac1471c6ed7b2f0e53a5612f9bbfa53ebfb41e4c3a11ed80d54c76f479.md](../../../../../malware-like/oraculo/botnet/4ce276ac1471c6ed7b2f0e53a5612f9bbfa53ebfb41e4c3a11ed80d54c76f479.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4ce276ac1471c6ed7b2f0e53a5612f9bbfa53ebfb41e4c3a11ed80d54c76f479`
- **SHA1:** `5f36e95f5966df9e1e9ee3581f2719037f537521`
- **MD5:** `7cdbda0336828f8c0bce74e4a2e948e7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.87 |
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
| hash | 4ce276ac1471c6ed7b2f0e53a5612f9bbfa53ebfb41e4c3a11ed80d54c76f479 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
