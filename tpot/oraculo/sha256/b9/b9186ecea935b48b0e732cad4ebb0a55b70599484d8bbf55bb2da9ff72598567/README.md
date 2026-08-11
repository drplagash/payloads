# 🧬 Payload Analysis

`b9186ecea935b48b0e732cad4ebb0a55b70599484d8bbf55bb2da9ff72598567`

## 📌 Resumen

Artefacto de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b9186ecea935b48b0e732cad4ebb0a55b70599484d8bbf55bb2da9ff72598567.md](../../../../../malware-like/oraculo/downloader/b9186ecea935b48b0e732cad4ebb0a55b70599484d8bbf55bb2da9ff72598567.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b9186ecea935b48b0e732cad4ebb0a55b70599484d8bbf55bb2da9ff72598567`
- **MD5:** `a6a39e23ae64e8c10f6257c50db3bc39`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 6.74 |
| Strings | 10 |

## 🧠 Comportamiento observado

1. **Limpieza**
2. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
shell:rm -rf /data/local/tmp/*
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | shell:rm -rf /data/local/tmp/* | strings |
| hash | b9186ecea935b48b0e732cad4ebb0a55b70599484d8bbf55bb2da9ff72598567 | static_analysis |
| ip | 218.205.95.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
