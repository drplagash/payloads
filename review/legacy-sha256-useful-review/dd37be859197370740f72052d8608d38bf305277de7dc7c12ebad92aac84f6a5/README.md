# 🧬 Payload Analysis

`dd37be859197370740f72052d8608d38bf305277de7dc7c12ebad92aac84f6a5`

## 📌 Resumen

Texto ASCII de 275 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/dd37be859197370740f72052d8608d38bf305277de7dc7c12ebad92aac84f6a5.md](../../../../../malware-like/oraculo/downloader/dd37be859197370740f72052d8608d38bf305277de7dc7c12ebad92aac84f6a5.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dd37be859197370740f72052d8608d38bf305277de7dc7c12ebad92aac84f6a5`
- **MD5:** `99bbeeaf121c33e653d953cd2abc6e97`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 275 B |
| Entropía | 5.12 |
| Strings | 12 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 31.56.209.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | dd37be859197370740f72052d8608d38bf305277de7dc7c12ebad92aac84f6a5 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
