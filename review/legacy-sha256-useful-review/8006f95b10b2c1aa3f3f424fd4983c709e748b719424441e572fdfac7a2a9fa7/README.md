# 🧬 Payload Analysis

`8006f95b10b2c1aa3f3f424fd4983c709e748b719424441e572fdfac7a2a9fa7`

## 📌 Resumen

Texto ASCII de 78 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/8006f95b10b2c1aa3f3f424fd4983c709e748b719424441e572fdfac7a2a9fa7.md](../../../../../malware-like/oraculo/downloader/8006f95b10b2c1aa3f3f424fd4983c709e748b719424441e572fdfac7a2a9fa7.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8006f95b10b2c1aa3f3f424fd4983c709e748b719424441e572fdfac7a2a9fa7`
- **MD5:** `4f14962774f4db0ab8ce6f5e2d561b38`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 78 B |
| Entropía | 4.77 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.29.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.29.0 | strings |
| hash | 8006f95b10b2c1aa3f3f424fd4983c709e748b719424441e572fdfac7a2a9fa7 | static_analysis |
| ip | 118.193.44.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
