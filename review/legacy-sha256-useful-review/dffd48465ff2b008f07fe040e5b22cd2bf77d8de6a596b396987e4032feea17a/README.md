# 🧬 Payload Analysis

`dffd48465ff2b008f07fe040e5b22cd2bf77d8de6a596b396987e4032feea17a`

## 📌 Resumen

Artefacto de 111 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.95. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dffd48465ff2b008f07fe040e5b22cd2bf77d8de6a596b396987e4032feea17a`
- **SHA1:** `6b1007513487a2af9c05ec6d5c2403743789ae07`
- **MD5:** `f26ef9ee4e8bf795d2f5ab82b4dd37c5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 111 B |
| Entropía | 4.95 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.74.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.74.0 | strings |
| hash | dffd48465ff2b008f07fe040e5b22cd2bf77d8de6a596b396987e4032feea17a | static_analysis |
| ip | 47.250.95.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
