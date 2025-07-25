from targeta import TarjetaCredito

if __name__ == "__main__":
    print("\n")
    targeta1 = TarjetaCredito.crear_tarjeta_normal()
    targeta2 = TarjetaCredito.crear_tarjeta_normal()
    targeta3 = TarjetaCredito.crear_tarjeta_premium()

    targeta1.uso().compra(100).compra(200).pago(50).cobrar_interes().mostrar_info_tarjeta()
    targeta2.uso().compra(100).compra(200).compra(300).pago(500).pago(100).cobrar_interes().mostrar_info_tarjeta()
    targeta3.uso().compra(1600).compra(1700).compra(1200).compra(500).compra(800).cobrar_interes().mostrar_info_tarjeta()
    TarjetaCredito.mostrar_todas_las_tarjetas()
