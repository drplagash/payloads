# 🧬 Payload Analysis

`f1ee72036c9ba6de37e7a9069fc2f8e56e87ce47bbe37795519ecd9cf991e1ca`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/f1ee72036c9ba6de37e7a9069fc2f8e56e87ce47bbe37795519ecd9cf991e1ca.md](../../../../../malware-like/oraculo/botnet/f1ee72036c9ba6de37e7a9069fc2f8e56e87ce47bbe37795519ecd9cf991e1ca.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f1ee72036c9ba6de37e7a9069fc2f8e56e87ce47bbe37795519ecd9cf991e1ca`
- **SHA1:** `82b5b06889201db78ffbfe57caa9425a51910578`
- **MD5:** `b69b0e0ba3ea57ce051c75803122e9d8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.83 |
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
| hash | f1ee72036c9ba6de37e7a9069fc2f8e56e87ce47bbe37795519ecd9cf991e1ca | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
