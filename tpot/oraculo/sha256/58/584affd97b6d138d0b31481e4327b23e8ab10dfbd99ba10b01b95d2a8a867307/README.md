# 🧬 Payload Analysis

`584affd97b6d138d0b31481e4327b23e8ab10dfbd99ba10b01b95d2a8a867307`

## 📌 Resumen

Artefacto de 4.0 KiB. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `584affd97b6d138d0b31481e4327b23e8ab10dfbd99ba10b01b95d2a8a867307`
- **MD5:** `87498d1b32b3f0338df8710e716ae613`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 6.74 |
| Strings | 28 |

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
| hash | 584affd97b6d138d0b31481e4327b23e8ab10dfbd99ba10b01b95d2a8a867307 | static_analysis |
| ip | 218.205.95.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
