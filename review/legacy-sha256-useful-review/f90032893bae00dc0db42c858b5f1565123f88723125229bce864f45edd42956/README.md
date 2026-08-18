# 🧬 Payload Analysis

`f90032893bae00dc0db42c858b5f1565123f88723125229bce864f45edd42956`

## 📌 Resumen

Artefacto de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 2 comandos observados o extraídos. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f90032893bae00dc0db42c858b5f1565123f88723125229bce864f45edd42956.md](../../../../../malware-like/oraculo/downloader/f90032893bae00dc0db42c858b5f1565123f88723125229bce864f45edd42956.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:08.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f90032893bae00dc0db42c858b5f1565123f88723125229bce864f45edd42956`
- **MD5:** `62a04e027020847e963c6ff6341abe15`

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
| hash | f90032893bae00dc0db42c858b5f1565123f88723125229bce864f45edd42956 | static_analysis |
| ip | 180.105.74.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
