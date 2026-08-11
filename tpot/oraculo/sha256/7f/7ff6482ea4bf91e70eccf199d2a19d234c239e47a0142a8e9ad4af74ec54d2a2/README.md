# 🧬 Payload Analysis

`7ff6482ea4bf91e70eccf199d2a19d234c239e47a0142a8e9ad4af74ec54d2a2`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/7ff6482ea4bf91e70eccf199d2a19d234c239e47a0142a8e9ad4af74ec54d2a2.md](../../../../../malware-like/oraculo/downloader/7ff6482ea4bf91e70eccf199d2a19d234c239e47a0142a8e9ad4af74ec54d2a2.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7ff6482ea4bf91e70eccf199d2a19d234c239e47a0142a8e9ad4af74ec54d2a2`
- **MD5:** `7663b887a6c3866e4281932c7bd02767`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.77 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 7ff6482ea4bf91e70eccf199d2a19d234c239e47a0142a8e9ad4af74ec54d2a2 | static_analysis |
| ip | 8.211.36.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
