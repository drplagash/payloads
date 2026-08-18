<p align="center">
  <img src="assets/payloads.png" alt="Payloads" width="100%">
</p>

# Payloads

Biblioteca pública de evidencia de Oraculo SOC para payloads, malware y campañas observadas en T-Pot.

Este repositorio está pensado para humanos: abrir, entender, hacer clic y ver evidencia. No es un depósito de hashes tirados en una zanja digital.

## Acceso rápido

| Quiero ver | Entrar acá |
|---|---|
| Casos explicados | [`casos/`](casos/) |
| Firmas y payloads confirmados | [`firmas/`](firmas/) |
| Detecciones | [`detecciones/`](detecciones/) |
| Inteligencia / CTI | [`intel/`](intel/) |
| Volumen procesado / hallazgos | [`hallazgos/`](hallazgos/) |

## Casos principales

- [`router-downloader-91-92-40`](casos/tpot-router-downloader-campaign-91-92-40/)  
  Campaña router/IoT downloader agrupada desde 517 artefactos high-signal de T-Pot.

- [`mips-cad9e90`](casos/tpot-mips-payload-cad9e90/)  
  Payload ELF32 MIPS promovido como muestra confirmada con evidencia y análisis.

## Firma confirmada

- [`cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41`](firmas/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/)  
  Payload ELF32 MIPS capturado desde telemetría controlada de honeypot.

## Regla humana

Primero se ven los casos.

Después se ven las firmas.

Cada firma debe abrir en una carpeta con toda la información posible: README, evidencia, metadata, IOCs, análisis y material inerte.

El material histórico, ruido, review masivo y basura de hashes no va en la cara del visitante.

## Seguridad

Este repositorio es para investigación defensiva, análisis de malware, SOC y laboratorio controlado.

No ejecutar muestras en producción. No usar este material para actividad no autorizada. Los payloads deben mantenerse inertes.
