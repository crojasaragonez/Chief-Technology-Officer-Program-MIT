#!/usr/bin/env python3
"""Estimación de la inversión en I+D de Nu Holdings (Nubank), 2023-2025.

Nu no reporta una línea de I+D: según su 20-F, el gasto en investigación y
desarrollo está dentro de los gastos generales y de administración (G&A),
junto con back-office y overhead. Se estima con tres componentes, todos en
millones de US$ y tomados del 20-F del ejercicio 2025:

  a) desarrollo capitalizado: adiciones de intangibles desarrollados
     internamente (nota 19);
  b) infraestructura y procesamiento de datos registrados en G&A, es decir,
     la tecnología que no está ligada a transacciones de clientes;
  c) gasto de personal de G&A (salarios, pagos en acciones y otros costos de
     personal) multiplicado por la participación del personal de tecnología
     dentro de las funciones que se registran en G&A.

Rango bajo = a + b.  Rango alto = a + b + c.

Supuesto: la proporción de 2025 (4 236 personas de tecnología frente a 1 415
de G&A) se aplica a 2023 y 2024, porque el 20-F solo la publica para 2025.

Uso: python3 calculos.py
"""

INGRESOS = {2023: 8029.0, 2024: 11517.0, 2025: 15774.8}
UTILIDAD = {2023: 1030.6, 2024: 1972.0, 2025: 2871.7}
CLIENTES = {2023: 94.0, 2024: 114.0, 2025: 131.0}          # millones
CAPITALIZADO = {2023: 165.1, 2024: 154.6, 2025: 285.7}
INFRA_GA = {2023: 174.6, 2024: 195.1, 2025: 254.9}
PERSONAL_GA = {  # salarios + pagos en acciones + otros costos de personal
    2023: 300.6 + 251.8 + 46.3,
    2024: 349.9 + 351.4 + 53.8,
    2025: 409.3 + 313.9 + 70.1,
}
TECNOLOGIA, ADMINISTRACION = 4236, 1415
CUOTA_TEC = TECNOLOGIA / (TECNOLOGIA + ADMINISTRACION)


def main():
    print(f"participación de tecnología en G&A: {CUOTA_TEC:.1%}\n")
    print("año  capit.  infra  personal  bajo    alto   %bajo  %alto  "
          "US$/cliente(alto)")
    for anio in sorted(INGRESOS):
        personal = PERSONAL_GA[anio] * CUOTA_TEC
        bajo = CAPITALIZADO[anio] + INFRA_GA[anio]
        alto = bajo + personal
        print(f"{anio} {CAPITALIZADO[anio]:7.1f} {INFRA_GA[anio]:6.1f} "
              f"{personal:8.1f} {bajo:7.1f} {alto:7.1f} "
              f"{bajo / INGRESOS[anio]:6.1%} {alto / INGRESOS[anio]:6.1%} "
              f"{alto / CLIENTES[anio]:8.2f}")
    print(f"\ningresos 2023-2025: x{INGRESOS[2025] / INGRESOS[2023]:.2f}   "
          f"utilidad: x{UTILIDAD[2025] / UTILIDAD[2023]:.2f}   "
          f"clientes: x{CLIENTES[2025] / CLIENTES[2023]:.2f}")


if __name__ == "__main__":
    main()
