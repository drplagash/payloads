# 🧬 Payload Analysis

`44a82d59bcd977750f08f868e5b5175b168b6cb1753658e0b2328f6c37717455`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/44a82d59bcd977750f08f868e5b5175b168b6cb1753658e0b2328f6c37717455.md](../../../../../malware-like/oraculo/botnet/44a82d59bcd977750f08f868e5b5175b168b6cb1753658e0b2328f6c37717455.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:58:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `44a82d59bcd977750f08f868e5b5175b168b6cb1753658e0b2328f6c37717455`
- **SHA1:** `901c0d90367613d39d230d9fe78e5d0acae0464e`
- **MD5:** `a01ddcca7e77fe5f5c418c7ddfc00820`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 866 B |
| Entropía | 5.09 |
| Strings | 36 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 176.100.36.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 44a82d59bcd977750f08f868e5b5175b168b6cb1753658e0b2328f6c37717455 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
