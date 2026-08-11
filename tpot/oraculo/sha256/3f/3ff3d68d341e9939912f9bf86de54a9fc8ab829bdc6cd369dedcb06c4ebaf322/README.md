# 🧬 Payload Analysis

`3ff3d68d341e9939912f9bf86de54a9fc8ab829bdc6cd369dedcb06c4ebaf322`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 4 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/3ff3d68d341e9939912f9bf86de54a9fc8ab829bdc6cd369dedcb06c4ebaf322.md](../../../../../malware-like/oraculo/botnet/3ff3d68d341e9939912f9bf86de54a9fc8ab829bdc6cd369dedcb06c4ebaf322.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:08:59.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3ff3d68d341e9939912f9bf86de54a9fc8ab829bdc6cd369dedcb06c4ebaf322`
- **SHA1:** `6b76a876c5729cc50b78679307658407cd674ccc`
- **MD5:** `daa9c406812f636d3e1b50296a581d20`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 858 B |
| Entropía | 5.48 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://www[.]google[.]com/ | strings |
| url | hxxps://alfabienes[.]com[.]co/api/v3/products?search=progressive&category=358&tag=progressive&page=423&per_page=945&orderby=date&_=1782138023703 | strings |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| hash | 3ff3d68d341e9939912f9bf86de54a9fc8ab829bdc6cd369dedcb06c4ebaf322 | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
