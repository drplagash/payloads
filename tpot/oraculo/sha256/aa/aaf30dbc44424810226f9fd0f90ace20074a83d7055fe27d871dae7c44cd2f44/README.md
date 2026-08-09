# 🧬 Payload Analysis

`aaf30dbc44424810226f9fd0f90ace20074a83d7055fe27d871dae7c44cd2f44`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 83 B. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `aaf30dbc44424810226f9fd0f90ace20074a83d7055fe27d871dae7c44cd2f44`
- **MD5:** `129790547e21dfd36bb4d344dd43f6ea`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.81 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | aaf30dbc44424810226f9fd0f90ace20074a83d7055fe27d871dae7c44cd2f44 | static_analysis |
| ip | 47.254.214.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
