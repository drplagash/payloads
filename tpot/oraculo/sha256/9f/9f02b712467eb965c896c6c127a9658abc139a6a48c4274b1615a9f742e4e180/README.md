# 🧬 Payload Analysis

`9f02b712467eb965c896c6c127a9658abc139a6a48c4274b1615a9f742e4e180`

## 📌 Resumen

Texto ASCII de 112 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/9f02b712467eb965c896c6c127a9658abc139a6a48c4274b1615a9f742e4e180.md](../../../../../malware-like/oraculo/downloader/9f02b712467eb965c896c6c127a9658abc139a6a48c4274b1615a9f742e4e180.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9f02b712467eb965c896c6c127a9658abc139a6a48c4274b1615a9f742e4e180`
- **MD5:** `7d3f846326ad49db70f8a25b19f9237f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 112 B |
| Entropía | 4.93 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.74.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.74.0 | strings |
| hash | 9f02b712467eb965c896c6c127a9658abc139a6a48c4274b1615a9f742e4e180 | static_analysis |
| ip | 47.77.234.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
