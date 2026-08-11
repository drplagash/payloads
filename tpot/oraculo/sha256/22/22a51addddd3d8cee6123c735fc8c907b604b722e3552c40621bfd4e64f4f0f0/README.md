# 🧬 Payload Analysis

`22a51addddd3d8cee6123c735fc8c907b604b722e3552c40621bfd4e64f4f0f0`

## 📌 Resumen

Texto ASCII de 79 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/22a51addddd3d8cee6123c735fc8c907b604b722e3552c40621bfd4e64f4f0f0.md](../../../../../malware-like/oraculo/downloader/22a51addddd3d8cee6123c735fc8c907b604b722e3552c40621bfd4e64f4f0f0.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:13.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `22a51addddd3d8cee6123c735fc8c907b604b722e3552c40621bfd4e64f4f0f0`
- **MD5:** `bf49410e1ae9a8245125cdd3e3ef5fba`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 79 B |
| Entropía | 4.76 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.78.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.78.0 | strings |
| hash | 22a51addddd3d8cee6123c735fc8c907b604b722e3552c40621bfd4e64f4f0f0 | static_analysis |
| ip | 47.84.115.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
