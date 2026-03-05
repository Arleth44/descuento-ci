def descuento(precio, porcentaje):
    """
    Calcula el precio final aplicando un descuento.

    Args:
        precio (int|float): Precio original (>= 0).
        porcentaje (int|float): Porcentaje de descuento (0 a 100).

    Returns:
        float: Precio final con descuento.

    Raises:
        TypeError: Si precio o porcentaje no son números.
        ValueError: Si precio < 0 o porcentaje no está entre 0 y 100.
    """
    if not isinstance(precio, (int, float)) or not isinstance(porcentaje, (int, float)):
        raise TypeError("precio y porcentaje deben ser números (int o float).")

    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100.")

    descuento_monto = precio * (porcentaje / 100)
    return float(precio - descuento_monto)