# 🧬 Payload Analysis

`26b6a7a8101104cc17544d1b45448c461ed6918a62c1fa084b9bdf2b0aa49b29`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/26b6a7a8101104cc17544d1b45448c461ed6918a62c1fa084b9bdf2b0aa49b29.md](../../../../../malware-like/oraculo/botnet/26b6a7a8101104cc17544d1b45448c461ed6918a62c1fa084b9bdf2b0aa49b29.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `26b6a7a8101104cc17544d1b45448c461ed6918a62c1fa084b9bdf2b0aa49b29`
- **SHA1:** `3facef61fee2fe03bd4352b526d9fc8f7d74e6bc`
- **MD5:** `67eb817fb5b5572849ad926c7796ebce`

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
| hash | 26b6a7a8101104cc17544d1b45448c461ed6918a62c1fa084b9bdf2b0aa49b29 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
