# 🧬 Payload Analysis

`9dc35b16222a70f4e57ab9c0de783c39ea5ba8b6d628feffdcdaf9c93ce3f8f6`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/9dc35b16222a70f4e57ab9c0de783c39ea5ba8b6d628feffdcdaf9c93ce3f8f6.md](../../../../../malware-like/oraculo/botnet/9dc35b16222a70f4e57ab9c0de783c39ea5ba8b6d628feffdcdaf9c93ce3f8f6.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9dc35b16222a70f4e57ab9c0de783c39ea5ba8b6d628feffdcdaf9c93ce3f8f6`
- **SHA1:** `b63be02d8673ded7ea0596493536d6126777bafd`
- **MD5:** `b965c259b7df52f82ab809d19b4b5f60`

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
| hash | 9dc35b16222a70f4e57ab9c0de783c39ea5ba8b6d628feffdcdaf9c93ce3f8f6 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
