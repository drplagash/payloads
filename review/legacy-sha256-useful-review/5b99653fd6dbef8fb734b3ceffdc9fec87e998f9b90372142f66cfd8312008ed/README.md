# 🧬 Payload Analysis

`5b99653fd6dbef8fb734b3ceffdc9fec87e998f9b90372142f66cfd8312008ed`

## 📌 Resumen

Artefacto de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 2 comandos observados o extraídos. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/5b99653fd6dbef8fb734b3ceffdc9fec87e998f9b90372142f66cfd8312008ed.md](../../../../../malware-like/oraculo/downloader/5b99653fd6dbef8fb734b3ceffdc9fec87e998f9b90372142f66cfd8312008ed.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5b99653fd6dbef8fb734b3ceffdc9fec87e998f9b90372142f66cfd8312008ed`
- **MD5:** `803130ffd0a927ba6f7876ae6a4fdb21`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.78 |
| Strings | 14 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Alta entropía / posible empaquetado o cifrado**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp); High entropy (7.8) — posible packer/encrypted

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/ufo.apkOKAY
/data/local/tmp/ufo.apk,33261DATA
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | /data/local/tmp/ufo.apkOKAY | strings |
| command | /data/local/tmp/ufo.apk,33261DATA | strings |
| hash | 5b99653fd6dbef8fb734b3ceffdc9fec87e998f9b90372142f66cfd8312008ed | static_analysis |
| ip | 36.150.155.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
