# 🧬 Payload Analysis

`87bdc54b2a454a8aa2307a836c7c77b29ec4cb8dfc579cc271395901dbecea01`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/87bdc54b2a454a8aa2307a836c7c77b29ec4cb8dfc579cc271395901dbecea01.md](../../../../../malware-like/oraculo/downloader/87bdc54b2a454a8aa2307a836c7c77b29ec4cb8dfc579cc271395901dbecea01.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `87bdc54b2a454a8aa2307a836c7c77b29ec4cb8dfc579cc271395901dbecea01`
- **MD5:** `63e50524e2498c3946bff916e44d56af`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.76 |
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
| ip | 190.179.164.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 87bdc54b2a454a8aa2307a836c7c77b29ec4cb8dfc579cc271395901dbecea01 | static_analysis |
| ip | 47.251.123.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
