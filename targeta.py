class TarjetaCredito:
    t_targetas = []

    def __init__(self, saldo_pagar, limite_credito, intereses, es_premium):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.es_premium = es_premium
        if self.es_premium: # Inicializamos el contador de compras solo si es premium
           self.contador_compras = 0
        TarjetaCredito.t_targetas.append(self)# Agregamos la tarjeta a la lista

    def compra(self, monto):
        monto_a_cobrar = monto
        descuento_aplicado = False
        if hasattr(self, 'contador_compras'):
            if self.contador_compras == 2:
                monto_a_cobrar = monto * 0.95
                print(f"Es tu 3ra compra. ¡Descuento Premium del 5% aplicado! se ha descontado $ -{monto * 0.05:.2f}")
                descuento_aplicado = True
        if self.saldo_pagar + monto_a_cobrar > self.limite_credito:
            print("Error: No tienes suficiente crédito para realizar la compra.")
        else:
            self.saldo_pagar += monto_a_cobrar
            print(f"Compra de ${monto} (cobrado ${monto_a_cobrar:.2f}) realizada. Nuevo saldo a pagar: ${self.saldo_pagar:.2f}")
            if hasattr(self, 'contador_compras'):
                if descuento_aplicado :
                    self.contador_compras = 0
                else:
                    self.contador_compras += 1
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        print(f"Pago realizado de ${monto}. Saldo restante: ${self.saldo_pagar:.2f}")
        return self
    def uso(self):
        id_calculado = TarjetaCredito.t_targetas.index(self) + 1
        print(f"--------------Usando la tarjeta {id_calculado}--------------")
        return self
    def mostrar_info_tarjeta(self):
        id_calculado = TarjetaCredito.t_targetas.index(self) + 1
        print("\n------ Información de la Tarjeta Nro. " + str(id_calculado) + " ------")
        print(f"Tipo: {'Premium' if self.es_premium else 'Normal'}")
        print(f"Saldo a pagar: ${self.saldo_pagar:,.2f}")
        print(f"Límite de crédito: ${self.limite_credito:,.2f}")
        print(f"Tasa de interés: {self.intereses:.2%}")
        if hasattr(self, 'contador_compras'):
            print(f"Compras realizadas para el descuento: {self.contador_compras} de 3")
        print("----------------------------------------------\n")
        return self
   
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        print(f"Interés de {self.intereses:.1%} cobrado. Nuevo saldo a pagar: ${self.saldo_pagar:.2f}")
        return self
 
    @classmethod
    def crear_tarjeta_normal(cls, limite_credito=1000, intereses=0.05):
        return cls(saldo_pagar=0, limite_credito=limite_credito, intereses=intereses, es_premium=False)

    @classmethod
    def crear_tarjeta_premium(cls, limite_credito=5000, intereses=0.02):
        return cls(saldo_pagar=0, limite_credito=limite_credito, intereses=intereses, es_premium=True)
        
    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        print("\n===== Resumen de Todas las Tarjetas Creadas =====")
        print(f"\nTienes un total de {len(cls.t_targetas)} tarjeta(s).")
        for tarjeta in cls.t_targetas:
            tarjeta.mostrar_info_tarjeta()
        print("================================================")
