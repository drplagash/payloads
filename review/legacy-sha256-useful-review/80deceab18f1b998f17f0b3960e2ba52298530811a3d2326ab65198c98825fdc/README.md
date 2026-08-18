# 🧬 Payload Analysis

`80deceab18f1b998f17f0b3960e2ba52298530811a3d2326ab65198c98825fdc`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/80deceab18f1b998f17f0b3960e2ba52298530811a3d2326ab65198c98825fdc.md](../../../../../malware-like/oraculo/botnet/80deceab18f1b998f17f0b3960e2ba52298530811a3d2326ab65198c98825fdc.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `80deceab18f1b998f17f0b3960e2ba52298530811a3d2326ab65198c98825fdc`
- **MD5:** `9449ffff5e2402748bdecd69d02bf395`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 87 B |
| Entropía | 4.79 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/8.5.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.175.XXX | static_analysis |
| command | User-Agent: curl/8.5.0 | strings |
| hash | 80deceab18f1b998f17f0b3960e2ba52298530811a3d2326ab65198c98825fdc | static_analysis |
| ip | 187.17.224.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
