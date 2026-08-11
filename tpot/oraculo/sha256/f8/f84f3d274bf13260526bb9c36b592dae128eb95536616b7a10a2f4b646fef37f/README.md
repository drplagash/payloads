# 🧬 Payload Analysis

`f84f3d274bf13260526bb9c36b592dae128eb95536616b7a10a2f4b646fef37f`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/f84f3d274bf13260526bb9c36b592dae128eb95536616b7a10a2f4b646fef37f.md](../../../../../malware-like/oraculo/botnet/f84f3d274bf13260526bb9c36b592dae128eb95536616b7a10a2f4b646fef37f.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f84f3d274bf13260526bb9c36b592dae128eb95536616b7a10a2f4b646fef37f`
- **SHA1:** `103edea5a41a8667a3fabc9655d4b2264ee7462f`
- **MD5:** `7262f17b2713db8ac148015b624a82d9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 91 B |
| Entropía | 4.84 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/8.14.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| command | User-Agent: curl/8.14.1 | strings |
| hash | f84f3d274bf13260526bb9c36b592dae128eb95536616b7a10a2f4b646fef37f | static_analysis |
| ip | 110.10.176.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
