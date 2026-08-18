# 🧬 Payload Analysis

`dd55ca9ffd53a83721d1092f128b1aba4852cecd3e3344579f6d82862c75e9e6`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/dd55ca9ffd53a83721d1092f128b1aba4852cecd3e3344579f6d82862c75e9e6.md](../../../../../malware-like/oraculo/botnet/dd55ca9ffd53a83721d1092f128b1aba4852cecd3e3344579f6d82862c75e9e6.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dd55ca9ffd53a83721d1092f128b1aba4852cecd3e3344579f6d82862c75e9e6`
- **SHA1:** `62a8164cc5c8ffc0998b69d208c079a7afe3b64b`
- **MD5:** `2788886ab821560dcd81a60e25b34c73`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.86 |
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
| hash | dd55ca9ffd53a83721d1092f128b1aba4852cecd3e3344579f6d82862c75e9e6 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
