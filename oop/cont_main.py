from oop.Cont_bancar import ContBancar

cont1 = ContBancar('Andy S', 'RO001')
cont2 = ContBancar('Crina S', 'RO002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.plataCard(500)
cont2.plataCard(550.39)

cont1.interogareSold()
cont2.interogareSold()
